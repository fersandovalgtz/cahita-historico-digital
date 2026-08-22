#!/usr/bin/env python3
"""Build a conservative post-v1 index of explicit historical variation evidence.

The index scans the currently canonical machine-readable layers of CHD:

- diplomatic page transcriptions;
- canonical lexical articles;
- structured grammar and numeral objects;
- transcription status metadata for coverage accounting.

It does not infer modern language identities, dialect taxonomies, cognacy, or
variety membership from linguistic similarity. It only records explicit source
labels or already-structured CHD variety metadata.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
TRANSCRIPTION_DIR = ROOT / "data" / "transcription" / "pages"
TRANSCRIPTION_STATUS = ROOT / "data" / "transcription" / "status.csv"
LEXICON_DIR = ROOT / "data" / "lexicon" / "articles"
GRAMMAR_DIR = ROOT / "data" / "grammar"
OBSERVATION_SCHEMA = ROOT / "schemas" / "historical-variety-observation.schema.json"

INDEX_JSONL = "chd_historical_variation_index.jsonl"
INDEX_CSV = "chd_historical_variation_index.csv"
OBSERVATIONS_JSONL = "chd_historical_variety_observations.jsonl"
COVERAGE_CSV = "chd_historical_variation_coverage.csv"
MANIFEST_JSON = "manifest.json"

CANONICAL_VERSION = "1.0.0"
CANONICAL_TAG = "v1.0.0"
CANONICAL_TAG_COMMIT = "dbcdecf0003ac5a10ae963caf6babdcf5c22128d"

# These classes are documentary labels, not modern language assignments.
LABEL_PATTERNS: dict[str, re.Pattern[str]] = {
    "Hiaqui": re.compile(r"\bhiaquis?\b", re.IGNORECASE),
    "Mayo": re.compile(r"\b(?:mayos?|mayes)\b", re.IGNORECASE),
    "Thehueco": re.compile(r"\b(?:thehuecos?|tehuecos?|teuecos?)\b", re.IGNORECASE),
    "Naciones": re.compile(r"\bnaciones?\b", re.IGNORECASE),
    "Cynaloa": re.compile(r"\b(?:cynaloas?|sinaloas?)\b", re.IGNORECASE),
}

OBSERVATION_SECTIONS = {
    "preliminaries",
    "part_i",
    "part_ii",
    "part_iii",
    "part_iv",
    "vocabulary",
    "numerals",
}

INDEX_FIELDS = [
    "evidenceId",
    "sourceLayer",
    "sourcePath",
    "sourcePageDigital",
    "sourcePagePrinted",
    "pageRangeDigital",
    "section",
    "objectId",
    "articleId",
    "evidenceKind",
    "labelClasses",
    "labelsRaw",
    "sourceText",
    "formRaw",
    "sourceQualifierRaw",
    "historicalVarietyStructured",
    "reviewStatus",
    "humanVerified",
    "attributionExplicit",
    "modernIdentityInferred",
]


def normalize(text: str) -> str:
    value = unicodedata.normalize("NFKC", text).replace("ſ", "s").casefold()
    return " ".join(value.split())


def compact_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def find_labels(text: str) -> tuple[list[str], list[str]]:
    classes: list[str] = []
    raw: list[str] = []
    for label_class, pattern in LABEL_PATTERNS.items():
        matches = list(pattern.finditer(text))
        if not matches:
            continue
        classes.append(label_class)
        for match in matches:
            token = match.group(0)
            if token not in raw:
                raw.append(token)
    return classes, raw


def labels_from_structured(value: str | None) -> tuple[list[str], list[str]]:
    if not value or value == "unspecified":
        return [], []
    classes, raw = find_labels(value)
    if classes:
        return classes, raw or [value]
    return ["other_explicit_source_label"], [value]


def split_paragraphs(text: str) -> list[str]:
    return [" ".join(part.split()) for part in re.split(r"\n\s*\n", text) if part.strip()]


def source_page_from_object(obj: dict[str, Any]) -> int | None:
    value = obj.get("sourcePageDigital")
    if isinstance(value, int):
        return value
    value = obj.get("pageDigital")
    if isinstance(value, int):
        return value
    return None


def page_range_from_object(obj: dict[str, Any]) -> list[int] | None:
    value = obj.get("pageRangeDigital")
    if isinstance(value, list) and len(value) == 2 and all(isinstance(item, int) for item in value):
        return value
    start = obj.get("sourcePageDigitalStart")
    end = obj.get("sourcePageDigitalEnd")
    if isinstance(start, int) and isinstance(end, int):
        return [start, end]
    return None


def object_identifier(obj: dict[str, Any]) -> str | None:
    for key in ("id", "objectId", "ruleId", "paradigmId", "constructionId", "articleId"):
        value = obj.get(key)
        if isinstance(value, str) and value:
            return value
    return None


def derive_review_status(obj: dict[str, Any]) -> str | None:
    value = obj.get("reviewStatus")
    return value if isinstance(value, str) else None


def derive_human_verified(obj: dict[str, Any]) -> bool:
    return obj.get("humanVerified") is True


def record_sort_key(row: dict[str, Any]) -> tuple[Any, ...]:
    page = row.get("sourcePageDigital")
    page_range = row.get("pageRangeDigital") or []
    anchor = page if isinstance(page, int) else (page_range[0] if page_range else 9999)
    return (
        anchor,
        row.get("sourceLayer") or "",
        row.get("sourcePath") or "",
        row.get("objectId") or "",
        row.get("articleId") or "",
        row.get("evidenceKind") or "",
        ";".join(row.get("labelClasses") or []),
        normalize(row.get("sourceText") or ""),
        row.get("formRaw") or "",
    )


def add_record(rows: list[dict[str, Any]], **kwargs: Any) -> None:
    row = {
        "sourceLayer": kwargs.get("sourceLayer"),
        "sourcePath": kwargs.get("sourcePath"),
        "sourcePageDigital": kwargs.get("sourcePageDigital"),
        "sourcePagePrinted": kwargs.get("sourcePagePrinted"),
        "pageRangeDigital": kwargs.get("pageRangeDigital"),
        "section": kwargs.get("section"),
        "objectId": kwargs.get("objectId"),
        "articleId": kwargs.get("articleId"),
        "evidenceKind": kwargs.get("evidenceKind"),
        "labelClasses": kwargs.get("labelClasses") or [],
        "labelsRaw": kwargs.get("labelsRaw") or [],
        "sourceText": kwargs.get("sourceText"),
        "formRaw": kwargs.get("formRaw"),
        "sourceQualifierRaw": kwargs.get("sourceQualifierRaw"),
        "historicalVarietyStructured": kwargs.get("historicalVarietyStructured"),
        "reviewStatus": kwargs.get("reviewStatus"),
        "humanVerified": bool(kwargs.get("humanVerified", False)),
        "attributionExplicit": bool(kwargs.get("attributionExplicit", True)),
        "modernIdentityInferred": False,
    }
    if not row["labelClasses"]:
        return
    rows.append(row)


def scan_page_transcriptions() -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[str]]:
    rows: list[dict[str, Any]] = []
    observation_candidates: list[dict[str, Any]] = []
    inputs: list[str] = []

    for path in sorted(TRANSCRIPTION_DIR.glob("ALC1737_p*.json")):
        rel = path.relative_to(ROOT).as_posix()
        inputs.append(rel)
        obj = json.loads(path.read_text(encoding="utf-8"))
        text = obj.get("text")
        if not isinstance(text, str) or not text:
            continue
        page = obj.get("sourcePageDigital")
        printed = obj.get("sourcePagePrinted")
        section = obj.get("section")
        for paragraph_index, paragraph in enumerate(split_paragraphs(text), start=1):
            classes, raw = find_labels(paragraph)
            if not classes:
                continue
            add_record(
                rows,
                sourceLayer="page_transcription",
                sourcePath=rel,
                sourcePageDigital=page,
                sourcePagePrinted=printed,
                section=section,
                objectId=f"{path.stem}:paragraph:{paragraph_index}",
                evidenceKind="explicit_surface_mention",
                labelClasses=classes,
                labelsRaw=raw,
                sourceText=paragraph,
                reviewStatus=obj.get("reviewStatus"),
                humanVerified=obj.get("humanVerified") is True,
            )
            if isinstance(page, int) and section in OBSERVATION_SECTIONS:
                observation_candidates.append(
                    {
                        "sourcePageDigital": page,
                        "sourcePagePrinted": printed if isinstance(printed, int) else None,
                        "section": section,
                        "varietiesRaw": raw,
                        "observationType": "other_explicit_source_attribution",
                        "phenomenon": None,
                        "sourceText": paragraph,
                        "structuredClaim": {
                            "labelClasses": classes,
                            "evidenceKind": "explicit_surface_mention",
                        },
                        "editorialInterpretation": None,
                        "caution": (
                            "Documentary source labels only; no modern language or dialect identity is inferred."
                        ),
                        "reviewStatus": (
                            obj.get("reviewStatus")
                            if obj.get("reviewStatus") in {
                                "machine_corrected_unverified",
                                "editorial_proposal",
                                "human_verified",
                                "unresolved",
                            }
                            else "machine_corrected_unverified"
                        ),
                        "humanVerified": obj.get("humanVerified") is True,
                        "provenance": {
                            "derivedFrom": rel,
                            "agent": "CHD deterministic historical-variation exporter",
                            "method": "Explicit historical-label detection in canonical diplomatic page transcription; no linguistic-similarity inference",
                            "processedAt": None,
                        },
                    }
                )

    return rows, observation_candidates, inputs


def scan_lexicon() -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[str], int]:
    rows: list[dict[str, Any]] = []
    observation_candidates: list[dict[str, Any]] = []
    inputs: list[str] = []
    article_count = 0

    for path in sorted(LEXICON_DIR.glob("*.jsonl")):
        rel = path.relative_to(ROOT).as_posix()
        inputs.append(rel)
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if not line.strip():
                continue
            article_count += 1
            obj = json.loads(line)
            article_id = obj.get("articleId")
            page = obj.get("sourcePageDigital")
            printed = obj.get("sourcePagePrinted")
            section = "vocabulary"
            review = derive_review_status(obj)
            verified = derive_human_verified(obj)
            transcription = obj.get("transcriptionRaw") if isinstance(obj.get("transcriptionRaw"), str) else None

            for form_index, form in enumerate(obj.get("cahitaFormsRaw") or [], start=1):
                structured = form.get("historicalVariety")
                qualifier = form.get("sourceQualifierRaw")
                classes, raw = labels_from_structured(structured)
                if qualifier:
                    q_classes, q_raw = find_labels(qualifier)
                    if q_classes:
                        for label in q_classes:
                            if label not in classes:
                                classes.append(label)
                        for token in q_raw:
                            if token not in raw:
                                raw.append(token)
                    elif not classes:
                        classes = ["other_explicit_source_label"]
                        raw = [qualifier]
                if not classes:
                    continue
                add_record(
                    rows,
                    sourceLayer="lexicon",
                    sourcePath=rel,
                    sourcePageDigital=page,
                    sourcePagePrinted=printed,
                    section=section,
                    objectId=f"{article_id}:form:{form_index}",
                    articleId=article_id,
                    evidenceKind="structured_form_metadata",
                    labelClasses=classes,
                    labelsRaw=raw,
                    sourceText=transcription,
                    formRaw=form.get("formRaw"),
                    sourceQualifierRaw=qualifier,
                    historicalVarietyStructured=structured,
                    reviewStatus=review,
                    humanVerified=verified,
                )
                if isinstance(page, int) and transcription:
                    observation_candidates.append(
                        {
                            "sourcePageDigital": page,
                            "sourcePagePrinted": printed if isinstance(printed, int) else None,
                            "section": "vocabulary",
                            "varietiesRaw": raw,
                            "observationType": "lexical",
                            "phenomenon": "explicit historical variety metadata on lexical form",
                            "sourceText": transcription,
                            "structuredClaim": {
                                "articleId": article_id,
                                "formRaw": form.get("formRaw"),
                                "historicalVariety": structured,
                                "sourceQualifierRaw": qualifier,
                                "labelClasses": classes,
                            },
                            "editorialInterpretation": None,
                            "caution": (
                                "Structured historical variety metadata is preserved as documentary attribution; no modern identity is inferred."
                            ),
                            "reviewStatus": (
                                review
                                if review in {
                                    "machine_corrected_unverified",
                                    "editorial_proposal",
                                    "human_verified",
                                    "unresolved",
                                }
                                else "machine_corrected_unverified"
                            ),
                            "humanVerified": verified,
                            "provenance": {
                                "derivedFrom": f"{rel}:{line_number}",
                                "agent": "CHD deterministic historical-variation exporter",
                                "method": "Projection of explicit canonical lexical historicalVariety/sourceQualifierRaw metadata",
                                "processedAt": None,
                            },
                        }
                    )

            if transcription:
                classes, raw = find_labels(transcription)
                if classes:
                    add_record(
                        rows,
                        sourceLayer="lexicon",
                        sourcePath=rel,
                        sourcePageDigital=page,
                        sourcePagePrinted=printed,
                        section=section,
                        objectId=article_id,
                        articleId=article_id,
                        evidenceKind="article_surface_candidate",
                        labelClasses=classes,
                        labelsRaw=raw,
                        sourceText=transcription,
                        reviewStatus=review,
                        humanVerified=verified,
                        attributionExplicit=False,
                    )

    return rows, observation_candidates, inputs, article_count


def iter_string_evidence(value: Any, path: tuple[str, ...] = ()) -> Iterable[tuple[tuple[str, ...], str]]:
    if isinstance(value, str):
        classes, _raw = find_labels(value)
        key_text = " ".join(path)
        key_classes, _key_raw = find_labels(key_text)
        if classes or key_classes:
            yield path, value
        return
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = path + (str(key),)
            key_classes, _ = find_labels(str(key))
            if key_classes and isinstance(child, (str, int, float, bool, list)):
                yield child_path, compact_json(child) if not isinstance(child, str) else child
            yield from iter_string_evidence(child, child_path)
        return
    if isinstance(value, list):
        for index, child in enumerate(value):
            yield from iter_string_evidence(child, path + (str(index),))


def scan_grammar() -> tuple[list[dict[str, Any]], list[str], int]:
    rows: list[dict[str, Any]] = []
    inputs: list[str] = []
    object_count = 0
    seen_record_keys: set[tuple[str, str, str]] = set()

    paths = sorted(
        path
        for path in GRAMMAR_DIR.rglob("*")
        if path.is_file() and path.suffix in {".json", ".jsonl"}
    )
    for path in paths:
        rel = path.relative_to(ROOT).as_posix()
        inputs.append(rel)
        objects: list[dict[str, Any]] = []
        if path.suffix == ".json":
            parsed = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(parsed, dict):
                objects = [parsed]
            elif isinstance(parsed, list):
                objects = [item for item in parsed if isinstance(item, dict)]
        else:
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    item = json.loads(line)
                    if isinstance(item, dict):
                        objects.append(item)

        for object_index, obj in enumerate(objects, start=1):
            object_count += 1
            page = source_page_from_object(obj)
            page_range = page_range_from_object(obj)
            object_id = object_identifier(obj) or f"{path.stem}:object:{object_index}"
            section = obj.get("section") if isinstance(obj.get("section"), str) else None
            review = derive_review_status(obj)
            verified = derive_human_verified(obj)
            for field_path, text in iter_string_evidence(obj):
                classes, raw = find_labels(text)
                key_classes, key_raw = find_labels(" ".join(field_path))
                for label in key_classes:
                    if label not in classes:
                        classes.append(label)
                for token in key_raw:
                    if token not in raw:
                        raw.append(token)
                if not classes:
                    continue
                signature = (rel, ".".join(field_path), compact_json([classes, text]))
                if signature in seen_record_keys:
                    continue
                seen_record_keys.add(signature)
                add_record(
                    rows,
                    sourceLayer="grammar",
                    sourcePath=rel,
                    sourcePageDigital=page,
                    pageRangeDigital=page_range,
                    section=section,
                    objectId=object_id,
                    evidenceKind="structured_grammar_label_evidence",
                    labelClasses=classes,
                    labelsRaw=raw or key_raw,
                    sourceText=text,
                    reviewStatus=review,
                    humanVerified=verified,
                )

    return rows, inputs, object_count


def load_coverage() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with TRANSCRIPTION_STATUS.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for raw in reader:
            page = int(raw["digital_page"])
            row = {
                "sourceId": raw["source_id"],
                "sourcePageDigital": page,
                "sourcePagePrinted": int(raw["printed_page"]) if raw.get("printed_page") else None,
                "section": raw.get("section") or None,
                "materialRole": raw.get("material_role") or None,
                "coverage": raw.get("coverage") or None,
                "reviewStatus": raw.get("review_status") or None,
                "transcriptionFile": raw.get("transcription_file") or None,
                "notes": raw.get("notes") or None,
            }
            rows.append(row)

    rows.sort(key=lambda item: item["sourcePageDigital"])
    if [row["sourcePageDigital"] for row in rows] != list(range(1, 183)):
        raise SystemExit("transcription status must account for exactly digital pages 1-182")

    coverage_counts = Counter(row["coverage"] or "blank" for row in rows)
    review_counts = Counter(row["reviewStatus"] or "blank" for row in rows)
    transcribed = [row["sourcePageDigital"] for row in rows if row["transcriptionFile"]]
    pending = [
        row["sourcePageDigital"]
        for row in rows
        if row["coverage"] == "pending" or row["reviewStatus"] == "unreviewed"
    ]
    not_applicable = [
        row["sourcePageDigital"]
        for row in rows
        if row["coverage"] == "not_applicable_material"
    ]
    summary = {
        "digitalPageTotal": len(rows),
        "transcriptionFilePageCount": len(transcribed),
        "transcriptionFilePages": transcribed,
        "pendingOrUnreviewedPageCount": len(pending),
        "pendingOrUnreviewedPages": pending,
        "notApplicableMaterialPageCount": len(not_applicable),
        "notApplicableMaterialPages": not_applicable,
        "coverageCounts": dict(sorted(coverage_counts.items())),
        "reviewStatusCounts": dict(sorted(review_counts.items())),
    }
    return rows, summary


def deduplicate_observations(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[str] = set()
    rows: list[dict[str, Any]] = []
    for item in sorted(
        candidates,
        key=lambda row: (
            row["sourcePageDigital"],
            row["section"],
            row["observationType"],
            normalize(row["sourceText"]),
            compact_json(row.get("structuredClaim")),
        ),
    ):
        signature = compact_json(
            {
                "page": item["sourcePageDigital"],
                "section": item["section"],
                "varietiesRaw": sorted(item["varietiesRaw"]),
                "observationType": item["observationType"],
                "sourceText": normalize(item["sourceText"]),
                "structuredClaim": item.get("structuredClaim"),
            }
        )
        if signature in seen:
            continue
        seen.add(signature)
        rows.append(item)

    if len(rows) > 9999:
        raise SystemExit("historical observation schema only supports four-digit sequential IDs")
    for index, row in enumerate(rows, start=1):
        row["id"] = f"ALC1737-var-{index:04d}"
        row["sourceId"] = "ALC1737"
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> bytes:
    data = ("\n".join(compact_json(row) for row in rows) + ("\n" if rows else "")).encode("utf-8")
    path.write_bytes(data)
    return data


def write_index_csv(path: Path, rows: list[dict[str, Any]]) -> bytes:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=INDEX_FIELDS, lineterminator="\n", extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            flat = dict(row)
            flat["pageRangeDigital"] = ";".join(str(value) for value in row.get("pageRangeDigital") or [])
            flat["labelClasses"] = ";".join(row.get("labelClasses") or [])
            flat["labelsRaw"] = ";".join(row.get("labelsRaw") or [])
            writer.writerow(flat)
    return path.read_bytes()


def write_coverage_csv(path: Path, rows: list[dict[str, Any]]) -> bytes:
    fields = [
        "sourceId",
        "sourcePageDigital",
        "sourcePagePrinted",
        "section",
        "materialRole",
        "coverage",
        "reviewStatus",
        "transcriptionFile",
        "notes",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return path.read_bytes()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=ROOT / "build" / "historical-variation-index",
        help="Output directory for the derived index.",
    )
    args = parser.parse_args()
    out_dir = args.out_dir if args.out_dir.is_absolute() else ROOT / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    page_rows, page_observations, page_inputs = scan_page_transcriptions()
    lex_rows, lex_observations, lex_inputs, article_count = scan_lexicon()
    grammar_rows, grammar_inputs, grammar_object_count = scan_grammar()
    coverage_rows, coverage_summary = load_coverage()

    rows = page_rows + lex_rows + grammar_rows
    rows.sort(key=record_sort_key)
    for index, row in enumerate(rows, start=1):
        row["evidenceId"] = f"CHD-var-evidence-{index:05d}"

    observations = deduplicate_observations(page_observations + lex_observations)

    payloads = {
        INDEX_JSONL: write_jsonl(out_dir / INDEX_JSONL, rows),
        INDEX_CSV: write_index_csv(out_dir / INDEX_CSV, rows),
        OBSERVATIONS_JSONL: write_jsonl(out_dir / OBSERVATIONS_JSONL, observations),
        COVERAGE_CSV: write_coverage_csv(out_dir / COVERAGE_CSV, coverage_rows),
    }

    label_counts: Counter[str] = Counter()
    layer_counts = Counter(row["sourceLayer"] for row in rows)
    kind_counts = Counter(row["evidenceKind"] for row in rows)
    page_mentions: defaultdict[int, int] = defaultdict(int)
    human_verified_count = 0
    for row in rows:
        for label in row["labelClasses"]:
            label_counts[label] += 1
        if isinstance(row.get("sourcePageDigital"), int):
            page_mentions[row["sourcePageDigital"]] += 1
        if row["humanVerified"]:
            human_verified_count += 1

    canonical_inputs = sorted(set(page_inputs + lex_inputs + grammar_inputs + [TRANSCRIPTION_STATUS.relative_to(ROOT).as_posix()]))
    manifest = {
        "sourceId": "ALC1737",
        "dataset": "post_v1_historical_variation_index",
        "canonicalDatasetVersion": CANONICAL_VERSION,
        "canonicalTag": CANONICAL_TAG,
        "canonicalTagCommit": CANONICAL_TAG_COMMIT,
        "derivation": (
            "Explicit documentary labels and already-structured historical-variety metadata from canonical CHD transcription, lexicon and grammar layers"
        ),
        "evidenceRecordCount": len(rows),
        "schemaObservationCount": len(observations),
        "lexicalArticleCountScanned": article_count,
        "grammarObjectCountScanned": grammar_object_count,
        "labelClassCounts": dict(sorted(label_counts.items())),
        "sourceLayerCounts": dict(sorted(layer_counts.items())),
        "evidenceKindCounts": dict(sorted(kind_counts.items())),
        "digitalPagesWithIndexedEvidence": sorted(page_mentions),
        "digitalPageEvidenceCounts": {str(key): page_mentions[key] for key in sorted(page_mentions)},
        "humanVerifiedEvidenceCount": human_verified_count,
        "coverage": coverage_summary,
        "coverageClaim": {
            "exhaustiveAcrossCurrentCanonicalMachineReadableLayers": True,
            "exhaustiveDiplomaticTranscriptionOfAll182Pages": False,
            "reason": (
                "The index scans every currently canonical machine-readable transcription, lexicon and grammar object, while transcription status still marks some textual pages as pending/unreviewed."
            ),
        },
        "authorityPolicy": {
            "modernLanguageIdentityInferred": False,
            "dialectTaxonomyInferred": False,
            "linguisticSimilarityUsed": False,
            "cognacyInferred": False,
            "sourceLabelsRemainHistoricalDocumentaryEvidence": True,
        },
        "observationSchema": OBSERVATION_SCHEMA.relative_to(ROOT).as_posix(),
        "canonicalInputCount": len(canonical_inputs),
        "canonicalInputs": canonical_inputs,
        "deterministic": True,
        "formats": {
            name: {"bytes": len(data), "sha256": sha256(data)}
            for name, data in sorted(payloads.items())
        },
    }
    manifest_bytes = (
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    ).encode("utf-8")
    (out_dir / MANIFEST_JSON).write_bytes(manifest_bytes)

    for name, metadata in manifest["formats"].items():
        actual = (out_dir / name).read_bytes()
        if len(actual) != metadata["bytes"] or sha256(actual) != metadata["sha256"]:
            raise SystemExit(f"integrity mismatch after writing {name}")

    print(
        "historical variation index generated: "
        f"evidence={len(rows)}; observations={len(observations)}; "
        f"labels={dict(sorted(label_counts.items()))}; "
        f"pagesWithEvidence={len(page_mentions)}"
    )
    print(
        "coverage: "
        f"182 pages accounted; transcriptionFiles={coverage_summary['transcriptionFilePageCount']}; "
        f"pendingOrUnreviewed={coverage_summary['pendingOrUnreviewedPageCount']}"
    )
    print(f"output: {out_dir}")


if __name__ == "__main__":
    main()

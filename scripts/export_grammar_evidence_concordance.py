#!/usr/bin/env python3
"""Export a conservative concordance of explicit evidence in data/grammar.

The concordance flattens forms, markers, headwords, lemmas and examples that are
already explicitly structured in the canonical grammar objects. It does not
normalize forms, infer linguistic identity across objects, or assign token-level
pages when the source object provides only a broader page span.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
GRAMMAR_DIR = ROOT / "data/grammar"

JSONL_NAME = "chd_grammar_evidence_concordance.jsonl"
CSV_NAME = "chd_grammar_evidence_concordance.csv"
MANIFEST_NAME = "manifest.json"

CSV_FIELDS = [
    "concordanceRowId",
    "sourceObjectId",
    "sourceObjectKey",
    "sourceFile",
    "sourceRecordIndex",
    "objectKind",
    "part",
    "ruleReferenceRaw",
    "sourcePagesDigital",
    "sourcePagesPrinted",
    "pageLocatorKind",
    "evidencePath",
    "evidenceRole",
    "rawText",
    "glossRaw",
    "varietyRaw",
    "reviewStatus",
    "humanVerified",
]

FIELD_ROLES = {
    "lemmaRaw": "lemma",
    "lemmaFormsRaw": "lemma",
    "headwordRaw": "headword",
    "formationMarkersRaw": "formation_marker",
    "particleRaw": "particle",
    "alternativesRaw": "alternative_form",
    "hiaquiExamplesRaw": "historical_variety_example",
    "examplesRaw": "example",
}


def compact_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def object_kind(path: Path) -> str:
    name = path.name
    prefixes = [
        ("rules_", "rule"),
        ("paradigms_", "paradigm"),
        ("modal_constructions_", "modal_construction"),
        ("nonfinite_constructions_", "nonfinite_construction"),
        ("participles_", "participial_construction"),
        ("predicative_modal_", "predicative_modal_construction"),
        ("irregular_verbs_", "irregular_verb_group"),
        ("prepositions_", "preposition_entry"),
        ("adverbs_", "adverb_group"),
        ("conjunctions_", "conjunction_group"),
        ("numerals_", "numeral_system"),
    ]
    for prefix, kind in prefixes:
        if name.startswith(prefix):
            return kind
    return "grammar_object"


def load_objects() -> list[tuple[Path, int, dict[str, Any]]]:
    objects: list[tuple[Path, int, dict[str, Any]]] = []
    for path in sorted(GRAMMAR_DIR.iterdir()):
        if not path.is_file():
            continue
        if path.suffix == ".jsonl":
            for record_index, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                if not line.strip():
                    continue
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise SystemExit(f"invalid JSON in {path}:{record_index}: {exc}") from exc
                if not isinstance(obj, dict):
                    raise SystemExit(f"grammar record is not an object: {path}:{record_index}")
                objects.append((path, record_index, obj))
        elif path.suffix == ".json":
            try:
                obj = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                raise SystemExit(f"invalid JSON in {path}: {exc}") from exc
            if not isinstance(obj, dict):
                raise SystemExit(f"grammar JSON root is not an object: {path}")
            objects.append((path, 1, obj))
    return objects


def pages_for_object(obj: dict[str, Any]) -> tuple[list[int], list[int], str]:
    digital: list[int] = []
    printed: list[int] = []
    locator_kind = "not_recorded"

    if isinstance(obj.get("sourcePagesDigital"), list):
        digital = [value for value in obj["sourcePagesDigital"] if isinstance(value, int)]
        locator_kind = "explicit_page_list"
    elif isinstance(obj.get("sourcePageDigital"), int):
        digital = [obj["sourcePageDigital"]]
        locator_kind = "explicit_single_page"
    elif isinstance(obj.get("pageRangeDigital"), list):
        digital = [value for value in obj["pageRangeDigital"] if isinstance(value, int)]
        locator_kind = "range_endpoints"

    if isinstance(obj.get("sourcePagesPrinted"), list):
        printed = [value for value in obj["sourcePagesPrinted"] if isinstance(value, int)]
    elif isinstance(obj.get("sourcePagePrinted"), int):
        printed = [obj["sourcePagePrinted"]]

    return digital, printed, locator_kind


def rule_reference(obj: dict[str, Any]) -> str | None:
    for key in ("sourceRuleRange", "ruleNumberRaw"):
        value = obj.get(key)
        if isinstance(value, str) and value.strip():
            return value
    value = obj.get("ruleNumberNumeric")
    return str(value) if isinstance(value, int) else None


def role_for_form(path_parts: tuple[str, ...]) -> str:
    if "cells" in path_parts:
        return "paradigm_form"
    if "systems" in path_parts or "cardinals" in path_parts:
        return "numeral_form"
    if "itemsRaw" in path_parts:
        return "item_form"
    return "form"


def child_context(current: dict[str, Any], inherited_gloss: str | None, inherited_variety: str | None) -> tuple[str | None, str | None]:
    gloss = inherited_gloss
    for key in ("glossRaw", "sourceGlossRaw"):
        value = current.get(key)
        if isinstance(value, str) and value.strip():
            gloss = value
            break

    variety = inherited_variety
    for key in ("varietyRaw", "historicalVariety"):
        value = current.get(key)
        if isinstance(value, str) and value.strip() and value != "unspecified":
            variety = value
            break
    return gloss, variety


def flatten_strings(value: Any) -> Iterable[tuple[int | None, str]]:
    if isinstance(value, str):
        if value.strip():
            yield None, value
        return
    if isinstance(value, list):
        for index, item in enumerate(value):
            if isinstance(item, str) and item.strip():
                yield index, item


def extract_evidence(obj: dict[str, Any]) -> list[dict[str, Any]]:
    emitted: list[dict[str, Any]] = []

    def walk(value: Any, path_parts: tuple[str, ...], gloss: str | None, variety: str | None) -> None:
        if isinstance(value, dict):
            local_gloss, local_variety = child_context(value, gloss, variety)
            for key, child in value.items():
                child_path = path_parts + (key,)

                if key == "formRaw":
                    for index, text in flatten_strings(child):
                        final_path = child_path if index is None else child_path + (str(index),)
                        emitted.append(
                            {
                                "evidencePath": ".".join(final_path),
                                "evidenceRole": role_for_form(path_parts),
                                "rawText": text,
                                "glossRaw": local_gloss,
                                "varietyRaw": local_variety,
                            }
                        )
                    continue

                if key == "formsRaw":
                    role = "item_form" if "itemsRaw" in path_parts else "form"
                    for index, text in flatten_strings(child):
                        final_path = child_path if index is None else child_path + (str(index),)
                        emitted.append(
                            {
                                "evidencePath": ".".join(final_path),
                                "evidenceRole": role,
                                "rawText": text,
                                "glossRaw": local_gloss,
                                "varietyRaw": local_variety,
                            }
                        )
                    continue

                if key in FIELD_ROLES:
                    for index, text in flatten_strings(child):
                        final_path = child_path if index is None else child_path + (str(index),)
                        emitted.append(
                            {
                                "evidencePath": ".".join(final_path),
                                "evidenceRole": FIELD_ROLES[key],
                                "rawText": text,
                                "glossRaw": local_gloss,
                                "varietyRaw": local_variety,
                            }
                        )
                    continue

                walk(child, child_path, local_gloss, local_variety)
            return

        if isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, path_parts + (str(index),), gloss, variety)

    walk(obj, tuple(), None, None)
    return emitted


def build_rows() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    objects = load_objects()
    rows: list[dict[str, Any]] = []
    source_files: set[str] = set()
    kind_counts: Counter[str] = Counter()
    object_status_counts: Counter[str] = Counter()
    human_verified_count = 0

    for path, record_index, obj in objects:
        relative = path.relative_to(ROOT).as_posix()
        source_files.add(relative)
        kind = object_kind(path)
        kind_counts[kind] += 1
        status = obj.get("reviewStatus") if isinstance(obj.get("reviewStatus"), str) else None
        object_status_counts[str(status)] += 1
        human_verified = obj.get("humanVerified") is True
        if human_verified:
            human_verified_count += 1

        source_object_id = obj.get("id") if isinstance(obj.get("id"), str) else None
        source_object_key = source_object_id or f"{relative}#record-{record_index}"
        digital_pages, printed_pages, locator_kind = pages_for_object(obj)

        for evidence in extract_evidence(obj):
            rows.append(
                {
                    "concordanceRowId": None,
                    "sourceObjectId": source_object_id,
                    "sourceObjectKey": source_object_key,
                    "sourceFile": relative,
                    "sourceRecordIndex": record_index,
                    "objectKind": kind,
                    "part": obj.get("part") or obj.get("section"),
                    "ruleReferenceRaw": rule_reference(obj),
                    "sourcePagesDigital": digital_pages,
                    "sourcePagesPrinted": printed_pages,
                    "pageLocatorKind": locator_kind,
                    **evidence,
                    "reviewStatus": status,
                    "humanVerified": human_verified,
                }
            )

    rows.sort(
        key=lambda row: (
            row["sourceFile"],
            row["sourceRecordIndex"],
            row["evidencePath"],
            row["evidenceRole"],
            row["rawText"],
        )
    )
    for index, row in enumerate(rows, 1):
        row["concordanceRowId"] = f"CHD-GRAM-CONC-{index:06d}"

    evidence_role_counts = Counter(row["evidenceRole"] for row in rows)
    manifest_core = {
        "sourceId": "ALC1737",
        "dataset": "historical_grammar_evidence_concordance",
        "derivation": "deterministic flattening of explicitly structured form/example evidence in data/grammar",
        "canonicalInputPattern": "data/grammar/*.jsonl and data/grammar/*.json",
        "canonicalInputFileCount": len(source_files),
        "canonicalObjectCount": len(objects),
        "evidenceRowCount": len(rows),
        "objectKindCounts": dict(sorted(kind_counts.items())),
        "objectReviewStatusCounts": dict(sorted(object_status_counts.items())),
        "evidenceRoleCounts": dict(sorted(evidence_role_counts.items())),
        "humanVerifiedObjectCount": human_verified_count,
        "linguisticIdentityInferred": False,
        "normalizedFormGenerated": False,
        "crossObjectLinkingPerformed": False,
        "tokenPagePrecisionInferred": False,
        "canonicalGrammarModified": False,
        "deterministic": True,
        "sortOrder": "sourceFile, sourceRecordIndex, evidencePath, evidenceRole, rawText",
        "canonicalInputs": sorted(source_files),
    }
    return rows, manifest_core


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> bytes:
    data = ("\n".join(compact_json(row) for row in rows) + ("\n" if rows else "")).encode("utf-8")
    path.write_bytes(data)
    return data


def csv_value(value: Any) -> Any:
    if isinstance(value, (dict, list)):
        return compact_json(value)
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    return value


def write_csv(path: Path, rows: list[dict[str, Any]]) -> bytes:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: csv_value(row.get(field)) for field in CSV_FIELDS})
    return path.read_bytes()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=ROOT / "build/grammar-evidence-concordance",
        help="Directory for derived grammar concordance outputs.",
    )
    args = parser.parse_args()

    rows, manifest = build_rows()
    if not rows:
        raise SystemExit("grammar concordance is empty; refusing empty export")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    payloads = {
        JSONL_NAME: write_jsonl(args.out_dir / JSONL_NAME, rows),
        CSV_NAME: write_csv(args.out_dir / CSV_NAME, rows),
    }
    manifest["formats"] = {
        name: {"bytes": len(data), "sha256": sha256_bytes(data)}
        for name, data in sorted(payloads.items())
    }
    (args.out_dir / MANIFEST_NAME).write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )

    for name, metadata in manifest["formats"].items():
        actual = (args.out_dir / name).read_bytes()
        if len(actual) != metadata["bytes"] or sha256_bytes(actual) != metadata["sha256"]:
            raise SystemExit(f"post-write integrity check failed for {name}")

    print(
        "exported grammar evidence concordance: "
        f"{manifest['canonicalObjectCount']} objects from {manifest['canonicalInputFileCount']} files; "
        f"{manifest['evidenceRowCount']} evidence rows; roles={manifest['evidenceRoleCounts']}; "
        f"outputs in {args.out_dir}"
    )
    for name, metadata in manifest["formats"].items():
        print(f"  {name}: {metadata['bytes']} bytes; sha256 {metadata['sha256']}")


if __name__ == "__main__":
    main()

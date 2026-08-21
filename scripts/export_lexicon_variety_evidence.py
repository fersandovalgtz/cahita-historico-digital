#!/usr/bin/env python3
"""Export explicit/candidate historical-variety evidence from the lexicon.

The exporter distinguishes already structured form metadata from conservative
surface mentions in transcriptionRaw. It never assigns a variety to an
unlabelled form by linguistic similarity.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
ARTICLE_DIR = ROOT / "data/lexicon/articles"

JSONL_NAME = "chd_lexicon_variety_evidence.jsonl"
CSV_NAME = "chd_lexicon_variety_evidence.csv"
MANIFEST_NAME = "manifest.json"

CSV_FIELDS = [
    "articleId",
    "sourcePageDigital",
    "column",
    "spanishGuideRaw",
    "evidenceKind",
    "labelClass",
    "labelRaw",
    "formRaw",
    "sourceQualifierRaw",
    "historicalVarietyStructured",
    "transcriptionRaw",
]

SURFACE_LABELS = {
    "Hiaqui": re.compile(r"\bhiaquis?\b"),
    "Mayo": re.compile(r"\bmayos?\b"),
    "Thehueco": re.compile(r"\bthehuecos?\b"),
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def compact_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def article_number(article_id: str) -> int:
    return int(article_id.rsplit("-", 1)[1])


def normalize(text: str) -> str:
    value = unicodedata.normalize("NFKC", text).replace("ſ", "s").casefold()
    return " ".join(value.split())


def class_from_raw_label(value: str | None) -> str:
    if not value:
        return "other_explicit_source_label"
    normalized = normalize(value)
    if SURFACE_LABELS["Hiaqui"].search(normalized):
        return "Hiaqui"
    if SURFACE_LABELS["Mayo"].search(normalized):
        return "Mayo"
    if SURFACE_LABELS["Thehueco"].search(normalized):
        return "Thehueco"
    return "other_explicit_source_label"


def load_evidence() -> tuple[list[dict[str, Any]], int, list[str]]:
    rows: list[dict[str, Any]] = []
    article_count = 0
    source_files: list[str] = []

    for path in sorted(ARTICLE_DIR.glob("*.jsonl")):
        source_files.append(path.relative_to(ROOT).as_posix())
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                article = json.loads(line)
            except json.JSONDecodeError as exc:
                raise SystemExit(f"invalid JSON in {path}:{line_number}: {exc}") from exc
            article_count += 1
            base = {
                "articleId": article["articleId"],
                "sourcePageDigital": article.get("sourcePageDigital"),
                "column": article.get("column"),
                "spanishGuideRaw": article.get("spanishGuideRaw"),
                "transcriptionRaw": article.get("transcriptionRaw"),
            }

            for form in article.get("cahitaFormsRaw") or []:
                structured = form.get("historicalVariety", "unspecified")
                qualifier = form.get("sourceQualifierRaw")
                if structured == "unspecified" and not qualifier:
                    continue
                if structured != "unspecified":
                    label_class = structured
                else:
                    label_class = class_from_raw_label(qualifier)
                rows.append(
                    {
                        **base,
                        "evidenceKind": "structured_form_metadata",
                        "labelClass": label_class,
                        "labelRaw": qualifier,
                        "formRaw": form.get("formRaw"),
                        "sourceQualifierRaw": qualifier,
                        "historicalVarietyStructured": structured,
                    }
                )

            transcription = article.get("transcriptionRaw")
            if isinstance(transcription, str) and transcription:
                normalized = normalize(transcription)
                for label_class, pattern in SURFACE_LABELS.items():
                    matches = list(pattern.finditer(normalized))
                    for surface_index, _match in enumerate(matches):
                        rows.append(
                            {
                                **base,
                                "evidenceKind": "transcription_surface_candidate",
                                "labelClass": label_class,
                                "labelRaw": label_class,
                                "formRaw": None,
                                "sourceQualifierRaw": None,
                                "historicalVarietyStructured": None,
                                "surfaceOccurrenceIndex": surface_index,
                            }
                        )

    rows.sort(
        key=lambda row: (
            article_number(row["articleId"]),
            row["evidenceKind"],
            row["labelClass"],
            int(row.get("surfaceOccurrenceIndex", 0)),
            str(row.get("formRaw") or ""),
        )
    )
    return rows, article_count, source_files


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> bytes:
    data = ("\n".join(compact_json(row) for row in rows) + ("\n" if rows else "")).encode("utf-8")
    path.write_bytes(data)
    return data


def write_csv(path: Path, rows: list[dict[str, Any]]) -> bytes:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return path.read_bytes()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=ROOT / "build/lexicon-variety-evidence",
        help="Directory for derived historical-variety evidence.",
    )
    args = parser.parse_args()

    rows, article_count, source_files = load_evidence()
    if not rows:
        raise SystemExit("no historical-variety evidence found in canonical lexicon")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    payloads = {
        JSONL_NAME: write_jsonl(args.out_dir / JSONL_NAME, rows),
        CSV_NAME: write_csv(args.out_dir / CSV_NAME, rows),
    }

    kind_counts = Counter(row["evidenceKind"] for row in rows)
    label_counts = Counter(row["labelClass"] for row in rows)
    article_ids = {row["articleId"] for row in rows}

    manifest = {
        "sourceId": "ALC1737",
        "dataset": "historical_variety_evidence",
        "derivation": "structured form metadata plus conservative surface-label candidates from canonical transcriptionRaw",
        "canonicalInputPattern": "data/lexicon/articles/*.jsonl",
        "canonicalInputFileCount": len(source_files),
        "canonicalArticleCountScanned": article_count,
        "evidenceRecordCount": len(rows),
        "articleCountWithEvidence": len(article_ids),
        "evidenceKindCounts": dict(sorted(kind_counts.items())),
        "labelClassCounts": dict(sorted(label_counts.items())),
        "surfaceLabelVocabulary": sorted(SURFACE_LABELS),
        "varietyAttributionInferred": False,
        "linguisticSimilarityUsed": False,
        "deterministic": True,
        "formats": {
            name: {"bytes": len(data), "sha256": sha256_bytes(data)}
            for name, data in sorted(payloads.items())
        },
        "canonicalInputs": source_files,
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
        "exported historical-variety evidence: "
        f"{len(rows)} records in {len(article_ids)} article(s); "
        f"labels={dict(sorted(label_counts.items()))}; outputs in {args.out_dir}"
    )
    for name, metadata in manifest["formats"].items():
        print(f"  {name}: {metadata['bytes']} bytes; sha256 {metadata['sha256']}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Export the explicit facsimile-recollation queue for historical Buſca reviews.

This derived queue is intentionally narrow: it contains only source-review
records whose current decision is `source_or_destination_requires_recollation`.
It does not create destinations, widen the strict graph, or promote OCR readings.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REVIEW_DIR = ROOT / "data/lexicon/review"
REVIEW_PATTERN = "crossreference_source_review_*.jsonl"
DECISION = "source_or_destination_requires_recollation"

JSONL_NAME = "chd_crossreference_recollation_queue.jsonl"
CSV_NAME = "chd_crossreference_recollation_queue.csv"
MANIFEST_NAME = "manifest.json"

CSV_FIELDS = [
    "queueRank",
    "reviewId",
    "sourceReviewFile",
    "sourceArticleId",
    "crossReferenceIndex",
    "sourcePageDigital",
    "sourceColumn",
    "sourceGuideRaw",
    "targetRaw",
    "targetNormalized",
    "priorityTier",
    "diagnosticCandidateCount",
    "diagnosticCandidateIds",
    "evidenceKinds",
    "evidenceLocators",
    "reviewNote",
    "currentStatus",
    "requiredAction",
    "humanVerified",
]

TIER_ORDER = {
    "A_unique_strong": 0,
    "B_multiple_strong": 1,
    "C_no_strong": 2,
}
COLUMN_ORDER = {"left": 0, "right": 1}


def compact_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def article_number(article_id: str) -> int:
    return int(article_id.rsplit("-", 1)[1])


def load_reviews() -> tuple[list[dict[str, Any]], list[str]]:
    reviews: list[dict[str, Any]] = []
    source_files: list[str] = []
    for path in sorted(REVIEW_DIR.glob(REVIEW_PATTERN)):
        rel = path.relative_to(ROOT).as_posix()
        source_files.append(rel)
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise SystemExit(f"invalid JSON in {rel}:{line_number}: {exc}") from exc
            if not isinstance(row, dict):
                raise SystemExit(f"non-object JSON value in {rel}:{line_number}")
            row = dict(row)
            row["__sourceReviewFile"] = rel
            row["__line"] = line_number
            reviews.append(row)
    if not source_files:
        raise SystemExit("no cross-reference source-review files found")
    return reviews, source_files


def build_queue() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    reviews, source_files = load_reviews()
    selected = [row for row in reviews if row.get("decisionStatus") == DECISION]

    selected.sort(
        key=lambda row: (
            TIER_ORDER.get(str(row.get("priorityTier")), 99),
            int(row.get("sourcePageDigital") or 0),
            COLUMN_ORDER.get(str(row.get("sourceColumn")), 9),
            article_number(str(row["sourceArticleId"])),
            int(row.get("crossReferenceIndex") or 0),
        )
    )

    rows: list[dict[str, Any]] = []
    for rank, source in enumerate(selected, 1):
        if source.get("humanVerified") is not False:
            raise SystemExit(
                f"recollation queue must remain non-human-verified: {source.get('reviewId')}"
            )
        candidates = source.get("diagnosticCandidates") or []
        evidence = source.get("evidence") or []
        row = {
            "queueRank": rank,
            "reviewId": source.get("reviewId"),
            "sourceReviewFile": source["__sourceReviewFile"],
            "sourceArticleId": source.get("sourceArticleId"),
            "crossReferenceIndex": source.get("crossReferenceIndex"),
            "sourcePageDigital": source.get("sourcePageDigital"),
            "sourceColumn": source.get("sourceColumn"),
            "sourceGuideRaw": source.get("sourceGuideRaw"),
            "targetRaw": source.get("targetRaw"),
            "targetNormalized": source.get("targetNormalized"),
            "priorityTier": source.get("priorityTier"),
            "diagnosticCandidates": candidates,
            "diagnosticCandidateCount": len(candidates),
            "evidence": evidence,
            "reviewNote": source.get("reviewNote"),
            "currentDecisionStatus": DECISION,
            "currentStatus": "awaiting_direct_facsimile_recollation",
            "requiredAction": "collate_source_and_destination_against_same_witness_page_image",
            "humanVerified": False,
        }
        rows.append(row)

    tier_counts = Counter(str(row.get("priorityTier")) for row in rows)
    page_counts = Counter(int(row["sourcePageDigital"]) for row in rows)
    manifest = {
        "sourceId": "ALC1737",
        "queueSemantics": (
            "explicit source-review records requiring direct same-witness facsimile recollation; "
            "no automatic destination promotion"
        ),
        "sourceReviewPattern": f"data/lexicon/review/{REVIEW_PATTERN}",
        "sourceReviewFileCount": len(source_files),
        "sourceReviewRecordCount": len(reviews),
        "decisionFilter": DECISION,
        "queueCount": len(rows),
        "priorityTierCounts": {
            tier: int(tier_counts.get(tier, 0))
            for tier in ("A_unique_strong", "B_multiple_strong", "C_no_strong")
        },
        "sourcePageCounts": {str(page): count for page, count in sorted(page_counts.items())},
        "humanVerifiedCount": 0,
        "canonicalStrictGraphModified": False,
        "sourceReviewFiles": source_files,
    }
    return rows, manifest


def write_outputs(output_dir: Path) -> tuple[dict[str, str], dict[str, int], dict[str, Any]]:
    rows, manifest = build_queue()
    output_dir.mkdir(parents=True, exist_ok=True)

    jsonl_bytes = (
        "".join(compact_json(row) + "\n" for row in rows).encode("utf-8")
    )
    (output_dir / JSONL_NAME).write_bytes(jsonl_bytes)

    csv_path = output_dir / CSV_NAME
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "queueRank": row["queueRank"],
                    "reviewId": row["reviewId"],
                    "sourceReviewFile": row["sourceReviewFile"],
                    "sourceArticleId": row["sourceArticleId"],
                    "crossReferenceIndex": row["crossReferenceIndex"],
                    "sourcePageDigital": row["sourcePageDigital"],
                    "sourceColumn": row["sourceColumn"],
                    "sourceGuideRaw": row["sourceGuideRaw"],
                    "targetRaw": row["targetRaw"],
                    "targetNormalized": row["targetNormalized"],
                    "priorityTier": row["priorityTier"],
                    "diagnosticCandidateCount": row["diagnosticCandidateCount"],
                    "diagnosticCandidateIds": "|".join(
                        str(item.get("candidateArticleId", ""))
                        for item in row["diagnosticCandidates"]
                    ),
                    "evidenceKinds": "|".join(
                        str(item.get("evidenceKind", "")) for item in row["evidence"]
                    ),
                    "evidenceLocators": " | ".join(
                        str(item.get("locator", "")) for item in row["evidence"]
                    ),
                    "reviewNote": row["reviewNote"],
                    "currentStatus": row["currentStatus"],
                    "requiredAction": row["requiredAction"],
                    "humanVerified": "false",
                }
            )

    csv_bytes = csv_path.read_bytes()
    hashes = {
        JSONL_NAME: sha256_bytes(jsonl_bytes),
        CSV_NAME: sha256_bytes(csv_bytes),
    }
    sizes = {
        JSONL_NAME: len(jsonl_bytes),
        CSV_NAME: len(csv_bytes),
    }
    manifest = dict(manifest)
    manifest["artifacts"] = {
        name: {"bytes": sizes[name], "sha256": hashes[name]}
        for name in (JSONL_NAME, CSV_NAME)
    }
    manifest_bytes = (json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode(
        "utf-8"
    )
    (output_dir / MANIFEST_NAME).write_bytes(manifest_bytes)
    hashes[MANIFEST_NAME] = sha256_bytes(manifest_bytes)
    sizes[MANIFEST_NAME] = len(manifest_bytes)
    return hashes, sizes, manifest


def print_next(rows: list[dict[str, Any]], limit: int) -> None:
    for row in rows[:limit]:
        candidates = ", ".join(
            f"{item.get('candidateArticleId')} [{item.get('candidateGuideRaw')}]"
            for item in row["diagnosticCandidates"]
        ) or "—"
        print(
            f"{row['queueRank']:02d}. {row['reviewId']} | p{row['sourcePageDigital']} {row['sourceColumn']} | "
            f"{row['sourceGuideRaw']} → {row['targetRaw']} | tier={row['priorityTier']} | candidates={candidates}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist" / "recollation")
    parser.add_argument("--print-next", type=int, default=0)
    args = parser.parse_args()

    hashes, sizes, manifest = write_outputs(args.output_dir)
    print(
        "exported cross-reference facsimile-recollation queue: "
        f"{manifest['queueCount']} cases from {manifest['sourceReviewRecordCount']} reviews; "
        f"tiers={manifest['priorityTierCounts']}; humanVerified=0; canonical strict graph modified=0"
    )
    for name in (JSONL_NAME, CSV_NAME, MANIFEST_NAME):
        print(f"  {name}: {sizes[name]} bytes; sha256 {hashes[name]}")
    if args.print_next > 0:
        rows, _manifest = build_queue()
        print_next(rows, args.print_next)


if __name__ == "__main__":
    main()

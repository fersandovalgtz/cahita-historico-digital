#!/usr/bin/env python3
"""Export the deterministic queue of unresolved cross-references still awaiting source review.

This queue subtracts explicit source-review overlays from the non-binding diagnostic
inventory. It is workflow state, not a resolution layer: rows remain strict
``not_located`` references and diagnostic candidates remain non-canonical until a
separate source-review record is added.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

from export_crossreference_candidate_diagnostics import build_diagnostics
from export_lexicon_crossreference_reviewed_view import load_source_reviews

ROOT = Path(__file__).resolve().parents[1]
JSONL_NAME = "chd_crossreference_review_queue.jsonl"
CSV_NAME = "chd_crossreference_review_queue.csv"
MANIFEST_NAME = "manifest.json"
PRIORITY_TIERS = ("A_unique_strong", "B_multiple_strong", "C_no_strong")

CSV_FIELDS = [
    "sourceArticleId",
    "sourcePageDigital",
    "sourceColumn",
    "sourceGuideRaw",
    "crossReferenceIndex",
    "targetRaw",
    "targetNormalized",
    "priorityTier",
    "strongCandidateCountShown",
    "candidateCountShown",
    "topCandidateArticleId",
    "topCandidatePageDigital",
    "topCandidateColumn",
    "topCandidateGuideRaw",
    "topCandidateDiagnosticClass",
    "topCandidateDiagnosticScore",
    "queueStatus",
    "policy",
]


def compact_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def build_queue(max_candidates: int = 5) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    diagnostics, diagnostic_meta = build_diagnostics(max_candidates)
    reviews, review_files = load_source_reviews()

    diagnostic_keys = {
        (row["sourceArticleId"], row["crossReferenceIndex"])
        for row in diagnostics
    }
    review_keys = set(reviews)
    outside = sorted(review_keys - diagnostic_keys)
    if outside:
        raise SystemExit(
            "source-review records do not belong to the strict-not-located diagnostic inventory: "
            f"{outside}"
        )

    queue: list[dict[str, Any]] = []
    for row in diagnostics:
        key = (row["sourceArticleId"], row["crossReferenceIndex"])
        if key in review_keys:
            continue
        queue.append(
            {
                **row,
                "queueStatus": "awaiting_source_review",
                "policy": "diagnostic_priority_only_no_resolution",
            }
        )

    tier_counts = Counter(row["priorityTier"] for row in queue)
    strong_counts = Counter(str(row["strongCandidateCountShown"]) for row in queue)
    summary = {
        "sourceId": "ALC1737",
        "dataset": "historical_crossreference_source_review_queue",
        "derivation": "strict-not-located diagnostic inventory minus explicit source-review records",
        "strictNotLocatedDiagnosticCount": len(diagnostics),
        "sourceReviewRecordCount": len(reviews),
        "awaitingSourceReviewCount": len(queue),
        "priorityTierCounts": {
            tier: int(tier_counts.get(tier, 0))
            for tier in PRIORITY_TIERS
        },
        "strongCandidateCountShownDistribution": dict(sorted(strong_counts.items())),
        "maxCandidatesShownPerReference": max_candidates,
        "canonicalResolutionPolicy": diagnostic_meta["canonicalResolutionPolicy"],
        "queuePolicy": "workflow_prioritization_only",
        "canonicalStrictGraphModified": False,
        "canonicalArticlesModified": False,
        "diagnosticCandidatesPromotedToEditorial": False,
        "destinationResolutionPerformed": False,
        "semanticEquivalenceInferred": False,
        "humanVerificationPerformed": False,
        "deterministic": True,
        "reviewInputs": review_files,
    }
    return queue, summary


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> bytes:
    payload = ("\n".join(compact_json(row) for row in rows) + ("\n" if rows else "")).encode("utf-8")
    path.write_bytes(payload)
    return payload


def csv_value(value: Any) -> Any:
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
            top = row["candidates"][0] if row.get("candidates") else {}
            writer.writerow(
                {
                    "sourceArticleId": row["sourceArticleId"],
                    "sourcePageDigital": csv_value(row.get("sourcePageDigital")),
                    "sourceColumn": csv_value(row.get("sourceColumn")),
                    "sourceGuideRaw": csv_value(row.get("sourceGuideRaw")),
                    "crossReferenceIndex": row["crossReferenceIndex"],
                    "targetRaw": row["targetRaw"],
                    "targetNormalized": row["targetNormalized"],
                    "priorityTier": row["priorityTier"],
                    "strongCandidateCountShown": row["strongCandidateCountShown"],
                    "candidateCountShown": row["candidateCountShown"],
                    "topCandidateArticleId": csv_value(top.get("articleId")),
                    "topCandidatePageDigital": csv_value(top.get("sourcePageDigital")),
                    "topCandidateColumn": csv_value(top.get("column")),
                    "topCandidateGuideRaw": csv_value(top.get("spanishGuideRaw")),
                    "topCandidateDiagnosticClass": csv_value(top.get("diagnosticClass")),
                    "topCandidateDiagnosticScore": csv_value(top.get("diagnosticScore")),
                    "queueStatus": row["queueStatus"],
                    "policy": row["policy"],
                }
            )
    return path.read_bytes()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=ROOT / "build/crossreference-review-queue",
    )
    parser.add_argument("--max-candidates", type=int, default=5)
    parser.add_argument(
        "--print-next",
        type=int,
        default=0,
        help="After deterministic export, print the first N queued rows in review order.",
    )
    parser.add_argument(
        "--tier",
        choices=PRIORITY_TIERS,
        default=None,
        help="When used with --print-next, restrict printed rows to one priority tier; files remain complete.",
    )
    args = parser.parse_args()

    if args.print_next < 0:
        raise SystemExit("--print-next must be zero or greater")

    rows, manifest = build_queue(args.max_candidates)
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

    for name, info in manifest["formats"].items():
        actual = (args.out_dir / name).read_bytes()
        if len(actual) != info["bytes"] or sha256_bytes(actual) != info["sha256"]:
            raise SystemExit(f"post-write integrity check failed for {name}")

    print(
        "exported cross-reference source-review queue: "
        f"strictNotLocated={manifest['strictNotLocatedDiagnosticCount']}; "
        f"reviewed={manifest['sourceReviewRecordCount']}; "
        f"awaiting={manifest['awaitingSourceReviewCount']}; "
        f"tiers={manifest['priorityTierCounts']}; canonical strict graph modified=0"
    )
    for name, info in manifest["formats"].items():
        print(f"  {name}: {info['bytes']} bytes; sha256 {info['sha256']}")

    if args.print_next:
        printable = rows
        if args.tier is not None:
            printable = [row for row in printable if row["priorityTier"] == args.tier]
        for row in printable[: args.print_next]:
            print("XREFQUEUE " + compact_json(row))


if __name__ == "__main__":
    main()

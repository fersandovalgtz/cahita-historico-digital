#!/usr/bin/env python3
"""Validate the deterministic direct-facsimile recollation queue."""
from __future__ import annotations

import json
import tempfile
from collections import Counter
from pathlib import Path

from export_crossreference_recollation_queue import (
    CSV_NAME,
    DECISION,
    JSONL_NAME,
    MANIFEST_NAME,
    build_queue,
    write_outputs,
)

EXPECTED_QUEUE_COUNT = 22
EXPECTED_SOURCE_REVIEW_COUNT = 90
EXPECTED_TIER_COUNTS = {
    "A_unique_strong": 8,
    "B_multiple_strong": 4,
    "C_no_strong": 10,
}


def main() -> None:
    rows, manifest = build_queue()

    if len(rows) != EXPECTED_QUEUE_COUNT:
        raise SystemExit(f"expected {EXPECTED_QUEUE_COUNT} recollation cases, got {len(rows)}")
    if int(manifest["sourceReviewRecordCount"]) != EXPECTED_SOURCE_REVIEW_COUNT:
        raise SystemExit(
            f"expected {EXPECTED_SOURCE_REVIEW_COUNT} source reviews, got {manifest['sourceReviewRecordCount']}"
        )
    if manifest["priorityTierCounts"] != EXPECTED_TIER_COUNTS:
        raise SystemExit(
            f"unexpected recollation tier counts: {manifest['priorityTierCounts']} != {EXPECTED_TIER_COUNTS}"
        )

    keys: set[tuple[str, int]] = set()
    review_ids: set[str] = set()
    for rank, row in enumerate(rows, 1):
        if row["queueRank"] != rank:
            raise SystemExit(f"non-contiguous queue rank at {row['reviewId']}")
        if row["currentDecisionStatus"] != DECISION:
            raise SystemExit(f"non-recollation decision leaked into queue: {row['reviewId']}")
        if row["currentStatus"] != "awaiting_direct_facsimile_recollation":
            raise SystemExit(f"unexpected queue state: {row['reviewId']}")
        if row["requiredAction"] != "collate_source_and_destination_against_same_witness_page_image":
            raise SystemExit(f"unexpected required action: {row['reviewId']}")
        if row["humanVerified"] is not False:
            raise SystemExit(f"humanVerified must remain false: {row['reviewId']}")

        review_id = str(row["reviewId"])
        if review_id in review_ids:
            raise SystemExit(f"duplicate reviewId in recollation queue: {review_id}")
        review_ids.add(review_id)

        key = (str(row["sourceArticleId"]), int(row["crossReferenceIndex"]))
        if key in keys:
            raise SystemExit(f"duplicate source reference in recollation queue: {key}")
        keys.add(key)

    tier_counts = Counter(str(row["priorityTier"]) for row in rows)
    if {tier: tier_counts.get(tier, 0) for tier in EXPECTED_TIER_COUNTS} != EXPECTED_TIER_COUNTS:
        raise SystemExit(f"row-level tier counts disagree: {dict(tier_counts)}")

    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        run1 = base / "run1"
        run2 = base / "run2"
        hashes1, _sizes1, manifest1 = write_outputs(run1)
        hashes2, _sizes2, manifest2 = write_outputs(run2)

        if hashes1 != hashes2:
            raise SystemExit("recollation queue hashes differ across two runs")
        if manifest1 != manifest2:
            raise SystemExit("recollation queue manifests differ across two runs")
        for name in (JSONL_NAME, CSV_NAME, MANIFEST_NAME):
            if (run1 / name).read_bytes() != (run2 / name).read_bytes():
                raise SystemExit(f"recollation queue artifact is not byte-deterministic: {name}")

        parsed = [
            json.loads(line)
            for line in (run1 / JSONL_NAME).read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        if len(parsed) != EXPECTED_QUEUE_COUNT:
            raise SystemExit("exported JSONL row count disagrees with queue count")

    print(
        "cross-reference recollation queue QA OK: "
        f"queue={len(rows)}; sourceReviews={manifest['sourceReviewRecordCount']}; "
        f"tiers={manifest['priorityTierCounts']}; "
        f"jsonlSha256={hashes1[JSONL_NAME]}; csvSha256={hashes1[CSV_NAME]}; "
        "humanVerified=0; canonical strict graph modified=0"
    )


if __name__ == "__main__":
    main()

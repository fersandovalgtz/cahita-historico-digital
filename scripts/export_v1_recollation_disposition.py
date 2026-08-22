#!/usr/bin/env python3
"""Export the v1.0 release disposition of unresolved cross-reference recollations.

This layer does NOT resolve the 22 philological cases. It freezes them as
explicit open uncertainties for the v1.0 release scope because direct
same-witness page-image recollation is still required. OCR, diagnostic
similarity and editorial candidates are not promoted to canonical targets.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

from export_crossreference_recollation_queue import build_queue

ROOT = Path(__file__).resolve().parents[1]
JSONL_NAME = "chd_v1_recollation_disposition.jsonl"
CSV_NAME = "chd_v1_recollation_disposition.csv"
MANIFEST_NAME = "manifest.json"

DISPOSITION = "frozen_open_uncertainty"
SOURCE_EVIDENCE_STATUS = "insufficient_without_direct_same_witness_facsimile_recollation"
REQUIRED_EVIDENCE = "direct_same_witness_page_image_recollation_or_explicit_human_philological_review"
POST_V1_ACTION = "reopen_case_when_required_evidence_is_available"

CSV_FIELDS = [
    "queueRank",
    "reviewId",
    "sourceArticleId",
    "crossReferenceIndex",
    "sourcePageDigital",
    "sourceColumn",
    "sourceGuideRaw",
    "targetRaw",
    "priorityTier",
    "disposition",
    "releaseScope",
    "sourceEvidenceStatus",
    "requiredEvidence",
    "canonicalAction",
    "selectedTargetArticleId",
    "humanVerified",
    "postV1Action",
]


def compact_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def build_disposition() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    queue, queue_manifest = build_queue()
    rows: list[dict[str, Any]] = []
    for item in queue:
        rows.append(
            {
                "queueRank": item["queueRank"],
                "reviewId": item["reviewId"],
                "sourceArticleId": item["sourceArticleId"],
                "crossReferenceIndex": item["crossReferenceIndex"],
                "sourcePageDigital": item["sourcePageDigital"],
                "sourceColumn": item["sourceColumn"],
                "sourceGuideRaw": item["sourceGuideRaw"],
                "targetRaw": item["targetRaw"],
                "priorityTier": item["priorityTier"],
                "disposition": DISPOSITION,
                "releaseScope": "v1.0",
                "sourceEvidenceStatus": SOURCE_EVIDENCE_STATUS,
                "requiredEvidence": REQUIRED_EVIDENCE,
                "canonicalAction": "none",
                "selectedTargetArticleId": None,
                "humanVerified": False,
                "postV1Action": POST_V1_ACTION,
            }
        )

    tiers = Counter(row["priorityTier"] for row in rows)
    manifest = {
        "sourceId": "ALC1737",
        "dataset": "v1_recollation_release_disposition",
        "releaseScope": "v1.0",
        "sourceQueueCount": queue_manifest["queueCount"],
        "dispositionCount": len(rows),
        "openUncertaintyCount": len(rows),
        "resolvedByThisLayerCount": 0,
        "canonicalChangesByThisLayerCount": 0,
        "selectedTargetCount": 0,
        "humanVerifiedCount": 0,
        "facsimileResolutionClaimed": False,
        "ocrAcceptedAsFacsimileSubstitute": False,
        "diagnosticSimilarityAcceptedAsCanonicalResolution": False,
        "priorityTierCounts": {
            tier: int(tiers.get(tier, 0))
            for tier in ("A_unique_strong", "B_multiple_strong", "C_no_strong")
        },
        "disposition": DISPOSITION,
        "sourceEvidenceStatus": SOURCE_EVIDENCE_STATUS,
        "requiredEvidence": REQUIRED_EVIDENCE,
        "postV1Action": POST_V1_ACTION,
        "releaseGateDisposition": "closed_for_v1_scope_as_explicit_open_uncertainties",
        "philologicalResolutionStatus": "open",
    }
    return rows, manifest


def write_outputs(output_dir: Path) -> tuple[dict[str, str], dict[str, int], dict[str, Any]]:
    rows, manifest = build_disposition()
    output_dir.mkdir(parents=True, exist_ok=True)

    jsonl_bytes = "".join(compact_json(row) + "\n" for row in rows).encode("utf-8")
    (output_dir / JSONL_NAME).write_bytes(jsonl_bytes)

    csv_path = output_dir / CSV_NAME
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for row in rows:
            flat = dict(row)
            flat["selectedTargetArticleId"] = ""
            flat["humanVerified"] = "false"
            writer.writerow(flat)

    csv_bytes = csv_path.read_bytes()
    hashes = {JSONL_NAME: sha256_bytes(jsonl_bytes), CSV_NAME: sha256_bytes(csv_bytes)}
    sizes = {JSONL_NAME: len(jsonl_bytes), CSV_NAME: len(csv_bytes)}
    manifest = dict(manifest)
    manifest["artifacts"] = {
        name: {"bytes": sizes[name], "sha256": hashes[name]}
        for name in (JSONL_NAME, CSV_NAME)
    }
    manifest_bytes = (json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    (output_dir / MANIFEST_NAME).write_bytes(manifest_bytes)
    hashes[MANIFEST_NAME] = sha256_bytes(manifest_bytes)
    sizes[MANIFEST_NAME] = len(manifest_bytes)
    return hashes, sizes, manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", type=Path, default=ROOT / "dist" / "v1-recollation-disposition")
    args = parser.parse_args()
    hashes, sizes, manifest = write_outputs(args.out_dir)
    print(
        "exported v1 recollation disposition: "
        f"cases={manifest['dispositionCount']}; open={manifest['openUncertaintyCount']}; "
        f"resolved=0; selectedTargets=0; tiers={manifest['priorityTierCounts']}; "
        "humanVerified=0; canonicalChanges=0"
    )
    for name in (JSONL_NAME, CSV_NAME, MANIFEST_NAME):
        print(f"  {name}: {sizes[name]} bytes; sha256 {hashes[name]}")


if __name__ == "__main__":
    main()

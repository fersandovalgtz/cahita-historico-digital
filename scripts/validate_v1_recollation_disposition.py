#!/usr/bin/env python3
"""Validate the v1.0 release disposition of the 22 recollation cases."""
from __future__ import annotations

import tempfile
from collections import Counter
from pathlib import Path

from export_crossreference_recollation_queue import build_queue
from export_lexicon_crossreference_graph import build_resolution
from export_v1_recollation_disposition import (
    DISPOSITION,
    REQUIRED_EVIDENCE,
    SOURCE_EVIDENCE_STATUS,
    build_disposition,
    write_outputs,
)

EXPECTED_TIERS = {
    "A_unique_strong": 8,
    "B_multiple_strong": 4,
    "C_no_strong": 10,
}


def main() -> None:
    queue, queue_manifest = build_queue()
    rows, manifest = build_disposition()

    if len(queue) != 22 or queue_manifest["queueCount"] != 22:
        raise SystemExit("source recollation queue must contain exactly 22 cases")
    if len(rows) != 22 or manifest["dispositionCount"] != 22:
        raise SystemExit("v1 recollation disposition must contain exactly 22 cases")

    source_identity = [(row["reviewId"], row["sourceArticleId"], row["crossReferenceIndex"]) for row in queue]
    disposition_identity = [(row["reviewId"], row["sourceArticleId"], row["crossReferenceIndex"]) for row in rows]
    if source_identity != disposition_identity:
        raise SystemExit("v1 recollation disposition is not identity-preserving against the canonical queue")
    if len(set(disposition_identity)) != 22:
        raise SystemExit("duplicate case identity in v1 recollation disposition")

    tiers = Counter(row["priorityTier"] for row in rows)
    if dict(tiers) != EXPECTED_TIERS:
        raise SystemExit(f"unexpected v1 recollation tier counts: {dict(tiers)}")

    for row in rows:
        if row["disposition"] != DISPOSITION:
            raise SystemExit(f"unexpected disposition: {row['reviewId']}")
        if row["releaseScope"] != "v1.0":
            raise SystemExit(f"unexpected release scope: {row['reviewId']}")
        if row["sourceEvidenceStatus"] != SOURCE_EVIDENCE_STATUS:
            raise SystemExit(f"unexpected evidence status: {row['reviewId']}")
        if row["requiredEvidence"] != REQUIRED_EVIDENCE:
            raise SystemExit(f"unexpected required evidence: {row['reviewId']}")
        if row["canonicalAction"] != "none":
            raise SystemExit(f"v1 disposition attempted canonical action: {row['reviewId']}")
        if row["selectedTargetArticleId"] is not None:
            raise SystemExit(f"v1 disposition selected a target: {row['reviewId']}")
        if row["humanVerified"] is not False:
            raise SystemExit(f"v1 disposition must remain non-human-verified: {row['reviewId']}")

    guards = {
        "openUncertaintyCount": 22,
        "resolvedByThisLayerCount": 0,
        "canonicalChangesByThisLayerCount": 0,
        "selectedTargetCount": 0,
        "humanVerifiedCount": 0,
    }
    for key, value in guards.items():
        if manifest[key] != value:
            raise SystemExit(f"v1 disposition guard drifted: {key}={manifest[key]} != {value}")
    for key in (
        "facsimileResolutionClaimed",
        "ocrAcceptedAsFacsimileSubstitute",
        "diagnosticSimilarityAcceptedAsCanonicalResolution",
    ):
        if manifest[key] is not False:
            raise SystemExit(f"v1 disposition safety guard must remain false: {key}")
    if manifest["priorityTierCounts"] != EXPECTED_TIERS:
        raise SystemExit("v1 disposition manifest tier counts drifted")
    if manifest["releaseGateDisposition"] != "closed_for_v1_scope_as_explicit_open_uncertainties":
        raise SystemExit("v1 release-gate disposition drifted")
    if manifest["philologicalResolutionStatus"] != "open":
        raise SystemExit("philological resolution must remain explicitly open")

    strict_rows, graph, _count, _files = build_resolution()
    statuses = Counter(row["resolutionStatus"] for row in strict_rows)
    if statuses != Counter({"not_located": 90, "exact_unique": 60}):
        raise SystemExit(f"canonical strict graph status drifted: {dict(statuses)}")
    if len(graph.get("edges", [])) != 60:
        raise SystemExit("canonical strict graph edge count drifted")

    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        hashes1, sizes1, manifest1 = write_outputs(base / "run1")
        hashes2, sizes2, manifest2 = write_outputs(base / "run2")
        if hashes1 != hashes2 or sizes1 != sizes2 or manifest1 != manifest2:
            raise SystemExit("v1 recollation disposition is not deterministic across two runs")
        files1 = sorted((base / "run1").iterdir())
        files2 = sorted((base / "run2").iterdir())
        if [p.name for p in files1] != [p.name for p in files2]:
            raise SystemExit("v1 recollation disposition output file sets differ")
        for first, second in zip(files1, files2):
            if first.read_bytes() != second.read_bytes():
                raise SystemExit(f"v1 recollation disposition bytes differ: {first.name}")

    print(
        "v1 recollation disposition QA OK: cases=22; tiers=8/4/10; "
        "openUncertainties=22; resolved=0; selectedTargets=0; canonicalChanges=0; "
        "humanVerified=0; philologicalResolution=open"
    )


if __name__ == "__main__":
    main()

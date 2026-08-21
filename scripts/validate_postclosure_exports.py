#!/usr/bin/env python3
"""Validate deterministic post-closure lexical export pipelines.

Each exporter is run twice into independent temporary directories. The validator
requires identical file sets and byte-identical outputs, then checks the
semantic guard flags of each manifest.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_exporter(script: str, out_dir: Path) -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / script), "--out-dir", str(out_dir)],
        cwd=ROOT,
        check=True,
    )


def compare_dirs(first: Path, second: Path, label: str) -> None:
    first_files = sorted(p.relative_to(first) for p in first.rglob("*") if p.is_file())
    second_files = sorted(p.relative_to(second) for p in second.rglob("*") if p.is_file())
    if first_files != second_files:
        raise SystemExit(f"{label}: file-set mismatch between deterministic runs")
    for relative in first_files:
        left = first / relative
        right = second / relative
        if left.read_bytes() != right.read_bytes():
            raise SystemExit(
                f"{label}: non-deterministic bytes for {relative}; "
                f"{sha256(left)} != {sha256(right)}"
            )


def load_manifest(out_dir: Path) -> dict:
    path = out_dir / "manifest.json"
    return json.loads(path.read_text(encoding="utf-8"))


def validate_corpus(manifest: dict) -> None:
    if manifest["articleCount"] <= 0:
        raise SystemExit("lexicon corpus export is empty")
    if manifest["articleCount"] != manifest["expectedArticleCountFromPhase2Summary"]:
        raise SystemExit("lexicon corpus manifest count disagrees with Phase II summary")
    if not manifest["deterministic"]:
        raise SystemExit("lexicon corpus manifest does not declare deterministic=true")


def validate_crossrefs(manifest: dict) -> None:
    if manifest["crossReferenceCount"] <= 0:
        raise SystemExit("cross-reference inventory is empty")
    if manifest["markerClassCounts"].get("busca", 0) <= 0:
        raise SystemExit("cross-reference inventory contains no Buſca-class references")
    if manifest["destinationResolutionPerformed"] is not False:
        raise SystemExit("cross-reference inventory must not resolve destinations automatically")


def validate_crossref_graph(manifest: dict) -> None:
    if manifest["crossReferenceCount"] <= 0:
        raise SystemExit("cross-reference resolution layer is empty")
    if sum(manifest["resolutionStatusCounts"].values()) != manifest["crossReferenceCount"]:
        raise SystemExit("cross-reference resolution status counts are inconsistent")
    if manifest["exactUniqueEdgeCount"] <= 0:
        raise SystemExit("cross-reference graph contains no strict exact-unique edges")
    if manifest["destinationResolutionPerformed"] is not True:
        raise SystemExit("cross-reference graph must declare destinationResolutionPerformed=true")
    for key in (
        "fuzzyMatchingUsed",
        "linguisticSimilarityUsed",
        "semanticEquivalenceInferred",
        "probableResolutionInferred",
        "canonicalArticlesModified",
    ):
        if manifest[key] is not False:
            raise SystemExit(f"cross-reference graph guard must remain false: {key}")
    if not manifest["deterministic"]:
        raise SystemExit("cross-reference graph manifest does not declare deterministic=true")


def validate_lo_mismo(manifest: dict) -> None:
    if manifest["candidateArticleCount"] <= 0:
        raise SystemExit("Lo miſmo candidate queue is empty")
    if manifest["surfaceOccurrenceCount"] < manifest["candidateArticleCount"]:
        raise SystemExit("Lo miſmo occurrence count is internally inconsistent")
    if manifest["anaphoraResolutionPerformed"] is not False:
        raise SystemExit("Lo miſmo queue must not resolve anaphora automatically")
    if manifest["semanticEquivalenceInferred"] is not False:
        raise SystemExit("Lo miſmo queue must not infer semantic equivalence")


def validate_variety(manifest: dict) -> None:
    if manifest["evidenceRecordCount"] <= 0:
        raise SystemExit("historical-variety evidence inventory is empty")
    if manifest["articleCountWithEvidence"] <= 0:
        raise SystemExit("historical-variety evidence has no source articles")
    if manifest["varietyAttributionInferred"] is not False:
        raise SystemExit("variety evidence must not infer attribution")
    if manifest["linguisticSimilarityUsed"] is not False:
        raise SystemExit("variety evidence must not use linguistic similarity")


def validate_physical_spans(manifest: dict) -> None:
    if manifest["articleCountWithPhysicalMetadata"] <= 0:
        raise SystemExit("physical-span audit is empty")
    if manifest["automaticRepairPerformed"] is not False:
        raise SystemExit("physical-span audit must not repair articles automatically")
    if manifest["philologicalCorrectionInferred"] is not False:
        raise SystemExit("physical-span audit must not infer philological corrections")
    if not manifest["deterministic"]:
        raise SystemExit("physical-span audit manifest does not declare deterministic=true")


def validate_pipeline(
    label: str,
    script: str,
    manifest_validator: Callable[[dict], None],
) -> dict:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        first = base / "run1"
        second = base / "run2"
        run_exporter(script, first)
        run_exporter(script, second)
        compare_dirs(first, second, label)
        manifest = load_manifest(first)
        manifest_validator(manifest)
        print(
            f"{label}: deterministic across two runs; "
            f"manifest sha256 {sha256(first / 'manifest.json')}"
        )
        return manifest


def main() -> None:
    results = {
        "lexicon": validate_pipeline(
            "lexicon corpus", "export_lexicon_corpus.py", validate_corpus
        ),
        "crossreferences": validate_pipeline(
            "cross-reference inventory",
            "export_lexicon_crossreferences.py",
            validate_crossrefs,
        ),
        "crossreference_graph": validate_pipeline(
            "cross-reference resolution graph",
            "export_lexicon_crossreference_graph.py",
            validate_crossref_graph,
        ),
        "lo_mismo": validate_pipeline(
            "Lo miſmo queue", "export_lexicon_lo_mismo.py", validate_lo_mismo
        ),
        "variety": validate_pipeline(
            "historical-variety evidence",
            "export_lexicon_variety_evidence.py",
            validate_variety,
        ),
        "physical_spans": validate_pipeline(
            "physical-span audit",
            "export_lexicon_physical_spans.py",
            validate_physical_spans,
        ),
    }
    if results["crossreference_graph"]["crossReferenceCount"] != results["crossreferences"]["crossReferenceCount"]:
        raise SystemExit("cross-reference graph count disagrees with canonical cross-reference inventory")
    print(
        "post-closure export QA OK: "
        f"{results['lexicon']['articleCount']} articles; "
        f"{results['crossreferences']['crossReferenceCount']} cross-references; "
        f"{results['crossreference_graph']['exactUniqueEdgeCount']} strict exact cross-reference edges, "
        f"{results['crossreference_graph']['cycleCount']} exact cycle(s); "
        f"{results['lo_mismo']['candidateArticleCount']} Lo miſmo candidate articles; "
        f"{results['variety']['evidenceRecordCount']} variety-evidence records; "
        f"{results['physical_spans']['articleCountWithPhysicalMetadata']} articles with physical metadata, "
        f"{results['physical_spans']['flaggedArticleCount']} flagged for structural review"
    )


if __name__ == "__main__":
    main()

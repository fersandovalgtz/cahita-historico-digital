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


def validate_crossref_diagnostics(manifest: dict) -> None:
    if manifest["strictNotLocatedAudited"] <= 0:
        raise SystemExit("cross-reference diagnostic queue is empty")
    if manifest["candidatePairCount"] <= 0:
        raise SystemExit("cross-reference diagnostic queue has no candidate pairs")
    if manifest["strongThreshold"] != 0.9:
        raise SystemExit("cross-reference diagnostic strong threshold drifted")
    priority_counts = manifest.get("priorityTierCounts") or {}
    expected_tiers = {"A_unique_strong", "B_multiple_strong", "C_no_strong"}
    if set(priority_counts) != expected_tiers:
        raise SystemExit("cross-reference diagnostic priority tiers are incomplete or unexpected")
    if sum(priority_counts.values()) != manifest["strictNotLocatedAudited"]:
        raise SystemExit("cross-reference diagnostic priority-tier counts are inconsistent")
    if priority_counts["A_unique_strong"] <= 0:
        raise SystemExit("cross-reference diagnostic queue has no tier-A cases")
    if manifest["diagnosticOnly"] is not True:
        raise SystemExit("cross-reference diagnostics must remain explicitly non-binding")
    for key in (
        "destinationResolutionPerformed",
        "canonicalResolutionsModified",
        "canonicalArticlesModified",
        "canonicalFuzzyMatchingUsed",
        "linguisticSimilarityUsed",
        "semanticEquivalenceInferred",
        "philologicalCorrectionInferred",
        "humanVerificationPerformed",
    ):
        if manifest[key] is not False:
            raise SystemExit(f"cross-reference diagnostic guard must remain false: {key}")
    if manifest["diagnosticGraphicSimilarityUsed"] is not True:
        raise SystemExit("cross-reference diagnostics must disclose graphic similarity use")
    if not manifest["deterministic"]:
        raise SystemExit("cross-reference diagnostic manifest does not declare deterministic=true")


def validate_crossref_reviewed_view(manifest: dict) -> None:
    if manifest["canonicalCrossReferenceCount"] <= 0:
        raise SystemExit("reviewed cross-reference view is empty")
    if manifest["sourceReviewRecordCount"] <= 0:
        raise SystemExit("reviewed cross-reference view contains no source-review records")
    if manifest["strictGraphEdgeCount"] <= 0:
        raise SystemExit("reviewed cross-reference view lost strict graph edges")
    if manifest["reviewedViewEdgeCount"] < manifest["strictGraphEdgeCount"]:
        raise SystemExit("reviewed cross-reference view has fewer edges than strict graph")

    status_counts = manifest.get("reviewedViewStatusCounts") or {}
    if sum(status_counts.values()) != manifest["canonicalCrossReferenceCount"]:
        raise SystemExit("reviewed cross-reference status counts are inconsistent")
    if status_counts.get("strict_exact_unique", 0) != manifest["strictGraphEdgeCount"]:
        raise SystemExit("reviewed view strict-edge count disagrees with strict graph")

    review_decisions = manifest.get("reviewDecisionCounts") or {}
    if sum(review_decisions.values()) != manifest["sourceReviewRecordCount"]:
        raise SystemExit("reviewed view decision counts disagree with source-review records")
    editorial_unique = status_counts.get("editorial_source_supported_unique", 0)
    if editorial_unique != review_decisions.get("source_supports_unique_target", 0):
        raise SystemExit("reviewed view editorial unique-edge count disagrees with review decisions")

    authority_counts = manifest.get("edgeAuthorityCounts") or {}
    if authority_counts.get("strict_exact_normalized_equality", 0) != manifest["strictGraphEdgeCount"]:
        raise SystemExit("reviewed view strict authority count drifted")
    if authority_counts.get("editorial_source_review", 0) != editorial_unique:
        raise SystemExit("reviewed view editorial authority count drifted")
    if sum(authority_counts.values()) != manifest["reviewedViewEdgeCount"]:
        raise SystemExit("reviewed view authority counts disagree with edge count")

    for key in (
        "canonicalArticlesModified",
        "canonicalStrictGraphModified",
        "editorialReviewsPromotedToCanonical",
        "humanValidationInferred",
    ):
        if manifest[key] is not False:
            raise SystemExit(f"reviewed cross-reference view guard must remain false: {key}")
    if not manifest["deterministic"]:
        raise SystemExit("reviewed cross-reference view manifest does not declare deterministic=true")


def validate_crossref_review_queue(manifest: dict) -> None:
    if manifest["strictNotLocatedDiagnosticCount"] <= 0:
        raise SystemExit("cross-reference source-review queue has no strict-not-located universe")
    if manifest["sourceReviewRecordCount"] <= 0:
        raise SystemExit("cross-reference source-review queue sees no completed reviews")
    if manifest["awaitingSourceReviewCount"] < 0:
        raise SystemExit("cross-reference source-review queue has an invalid awaiting count")
    if (
        manifest["sourceReviewRecordCount"] + manifest["awaitingSourceReviewCount"]
        != manifest["strictNotLocatedDiagnosticCount"]
    ):
        raise SystemExit("source-review queue does not partition strict not_located references")

    tier_counts = manifest.get("priorityTierCounts") or {}
    expected_tiers = {"A_unique_strong", "B_multiple_strong", "C_no_strong"}
    if set(tier_counts) != expected_tiers:
        raise SystemExit("source-review queue priority tiers are incomplete or unexpected")
    if sum(tier_counts.values()) != manifest["awaitingSourceReviewCount"]:
        raise SystemExit("source-review queue priority-tier counts are inconsistent")

    for key in (
        "canonicalStrictGraphModified",
        "canonicalArticlesModified",
        "diagnosticCandidatesPromotedToEditorial",
        "destinationResolutionPerformed",
        "semanticEquivalenceInferred",
        "humanVerificationPerformed",
    ):
        if manifest[key] is not False:
            raise SystemExit(f"source-review queue guard must remain false: {key}")
    if not manifest["deterministic"]:
        raise SystemExit("source-review queue manifest does not declare deterministic=true")


def validate_lo_mismo(manifest: dict) -> None:
    if manifest["candidateArticleCount"] <= 0:
        raise SystemExit("Lo miſmo candidate queue is empty")
    if manifest["surfaceOccurrenceCount"] < manifest["candidateArticleCount"]:
        raise SystemExit("Lo miſmo occurrence count is internally inconsistent")
    for key in (
        "formulaFunctionInferred",
        "referentialScopeInferred",
        "targetLanguageFormInferred",
        "borrowingInferred",
        "semanticEquivalenceInferred",
    ):
        if manifest[key] is not False:
            raise SystemExit(f"Lo miſmo surface queue guard must remain false: {key}")
    if not manifest["deterministic"]:
        raise SystemExit("Lo miſmo queue manifest does not declare deterministic=true")


def validate_variety(manifest: dict) -> None:
    if manifest["evidenceRecordCount"] <= 0:
        raise SystemExit("historical-variety evidence inventory is empty")
    if manifest["articleCountWithEvidence"] <= 0:
        raise SystemExit("historical-variety evidence has no source articles")
    if manifest["varietyAttributionInferred"] is not False:
        raise SystemExit("historical-variety evidence must not infer attribution")
    if manifest["linguisticSimilarityUsed"] is not False:
        raise SystemExit("historical-variety evidence must not use linguistic similarity")


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
        "crossreference_diagnostics": validate_pipeline(
            "cross-reference candidate diagnostics",
            "export_crossreference_candidate_diagnostics.py",
            validate_crossref_diagnostics,
        ),
        "crossreference_reviewed_view": validate_pipeline(
            "cross-reference reviewed view",
            "export_lexicon_crossreference_reviewed_view.py",
            validate_crossref_reviewed_view,
        ),
        "crossreference_review_queue": validate_pipeline(
            "cross-reference source-review queue",
            "export_crossreference_review_queue.py",
            validate_crossref_review_queue,
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
            "physical-span audit", "export_lexicon_physical_spans.py", validate_physical_spans
        ),
    }
    if results["crossreference_graph"]["crossReferenceCount"] != results["crossreferences"]["crossReferenceCount"]:
        raise SystemExit("cross-reference graph count disagrees with canonical cross-reference inventory")
    if (
        results["crossreference_diagnostics"]["strictNotLocatedAudited"]
        != results["crossreference_graph"]["resolutionStatusCounts"].get("not_located", 0)
    ):
        raise SystemExit("cross-reference diagnostic queue count disagrees with strict graph not_located count")
    if (
        results["crossreference_reviewed_view"]["canonicalCrossReferenceCount"]
        != results["crossreferences"]["crossReferenceCount"]
    ):
        raise SystemExit("reviewed cross-reference view count disagrees with canonical inventory")
    if (
        results["crossreference_reviewed_view"]["strictGraphEdgeCount"]
        != results["crossreference_graph"]["exactUniqueEdgeCount"]
    ):
        raise SystemExit("reviewed cross-reference view strict-edge count disagrees with canonical graph")
    if (
        results["crossreference_review_queue"]["strictNotLocatedDiagnosticCount"]
        != results["crossreference_diagnostics"]["strictNotLocatedAudited"]
    ):
        raise SystemExit("source-review queue strict universe disagrees with diagnostics")
    if (
        results["crossreference_review_queue"]["sourceReviewRecordCount"]
        != results["crossreference_reviewed_view"]["sourceReviewRecordCount"]
    ):
        raise SystemExit("source-review queue completed-review count disagrees with reviewed view")
    if (
        results["crossreference_review_queue"]["awaitingSourceReviewCount"]
        != results["crossreference_reviewed_view"]["reviewedViewStatusCounts"].get("strict_not_located_unreviewed", 0)
    ):
        raise SystemExit("source-review queue awaiting count disagrees with reviewed view")

    print(
        "post-closure export QA OK: "
        f"{results['lexicon']['articleCount']} articles; "
        f"{results['crossreferences']['crossReferenceCount']} cross-references; "
        f"{results['crossreference_graph']['exactUniqueEdgeCount']} strict exact cross-reference edges, "
        f"{results['crossreference_graph']['cycleCount']} exact cycle(s); "
        f"{results['crossreference_diagnostics']['strictNotLocatedAudited']} cross-reference diagnostics "
        f"with tiers={results['crossreference_diagnostics']['priorityTierCounts']}, "
        f"{results['crossreference_diagnostics']['candidatePairCount']} candidate pairs; "
        f"reviewedViewEdges={results['crossreference_reviewed_view']['reviewedViewEdgeCount']} "
        f"from {results['crossreference_reviewed_view']['sourceReviewRecordCount']} source-review records; "
        f"sourceReviewQueue={results['crossreference_review_queue']['awaitingSourceReviewCount']} "
        f"with tiers={results['crossreference_review_queue']['priorityTierCounts']}; "
        f"{results['lo_mismo']['candidateArticleCount']} Lo miſmo formula-candidate articles; "
        f"{results['variety']['evidenceRecordCount']} variety-evidence records; "
        f"{results['physical_spans']['articleCountWithPhysicalMetadata']} articles with physical metadata, "
        f"{results['physical_spans']['flaggedArticleCount']} flagged for structural review"
    )


if __name__ == "__main__":
    main()

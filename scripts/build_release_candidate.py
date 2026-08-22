#!/usr/bin/env python3
"""Build a deterministic CHD scientific release-candidate bundle.

This is deliberately a *release candidate*, not v1.0.0. It packages the
canonical/derived artifacts that already have deterministic QA while preserving
remaining open gates (facsimile recollation, metadata/tag, archival deposit and
DOI) as explicit manifest state.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BUNDLE_DIRNAME = "cahita-historico-digital-release-candidate"
ZIP_NAME = "cahita-historico-digital-release-candidate.zip"
MANIFEST_NAME = "RELEASE_CANDIDATE_MANIFEST.json"

EXPORTERS = [
    ("lexicon", "export_lexicon_corpus.py", "--out-dir"),
    ("crossreferences", "export_lexicon_crossreferences.py", "--out-dir"),
    ("crossreference_strict_graph", "export_lexicon_crossreference_graph.py", "--out-dir"),
    ("crossreference_diagnostics", "export_crossreference_candidate_diagnostics.py", "--out-dir"),
    ("crossreference_reviewed_view", "export_lexicon_crossreference_reviewed_view.py", "--out-dir"),
    ("crossreference_review_queue", "export_crossreference_review_queue.py", "--out-dir"),
    ("crossreference_recollation_queue", "export_crossreference_recollation_queue.py", "--output-dir"),
    ("lo_mismo", "export_lexicon_lo_mismo.py", "--out-dir"),
    ("historical_variety", "export_lexicon_variety_evidence.py", "--out-dir"),
    ("physical_spans", "export_lexicon_physical_spans.py", "--out-dir"),
    ("grammar_evidence", "export_grammar_evidence_concordance.py", "--out-dir"),
    ("grammar_rule_coverage", "export_grammar_rule_coverage.py", "--out-dir"),
    ("tei_lexicon", "export_lexicon_tei.py", "--out-dir"),
]

DOCUMENT_FILES = [
    "README.md",
    "LICENSE",
    "DATA_LICENSE.md",
    "CITATION.cff",
    "codemeta.json",
    "RELEASE_CHECKLIST_v1_0.md",
    "docs/RELEASE_READINESS_2026-08-21.md",
    "docs/PHASE2_COMPLETION_2026-08-21.md",
    "docs/GRAMMAR_COMPLETION_2026-08-21.md",
    "docs/CROSSREFERENCE_REVIEW_PROGRESS_2026-08-21.md",
    "docs/CROSSREFERENCE_RECOLLATION_QUEUE.md",
    "docs/TEI_LEXICON_PROFILE_V0_1.md",
    "docs/CLDF_SCOPE_DECISION_V1_0.md",
    "docs/RELEASE_CANDIDATE_PACKAGE.md",
    "data/source/alc1737/metadata.json",
    "data/source/alc1737/ingest_manifest.json",
    "data/source/alc1737/page_manifest.csv",
    "data/source/alc1737/sections.json",
]

OPEN_GATES = [
    "direct_facsimile_recollation_of_22_crossreference_cases",
    "final_schema_and_metadata_freeze",
    "final_release_tag_and_changelog",
    "archival_deposit_and_version_doi",
]

FIXED_ZIP_TIME = (1980, 1, 1, 0, 0, 0)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_commit() -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
    )
    return result.stdout.strip()


def run_exporters(bundle: Path) -> None:
    derived = bundle / "derived"
    for slug, script, output_flag in EXPORTERS:
        destination = derived / slug
        destination.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            [sys.executable, str(ROOT / "scripts" / script), output_flag, str(destination)],
            cwd=ROOT,
            check=True,
        )


def copy_documents(bundle: Path) -> None:
    for relative in DOCUMENT_FILES:
        source = ROOT / relative
        if not source.is_file():
            raise SystemExit(f"release-candidate document/input is missing: {relative}")
        destination = bundle / "project" / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)


def inventory_files(bundle: Path, exclude: set[str] | None = None) -> list[dict[str, Any]]:
    exclude = exclude or set()
    records: list[dict[str, Any]] = []
    for path in sorted(p for p in bundle.rglob("*") if p.is_file()):
        relative = path.relative_to(bundle).as_posix()
        if relative in exclude:
            continue
        records.append(
            {
                "path": relative,
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )
    return records


def load_nested_manifest(bundle: Path, slug: str) -> dict[str, Any]:
    path = bundle / "derived" / slug / "manifest.json"
    if not path.is_file():
        raise SystemExit(f"missing nested exporter manifest: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def build_manifest(bundle: Path) -> dict[str, Any]:
    lexicon = load_nested_manifest(bundle, "lexicon")
    strict = load_nested_manifest(bundle, "crossreference_strict_graph")
    reviewed = load_nested_manifest(bundle, "crossreference_reviewed_view")
    recollation = load_nested_manifest(bundle, "crossreference_recollation_queue")
    tei = load_nested_manifest(bundle, "tei_lexicon")
    grammar_evidence = load_nested_manifest(bundle, "grammar_evidence")
    grammar_coverage = load_nested_manifest(bundle, "grammar_rule_coverage")

    files = inventory_files(bundle, exclude={MANIFEST_NAME})
    manifest: dict[str, Any] = {
        "project": "Cahíta Histórico Digital",
        "sourceId": "ALC1737",
        "packageType": "scientific_release_candidate",
        "packageStatus": "development_not_v1_0_0",
        "sourceCommit": git_commit(),
        "deterministicBuild": True,
        "canonicalRepresentation": "data/lexicon/articles/*.jsonl and canonical grammar JSON/JSONL in repository",
        "facsimileIncluded": False,
        "thirdPartyReproductionsRelicensed": False,
        "humanVerifiedCount": 0,
        "releaseReady": False,
        "openGates": OPEN_GATES,
        "interoperabilityDecision": {
            "primaryLexicalReleaseProfile": "TEI Lex-0 0.9.5",
            "cldfRequiredForV1": False,
            "cldfStatus": "deferred_post_v1_analytic_derivative",
            "decisionDocument": "docs/CLDF_SCOPE_DECISION_V1_0.md",
            "canonicalDataReplacedByInteroperabilityFormats": False,
        },
        "summary": {
            "lexiconArticleCount": int(lexicon["articleCount"]),
            "canonicalCrossReferenceCount": int(strict["crossReferenceCount"]),
            "strictCrossReferenceEdgeCount": int(strict["exactUniqueEdgeCount"]),
            "strictCrossReferenceCycleCount": int(strict["cycleCount"]),
            "sourceReviewRecordCount": int(reviewed["sourceReviewRecordCount"]),
            "reviewedViewEdgeCount": int(reviewed["reviewedViewEdgeCount"]),
            "facsimileRecollationQueueCount": int(recollation["queueCount"]),
            "grammarObjectCount": int(grammar_evidence["canonicalObjectCount"]),
            "grammarEvidenceRowCount": int(grammar_evidence["evidenceRowCount"]),
            "grammarRulesWithStructuredClaim": int(grammar_coverage["rulesWithStructuredClaim"]),
            "grammarRuleComparisonUniverse": int(grammar_coverage["comparisonUniverse"]["ruleCount"]),
            "teiEntryCount": int(tei["articleCount"]),
            "teiLex0ConformanceClaimed": bool(tei["teiLex0ConformanceClaimed"]),
            "externalLex0SchemaValidationEnforcedInCI": bool(
                tei["externalLex0SchemaValidationEnforcedInCI"]
            ),
            "externalLex0SchemaUrl": tei["externalLex0SchemaUrl"],
            "externalLex0SchemaSha256": tei["externalLex0SchemaSha256"],
        },
        "artifactFileCount": len(files),
        "artifactBytes": sum(int(item["bytes"]) for item in files),
        "files": files,
    }

    expected = manifest["summary"]
    if expected["lexiconArticleCount"] != 2302:
        raise SystemExit("release candidate lost canonical lexicon count")
    if expected["canonicalCrossReferenceCount"] != 150:
        raise SystemExit("release candidate lost canonical cross-reference count")
    if expected["strictCrossReferenceEdgeCount"] != 60:
        raise SystemExit("release candidate strict edge count drifted")
    if expected["sourceReviewRecordCount"] != 90:
        raise SystemExit("release candidate source-review count drifted")
    if expected["facsimileRecollationQueueCount"] != 22:
        raise SystemExit("release candidate recollation queue count drifted")
    if expected["grammarObjectCount"] != 302:
        raise SystemExit("release candidate grammar object count drifted")
    if expected["grammarEvidenceRowCount"] != 1215:
        raise SystemExit("release candidate grammar evidence count drifted")
    if expected["teiEntryCount"] != 2302:
        raise SystemExit("release candidate TEI entry count drifted")
    if expected["teiLex0ConformanceClaimed"] is not True:
        raise SystemExit("release candidate must expose the CI-backed Lex-0 conformance claim")
    if expected["externalLex0SchemaValidationEnforcedInCI"] is not True:
        raise SystemExit("release candidate must disclose the external Lex-0 CI gate")
    if expected["externalLex0SchemaUrl"] != "https://lex-0.org/releases/v0.9.5/schema/lex-0.rng":
        raise SystemExit("release candidate Lex-0 schema URL drifted")
    if expected["externalLex0SchemaSha256"] != "35e73fef48526634714bdf3d16b924f958fca078a903d0bdc2dd4d7d116d1aaa":
        raise SystemExit("release candidate Lex-0 schema hash drifted")

    interoperability = manifest["interoperabilityDecision"]
    if interoperability["primaryLexicalReleaseProfile"] != "TEI Lex-0 0.9.5":
        raise SystemExit("release candidate primary interoperability profile drifted")
    if interoperability["cldfRequiredForV1"] is not False:
        raise SystemExit("release candidate must not make CLDF a v1 gate")
    if interoperability["cldfStatus"] != "deferred_post_v1_analytic_derivative":
        raise SystemExit("release candidate CLDF scope decision drifted")
    if interoperability["canonicalDataReplacedByInteroperabilityFormats"] is not False:
        raise SystemExit("interoperability derivatives must not replace canonical data")
    return manifest


def write_manifest(bundle: Path) -> dict[str, Any]:
    manifest = build_manifest(bundle)
    payload = (json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    (bundle / MANIFEST_NAME).write_bytes(payload)
    return manifest


def write_deterministic_zip(bundle: Path, destination: Path) -> None:
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(p for p in bundle.rglob("*") if p.is_file()):
            relative = Path(BUNDLE_DIRNAME) / path.relative_to(bundle)
            info = zipfile.ZipInfo(relative.as_posix(), date_time=FIXED_ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def build(output_dir: Path) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    bundle = output_dir / BUNDLE_DIRNAME
    if bundle.exists():
        shutil.rmtree(bundle)
    bundle.mkdir(parents=True)

    run_exporters(bundle)
    copy_documents(bundle)
    manifest = write_manifest(bundle)

    zip_path = output_dir / ZIP_NAME
    if zip_path.exists():
        zip_path.unlink()
    write_deterministic_zip(bundle, zip_path)

    result = {
        "bundleDir": bundle,
        "zipPath": zip_path,
        "zipBytes": zip_path.stat().st_size,
        "zipSha256": sha256_file(zip_path),
        "manifest": manifest,
    }
    print(
        "built CHD scientific release candidate: "
        f"files={manifest['artifactFileCount'] + 1}; "
        f"lexicon={manifest['summary']['lexiconArticleCount']}; "
        f"grammarEvidence={manifest['summary']['grammarEvidenceRowCount']}; "
        f"recollationQueue={manifest['summary']['facsimileRecollationQueueCount']}; "
        f"openGates={len(manifest['openGates'])}; "
        f"releaseReady={str(manifest['releaseReady']).lower()}"
    )
    print(f"  {ZIP_NAME}: {result['zipBytes']} bytes; sha256 {result['zipSha256']}")
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "build" / "release-candidate",
    )
    args = parser.parse_args()
    build(args.output_dir)


if __name__ == "__main__":
    main()

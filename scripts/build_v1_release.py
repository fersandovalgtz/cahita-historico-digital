#!/usr/bin/env python3
"""Build the deterministic Cahíta Histórico Digital v1.0.0 release payload."""
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
VERSION = "1.0.0"
TAG = "v1.0.0"
BUNDLE_DIRNAME = f"cahita-historico-digital-{TAG}"
ZIP_NAME = f"{BUNDLE_DIRNAME}.zip"
MANIFEST_NAME = "RELEASE_MANIFEST.json"
FIXED_ZIP_TIME = (1980, 1, 1, 0, 0, 0)
DATA_FREEZE_PATH = ROOT / "release/v1_data_manifest.json"
CONTRACT_FREEZE_PATH = ROOT / "release/v1_contract_manifest.json"

EXPORTERS = [
    ("lexicon", "export_lexicon_corpus.py", "--out-dir"),
    ("crossreferences", "export_lexicon_crossreferences.py", "--out-dir"),
    ("crossreference_strict_graph", "export_lexicon_crossreference_graph.py", "--out-dir"),
    ("crossreference_diagnostics", "export_crossreference_candidate_diagnostics.py", "--out-dir"),
    ("crossreference_reviewed_view", "export_lexicon_crossreference_reviewed_view.py", "--out-dir"),
    ("crossreference_review_queue", "export_crossreference_review_queue.py", "--out-dir"),
    ("crossreference_recollation_queue", "export_crossreference_recollation_queue.py", "--output-dir"),
    ("v1_recollation_disposition", "export_v1_recollation_disposition.py", "--out-dir"),
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
    "CHANGELOG.md",
    "RELEASE_CHECKLIST_v1_0.md",
    "release/v1_contract_manifest.json",
    "release/v1_data_manifest.json",
    "release/RELEASE_NOTES_v1.0.0.md",
    "docs/RELEASE_READINESS_2026-08-21.md",
    "docs/PHASE2_COMPLETION_2026-08-21.md",
    "docs/GRAMMAR_COMPLETION_2026-08-21.md",
    "docs/CROSSREFERENCE_REVIEW_PROGRESS_2026-08-21.md",
    "docs/CROSSREFERENCE_RECOLLATION_QUEUE.md",
    "docs/V1_RECOLLATION_DISPOSITION.md",
    "docs/TEI_LEXICON_PROFILE_V0_1.md",
    "docs/CLDF_SCOPE_DECISION_V1_0.md",
]


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_commit() -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, check=True, text=True, stdout=subprocess.PIPE
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
            raise SystemExit(f"v1 release document/input is missing: {relative}")
        destination = bundle / "project" / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def copy_frozen_scientific_data(bundle: Path) -> dict[str, Any]:
    if not DATA_FREEZE_PATH.is_file():
        raise SystemExit("missing v1 scientific-data freeze manifest")
    manifest = load_json(DATA_FREEZE_PATH)
    if manifest.get("version") != VERSION:
        raise SystemExit("v1 data freeze version mismatch")
    for item in manifest.get("files", []):
        relative = str(item["path"])
        source = ROOT / relative
        if not source.is_file():
            raise SystemExit(f"frozen scientific-data file missing: {relative}")
        actual_sha = sha256_file(source)
        actual_bytes = source.stat().st_size
        if actual_sha != item["sha256"] or actual_bytes != int(item["bytes"]):
            raise SystemExit(f"frozen scientific-data file drifted before packaging: {relative}")
        destination = bundle / "canonical_data" / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
    return manifest


def inventory_files(bundle: Path, exclude: set[str] | None = None) -> list[dict[str, Any]]:
    exclude = exclude or set()
    rows: list[dict[str, Any]] = []
    for path in sorted(p for p in bundle.rglob("*") if p.is_file()):
        relative = path.relative_to(bundle).as_posix()
        if relative in exclude:
            continue
        rows.append({"path": relative, "bytes": path.stat().st_size, "sha256": sha256_file(path)})
    return rows


def nested_manifest(bundle: Path, slug: str) -> dict[str, Any]:
    path = bundle / "derived" / slug / "manifest.json"
    if not path.is_file():
        raise SystemExit(f"missing nested exporter manifest: {slug}")
    return load_json(path)


def build_manifest(bundle: Path, data_freeze: dict[str, Any]) -> dict[str, Any]:
    lexicon = nested_manifest(bundle, "lexicon")
    strict = nested_manifest(bundle, "crossreference_strict_graph")
    reviewed = nested_manifest(bundle, "crossreference_reviewed_view")
    recollation = nested_manifest(bundle, "crossreference_recollation_queue")
    disposition = nested_manifest(bundle, "v1_recollation_disposition")
    tei = nested_manifest(bundle, "tei_lexicon")
    grammar_evidence = nested_manifest(bundle, "grammar_evidence")
    grammar_coverage = nested_manifest(bundle, "grammar_rule_coverage")
    contract_freeze = load_json(CONTRACT_FREEZE_PATH)

    files = inventory_files(bundle, exclude={MANIFEST_NAME})
    manifest: dict[str, Any] = {
        "project": "Cahíta Histórico Digital",
        "sourceId": "ALC1737",
        "packageType": "scientific_release",
        "version": VERSION,
        "tag": TAG,
        "releaseDate": "2026-08-21",
        "sourceCommit": git_commit(),
        "deterministicBuild": True,
        "githubReleasePayloadReady": True,
        "archivalDepositStatus": "pending",
        "versionDoi": None,
        "conceptDoi": None,
        "doiInferred": False,
        "facsimileIncluded": False,
        "thirdPartyReproductionsRelicensed": False,
        "humanVerifiedCount": 0,
        "scientificDataFreeze": {
            "freezeId": data_freeze["freezeId"],
            "manifestPath": "release/v1_data_manifest.json",
            "manifestSha256": sha256_file(DATA_FREEZE_PATH),
            "fileCount": int(data_freeze["fileCount"]),
            "totalBytes": int(data_freeze["totalBytes"]),
            "exactBytesFrozen": True,
            "silentChangesAllowed": False,
        },
        "contractFreeze": {
            "freezeId": contract_freeze["freezeId"],
            "manifestPath": "release/v1_contract_manifest.json",
            "manifestSha256": sha256_file(CONTRACT_FREEZE_PATH),
            "contractCount": int(contract_freeze["contractCount"]),
        },
        "summary": {
            "lexiconArticleCount": int(lexicon["articleCount"]),
            "canonicalCrossReferenceCount": int(strict["crossReferenceCount"]),
            "strictCrossReferenceEdgeCount": int(strict["exactUniqueEdgeCount"]),
            "strictCrossReferenceCycleCount": int(strict["cycleCount"]),
            "sourceReviewRecordCount": int(reviewed["sourceReviewRecordCount"]),
            "reviewedViewEdgeCount": int(reviewed["reviewedViewEdgeCount"]),
            "facsimileRecollationQueueCount": int(recollation["queueCount"]),
            "v1OpenRecollationUncertaintyCount": int(disposition["openUncertaintyCount"]),
            "v1RecollationsResolvedByReleaseLayer": int(disposition["resolvedByThisLayerCount"]),
            "grammarObjectCount": int(grammar_evidence["canonicalObjectCount"]),
            "grammarEvidenceRowCount": int(grammar_evidence["evidenceRowCount"]),
            "grammarRulesWithStructuredClaim": int(grammar_coverage["rulesWithStructuredClaim"]),
            "grammarRuleComparisonUniverse": int(grammar_coverage["comparisonUniverse"]["ruleCount"]),
            "teiEntryCount": int(tei["articleCount"]),
            "teiLex0ConformanceClaimed": bool(tei["teiLex0ConformanceClaimed"]),
            "externalLex0SchemaValidationEnforcedInCI": bool(tei["externalLex0SchemaValidationEnforcedInCI"]),
        },
        "limitations": {
            "philologicalHumanValidationComplete": False,
            "openRecollationUncertainties": 22,
            "ocrAcceptedAsFacsimileSubstitute": False,
            "archivalDoiPending": True,
        },
        "artifactFileCount": len(files),
        "artifactBytes": sum(int(item["bytes"]) for item in files),
        "files": files,
    }

    expected = manifest["summary"]
    required = {
        "lexiconArticleCount": 2302,
        "canonicalCrossReferenceCount": 150,
        "strictCrossReferenceEdgeCount": 60,
        "strictCrossReferenceCycleCount": 4,
        "sourceReviewRecordCount": 90,
        "reviewedViewEdgeCount": 100,
        "facsimileRecollationQueueCount": 22,
        "v1OpenRecollationUncertaintyCount": 22,
        "v1RecollationsResolvedByReleaseLayer": 0,
        "grammarObjectCount": 302,
        "grammarEvidenceRowCount": 1215,
        "grammarRulesWithStructuredClaim": 370,
        "grammarRuleComparisonUniverse": 373,
        "teiEntryCount": 2302,
        "teiLex0ConformanceClaimed": True,
        "externalLex0SchemaValidationEnforcedInCI": True,
    }
    if expected != required:
        raise SystemExit(f"v1 release scientific summary drifted: {expected} != {required}")
    if manifest["contractFreeze"]["contractCount"] != 26:
        raise SystemExit("v1 release must preserve 26 frozen contracts")
    return manifest


def write_manifest(bundle: Path, data_freeze: dict[str, Any]) -> dict[str, Any]:
    manifest = build_manifest(bundle, data_freeze)
    (bundle / MANIFEST_NAME).write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
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

    data_freeze = copy_frozen_scientific_data(bundle)
    run_exporters(bundle)
    copy_documents(bundle)
    manifest = write_manifest(bundle, data_freeze)

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
        "built CHD v1.0.0 scientific release: "
        f"files={manifest['artifactFileCount'] + 1}; lexicon={manifest['summary']['lexiconArticleCount']}; "
        f"frozenDataFiles={manifest['scientificDataFreeze']['fileCount']}; "
        f"openRecollations={manifest['summary']['v1OpenRecollationUncertaintyCount']}; "
        "githubReleasePayloadReady=true; archivalDepositStatus=pending; humanVerified=0"
    )
    print(f"  {ZIP_NAME}: {result['zipBytes']} bytes; sha256 {result['zipSha256']}")
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=ROOT / "build" / "v1-release")
    args = parser.parse_args()
    build(args.output_dir)


if __name__ == "__main__":
    main()

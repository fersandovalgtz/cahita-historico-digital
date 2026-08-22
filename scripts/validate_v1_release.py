#!/usr/bin/env python3
"""Validate the deterministic Cahíta Histórico Digital v1.0.0 release payload."""
from __future__ import annotations

import tempfile
import zipfile
from pathlib import Path

from build_v1_release import BUNDLE_DIRNAME, MANIFEST_NAME, TAG, VERSION, ZIP_NAME, build


def validate_manifest(manifest: dict) -> None:
    if manifest.get("packageType") != "scientific_release":
        raise SystemExit("unexpected v1 package type")
    if manifest.get("version") != VERSION or manifest.get("tag") != TAG:
        raise SystemExit("v1 release identity drifted")
    if manifest.get("githubReleasePayloadReady") is not True:
        raise SystemExit("v1 payload must be ready for GitHub Release")
    if manifest.get("archivalDepositStatus") != "pending":
        raise SystemExit("archival deposit must remain explicitly pending before DOI gate")
    if manifest.get("versionDoi") is not None or manifest.get("conceptDoi") is not None:
        raise SystemExit("v1 package must not invent DOI before archival deposit")
    if manifest.get("doiInferred") is not False:
        raise SystemExit("DOI inference is forbidden")
    if manifest.get("humanVerifiedCount") != 0:
        raise SystemExit("v1 package must preserve humanVerifiedCount=0")
    if manifest.get("facsimileIncluded") is not False:
        raise SystemExit("v1 package must not include third-party facsimile")
    if manifest.get("contractFreeze", {}).get("contractCount") != 26:
        raise SystemExit("v1 package contract freeze count drifted")
    freeze = manifest.get("scientificDataFreeze", {})
    if freeze.get("exactBytesFrozen") is not True or freeze.get("silentChangesAllowed") is not False:
        raise SystemExit("v1 scientific-data freeze guarantees drifted")
    if freeze.get("fileCount", 0) < 230:
        raise SystemExit("v1 scientific-data freeze file count is unexpectedly small")

    expected_summary = {
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
    if manifest.get("summary") != expected_summary:
        raise SystemExit("v1 release scientific summary drifted")
    limitations = manifest.get("limitations", {})
    if limitations != {
        "philologicalHumanValidationComplete": False,
        "openRecollationUncertainties": 22,
        "ocrAcceptedAsFacsimileSubstitute": False,
        "archivalDoiPending": True,
    }:
        raise SystemExit("v1 release limitations drifted")


def validate_zip(result: dict) -> None:
    manifest = result["manifest"]
    with zipfile.ZipFile(result["zipPath"]) as archive:
        names = archive.namelist()
        if names != sorted(names):
            raise SystemExit("v1 ZIP members are not sorted deterministically")
        if len(names) != manifest["artifactFileCount"] + 1:
            raise SystemExit("v1 ZIP member count disagrees with manifest")
        required = {
            f"{BUNDLE_DIRNAME}/{MANIFEST_NAME}",
            f"{BUNDLE_DIRNAME}/project/CITATION.cff",
            f"{BUNDLE_DIRNAME}/project/codemeta.json",
            f"{BUNDLE_DIRNAME}/project/CHANGELOG.md",
            f"{BUNDLE_DIRNAME}/project/release/v1_data_manifest.json",
            f"{BUNDLE_DIRNAME}/project/release/v1_contract_manifest.json",
            f"{BUNDLE_DIRNAME}/project/release/RELEASE_NOTES_v1.0.0.md",
            f"{BUNDLE_DIRNAME}/derived/tei_lexicon/chd_lexicon_tei.xml",
        }
        missing = sorted(required - set(names))
        if missing:
            raise SystemExit(f"v1 ZIP missing required release records: {missing}")
        if not any(name.startswith(f"{BUNDLE_DIRNAME}/canonical_data/data/lexicon/articles/") for name in names):
            raise SystemExit("v1 ZIP missing frozen canonical lexicon data")
        if not any(name.startswith(f"{BUNDLE_DIRNAME}/canonical_data/data/grammar/") for name in names):
            raise SystemExit("v1 ZIP missing frozen canonical grammar data")
        for info in archive.infolist():
            if info.date_time != (1980, 1, 1, 0, 0, 0):
                raise SystemExit(f"non-deterministic ZIP timestamp for {info.filename}")


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        first = build(base / "run1")
        second = build(base / "run2")
        validate_manifest(first["manifest"])
        validate_manifest(second["manifest"])
        validate_zip(first)
        validate_zip(second)

        if first["manifest"] != second["manifest"]:
            raise SystemExit("v1 release manifests differ across two builds")
        if first["zipSha256"] != second["zipSha256"]:
            raise SystemExit("v1 release ZIP hashes differ across two builds")
        if first["zipPath"].read_bytes() != second["zipPath"].read_bytes():
            raise SystemExit("v1 release ZIP bytes differ across two builds")

        print(
            "v1 release QA OK: "
            f"version={VERSION}; tag={TAG}; zip={ZIP_NAME}; sha256={first['zipSha256']}; "
            f"zipBytes={first['zipBytes']}; files={first['manifest']['artifactFileCount'] + 1}; "
            f"frozenDataFiles={first['manifest']['scientificDataFreeze']['fileCount']}; "
            "openRecollations=22; versionDoi=null; archivalDepositStatus=pending; humanVerified=0"
        )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Validate the deterministic CHD scientific release-candidate bundle."""
from __future__ import annotations

import tempfile
import zipfile
from pathlib import Path

from build_release_candidate import (
    BUNDLE_DIRNAME,
    EXPECTED_CONTRACT_FREEZE_SHA256,
    MANIFEST_NAME,
    ZIP_NAME,
    build,
)

EXPECTED_SCHEMA_URL = "https://lex-0.org/releases/v0.9.5/schema/lex-0.rng"
EXPECTED_SCHEMA_SHA256 = "35e73fef48526634714bdf3d16b924f958fca078a903d0bdc2dd4d7d116d1aaa"
EXPECTED_OPEN_GATES = {
    "direct_facsimile_recollation_of_22_crossreference_cases",
    "final_release_tag_and_changelog",
    "archival_deposit_and_version_doi",
}
EXPECTED_INTEROPERABILITY = {
    "primaryLexicalReleaseProfile": "TEI Lex-0 0.9.5",
    "cldfRequiredForV1": False,
    "cldfStatus": "deferred_post_v1_analytic_derivative",
    "decisionDocument": "docs/CLDF_SCOPE_DECISION_V1_0.md",
    "canonicalDataReplacedByInteroperabilityFormats": False,
}
EXPECTED_CONTRACT_FREEZE = {
    "freezeId": "CHD-v1-contracts-2026-08-21",
    "manifestPath": "release/v1_contract_manifest.json",
    "manifestSha256": EXPECTED_CONTRACT_FREEZE_SHA256,
    "schemaContractCount": 22,
    "sourceScopeMetadataCount": 4,
    "contractCount": 26,
    "exactBytesFrozenForV1": True,
    "silentContractChangesAllowed": False,
    "releaseIdentityMetadataDeferredToTagGate": True,
}


def validate_manifest(manifest: dict) -> None:
    if manifest["packageType"] != "scientific_release_candidate":
        raise SystemExit("unexpected release-candidate package type")
    if manifest["packageStatus"] != "development_not_v1_0_0":
        raise SystemExit("release candidate must remain explicitly pre-v1.0")
    if manifest["releaseReady"] is not False:
        raise SystemExit("release candidate must not declare releaseReady=true")
    if manifest["facsimileIncluded"] is not False:
        raise SystemExit("release candidate unexpectedly includes/reports facsimile")
    if manifest["thirdPartyReproductionsRelicensed"] is not False:
        raise SystemExit("release candidate must not relicense third-party reproductions")
    if manifest["humanVerifiedCount"] != 0:
        raise SystemExit("release candidate must preserve humanVerifiedCount=0")
    if set(manifest["openGates"]) != EXPECTED_OPEN_GATES:
        raise SystemExit(f"release-candidate open gates drifted: {manifest['openGates']}")
    if manifest.get("interoperabilityDecision") != EXPECTED_INTEROPERABILITY:
        raise SystemExit("release-candidate interoperability decision drifted")
    if manifest.get("contractFreeze") != EXPECTED_CONTRACT_FREEZE:
        raise SystemExit(
            "release-candidate v1 contract freeze drifted: "
            f"{manifest.get('contractFreeze')} != {EXPECTED_CONTRACT_FREEZE}"
        )

    summary = manifest["summary"]
    expected = {
        "lexiconArticleCount": 2302,
        "canonicalCrossReferenceCount": 150,
        "strictCrossReferenceEdgeCount": 60,
        "strictCrossReferenceCycleCount": 4,
        "sourceReviewRecordCount": 90,
        "reviewedViewEdgeCount": 100,
        "facsimileRecollationQueueCount": 22,
        "grammarObjectCount": 302,
        "grammarEvidenceRowCount": 1215,
        "grammarRulesWithStructuredClaim": 370,
        "grammarRuleComparisonUniverse": 373,
        "teiEntryCount": 2302,
        "teiLex0ConformanceClaimed": True,
        "externalLex0SchemaValidationEnforcedInCI": True,
        "externalLex0SchemaUrl": EXPECTED_SCHEMA_URL,
        "externalLex0SchemaSha256": EXPECTED_SCHEMA_SHA256,
    }
    if summary != expected:
        raise SystemExit(f"release-candidate scientific summary drifted: {summary} != {expected}")
    if manifest["artifactFileCount"] <= 20 or manifest["artifactBytes"] <= 0:
        raise SystemExit("release candidate artifact inventory is invalid")


def validate_zip(result: dict) -> None:
    zip_path = result["zipPath"]
    manifest = result["manifest"]
    with zipfile.ZipFile(zip_path) as archive:
        names = archive.namelist()
        if names != sorted(names):
            raise SystemExit("release-candidate ZIP members are not sorted deterministically")
        if len(names) != manifest["artifactFileCount"] + 1:
            raise SystemExit("ZIP member count disagrees with package manifest")
        required = {
            f"{BUNDLE_DIRNAME}/{MANIFEST_NAME}",
            f"{BUNDLE_DIRNAME}/project/docs/CLDF_SCOPE_DECISION_V1_0.md",
            f"{BUNDLE_DIRNAME}/project/release/v1_contract_manifest.json",
        }
        missing = sorted(required - set(names))
        if missing:
            raise SystemExit(f"release-candidate ZIP missing required release records: {missing}")
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
            raise SystemExit("release-candidate manifests differ across two builds")
        if first["zipSha256"] != second["zipSha256"]:
            raise SystemExit(
                "release-candidate ZIP hash differs across two builds: "
                f"{first['zipSha256']} != {second['zipSha256']}"
            )
        if first["zipPath"].read_bytes() != second["zipPath"].read_bytes():
            raise SystemExit("release-candidate ZIP bytes differ across two builds")

        print(
            "release-candidate QA OK: "
            f"zip={ZIP_NAME}; sha256={first['zipSha256']}; "
            f"files={first['manifest']['artifactFileCount'] + 1}; "
            f"artifactBytes={first['manifest']['artifactBytes']}; "
            f"openGates={len(first['manifest']['openGates'])}; "
            "Lex0ConformanceClaimed=true; CLDFRequiredForV1=false; "
            "contractsFrozen=26; releaseReady=false; humanVerified=0"
        )


if __name__ == "__main__":
    main()

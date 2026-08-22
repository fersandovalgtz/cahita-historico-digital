#!/usr/bin/env python3
"""Validate deterministic CHD post-v1 historical-variation exports."""
from __future__ import annotations

import filecmp
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPORTER = ROOT / "scripts" / "export_historical_variation_index.py"
SCHEMA_VALIDATOR = ROOT / "scripts" / "validate_jsonl.py"
SCHEMA = ROOT / "schemas" / "historical-variety-observation.schema.json"
EXPECTED_FILES = {
    "chd_historical_variation_index.jsonl",
    "chd_historical_variation_index.csv",
    "chd_historical_variety_observations.jsonl",
    "chd_historical_variation_coverage.csv",
    "manifest.json",
}
REQUIRED_LABELS = {"Hiaqui", "Mayo", "Thehueco", "Naciones", "Cynaloa"}


def run_export(path: Path) -> None:
    subprocess.run(
        [sys.executable, str(EXPORTER), "--out-dir", str(path)],
        cwd=ROOT,
        check=True,
    )


def load_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"invalid JSONL at {path}:{line_number}: {exc}") from exc
        if not isinstance(obj, dict):
            raise SystemExit(f"JSONL record is not an object at {path}:{line_number}")
        rows.append(obj)
    return rows


def validate_manifest(path: Path) -> dict:
    manifest = json.loads((path / "manifest.json").read_text(encoding="utf-8"))
    if manifest.get("canonicalDatasetVersion") != "1.0.0":
        raise SystemExit("historical-variation manifest lost canonical dataset version")
    if manifest.get("canonicalTag") != "v1.0.0":
        raise SystemExit("historical-variation manifest lost canonical tag")
    if manifest.get("canonicalTagCommit") != "dbcdecf0003ac5a10ae963caf6babdcf5c22128d":
        raise SystemExit("historical-variation manifest lost immutable v1 provenance anchor")

    policy = manifest.get("authorityPolicy", {})
    forbidden_true = (
        "modernLanguageIdentityInferred",
        "dialectTaxonomyInferred",
        "linguisticSimilarityUsed",
        "cognacyInferred",
    )
    for key in forbidden_true:
        if policy.get(key) is not False:
            raise SystemExit(f"authority policy must keep {key}=false")
    if policy.get("sourceLabelsRemainHistoricalDocumentaryEvidence") is not True:
        raise SystemExit("historical labels must remain documentary evidence")

    coverage = manifest.get("coverage", {})
    if coverage.get("digitalPageTotal") != 182:
        raise SystemExit("coverage must account for all 182 digital pages")
    claim = manifest.get("coverageClaim", {})
    if claim.get("exhaustiveAcrossCurrentCanonicalMachineReadableLayers") is not True:
        raise SystemExit("manifest must declare exhaustive scan of current canonical machine-readable layers")
    if claim.get("exhaustiveDiplomaticTranscriptionOfAll182Pages") is not False:
        raise SystemExit("manifest must not claim exhaustive diplomatic transcription of 182 pages")
    pending = coverage.get("pendingOrUnreviewedPages") or []
    if not pending:
        raise SystemExit("coverage unexpectedly claims no pending/unreviewed pages")
    for expected_page in (176, 177, 178, 179, 180):
        if expected_page not in pending:
            raise SystemExit(f"known pending/unreviewed page {expected_page} missing from coverage manifest")

    labels = set((manifest.get("labelClassCounts") or {}).keys())
    missing = REQUIRED_LABELS - labels
    if missing:
        raise SystemExit(f"expected documentary label classes absent from index: {sorted(missing)}")

    if manifest.get("evidenceRecordCount", 0) <= 0:
        raise SystemExit("historical-variation index is empty")
    if manifest.get("schemaObservationCount", 0) <= 0:
        raise SystemExit("schema-conforming historical observations are empty")
    return manifest


def validate_rows(path: Path, manifest: dict) -> None:
    evidence = load_jsonl(path / "chd_historical_variation_index.jsonl")
    observations = load_jsonl(path / "chd_historical_variety_observations.jsonl")
    if len(evidence) != manifest["evidenceRecordCount"]:
        raise SystemExit("evidence record count differs from manifest")
    if len(observations) != manifest["schemaObservationCount"]:
        raise SystemExit("observation count differs from manifest")

    ids = [row.get("evidenceId") for row in evidence]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate evidenceId in historical-variation index")
    observation_ids = [row.get("id") for row in observations]
    if len(observation_ids) != len(set(observation_ids)):
        raise SystemExit("duplicate historical observation ID")

    for row in evidence:
        if row.get("modernIdentityInferred") is not False:
            raise SystemExit(f"modern identity inference detected in {row.get('evidenceId')}")
        if not row.get("labelClasses"):
            raise SystemExit(f"empty labelClasses in {row.get('evidenceId')}")

    human_verified_evidence = sum(1 for row in evidence if row.get("humanVerified") is True)
    if human_verified_evidence != manifest.get("humanVerifiedEvidenceCount"):
        raise SystemExit("humanVerified evidence count drift")
    if human_verified_evidence != 0:
        raise SystemExit(
            "post-v1 historical variation unexpectedly contains human-verified evidence; "
            "review provenance before changing this invariant"
        )

    for row in observations:
        if row.get("humanVerified") is True or row.get("reviewStatus") == "human_verified":
            raise SystemExit("schema observation silently elevated human verification")
        caution = row.get("caution") or ""
        if "modern" not in caution.lower():
            raise SystemExit(f"observation {row.get('id')} lacks explicit modern-identity caution")


def compare_directories(first: Path, second: Path) -> None:
    first_files = {path.name for path in first.iterdir() if path.is_file()}
    second_files = {path.name for path in second.iterdir() if path.is_file()}
    if first_files != EXPECTED_FILES or second_files != EXPECTED_FILES:
        raise SystemExit(
            f"unexpected output file set: first={sorted(first_files)} second={sorted(second_files)}"
        )
    for name in sorted(EXPECTED_FILES):
        if not filecmp.cmp(first / name, second / name, shallow=False):
            raise SystemExit(f"historical-variation export is not deterministic: {name}")


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="chd-var-a-") as a, tempfile.TemporaryDirectory(
        prefix="chd-var-b-"
    ) as b:
        first = Path(a)
        second = Path(b)
        run_export(first)
        run_export(second)
        compare_directories(first, second)
        manifest = validate_manifest(first)
        validate_rows(first, manifest)
        subprocess.run(
            [
                sys.executable,
                str(SCHEMA_VALIDATOR),
                "--schema",
                str(SCHEMA),
                "--jsonl",
                str(first / "chd_historical_variety_observations.jsonl"),
            ],
            cwd=ROOT,
            check=True,
        )
        print(
            "historical variation QA OK: "
            f"evidence={manifest['evidenceRecordCount']}; "
            f"observations={manifest['schemaObservationCount']}; "
            f"labels={manifest['labelClassCounts']}; "
            "deterministic=true; modernIdentityInferred=false; humanVerified=0"
        )


if __name__ == "__main__":
    main()

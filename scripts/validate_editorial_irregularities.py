#!/usr/bin/env python3
"""Validate deterministic CHD post-v1 editorial-irregularity exports and authority invariants."""
from __future__ import annotations

import filecmp
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPORTER = ROOT / "scripts" / "export_editorial_irregularities.py"
SCHEMA_VALIDATOR = ROOT / "scripts" / "validate_jsonl.py"
SCHEMA = ROOT / "schemas" / "editorial-irregularity.schema.json"
EXPECTED_FILES = {
    "chd_editorial_irregularities.jsonl",
    "chd_editorial_irregularities.csv",
    "manifest.json",
}
EXPECTED_IDS = {
    "ALC1737-irreg-structural-part-count",
    "ALC1737-irreg-rule-0127-omission",
    "ALC1737-irreg-rule-0129-repetition",
    "ALC1737-irreg-rule-0178-omission",
    "ALC1737-irreg-rule-0294-omission",
    "ALC1737-irreg-boundary-p069",
    "ALC1737-irreg-boundary-p105",
    "ALC1737-irreg-ocr-rule-p089-0242",
    "ALC1737-irreg-ocr-rule-p102-0282",
}
EXPECTED_CATEGORIES = {
    "structural_self_description_conflict": 1,
    "printed_number_omission": 3,
    "printed_number_repetition": 1,
    "intra_page_section_boundary": 2,
    "ocr_facsimile_disagreement": 2,
}


def run_export(out_dir: Path) -> None:
    subprocess.run(
        [sys.executable, str(EXPORTER), "--out-dir", str(out_dir)],
        cwd=ROOT,
        check=True,
    )


def load_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"invalid JSONL at {path}:{number}: {exc}") from exc
        if not isinstance(obj, dict):
            raise SystemExit(f"record at {path}:{number} is not a JSON object")
        rows.append(obj)
    return rows


def compare_directories(a: Path, b: Path) -> None:
    a_files = {p.name for p in a.iterdir() if p.is_file()}
    b_files = {p.name for p in b.iterdir() if p.is_file()}
    if a_files != EXPECTED_FILES or b_files != EXPECTED_FILES:
        raise SystemExit(f"unexpected derivative file set: a={sorted(a_files)} b={sorted(b_files)}")
    for name in sorted(EXPECTED_FILES):
        if not filecmp.cmp(a / name, b / name, shallow=False):
            raise SystemExit(f"editorial-irregularity export is not deterministic: {name}")


def validate_manifest(out_dir: Path) -> dict:
    manifest = json.loads((out_dir / "manifest.json").read_text(encoding="utf-8"))
    if manifest.get("canonicalDatasetVersion") != "1.0.0":
        raise SystemExit("manifest lost canonical v1 dataset version")
    if manifest.get("canonicalTag") != "v1.0.0":
        raise SystemExit("manifest lost canonical v1 tag")
    if manifest.get("canonicalTagCommit") != "dbcdecf0003ac5a10ae963caf6babdcf5c22128d":
        raise SystemExit("manifest lost immutable v1 provenance anchor")
    if manifest.get("recordCount") != 9:
        raise SystemExit(f"expected 9 documented irregularities, got {manifest.get('recordCount')}")
    if manifest.get("categoryCounts") != EXPECTED_CATEGORIES:
        raise SystemExit(f"category count drift: {manifest.get('categoryCounts')}")
    if manifest.get("humanVerifiedRecordCount") != 0:
        raise SystemExit("derivative unexpectedly contains human-verified irregularity records")
    if manifest.get("deterministic") is not True:
        raise SystemExit("manifest must declare deterministic=true")

    policy = manifest.get("authorityPolicy", {})
    expected_policy = {
        "sourceDescriptionPreserved": True,
        "silentNormalizationPerformed": False,
        "silentRenumberingPerformed": False,
        "modernLinguisticInferencePerformed": False,
        "humanVerificationElevatedByDerivative": False,
    }
    if policy != expected_policy:
        raise SystemExit(f"authority policy drift: {policy}")
    return manifest


def validate_records(out_dir: Path, manifest: dict) -> None:
    rows = load_jsonl(out_dir / "chd_editorial_irregularities.jsonl")
    if len(rows) != manifest["recordCount"]:
        raise SystemExit("record count differs from manifest")
    ids = [row.get("id") for row in rows]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate irregularity IDs")
    if set(ids) != EXPECTED_IDS:
        raise SystemExit(f"irregularity ID set drift: got={sorted(ids)}")

    for row in rows:
        if row.get("humanVerified") is not False:
            raise SystemExit(f"humanVerified must remain false in {row.get('id')}")
        authority = row.get("authority", {})
        if authority.get("sourceDescriptionPreserved") is not True:
            raise SystemExit(f"source description not preserved in {row.get('id')}")
        for key in (
            "silentNormalizationPerformed",
            "silentRenumberingPerformed",
            "modernLinguisticInferencePerformed",
        ):
            if authority.get(key) is not False:
                raise SystemExit(f"forbidden authority transition {key}=true in {row.get('id')}")

    omission_numbers = sorted(
        row.get("structuredData", {}).get("omittedRuleNumber")
        for row in rows
        if row.get("category") == "printed_number_omission"
    )
    if omission_numbers != [127, 178, 294]:
        raise SystemExit(f"printed-number omission set drift: {omission_numbers}")

    repeated = [row for row in rows if row.get("category") == "printed_number_repetition"]
    if len(repeated) != 1 or repeated[0].get("structuredData", {}).get("printedRuleNumber") != 129:
        raise SystemExit("printed-number repetition 129 is not represented exactly once")

    boundary_pages = sorted(
        row["sourcePagesDigital"][0]
        for row in rows
        if row.get("category") == "intra_page_section_boundary"
    )
    if boundary_pages != [69, 105]:
        raise SystemExit(f"intra-page boundary set drift: {boundary_pages}")

    ocr_pairs = sorted(
        (
            row.get("structuredData", {}).get("ocrReading"),
            row.get("structuredData", {}).get("facsimileReading"),
        )
        for row in rows
        if row.get("category") == "ocr_facsimile_disagreement"
    )
    if ocr_pairs != [(241, 242), (281, 282)]:
        raise SystemExit(f"OCR/facsimile disagreement set drift: {ocr_pairs}")


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="chd-irreg-a-") as a, tempfile.TemporaryDirectory(
        prefix="chd-irreg-b-"
    ) as b:
        first = Path(a)
        second = Path(b)
        run_export(first)
        run_export(second)
        compare_directories(first, second)
        manifest = validate_manifest(first)
        validate_records(first, manifest)
        subprocess.run(
            [
                sys.executable,
                str(SCHEMA_VALIDATOR),
                "--schema",
                str(SCHEMA),
                "--jsonl",
                str(first / "chd_editorial_irregularities.jsonl"),
            ],
            cwd=ROOT,
            check=True,
        )
        print(
            "editorial irregularities QA OK: "
            f"records={manifest['recordCount']}; categories={manifest['categoryCounts']}; "
            "deterministic=true; silentRenumbering=false; humanVerified=0"
        )


if __name__ == "__main__":
    main()

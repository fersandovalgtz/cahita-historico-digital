#!/usr/bin/env python3
"""Validate deterministic grammar-derived exports without adding authority."""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPORTER = ROOT / "scripts/export_grammar_evidence_concordance.py"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_export(out_dir: Path) -> None:
    subprocess.run(
        [sys.executable, str(EXPORTER), "--out-dir", str(out_dir)],
        cwd=ROOT,
        check=True,
    )


def compare_dirs(first: Path, second: Path) -> None:
    first_files = sorted(p.relative_to(first) for p in first.rglob("*") if p.is_file())
    second_files = sorted(p.relative_to(second) for p in second.rglob("*") if p.is_file())
    if first_files != second_files:
        raise SystemExit("grammar concordance file-set mismatch between deterministic runs")
    for relative in first_files:
        left = first / relative
        right = second / relative
        if left.read_bytes() != right.read_bytes():
            raise SystemExit(
                f"grammar concordance non-deterministic bytes for {relative}: "
                f"{sha256(left)} != {sha256(right)}"
            )


def validate_manifest(manifest: dict) -> None:
    if manifest["canonicalInputFileCount"] <= 0:
        raise SystemExit("grammar concordance has no canonical input files")
    if manifest["canonicalObjectCount"] <= 0:
        raise SystemExit("grammar concordance has no canonical objects")
    if manifest["evidenceRowCount"] <= 0:
        raise SystemExit("grammar concordance is empty")
    if sum(manifest["objectKindCounts"].values()) != manifest["canonicalObjectCount"]:
        raise SystemExit("grammar object-kind counts are inconsistent")
    if sum(manifest["evidenceRoleCounts"].values()) != manifest["evidenceRowCount"]:
        raise SystemExit("grammar evidence-role counts are inconsistent")
    for key in (
        "linguisticIdentityInferred",
        "normalizedFormGenerated",
        "crossObjectLinkingPerformed",
        "tokenPagePrecisionInferred",
        "canonicalGrammarModified",
    ):
        if manifest[key] is not False:
            raise SystemExit(f"grammar concordance guard must remain false: {key}")
    if not manifest["deterministic"]:
        raise SystemExit("grammar concordance must declare deterministic=true")
    required_roles = {"example", "lemma", "formation_marker", "paradigm_form"}
    missing = sorted(required_roles - set(manifest["evidenceRoleCounts"]))
    if missing:
        raise SystemExit(f"grammar concordance is missing expected evidence roles: {missing}")


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        first = base / "run1"
        second = base / "run2"
        run_export(first)
        run_export(second)
        compare_dirs(first, second)
        manifest = json.loads((first / "manifest.json").read_text(encoding="utf-8"))
        validate_manifest(manifest)
        print(
            "grammar export QA OK: "
            f"{manifest['canonicalObjectCount']} objects from "
            f"{manifest['canonicalInputFileCount']} files; "
            f"{manifest['evidenceRowCount']} evidence rows; "
            f"humanVerified={manifest['humanVerifiedObjectCount']}; "
            f"manifest sha256 {sha256(first / 'manifest.json')}"
        )


if __name__ == "__main__":
    main()

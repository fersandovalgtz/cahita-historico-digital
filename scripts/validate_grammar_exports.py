#!/usr/bin/env python3
"""Validate deterministic grammar-derived exports without adding authority."""
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


def run_export(script: str, out_dir: Path) -> None:
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
                f"{label}: non-deterministic bytes for {relative}: "
                f"{sha256(left)} != {sha256(right)}"
            )


def validate_concordance(manifest: dict) -> None:
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


def validate_rule_coverage(manifest: dict) -> None:
    universe = manifest["comparisonUniverse"]
    if universe != {"minRule": 1, "maxRule": 373, "ruleCount": 373}:
        raise SystemExit(f"unexpected grammar rule comparison universe: {universe}")
    covered = manifest["rulesWithStructuredClaim"]
    uncovered = manifest["rulesWithoutStructuredClaim"]
    if covered <= 0 or uncovered <= 0:
        raise SystemExit("grammar rule coverage audit must expose both covered and uncovered rules")
    if covered + uncovered != 373:
        raise SystemExit("grammar rule coverage counts do not sum to 373")
    if manifest["grammarObjectCount"] <= 0 or manifest["grammarFileCount"] <= 0:
        raise SystemExit("grammar rule coverage audit has no canonical grammar inputs")
    if manifest["objectsWithoutExplicitRuleClaim"] <= 0:
        raise SystemExit("grammar rule coverage audit unexpectedly reports no unlocated objects")
    if manifest["gapRangeCount"] <= 0:
        raise SystemExit("grammar rule coverage audit unexpectedly reports no gap ranges")
    if manifest["outsideComparisonUniverseClaimCount"] != 0:
        raise SystemExit("grammar rule coverage audit found claims outside rules 1..373")
    for key in (
        "sourceRuleExistenceInferred",
        "ruleContentInferred",
        "implicitCoverageInferred",
        "canonicalGrammarModified",
    ):
        if manifest[key] is not False:
            raise SystemExit(f"grammar rule coverage guard must remain false: {key}")
    if not manifest["deterministic"]:
        raise SystemExit("grammar rule coverage audit must declare deterministic=true")


def validate_pipeline(
    label: str,
    script: str,
    validator: Callable[[dict], None],
) -> dict:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        first = base / "run1"
        second = base / "run2"
        run_export(script, first)
        run_export(script, second)
        compare_dirs(first, second, label)
        manifest = json.loads((first / "manifest.json").read_text(encoding="utf-8"))
        validator(manifest)
        print(
            f"{label}: deterministic across two runs; "
            f"manifest sha256 {sha256(first / 'manifest.json')}"
        )
        return manifest


def main() -> None:
    concordance = validate_pipeline(
        "grammar evidence concordance",
        "export_grammar_evidence_concordance.py",
        validate_concordance,
    )
    coverage = validate_pipeline(
        "grammar rule-coverage audit",
        "export_grammar_rule_coverage.py",
        validate_rule_coverage,
    )
    print(
        "grammar export QA OK: "
        f"{concordance['canonicalObjectCount']} objects from "
        f"{concordance['canonicalInputFileCount']} files; "
        f"{concordance['evidenceRowCount']} evidence rows; "
        f"humanVerified={concordance['humanVerifiedObjectCount']}; "
        f"numbered-rule coverage={coverage['rulesWithStructuredClaim']}/373; "
        f"uncovered={coverage['rulesWithoutStructuredClaim']}; "
        f"gap ranges={coverage['gapRangeCount']}"
    )


if __name__ == "__main__":
    main()

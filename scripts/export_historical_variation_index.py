#!/usr/bin/env python3
"""Generate the historical-variation derivative and synchronize terminal coverage semantics."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "scripts" / "export_historical_variation_index_core.py"
DEFAULT_OUT_DIR = ROOT / "build" / "historical-variation-index"
MATERIAL_PAGES = [1, 2, 4, 14, 181, 182]
TEXTUAL_PAGE_COUNT = 176


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    args = parser.parse_args()
    out_dir = args.out_dir if args.out_dir.is_absolute() else ROOT / args.out_dir

    subprocess.run(
        [sys.executable, str(CORE), "--out-dir", str(out_dir)],
        cwd=ROOT,
        check=True,
    )

    manifest_path = out_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    coverage = manifest.get("coverage") or {}
    claim = manifest.setdefault("coverageClaim", {})

    terminal = (
        coverage.get("digitalPageTotal") == 182
        and coverage.get("transcriptionFilePageCount") == TEXTUAL_PAGE_COUNT
        and coverage.get("pendingOrUnreviewedPageCount") == 0
        and coverage.get("notApplicableMaterialPages") == MATERIAL_PAGES
    )
    claim["exhaustiveDiplomaticTranscriptionOfAllTextualPages"] = terminal
    if terminal:
        claim["reason"] = (
            "All 176 textual digital pages have canonical full-page diplomatic transcriptions; "
            "six digital pages are non-textual material and remain not_applicable_material."
        )
    else:
        claim["reason"] = (
            "The index scans every currently canonical machine-readable transcription, lexicon and grammar object; "
            "coverage details identify any remaining textual or material gaps."
        )

    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        "historical variation coverage claim synchronized: "
        f"textualComplete={str(terminal).lower()}; "
        f"transcriptionFiles={coverage.get('transcriptionFilePageCount')}; "
        f"pending={coverage.get('pendingOrUnreviewedPageCount')}"
    )


if __name__ == "__main__":
    main()

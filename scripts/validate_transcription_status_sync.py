#!/usr/bin/env python3
"""Validate deterministic reconciliation of transcription status metadata."""
from __future__ import annotations

import csv
import filecmp
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECONCILER = ROOT / "scripts" / "reconcile_transcription_status.py"
PAGES_DIR = ROOT / "data" / "transcription" / "pages"


def run(out_dir: Path) -> None:
    subprocess.run(
        [sys.executable, str(RECONCILER), "--out-dir", str(out_dir)],
        cwd=ROOT,
        check=True,
    )


def load_status(path: Path) -> dict[int, dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 182:
        raise SystemExit(f"candidate status must contain 182 rows, got {len(rows)}")
    pages = [int(row["digital_page"]) for row in rows]
    if pages != list(range(1, 183)):
        raise SystemExit("candidate status pages must be exactly 1-182 in order")
    return {int(row["digital_page"]): row for row in rows}


def actual_page_files() -> dict[int, tuple[Path, dict]]:
    found: dict[int, tuple[Path, dict]] = {}
    for path in sorted(PAGES_DIR.glob("ALC1737_p*.json")):
        obj = json.loads(path.read_text(encoding="utf-8"))
        page = obj.get("sourcePageDigital")
        if not isinstance(page, int):
            raise SystemExit(f"invalid sourcePageDigital in {path}")
        if page in found:
            raise SystemExit(f"duplicate page JSON for page {page}")
        found[page] = (path, obj)
    return found


def validate_candidate(out_dir: Path) -> dict:
    candidate = load_status(out_dir / "status.csv")
    audit = json.loads((out_dir / "audit.json").read_text(encoding="utf-8"))
    actual = actual_page_files()

    if audit.get("digitalPageTotal") != 182:
        raise SystemExit("audit lost 182-page accounting")
    if audit.get("actualPageTranscriptionFileCount") != len(actual):
        raise SystemExit("audit actual page-file count drift")
    if audit.get("reconciledTranscriptionFileCount") != len(actual):
        raise SystemExit("candidate status does not declare every actual page file exactly once")
    if audit.get("statusWillMatchActualPageFilesAfterApply") is not True:
        raise SystemExit("audit does not certify post-apply page-file synchronization")

    declared_pages: set[int] = set()
    for page, row in candidate.items():
        declared = row.get("transcription_file", "").strip()
        if declared:
            declared_pages.add(page)
            if page not in actual:
                raise SystemExit(f"candidate declares page file for page {page}, but no canonical JSON exists")
        if page not in actual:
            continue
        path, obj = actual[page]
        expected_path = path.relative_to(ROOT).as_posix()
        if declared != expected_path:
            raise SystemExit(
                f"page {page} transcription path mismatch: expected {expected_path!r}, got {declared!r}"
            )
        checks = {
            "coverage": obj.get("coverage"),
            "review_status": obj.get("reviewStatus"),
            "section": obj.get("section"),
            "uncertainty_count": str(len(obj.get("uncertainties") or [])),
        }
        if obj.get("sourcePagePrinted") is not None:
            checks["printed_page"] = str(obj["sourcePagePrinted"])
        for field, expected in checks.items():
            if expected is None:
                continue
            if row.get(field, "") != str(expected):
                raise SystemExit(
                    f"page {page} field {field} mismatch: expected {expected!r}, got {row.get(field)!r}"
                )

    if declared_pages != set(actual):
        raise SystemExit("candidate declared page set differs from canonical page JSON set")

    pending = audit.get("remainingPendingTextualPages") or []
    if any(page in actual for page in pending):
        raise SystemExit("audit marks an existing canonical page JSON as pending textual work")
    if audit.get("remainingPendingTextualPageCount") != len(pending):
        raise SystemExit("pending textual page count drift")

    material = audit.get("materialPagesWithoutTranscription") or []
    if any(page in actual for page in material):
        raise SystemExit("audit marks an existing canonical page JSON as material-without-transcription")

    return audit


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="chd-status-a-") as a, tempfile.TemporaryDirectory(
        prefix="chd-status-b-"
    ) as b:
        first = Path(a)
        second = Path(b)
        run(first)
        run(second)
        for name in ("status.csv", "audit.json"):
            if not filecmp.cmp(first / name, second / name, shallow=False):
                raise SystemExit(f"status reconciliation is not deterministic: {name}")
        audit = validate_candidate(first)
        print(
            "transcription status sync QA OK: "
            f"actualFiles={audit['actualPageTranscriptionFileCount']}; "
            f"declaredBefore={audit['statusDeclaredTranscriptionFileCountBefore']}; "
            f"missingDeclarationsBefore={audit['actualFilesMissingFromStatusDeclarationCount']}; "
            f"fullPageAfter={audit['reconciledFullPageCount']}; "
            f"remainingPendingTextual={audit['remainingPendingTextualPageCount']}; "
            "deterministic=true"
        )


if __name__ == "__main__":
    main()

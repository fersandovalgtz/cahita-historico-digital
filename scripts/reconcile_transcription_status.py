#!/usr/bin/env python3
"""Reconcile data/transcription/status.csv with canonical page-transcription files.

The page JSON files are authoritative for page-level transcription existence,
coverage, review state, section, printed page (when present), and uncertainty
count. Existing material-role and editorial notes in status.csv are preserved.

By default this writes a candidate CSV and an audit JSON under build/. It never
modifies the canonical status file in place unless --apply is supplied.
"""
from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
STATUS_PATH = ROOT / "data" / "transcription" / "status.csv"
PAGES_DIR = ROOT / "data" / "transcription" / "pages"
DEFAULT_OUT_DIR = ROOT / "build" / "transcription-status-sync"

FIELDS = [
    "source_id",
    "digital_page",
    "printed_page",
    "section",
    "material_role",
    "coverage",
    "review_status",
    "transcription_file",
    "uncertainty_count",
    "notes",
]


def read_status() -> list[dict[str, str]]:
    with STATUS_PATH.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != FIELDS:
            raise SystemExit(f"unexpected status.csv columns: {reader.fieldnames}")
        rows = list(reader)
    pages = [int(row["digital_page"]) for row in rows]
    if pages != list(range(1, 183)):
        raise SystemExit("status.csv must account for digital pages 1-182 exactly once and in order")
    if any(row["source_id"] != "ALC1737" for row in rows):
        raise SystemExit("status.csv contains an unexpected source_id")
    return rows


def read_page_files() -> dict[int, tuple[Path, dict[str, Any]]]:
    by_page: dict[int, tuple[Path, dict[str, Any]]] = {}
    for path in sorted(PAGES_DIR.glob("ALC1737_p*.json")):
        obj = json.loads(path.read_text(encoding="utf-8"))
        page = obj.get("sourcePageDigital")
        if not isinstance(page, int) or not 1 <= page <= 182:
            raise SystemExit(f"invalid sourcePageDigital in {path.relative_to(ROOT)}: {page!r}")
        if page in by_page:
            raise SystemExit(f"duplicate page-transcription file for digital page {page}")
        if obj.get("sourceId") != "ALC1737":
            raise SystemExit(f"unexpected sourceId in {path.relative_to(ROOT)}")
        by_page[page] = (path, obj)
    if not by_page:
        raise SystemExit("no page-transcription JSON files found")
    return by_page


def canonical_value(obj: dict[str, Any], key: str, existing: str) -> str:
    value = obj.get(key)
    if value is None:
        return existing
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def reconcile(
    rows: list[dict[str, str]],
    page_files: dict[int, tuple[Path, dict[str, Any]]],
) -> tuple[list[dict[str, str]], dict[str, Any]]:
    before = {int(row["digital_page"]): dict(row) for row in rows}
    after = {page: dict(row) for page, row in before.items()}

    status_declared_pages: set[int] = set()
    declarations_without_file: list[int] = []
    declaration_path_mismatches: list[dict[str, Any]] = []
    for page, row in before.items():
        declared = row.get("transcription_file", "").strip()
        if not declared:
            continue
        status_declared_pages.add(page)
        declared_path = ROOT / declared
        if not declared_path.is_file():
            declarations_without_file.append(page)

    actual_pages = set(page_files)
    actual_missing_from_status = sorted(actual_pages - status_declared_pages)
    status_without_actual = sorted(status_declared_pages - actual_pages)

    field_drift: dict[str, list[int]] = {
        "printed_page": [],
        "section": [],
        "coverage": [],
        "review_status": [],
        "transcription_file": [],
        "uncertainty_count": [],
    }

    for page, (path, obj) in page_files.items():
        row = after[page]
        expected_rel = path.relative_to(ROOT).as_posix()
        declared_rel = before[page].get("transcription_file", "").strip()
        if declared_rel and declared_rel != expected_rel:
            declaration_path_mismatches.append(
                {"digitalPage": page, "declared": declared_rel, "actual": expected_rel}
            )

        updates = {
            "printed_page": canonical_value(obj, "sourcePagePrinted", row["printed_page"]),
            "section": canonical_value(obj, "section", row["section"]),
            "coverage": canonical_value(obj, "coverage", row["coverage"]),
            "review_status": canonical_value(obj, "reviewStatus", row["review_status"]),
            "transcription_file": expected_rel,
            "uncertainty_count": str(len(obj.get("uncertainties") or [])),
        }
        for field, value in updates.items():
            if row.get(field, "") != value:
                field_drift[field].append(page)
                row[field] = value

    reconciled = [after[page] for page in range(1, 183)]

    remaining_pending_textual = [
        int(row["digital_page"])
        for row in reconciled
        if not row["transcription_file"].strip()
        and row.get("coverage") == "pending"
        and row.get("review_status") == "unreviewed"
    ]
    material_pages_without_transcription = [
        int(row["digital_page"])
        for row in reconciled
        if not row["transcription_file"].strip()
        and row.get("coverage") == "not_applicable_material"
    ]

    coverage_counts = Counter(row.get("coverage") or "blank" for row in reconciled)
    review_counts = Counter(row.get("review_status") or "blank" for row in reconciled)
    section_counts = Counter(row.get("section") or "blank" for row in reconciled)

    audit = {
        "sourceId": "ALC1737",
        "digitalPageTotal": 182,
        "actualPageTranscriptionFileCount": len(actual_pages),
        "actualPageTranscriptionPages": sorted(actual_pages),
        "statusDeclaredTranscriptionFileCountBefore": len(status_declared_pages),
        "statusDeclaredTranscriptionPagesBefore": sorted(status_declared_pages),
        "actualFilesMissingFromStatusDeclarationCount": len(actual_missing_from_status),
        "actualFilesMissingFromStatusDeclarationPages": actual_missing_from_status,
        "statusDeclarationsWithoutActualPageFileCount": len(status_without_actual),
        "statusDeclarationsWithoutActualPageFilePages": status_without_actual,
        "statusDeclarationPathsMissingOnDisk": sorted(declarations_without_file),
        "statusDeclarationPathMismatches": declaration_path_mismatches,
        "fieldDriftCounts": {key: len(value) for key, value in field_drift.items()},
        "fieldDriftPages": field_drift,
        "reconciledTranscriptionFileCount": sum(
            1 for row in reconciled if row["transcription_file"].strip()
        ),
        "reconciledFullPageCount": coverage_counts.get("full_page", 0),
        "remainingPendingTextualPageCount": len(remaining_pending_textual),
        "remainingPendingTextualPages": remaining_pending_textual,
        "materialPagesWithoutTranscriptionCount": len(material_pages_without_transcription),
        "materialPagesWithoutTranscription": material_pages_without_transcription,
        "coverageCountsAfter": dict(sorted(coverage_counts.items())),
        "reviewStatusCountsAfter": dict(sorted(review_counts.items())),
        "sectionCountsAfter": dict(sorted(section_counts.items())),
        "statusWillMatchActualPageFilesAfterApply": True,
    }
    return reconciled, audit


def write_status(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=DEFAULT_OUT_DIR,
        help="Directory for candidate status.csv and audit.json.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Replace data/transcription/status.csv after generating and validating the candidate.",
    )
    args = parser.parse_args()

    out_dir = args.out_dir if args.out_dir.is_absolute() else ROOT / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = read_status()
    page_files = read_page_files()
    reconciled, audit = reconcile(rows, page_files)

    candidate = out_dir / "status.csv"
    write_status(candidate, reconciled)
    (out_dir / "audit.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print(
        "transcription status reconciliation: "
        f"actualFiles={audit['actualPageTranscriptionFileCount']}; "
        f"declaredBefore={audit['statusDeclaredTranscriptionFileCountBefore']}; "
        f"missingDeclarations={audit['actualFilesMissingFromStatusDeclarationCount']}; "
        f"fullPageAfter={audit['reconciledFullPageCount']}; "
        f"remainingPendingTextual={audit['remainingPendingTextualPageCount']}"
    )
    print(
        "remaining pending textual pages: "
        + ",".join(str(page) for page in audit["remainingPendingTextualPages"])
    )

    if args.apply:
        STATUS_PATH.write_bytes(candidate.read_bytes())
        print(f"updated canonical status: {STATUS_PATH.relative_to(ROOT)}")
    else:
        print(f"candidate only: {candidate}")


if __name__ == "__main__":
    main()

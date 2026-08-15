#!/usr/bin/env python3
"""Reproducible local ingest for Cahíta Histórico Digital source ALC1737.

The script does not download or redistribute the facsimile. It takes the two
working files as explicit inputs, computes checksums, extracts the PDF text
layer page by page with Poppler's pdftotext, and writes auditable derivatives.

Usage:
    python scripts/ingest_alc1737.py \
        --pdf /path/to/Cahíta.pdf \
        --html /path/to/Cahíta.html \
        --out build/alc1737
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

SOURCE_ID = "ALC1737"
PAGE_COUNT = 182


class PreTextExtractor(HTMLParser):
    """Collect text inside the first HTML <pre> element without web requests."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_pre = False
        self.finished = False
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag.lower() == "pre" and not self.finished:
            self.in_pre = True

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "pre" and self.in_pre:
            self.in_pre = False
            self.finished = True

    def handle_data(self, data: str) -> None:
        if self.in_pre and not self.finished:
            self.parts.append(data)

    def text(self) -> str:
        return "".join(self.parts)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def section_for(page: int) -> str:
    if 1 <= page <= 14:
        return "preliminaries"
    if 15 <= page <= 50:
        return "part_i"
    if 51 <= page <= 68:
        return "part_ii"
    if 69 <= page <= 104:
        return "part_iii"
    if 105 <= page <= 132:
        return "part_iv"
    if 133 <= page <= 177:
        return "vocabulary"
    if 178 <= page <= 180:
        return "numerals"
    return "end_matter"


STRUCTURAL_LABELS = {
    1: "front_cover",
    2: "bookplate",
    3: "title_page",
    4: "title_page_verso_drawing",
    5: "dedication_start",
    11: "al_lector",
    13: "errata_and_vocabulario_abbreviations",
    14: "errata_verso",
    15: "part_i_start",
    51: "part_ii_start",
    69: "part_iii_start",
    105: "part_iv_start",
    132: "fin_del_arte",
    133: "vocabulary_start",
    178: "numerals_start",
    180: "fin_volume",
    181: "inside_back_cover",
    182: "back_cover",
}


def printed_page(page: int) -> int | None:
    return page - 14 if 15 <= page <= 132 else None


def extract_pdf_page(pdf: Path, page: int) -> str:
    cmd = [
        "pdftotext",
        "-f",
        str(page),
        "-l",
        str(page),
        "-layout",
        str(pdf),
        "-",
    ]
    result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode("utf-8", errors="replace")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", required=True, type=Path)
    parser.add_argument("--html", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()

    if shutil.which("pdftotext") is None:
        raise SystemExit("pdftotext (Poppler) is required but was not found in PATH")
    if not args.pdf.is_file() or not args.html.is_file():
        raise SystemExit("Both --pdf and --html must point to existing files")

    args.out.mkdir(parents=True, exist_ok=True)

    html_source = args.html.read_text(encoding="utf-8", errors="replace")
    extractor = PreTextExtractor()
    extractor.feed(html_source)
    archive_text = extractor.text()
    if not archive_text:
        raise SystemExit("No <pre> full-text block was found in the saved HTML")
    archive_text_path = args.out / "archive_fulltext_raw.txt"
    archive_text_path.write_text(archive_text, encoding="utf-8")

    rows: list[dict[str, object]] = []
    jsonl: list[str] = []

    for page in range(1, PAGE_COUNT + 1):
        raw_text = extract_pdf_page(args.pdf, page)
        raw_hash = sha256_bytes(raw_text.encode("utf-8"))
        pprinted = printed_page(page)
        label = STRUCTURAL_LABELS.get(page, "")
        status = "boundary_sample_verified" if pprinted is not None else (
            "structural_manual" if label else "unpaginated"
        )
        rows.append(
            {
                "digital_page": page,
                "printed_page": pprinted if pprinted is not None else "",
                "section": section_for(page),
                "structural_label": label,
                "ocr_source": "pdf_text_layer_pdftotext_layout",
                "ocr_characters": len(raw_text),
                "ocr_sha256": raw_hash,
                "has_nonwhitespace_ocr": "true" if raw_text.strip("\x0c\r\n \t") else "false",
                "mapping_status": status,
            }
        )
        jsonl.append(
            json.dumps(
                {
                    "source_id": SOURCE_ID,
                    "digital_page": page,
                    "printed_page": pprinted,
                    "section": section_for(page),
                    "structural_label": label or None,
                    "extraction_method": "pdftotext -layout (Poppler)",
                    "text_sha256": raw_hash,
                    "raw_text": raw_text,
                },
                ensure_ascii=False,
            )
        )

    page_manifest = args.out / "page_manifest_full.csv"
    with page_manifest.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    ocr_jsonl = args.out / "ocr_raw_pages.jsonl"
    ocr_jsonl.write_text("\n".join(jsonl) + "\n", encoding="utf-8")

    manifest = {
        "source_id": SOURCE_ID,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "input_files": [
            {
                "name": args.pdf.name,
                "bytes": args.pdf.stat().st_size,
                "sha256": sha256_file(args.pdf),
                "role": "working_facsimile_pdf",
                "pages": PAGE_COUNT,
            },
            {
                "name": args.html.name,
                "bytes": args.html.stat().st_size,
                "sha256": sha256_file(args.html),
                "role": "saved_internet_archive_full_text_page",
            },
        ],
        "derived_files": [
            {
                "name": archive_text_path.name,
                "bytes": archive_text_path.stat().st_size,
                "sha256": sha256_file(archive_text_path),
                "method": "first <pre> text extracted from saved HTML",
            },
            {
                "name": ocr_jsonl.name,
                "bytes": ocr_jsonl.stat().st_size,
                "sha256": sha256_file(ocr_jsonl),
                "records": PAGE_COUNT,
                "method": "pdftotext -layout, one JSON object per PDF page",
            },
            {
                "name": page_manifest.name,
                "bytes": page_manifest.stat().st_size,
                "sha256": sha256_file(page_manifest),
                "records": PAGE_COUNT,
            },
        ],
        "printed_pagination_mapping": {
            "digital_pages": "15-132",
            "printed_pages": "1-118",
            "formula": "printed_page = digital_page - 14",
            "verification": "sampled visually at digital pages 15, 51, 69, 105 and 132",
        },
        "warning": "OCR outputs are evidence layers and are not diplomatic transcriptions.",
    }
    (args.out / "ingest_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

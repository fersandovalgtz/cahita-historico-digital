#!/usr/bin/env python3
"""Extract page/column-aware raw OCR lines for ALC1737 vocabulary pages.

Uses Poppler's `pdftotext -bbox-layout` so that the two-column vocabulary can
be represented as layout-aware OCR evidence without pretending that OCR lines
are lexicographic entries.

The source scan alternates recto/verso horizontal placement. Column origins are
therefore inferred independently on every page from line-start coordinates.
Lines that appear to merge both columns are retained as `other`.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

NS = {"x": "http://www.w3.org/1999/xhtml"}
SOURCE = "ALC1737"


def page_xml(pdf: Path, page: int) -> bytes:
    return subprocess.check_output(
        ["pdftotext", "-f", str(page), "-l", str(page), "-bbox-layout", str(pdf), "-"]
    )


def infer_split(starts: list[float]) -> tuple[float, float, float]:
    """Infer two column origins from line-start x coordinates via 1-D k-means."""
    if len(starts) < 4:
        return 0.0, 106.5, 53.25
    c1, c2 = min(starts), max(starts)
    for _ in range(20):
        g1 = [x for x in starts if abs(x - c1) <= abs(x - c2)]
        g2 = [x for x in starts if abs(x - c1) > abs(x - c2)]
        if not g1 or not g2:
            break
        n1, n2 = sum(g1) / len(g1), sum(g2) / len(g2)
        if abs(n1 - c1) + abs(n2 - c2) < 1e-6:
            c1, c2 = n1, n2
            break
        c1, c2 = n1, n2
    left, right = sorted((c1, c2))
    return left, right, (left + right) / 2


def classify_column(xmin: float, xmax: float, split: float) -> str:
    # OCR occasionally merges text from both physical columns into one line.
    if xmax - xmin > 135:
        return "other"
    return "left" if xmin < split else "right"


def extract_page(pdf: Path, page_num: int):
    root = ET.fromstring(page_xml(pdf, page_num))
    page = root.find(".//x:page", NS)
    raw = []
    for line in page.findall(".//x:line", NS):
        words = line.findall("x:word", NS)
        if not words:
            continue
        text = " ".join((w.text or "") for w in words).strip()
        if not text:
            continue
        raw.append(
            {
                "xmin": min(float(w.attrib["xMin"]) for w in words),
                "xmax": max(float(w.attrib["xMax"]) for w in words),
                "ymin": min(float(w.attrib["yMin"]) for w in words),
                "ymax": max(float(w.attrib["yMax"]) for w in words),
                "text_raw": text,
            }
        )

    starts = [r["xmin"] for r in raw if len(r["text_raw"]) > 1]
    left_origin, right_origin, split = infer_split(starts)
    out = []
    for r in raw:
        r["column"] = classify_column(r["xmin"], r["xmax"], split)
        r["split_x"] = split
        r["left_origin_x"] = left_origin
        r["right_origin_x"] = right_origin
        out.append(r)

    rank = {"left": 0, "right": 1, "other": 2}
    out.sort(key=lambda r: (rank[r["column"]], r["ymin"], r["xmin"]))
    counters = {"left": 0, "right": 0, "other": 0}
    for r in out:
        counters[r["column"]] += 1
        r["order_in_column"] = counters[r["column"]]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", type=Path, required=True)
    ap.add_argument("--start-page", type=int, default=133)
    ap.add_argument("--end-page", type=int, default=177)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    args.out.parent.mkdir(parents=True, exist_ok=True)

    total = 0
    with args.out.open("w", encoding="utf-8") as f:
        for p in range(args.start_page, args.end_page + 1):
            section = "vocabulary" if p <= 177 else "numerals"
            for r in extract_page(args.pdf, p):
                total += 1
                rec = {
                    "id": f'{SOURCE}-vline-p{p:03d}-{r["column"][0].upper()}-{r["order_in_column"]:03d}',
                    "sourceId": SOURCE,
                    "sourcePageDigital": p,
                    "sourcePagePrinted": None,
                    "section": section,
                    "column": r["column"],
                    "orderInColumn": r["order_in_column"],
                    "bbox": {
                        k: round(r[k], 3) for k in ("xmin", "ymin", "xmax", "ymax")
                    },
                    "textRaw": r["text_raw"],
                    "extractionMethod": "pdftotext -bbox-layout (Poppler)",
                    "evidenceLayer": "ocr_raw",
                    "reviewStatus": "raw_ocr",
                }
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"wrote {total} raw layout lines to {args.out}")


if __name__ == "__main__":
    main()

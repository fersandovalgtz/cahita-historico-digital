#!/usr/bin/env python3
"""Generate conservative article-boundary candidates from ALC1737 vocabulary layout.

This script intentionally does NOT split a candidate into Spanish lemma and Cahíta form.
It only groups raw OCR lines using indentation/layout cues. Every record remains a
machine candidate and must be promoted editorially before becoming a lexical entry.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from extract_vocab_layout import extract_page

SOURCE = "ALC1737"


def meaningful(text: str) -> bool:
    text = text.strip()
    if not text or len(text) < 2:
        return False
    if re.fullmatch(r"[\W_0-9]+", text):
        return False
    return True


def start_margin(rows) -> float:
    xs = sorted(r["xmin"] for r in rows if meaningful(r["text_raw"]))
    if not xs:
        return 0.0
    # Lower decile is more stable than min against stray ornament/noise fragments.
    return xs[max(0, int(len(xs) * 0.10) - 1)]


def group_column(page: int, column: str, rows):
    rows = [
        r
        for r in rows
        if r["column"] == column and r["ymin"] >= 65 and meaningful(r["text_raw"])
    ]
    rows.sort(key=lambda r: (r["ymin"], r["xmin"]))
    if not rows:
        return []

    margin = start_margin(rows)
    threshold = margin + 5.0
    groups = []
    current = None

    for r in rows:
        first = (r["text_raw"].lstrip()[:1] or "")
        letterish = first.isalpha() or first in "ÁÉÍÓÚÜÑáéíóúüñſ"
        is_start = r["xmin"] <= threshold and letterish
        if is_start:
            if current:
                groups.append(current)
            current = {"lines": [r], "margin": margin, "threshold": threshold}
        elif current:
            current["lines"].append(r)
        # Pre-start material is deliberately not forced into an article.

    if current:
        groups.append(current)
    return groups


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
        for page in range(args.start_page, args.end_page + 1):
            layout = extract_page(args.pdf, page)
            for column in ("left", "right"):
                groups = group_column(page, column, layout)
                for idx, group in enumerate(groups, 1):
                    total += 1
                    lines = group["lines"]
                    raw = " ".join(r["text_raw"] for r in lines)
                    flags = []
                    if idx == 1:
                        flags.append("first_candidate_in_column_may_continue_previous_text")
                    if raw.endswith("-"):
                        flags.append("ends_with_hyphen_possible_continuation")

                    rec = {
                        "candidateId": f"{SOURCE}-vcand-p{page:03d}-{column[0].upper()}-{idx:03d}",
                        "sourceId": SOURCE,
                        "sourcePageDigital": page,
                        "sourcePagePrinted": None,
                        "column": column,
                        "candidateOrderInColumn": idx,
                        "startY": round(lines[0]["ymin"], 3),
                        "lineCount": len(lines),
                        "rawLines": [r["text_raw"] for r in lines],
                        "rawText": raw,
                        "boundaryMethod": "indentation_margin_v0.1",
                        "boundaryStatus": "machine_candidate",
                        "reviewStatus": "raw_ocr",
                        "flags": flags,
                    }
                    f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    print(f"wrote {total} article-boundary candidates to {args.out}")


if __name__ == "__main__":
    main()

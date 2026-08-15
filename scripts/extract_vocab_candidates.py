#!/usr/bin/env python3
"""Generate conservative article-boundary candidates from ALC1737 vocabulary layout.

Version 0.2 improves article-start recall while preserving the high precision of
v0.1. It uses a modal left-margin estimate for ordinary vocabulary pages and
retains v0.1's lower-decile rule for the first vocabulary page (digital p. 133),
whose section-opening material destabilizes the modal estimator.

This script intentionally does NOT split a candidate into Spanish lemma and
Cahíta form. Every record remains a machine candidate and must be reviewed
before promotion to a lexical entry.
"""
from __future__ import annotations

import argparse
import json
import re
import statistics
from pathlib import Path

from extract_vocab_layout import extract_page

SOURCE = "ALC1737"
METHOD = "hybrid_margin_mode_v0.2"
HEADER = re.compile(
    r"^(VOCAB|DE LA LENGV|DE LA LENGUA|YOCXB|VELA LEUG|DE LA LEUG)", re.I
)


def meaningful(text: str) -> bool:
    text = text.strip()
    if not text or len(text) < 2:
        return False
    if re.fullmatch(r"[\W_0-9]+", text):
        return False
    return True


def legacy_start_margin(rows) -> float:
    """v0.1 lower-decile estimator used only on the first vocabulary page."""
    xs = sorted(r["xmin"] for r in rows if meaningful(r["text_raw"]))
    if not xs:
        return 0.0
    return xs[max(0, int(len(xs) * 0.10) - 1)]


def modal_start_margin(rows) -> float:
    """Estimate the recurrent article-start x-position from 3-point bins."""
    xs = [
        r["xmin"]
        for r in rows
        if meaningful(r["text_raw"]) and not HEADER.search(r["text_raw"])
    ]
    if not xs:
        return 0.0
    bins: dict[float, list[float]] = {}
    for x in xs:
        b = round(x / 3.0) * 3.0
        bins.setdefault(b, []).append(x)
    peak = max(bins, key=lambda k: (len(bins[k]), -k))
    neighborhood = [
        x for k, values in bins.items() if abs(k - peak) <= 3 for x in values
    ]
    return statistics.median(neighborhood)


def group_column(page: int, column: str, rows):
    if page == 133:
        # The section-opening page has header/carry-over material that makes the
        # modal estimator unstable. Preserve v0.1's more conservative geometry.
        page_rows = [
            r
            for r in rows
            if r["column"] == column
            and r["ymin"] >= 65
            and meaningful(r["text_raw"])
        ]
        page_rows.sort(key=lambda r: (r["ymin"], r["xmin"]))
        margin = legacy_start_margin(page_rows)
        threshold = margin + 5.0
        start_predicate = lambda r: r["xmin"] <= threshold
        rule = "legacy_first_vocabulary_page"
    else:
        page_rows = [
            r
            for r in rows
            if r["column"] == column
            and r["ymin"] >= 50
            and meaningful(r["text_raw"])
            and not HEADER.search(r["text_raw"])
        ]
        page_rows.sort(key=lambda r: (r["ymin"], r["xmin"]))
        margin = modal_start_margin(page_rows)
        tolerance = 6.0
        start_predicate = lambda r: abs(r["xmin"] - margin) <= tolerance
        rule = "modal_margin"

    groups = []
    current = None
    for r in page_rows:
        first = (r["text_raw"].lstrip()[:1] or "")
        letterish = first.isalpha() or first in "ÁÉÍÓÚÜÑáéíóúüñſ"
        is_start = bool(letterish and start_predicate(r))
        if is_start:
            if current:
                groups.append(current)
            current = {"lines": [r]}
        elif current:
            current["lines"].append(r)
    if current:
        groups.append(current)
    return margin, rule, groups


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
                margin, page_rule, groups = group_column(page, column, layout)
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
                        "candidateId": (
                            f"{SOURCE}-vcand-p{page:03d}-{column[0].upper()}-{idx:03d}"
                        ),
                        "sourceId": SOURCE,
                        "sourcePageDigital": page,
                        "sourcePagePrinted": None,
                        "column": column,
                        "candidateOrderInColumn": idx,
                        "startY": round(lines[0]["ymin"], 3),
                        "lineCount": len(lines),
                        "rawLines": [r["text_raw"] for r in lines],
                        "rawText": raw,
                        "boundaryMethod": METHOD,
                        "pageRule": page_rule,
                        "estimatedStartMarginX": round(margin, 3),
                        "boundaryStatus": "machine_candidate",
                        "reviewStatus": "raw_ocr",
                        "flags": flags,
                    }
                    f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    print(f"wrote {total} article-boundary candidates to {args.out}")


if __name__ == "__main__":
    main()

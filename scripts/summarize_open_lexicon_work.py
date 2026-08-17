#!/usr/bin/env python3
"""Summarize open lexicon curation work for digital pages 145–177.

The script is intentionally read-only with respect to canonical and curatorial data.
It derives a compact, machine-readable Phase II baseline from each page's
`pNNN_machine_reconciliation_status.json` record.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RECON = ROOT / "data" / "lexicon" / "reconciliation"


def _get(d: dict[str, Any], *paths: tuple[str, ...], default: Any = None) -> Any:
    for path in paths:
        cur: Any = d
        ok = True
        for key in path:
            if not isinstance(cur, dict) or key not in cur:
                ok = False
                break
            cur = cur[key]
        if ok:
            return cur
    return default


def page_record(page: int) -> dict[str, Any]:
    path = RECON / f"p{page}_machine_reconciliation_status.json"
    status = json.loads(path.read_text(encoding="utf-8"))

    classes = status.get("candidateInventory", {}).get("classification", {})
    boundaries = status.get("candidateInventory", {}).get("boundaryAssessment", {})

    pending = _get(
        status,
        ("promotion", "articleCandidatesPendingPromotion"),
        ("linkage", "articleCandidatesPendingPromotion"),
        default=0,
    )
    corpus = _get(
        status,
        ("promotion", "corpusTotalAfterPass"),
        ("curation", "corpusTotalAfterPass"),
        default=None,
    )
    exhaustive = _get(
        status,
        ("visibleStartEvidence", "exhaustive"),
        ("visibleStartCensus", "exhaustive"),
        default=False,
    )
    known_starts = _get(
        status,
        ("visibleStartEvidence", "knownVisibleStartsMinimum"),
        default=None,
    )
    known_misses = _get(
        status,
        ("visibleStartEvidence", "knownMissedStartRecords"),
        default=None,
    )

    evidence = status.get("evidence", {})
    terminal_decision = evidence.get("terminalDecision")
    unresolved = int(classes.get("unresolved", 0) or 0)

    return {
        "page": page,
        "candidateCount": status.get("candidateInventory", {}).get("total"),
        "articleCandidates": int(classes.get("article", 0) or 0),
        "continuations": int(classes.get("continuation", 0) or 0),
        "falsePositives": int(classes.get("false_positive", 0) or 0),
        "unresolvedCandidates": unresolved,
        "ambiguousBoundaries": int(boundaries.get("ambiguous", 0) or 0),
        "pendingPromotion": int(pending or 0),
        "knownVisibleStartsMinimum": known_starts,
        "knownMissedStartRecords": known_misses,
        "visibleStartCensusExhaustive": bool(exhaustive),
        "technicalClosure": bool(status.get("pageStatus", {}).get("technicalClosure", False)),
        "humanVerified": bool(status.get("humanVerified", False)),
        "corpusTotalAfterPass": corpus,
        "terminalDecision": terminal_decision,
        "statusPath": str(path.relative_to(ROOT)),
    }


def build_summary(start: int = 145, end: int = 177) -> dict[str, Any]:
    pages = [page_record(page) for page in range(start, end + 1)]
    pending_total = sum(p["pendingPromotion"] for p in pages)
    unresolved_total = sum(p["unresolvedCandidates"] for p in pages)
    ambiguous_total = sum(p["ambiguousBoundaries"] for p in pages)

    unresolved_pages = [
        {
            "page": p["page"],
            "count": p["unresolvedCandidates"],
            "terminalDecision": p["terminalDecision"],
        }
        for p in pages
        if p["unresolvedCandidates"]
    ]
    pending_rank = sorted(
        (
            {"page": p["page"], "pendingPromotion": p["pendingPromotion"]}
            for p in pages
            if p["pendingPromotion"]
        ),
        key=lambda x: (-x["pendingPromotion"], x["page"]),
    )

    corpus_totals = {p["corpusTotalAfterPass"] for p in pages if p["corpusTotalAfterPass"] is not None}

    return {
        "sourceId": "ALC1737",
        "scope": {"startDigitalPage": start, "endDigitalPage": end},
        "phase": "phase_ii_promotion_linkage_and_visible_start_census",
        "generatedFrom": "pNNN_machine_reconciliation_status.json",
        "summary": {
            "pages": len(pages),
            "pendingPromotionTotal": pending_total,
            "unresolvedCandidateTotal": unresolved_total,
            "ambiguousBoundaryTotal": ambiguous_total,
            "pagesWithExhaustiveVisibleStartCensus": sum(1 for p in pages if p["visibleStartCensusExhaustive"]),
            "pagesWithTechnicalClosure": sum(1 for p in pages if p["technicalClosure"]),
            "humanVerifiedPages": sum(1 for p in pages if p["humanVerified"]),
            "corpusTotalsObserved": sorted(corpus_totals),
        },
        "unresolvedPages": unresolved_pages,
        "pendingPromotionRanking": pending_rank,
        "pages": pages,
        "interpretiveGuards": [
            "pendingPromotion counts candidate-level article starts not yet promoted to curatorial lexical objects; it is not equivalent to missing articles without further collation.",
            "unresolved candidate structure is distinct from unresolved semantic/anaphoric content inside already structured articles.",
            "visible-start metrics remain withheld where exhaustive=false.",
            "humanVerified=false is preserved as the current project policy and must not be restated as human philological verification.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=145)
    parser.add_argument("--end", type=int, default=177)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    summary = build_summary(args.start, args.end)
    payload = json.dumps(summary, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        output = args.output if args.output.is_absolute() else ROOT / args.output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Summarize open Phase II lexicon work from machine reconciliation status files."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RECON_DIR = ROOT / "data" / "lexicon" / "reconciliation"
ARTICLES_DIR = ROOT / "data" / "lexicon" / "articles"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def current_article_ids() -> set[str]:
    ids: set[str] = set()
    for path in sorted(ARTICLES_DIR.glob("*.jsonl")):
        for raw_line in path.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line:
                continue
            obj = json.loads(line)
            article_id = obj.get("articleId")
            if isinstance(article_id, str):
                ids.add(article_id)
    return ids


def _first_int(*values: Any) -> int | None:
    for value in values:
        if isinstance(value, int) and not isinstance(value, bool):
            return value
    return None


def build_summary(start_page: int, end_page: int) -> dict[str, Any]:
    article_ids = current_article_ids()
    pages: list[dict[str, Any]] = []
    historical_corpus_totals: set[int] = set()

    for page in range(start_page, end_page + 1):
        status_path = RECON_DIR / f"p{page}_machine_reconciliation_status.json"
        if not status_path.exists():
            raise FileNotFoundError(status_path.relative_to(ROOT))

        status = load_json(status_path)
        inventory = status.get("candidateInventory", {})
        classification = inventory.get("classification", {})
        boundary = inventory.get("boundaryAssessment", {})
        linkage = status.get("linkage", {})
        promotion = status.get("promotion", {})
        page_status = status.get("pageStatus", {})
        visible = status.get("visibleStartEvidence", status.get("visibleStartCensus", {}))
        curation = status.get("curation", {})
        terminal = status.get("terminalDecision", {})

        candidate_count = _first_int(inventory.get("total"), status.get("canonicalCandidates")) or 0
        article_candidates = _first_int(classification.get("article"), status.get("articleCandidates")) or 0
        continuations = _first_int(classification.get("continuation"), status.get("continuationCandidates")) or 0
        false_positives = _first_int(classification.get("false_positive"), status.get("falsePositiveCandidates")) or 0
        unresolved_candidates = _first_int(classification.get("unresolved"), status.get("unresolvedCandidates")) or 0
        ambiguous_boundaries = _first_int(boundary.get("ambiguous"), status.get("ambiguousBoundaries")) or 0
        pending_promotion = _first_int(
            linkage.get("articleCandidatesPendingPromotion"),
            promotion.get("pendingPromotion"),
            status.get("pendingPromotion"),
        ) or 0

        visible_minimum = _first_int(
            visible.get("knownVisibleStartsMinimum"),
            visible.get("visibleHistoricalArticleStarts"),
            status.get("knownVisibleStartsMinimum"),
        )
        known_missed = _first_int(
            visible.get("knownMissedStartRecords"),
            visible.get("knownMissedStarts"),
            status.get("knownMissedStartRecords"),
        )
        exhaustive = bool(
            visible.get("exhaustive") is True
            or page_status.get("visibleStartCensus") in {
                "complete_exhaustive",
                "exhaustive_direct_local_facsimile",
            }
        )
        technical_closure = bool(page_status.get("technicalClosure") is True)
        human_verified = bool(status.get("humanVerified") is True)
        corpus_total = _first_int(curation.get("corpusTotalAfterPass"), status.get("corpusTotalAfterPass"))
        if corpus_total is not None:
            historical_corpus_totals.add(corpus_total)

        terminal_decision: str | None = None
        if isinstance(terminal, dict):
            value = terminal.get("decision")
            if isinstance(value, str):
                terminal_decision = value
        elif isinstance(terminal, str):
            terminal_decision = terminal

        pages.append(
            {
                "page": page,
                "candidateCount": candidate_count,
                "articleCandidates": article_candidates,
                "continuations": continuations,
                "falsePositives": false_positives,
                "unresolvedCandidates": unresolved_candidates,
                "ambiguousBoundaries": ambiguous_boundaries,
                "pendingPromotion": pending_promotion,
                "knownVisibleStartsMinimum": visible_minimum,
                "knownMissedStartRecords": known_missed,
                "visibleStartCensusExhaustive": exhaustive,
                "technicalClosure": technical_closure,
                "humanVerified": human_verified,
                "corpusTotalAfterPass": corpus_total,
                "terminalDecision": terminal_decision,
                "statusPath": str(status_path.relative_to(ROOT)),
            }
        )

    pending_total = sum(p["pendingPromotion"] for p in pages)
    unresolved_total = sum(p["unresolvedCandidates"] for p in pages)
    ambiguous_total = sum(p["ambiguousBoundaries"] for p in pages)

    pending_rank = [
        {"page": p["page"], "pendingPromotion": p["pendingPromotion"]}
        for p in sorted(pages, key=lambda p: (-p["pendingPromotion"], p["page"]))
        if p["pendingPromotion"] > 0
    ]
    unresolved_pages = [
        {
            "page": p["page"],
            "count": p["unresolvedCandidates"],
            "terminalDecision": p["terminalDecision"],
        }
        for p in pages
        if p["unresolvedCandidates"] > 0
    ]

    return {
        "sourceId": "ALC1737",
        "scope": {
            "startDigitalPage": start_page,
            "endDigitalPage": end_page,
        },
        "phase": "phase_ii_promotion_linkage_and_visible_start_census",
        "generatedFrom": [
            "pNNN_machine_reconciliation_status.json",
            "data/lexicon/articles/*.jsonl",
        ],
        "summary": {
            "pages": len(pages),
            "pendingPromotionTotal": pending_total,
            "unresolvedCandidateTotal": unresolved_total,
            "ambiguousBoundaryTotal": ambiguous_total,
            "pagesWithExhaustiveVisibleStartCensus": sum(1 for p in pages if p["visibleStartCensusExhaustive"]),
            "pagesWithTechnicalClosure": sum(1 for p in pages if p["technicalClosure"]),
            "humanVerifiedPages": sum(1 for p in pages if p["humanVerified"]),
            "currentCuratorialArticleCount": len(article_ids),
            "historicalCorpusTotalsRecordedInPageStatuses": sorted(historical_corpus_totals),
        },
        "unresolvedPages": unresolved_pages,
        "pendingPromotionRanking": pending_rank,
        "pages": pages,
        "interpretiveGuards": [
            "pendingPromotion counts candidate-level article starts not yet promoted to curatorial lexical objects; it is not equivalent to missing articles without further collation.",
            "currentCuratorialArticleCount is computed from unique articleId values across data/lexicon/articles/*.jsonl and represents the current repository state.",
            "historicalCorpusTotalsRecordedInPageStatuses are pass-time snapshots and may legitimately differ from the current curatorial count after later promotions.",
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
    payload = json.dumps(summary, ensure_ascii=False, separators=(",", ":")) + "\n"
    if args.output:
        output = args.output if args.output.is_absolute() else ROOT / args.output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()

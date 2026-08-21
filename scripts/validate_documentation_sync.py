#!/usr/bin/env python3
"""Fail CI when central current-status documentation drifts from canonical state.

This intentionally validates only a small set of current-status assertions for
completed Phase II and the active historical cross-reference review layer. It
is not a prose linter and does not rewrite documentation. Historical snapshots
may retain earlier counts elsewhere in the repository.
"""
from __future__ import annotations

import json
from pathlib import Path

from export_crossreference_candidate_diagnostics import build_diagnostics
from export_lexicon_crossreference_reviewed_view import build_view

ROOT = Path(__file__).resolve().parents[1]
SUMMARY = ROOT / "data/lexicon/reconciliation/phase2_open_work_summary.json"
PHASE2_DOCS = {
    "README.md": ROOT / "README.md",
    "ROADMAP.md": ROOT / "ROADMAP.md",
    "docs/PHASE2_COMPLETION_2026-08-21.md": ROOT / "docs/PHASE2_COMPLETION_2026-08-21.md",
}
XREF_DOC_NAME = "docs/CROSSREFERENCE_REVIEW_PROGRESS_2026-08-21.md"
XREF_DOC = ROOT / XREF_DOC_NAME


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise SystemExit(f"documentation sync failure: {label} missing {needle!r}")


def forbid(text: str, needle: str, label: str) -> None:
    if needle in text:
        raise SystemExit(f"documentation sync failure: {label} still contains stale {needle!r}")


def validate_phase2() -> tuple[int, int, int, int, int, int]:
    data = json.loads(SUMMARY.read_text(encoding="utf-8"))
    summary = data["summary"]

    pages = int(summary["pages"])
    closed = int(summary["pagesWithTechnicalClosure"])
    exhaustive = int(summary["pagesWithExhaustiveVisibleStartCensus"])
    pending = int(summary["pendingPromotionTotal"])
    unresolved = int(summary["unresolvedCandidateTotal"])
    ambiguous = int(summary["ambiguousBoundaryTotal"])
    articles = int(summary["currentCuratorialArticleCount"])
    human = int(summary["humanVerifiedPages"])

    if not (
        pages == 33
        and closed == pages
        and exhaustive == pages
        and pending == 0
        and unresolved == 0
        and ambiguous == 0
        and human == 0
    ):
        raise SystemExit(
            "documentation sync guard expects completed Phase II; canonical "
            f"state is pages={pages}, closed={closed}, exhaustive={exhaustive}, "
            f"pending={pending}, unresolved={unresolved}, ambiguous={ambiguous}, "
            f"humanVerifiedPages={human}"
        )

    rendered_articles = f"{articles:,}"
    texts = {name: path.read_text(encoding="utf-8") for name, path in PHASE2_DOCS.items()}

    for name, text in texts.items():
        require(text, rendered_articles, name)
        require(text, "33", name)
        forbid(text, "1,047 candidatos `pending_promotion`", name)
        forbid(text, "1,049 artículos históricos estructurados", name)

    require(texts["README.md"], "0 candidatos `pending_promotion`", "README.md")
    require(texts["README.md"], "33/33 páginas", "README.md")
    require(texts["ROADMAP.md"], "`pendingPromotionTotal = 0`", "ROADMAP.md")
    require(texts["ROADMAP.md"], "33 / 33 páginas", "ROADMAP.md")
    require(
        texts["docs/PHASE2_COMPLETION_2026-08-21.md"],
        "**0** candidatos `pending_promotion`",
        "docs/PHASE2_COMPLETION_2026-08-21.md",
    )
    return closed, pages, articles, pending, unresolved, ambiguous


def validate_crossreference_review_docs() -> tuple[int, int, int, int, int, int]:
    _diagnostic_rows, diagnostic = build_diagnostics(5)
    _view_rows, _view_graph, reviewed = build_view()

    total = int(reviewed["canonicalCrossReferenceCount"])
    strict_edges = int(reviewed["strictGraphEdgeCount"])
    reviews = int(reviewed["sourceReviewRecordCount"])
    view_edges = int(reviewed["reviewedViewEdgeCount"])
    statuses = reviewed["reviewedViewStatusCounts"]
    decisions = reviewed["reviewDecisionCounts"]
    tiers = diagnostic["priorityTierCounts"]

    strict_not_located = int(diagnostic["strictNotLocatedAudited"])
    editorial_unique = int(statuses.get("editorial_source_supported_unique", 0))
    recollation = int(statuses.get("editorial_requires_recollation", 0))
    unreviewed = int(statuses.get("strict_not_located_unreviewed", 0))

    if strict_edges + strict_not_located + 1 != total:
        raise SystemExit(
            "cross-reference documentation guard found unexpected strict-state arithmetic: "
            f"strictEdges={strict_edges}, notLocated={strict_not_located}, total={total}"
        )
    if reviews != sum(int(value) for value in decisions.values()):
        raise SystemExit("cross-reference review decision counts are inconsistent")
    if editorial_unique != int(decisions.get("source_supports_unique_target", 0)):
        raise SystemExit("cross-reference reviewed-view and decision counts disagree")
    if reviews + unreviewed != strict_not_located:
        raise SystemExit(
            "cross-reference reviewed/unreviewed counts do not partition strict not_located"
        )
    if view_edges != strict_edges + editorial_unique:
        raise SystemExit("reviewed-view edge count does not equal strict + editorial unique edges")

    text = XREF_DOC.read_text(encoding="utf-8")
    require(text, f"**{total} remisiones históricas**", XREF_DOC_NAME)
    require(text, f"**{strict_edges} aristas `exact_unique`**", XREF_DOC_NAME)
    require(text, f"**{strict_not_located} remisiones `not_located`**", XREF_DOC_NAME)
    require(text, f"**{int(tiers['A_unique_strong'])} `A_unique_strong`**", XREF_DOC_NAME)
    require(text, f"**{int(tiers['B_multiple_strong'])} `B_multiple_strong`**", XREF_DOC_NAME)
    require(text, f"**{int(tiers['C_no_strong'])} `C_no_strong`**", XREF_DOC_NAME)
    require(text, f"**{reviews} revisiones explícitas**", XREF_DOC_NAME)
    require(
        text,
        f"**{editorial_unique}** tienen `decisionStatus=source_supports_unique_target`",
        XREF_DOC_NAME,
    )
    require(text, f"**{view_edges} aristas efectivas**", XREF_DOC_NAME)
    recollation_noun = "caso" if recollation == 1 else "casos"
    require(
        text,
        f"**{recollation} {recollation_noun} `editorial_requires_recollation`**",
        XREF_DOC_NAME,
    )
    require(text, f"**{unreviewed} casos `strict_not_located_unreviewed`**", XREF_DOC_NAME)

    return total, strict_edges, strict_not_located, reviews, editorial_unique, unreviewed


def main() -> None:
    closed, pages, articles, pending, unresolved, ambiguous = validate_phase2()
    total, strict_edges, strict_not_located, reviews, editorial_unique, unreviewed = (
        validate_crossreference_review_docs()
    )

    print(
        "documentation sync OK: "
        f"Phase II {closed}/{pages} closed, {articles} articles, "
        f"pending={pending}, unresolved={unresolved}, ambiguous={ambiguous}; "
        f"crossRefs={total}, strictEdges={strict_edges}, strictNotLocated={strict_not_located}, "
        f"sourceReviews={reviews}, editorialUnique={editorial_unique}, unreviewed={unreviewed}"
    )


if __name__ == "__main__":
    main()

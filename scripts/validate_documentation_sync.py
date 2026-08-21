#!/usr/bin/env python3
"""Fail CI when central Phase II documentation drifts from canonical state.

This intentionally validates only a small set of current-status assertions. It
is not a prose linter and does not rewrite documentation. Historical snapshots
may retain earlier counts elsewhere in the repository.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUMMARY = ROOT / "data/lexicon/reconciliation/phase2_open_work_summary.json"
DOCS = {
    "README.md": ROOT / "README.md",
    "ROADMAP.md": ROOT / "ROADMAP.md",
    "docs/PHASE2_COMPLETION_2026-08-21.md": ROOT / "docs/PHASE2_COMPLETION_2026-08-21.md",
}


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise SystemExit(f"documentation sync failure: {label} missing {needle!r}")


def forbid(text: str, needle: str, label: str) -> None:
    if needle in text:
        raise SystemExit(f"documentation sync failure: {label} still contains stale {needle!r}")


def main() -> None:
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
    texts = {name: path.read_text(encoding="utf-8") for name, path in DOCS.items()}

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

    print(
        "documentation sync OK: "
        f"Phase II {closed}/{pages} closed, {articles} articles, "
        f"pending={pending}, unresolved={unresolved}, ambiguous={ambiguous}"
    )


if __name__ == "__main__":
    main()

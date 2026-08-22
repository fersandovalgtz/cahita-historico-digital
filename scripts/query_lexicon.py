#!/usr/bin/env python3
"""Conservative local query tool for the canonical CHD lexical corpus.

The command reads ``data/lexicon/articles/*.jsonl`` directly. It performs
case-insensitive Unicode substring matching only; it does not modernize spelling,
replace long-s, infer cognacy, or map historical language labels to modern ones.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
ARTICLE_DIR = ROOT / "data/lexicon/articles"


def load_articles() -> list[dict[str, Any]]:
    articles: list[dict[str, Any]] = []
    for path in sorted(ARTICLE_DIR.glob("*.jsonl")):
        for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not raw.strip():
                continue
            try:
                articles.append(json.loads(raw))
            except json.JSONDecodeError as exc:
                raise SystemExit(f"invalid JSON in {path}:{line_no}: {exc}") from exc
    articles.sort(key=lambda row: int(str(row["articleId"]).rsplit("-", 1)[1]))
    return articles


def flatten_strings(value: Any) -> Iterable[str]:
    if value is None:
        return
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from flatten_strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from flatten_strings(item)


def fields_for(article: dict[str, Any], field: str) -> list[str]:
    keys_by_field = {
        "spanish": ["spanishGuideRaw", "sourceGroupingRaw"],
        "cahita": ["cahitaFormsRaw"],
        "transcription": ["transcriptionRaw"],
        "all": [
            "spanishGuideRaw",
            "sourceGroupingRaw",
            "cahitaFormsRaw",
            "transcriptionRaw",
            "notesRaw",
            "editorialNote",
        ],
    }
    strings: list[str] = []
    for key in keys_by_field[field]:
        strings.extend(flatten_strings(article.get(key)))
    return strings


def article_summary(article: dict[str, Any]) -> dict[str, Any]:
    return {
        "articleId": article.get("articleId"),
        "sourcePageDigital": article.get("sourcePageDigital"),
        "sourcePagePrinted": article.get("sourcePagePrinted"),
        "column": article.get("column"),
        "spanishGuideRaw": article.get("spanishGuideRaw"),
        "cahitaFormsRaw": article.get("cahitaFormsRaw"),
        "articleType": article.get("articleType"),
        "reviewStatus": article.get("reviewStatus"),
        "humanVerified": article.get("humanVerified"),
    }


def print_text(rows: list[dict[str, Any]]) -> None:
    for row in rows:
        guide = row.get("spanishGuideRaw")
        cahita = row.get("cahitaFormsRaw")
        print(
            f"{row.get('articleId')} | p.{row.get('sourcePageDigital')} "
            f"{row.get('column')} | {guide!r} → {cahita!r} | "
            f"review={row.get('reviewStatus')} humanVerified={row.get('humanVerified')}"
        )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Query canonical Cahíta Histórico Digital lexical articles without normalization/inference."
    )
    parser.add_argument("query", nargs="?", help="Unicode substring to search for")
    parser.add_argument(
        "--field",
        choices=["spanish", "cahita", "transcription", "all"],
        default="all",
        help="Field group to search (default: all)",
    )
    parser.add_argument("--limit", type=int, default=20, help="Maximum matches to print")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of human-readable lines")
    parser.add_argument("--stats", action="store_true", help="Print canonical corpus statistics and exit")
    args = parser.parse_args()

    if args.limit < 1:
        raise SystemExit("--limit must be >= 1")

    articles = load_articles()

    if args.stats:
        stats = {
            "canonicalArticleFiles": len(list(ARTICLE_DIR.glob("*.jsonl"))),
            "historicalLexicalArticles": len(articles),
            "humanVerifiedCount": sum(bool(row.get("humanVerified")) for row in articles),
            "queryPolicy": "case-insensitive Unicode substring; no spelling modernization or language-identity inference",
        }
        if args.json:
            print(json.dumps(stats, ensure_ascii=False, sort_keys=True, indent=2))
        else:
            for key, value in stats.items():
                print(f"{key}: {value}")
        return

    if not args.query:
        parser.error("query is required unless --stats is used")

    needle = args.query.casefold()
    matches: list[dict[str, Any]] = []
    for article in articles:
        haystack = fields_for(article, args.field)
        if any(needle in value.casefold() for value in haystack):
            matches.append(article_summary(article))
            if len(matches) >= args.limit:
                break

    if args.json:
        print(json.dumps(matches, ensure_ascii=False, sort_keys=True, indent=2))
    else:
        print_text(matches)
        print(f"matchesShown: {len(matches)}")


if __name__ == "__main__":
    main()

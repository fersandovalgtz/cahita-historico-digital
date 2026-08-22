#!/usr/bin/env python3
"""Validate the explicit review layer for historical `Lo miſmo` formulas."""
from __future__ import annotations

import json
import unicodedata
from collections import Counter
from pathlib import Path

from jsonschema import Draft202012Validator

from export_lexicon_crossreference_graph import load_articles
from export_lexicon_lo_mismo import load_candidates

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas/lo-mismo-source-review.schema.json"
REVIEW_GLOB = "data/lexicon/review/lo_mismo_source_review_*.jsonl"


def norm(text: str) -> str:
    value = unicodedata.normalize("NFKC", text).replace("ſ", "s").casefold()
    return " ".join(value.split()).strip(" .,:;")


def load_reviews() -> tuple[list[dict], list[Path]]:
    records: list[dict] = []
    paths = sorted(ROOT.glob(REVIEW_GLOB))
    if not paths:
        raise SystemExit("no Lo miſmo source-review files found")
    for path in paths:
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise SystemExit(f"invalid JSON in {path}:{lineno}: {exc}") from exc
    return records, paths


def main() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    reviews, paths = load_reviews()
    candidates, _, _ = load_candidates()
    articles, _ = load_articles()
    article_by_id = {a["articleId"]: a for a in articles}

    errors: list[str] = []
    review_ids: set[str] = set()
    source_ids: set[str] = set()

    for record in reviews:
        rid = record.get("reviewId", "<missing-reviewId>")
        for error in sorted(validator.iter_errors(record), key=lambda e: list(e.path)):
            errors.append(f"{rid}: schema error at {list(error.path)}: {error.message}")

        if rid in review_ids:
            errors.append(f"duplicate reviewId: {rid}")
        review_ids.add(rid)

        aid = record.get("sourceArticleId")
        if aid in source_ids:
            errors.append(f"duplicate sourceArticleId in Lo miſmo reviews: {aid}")
        source_ids.add(aid)

        if norm(str(record.get("formulaRaw", ""))) != "lo mismo":
            errors.append(f"{rid}: formulaRaw is not normalized Lo miſmo")

        if record.get("humanVerified") is not False:
            errors.append(f"{rid}: current Lo miſmo review layer must remain humanVerified=false")
        if record.get("reviewStatus") == "human_verified":
            errors.append(f"{rid}: human_verified is not supported by current evidence")
        if record.get("previousEntryAnaphoraSupported") is True:
            errors.append(f"{rid}: previous-entry anaphora cannot be asserted in current review layer")

        for guard in (
            "referentialScopeInferred",
            "targetLanguageFormInferred",
            "borrowingInferred",
            "semanticEquivalenceInferred",
        ):
            if record.get(guard) is not False:
                errors.append(f"{rid}: non-inference guard must be false: {guard}")

        article = article_by_id.get(aid)
        if article is None:
            errors.append(f"{rid}: source article not found: {aid}")
            continue
        if norm(str(article.get("spanishGuideRaw", ""))) != norm(str(record.get("sourceGuideRaw", ""))):
            errors.append(f"{rid}: sourceGuideRaw disagrees with canonical article")
        if "lo mismo" not in norm(str(article.get("transcriptionRaw", ""))):
            errors.append(f"{rid}: canonical article no longer contains Lo miſmo formula")

    candidate_ids = {row["articleId"] for row in candidates}
    if source_ids != candidate_ids:
        errors.append(
            "Lo miſmo review coverage mismatch: "
            f"missing={sorted(candidate_ids-source_ids)} extra={sorted(source_ids-candidate_ids)}"
        )
    if len(reviews) != len(candidate_ids):
        errors.append(f"review count {len(reviews)} != candidate count {len(candidate_ids)}")

    # The formula review layer replaces the earlier exceptional treatment of
    # `Lo miſmo` as a canonical cross-reference. No canonical cross-reference
    # marker may now use this formula.
    lo_mismo_crossrefs = []
    for article in articles:
        for ref in article.get("crossReferences") or []:
            if norm(str(ref.get("markerRaw", ""))) == "lo mismo":
                lo_mismo_crossrefs.append(article["articleId"])
    if lo_mismo_crossrefs:
        errors.append(f"canonical Lo miſmo cross-references remain: {lo_mismo_crossrefs}")

    if errors:
        raise SystemExit("\n".join(errors))

    decisions = Counter(record["decisionStatus"] for record in reviews)
    interpretations = Counter(record["interpretationStatus"] for record in reviews)
    print(
        "Lo miſmo source-review QA OK: "
        f"{len(reviews)} records across {len(paths)} file(s); "
        f"decisions={dict(sorted(decisions.items()))}; "
        f"interpretations={dict(sorted(interpretations.items()))}; "
        f"canonicalLoMismoCrossReferences=0; humanVerified=0"
    )


if __name__ == "__main__":
    main()

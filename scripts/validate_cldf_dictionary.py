#!/usr/bin/env python3
"""Validate CHD's generated CLDF Dictionary projection against canonical JSONL."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTICLES_DIR = ROOT / "data" / "lexicon" / "articles"
DEFAULT_CLDF_DIR = ROOT / "build" / "cldf"
LANGUAGE_ID = "cahita-historical-source"


def load_articles() -> list[dict]:
    rows: list[dict] = []
    ids: set[str] = set()
    for path in sorted(ARTICLES_DIR.glob("*.jsonl")):
        with path.open("r", encoding="utf-8") as handle:
            for line_number, raw in enumerate(handle, start=1):
                if not raw.strip():
                    continue
                obj = json.loads(raw)
                article_id = obj.get("articleId")
                if article_id in ids:
                    raise SystemExit(
                        f"canonical duplicate articleId while validating CLDF: {article_id} "
                        f"({path.relative_to(ROOT)}:{line_number})"
                    )
                ids.add(article_id)
                rows.append(obj)
    rows.sort(key=lambda item: item["articleId"])
    if not rows:
        raise SystemExit("canonical article corpus is empty")
    return rows


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        raise SystemExit(f"missing CLDF table: {path}")
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def expected_projection(articles: list[dict]) -> tuple[dict[str, dict], dict[str, dict], int, int]:
    entries: dict[str, dict] = {}
    senses: dict[str, dict] = {}
    with_forms = 0
    without_forms = 0

    for article in articles:
        forms = article.get("cahitaFormsRaw") or []
        if not forms:
            without_forms += 1
            continue
        with_forms += 1
        description = article.get("spanishGuideRaw") or article.get("transcriptionRaw")
        for index, form in enumerate(forms, start=1):
            entry_id = f"{article['articleId']}-f{index:02d}"
            sense_id = f"{entry_id}-s01"
            entries[entry_id] = {
                "Language_ID": LANGUAGE_ID,
                "Headword": form["formRaw"],
                "Article_ID": article["articleId"],
                "Form_Index": str(index),
                "Historical_Variety_Label": form.get("historicalVariety") or "unspecified",
                "Source_Qualifier_Raw": form.get("sourceQualifierRaw") or "",
                "Source_Page_Digital": str(article.get("sourcePageDigital") or ""),
                "Source_Column": article.get("column") or "",
                "Article_Type": article.get("articleType") or "",
                "Review_Status": article.get("reviewStatus") or "",
                "Human_Verified": article.get("humanVerified") is True,
                "Transcription_Raw": article.get("transcriptionRaw") or "",
            }
            senses[sense_id] = {
                "Description": description,
                "Entry_ID": entry_id,
                "Article_ID": article["articleId"],
                "Source_Grouping_Raw": article.get("sourceGroupingRaw") or "",
            }
    return entries, senses, with_forms, without_forms


def parse_boolean(value: str, field: str) -> bool:
    normalized = value.strip().lower()
    if normalized in {"true", "1"}:
        return True
    if normalized in {"false", "0"}:
        return False
    raise SystemExit(f"invalid boolean in {field}: {value!r}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--cldf-dir",
        type=Path,
        default=DEFAULT_CLDF_DIR,
        help="Generated CLDF directory.",
    )
    args = parser.parse_args()
    cldf_dir = args.cldf_dir if args.cldf_dir.is_absolute() else ROOT / args.cldf_dir

    metadata_path = cldf_dir / "Dictionary-metadata.json"
    if not metadata_path.is_file():
        raise SystemExit(f"missing CLDF metadata: {metadata_path}")
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    if metadata.get("dc:conformsTo") != "http://cldf.clld.org/v1.0/terms.rdf#Dictionary":
        raise SystemExit("generated metadata is not a CLDF Dictionary module")

    articles = load_articles()
    expected_entries, expected_senses, with_forms, without_forms = expected_projection(articles)
    actual_entries = read_csv(cldf_dir / "entries.csv")
    actual_senses = read_csv(cldf_dir / "senses.csv")
    languages = read_csv(cldf_dir / "languages.csv")

    if len(languages) != 1:
        raise SystemExit(f"expected exactly one documentary LanguageTable row, got {len(languages)}")
    language = languages[0]
    if language.get("ID") != LANGUAGE_ID:
        raise SystemExit("unexpected CLDF Language_ID; modern identity inference is not allowed")
    if language.get("Glottocode", "").strip() or language.get("ISO639P3code", "").strip():
        raise SystemExit("Glottocode/ISO639P3code must remain empty for the historical source label")

    actual_entry_ids = [row.get("ID", "") for row in actual_entries]
    if len(actual_entry_ids) != len(set(actual_entry_ids)):
        raise SystemExit("duplicate CLDF EntryTable IDs")
    if set(actual_entry_ids) != set(expected_entries):
        missing = sorted(set(expected_entries) - set(actual_entry_ids))[:10]
        extra = sorted(set(actual_entry_ids) - set(expected_entries))[:10]
        raise SystemExit(f"CLDF entry identity drift: missing={missing}; extra={extra}")

    for row in actual_entries:
        entry_id = row["ID"]
        expected = expected_entries[entry_id]
        for field in (
            "Language_ID",
            "Headword",
            "Article_ID",
            "Form_Index",
            "Historical_Variety_Label",
            "Source_Qualifier_Raw",
            "Source_Page_Digital",
            "Source_Column",
            "Article_Type",
            "Review_Status",
            "Transcription_Raw",
        ):
            if (row.get(field) or "") != expected[field]:
                raise SystemExit(
                    f"CLDF entry drift {entry_id} field {field}: "
                    f"expected={expected[field]!r} actual={(row.get(field) or '')!r}"
                )
        if parse_boolean(row.get("Human_Verified", ""), f"{entry_id}.Human_Verified") \
                != expected["Human_Verified"]:
            raise SystemExit(f"CLDF human-verification drift for {entry_id}")

    actual_sense_ids = [row.get("ID", "") for row in actual_senses]
    if len(actual_sense_ids) != len(set(actual_sense_ids)):
        raise SystemExit("duplicate CLDF SenseTable IDs")
    if set(actual_sense_ids) != set(expected_senses):
        missing = sorted(set(expected_senses) - set(actual_sense_ids))[:10]
        extra = sorted(set(actual_sense_ids) - set(expected_senses))[:10]
        raise SystemExit(f"CLDF sense identity drift: missing={missing}; extra={extra}")

    for row in actual_senses:
        sense_id = row["ID"]
        expected = expected_senses[sense_id]
        for field in ("Description", "Entry_ID", "Article_ID", "Source_Grouping_Raw"):
            if (row.get(field) or "") != (expected[field] or ""):
                raise SystemExit(
                    f"CLDF sense drift {sense_id} field {field}: "
                    f"expected={expected[field]!r} actual={(row.get(field) or '')!r}"
                )

    manifest_path = cldf_dir / "projection-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    expected_counts = {
        "articleCount": len(articles),
        "articlesWithCahitaForms": with_forms,
        "articlesWithoutCahitaForms": without_forms,
        "entryCount": len(expected_entries),
        "senseCount": len(expected_senses),
        "humanVerifiedEntryCount": sum(
            1 for item in expected_entries.values() if item["Human_Verified"]
        ),
    }
    for key, value in expected_counts.items():
        if manifest.get(key) != value:
            raise SystemExit(
                f"projection manifest count drift: {key} expected={value} actual={manifest.get(key)}"
            )

    if manifest.get("canonicalTag") != "v1.0.0" or \
            manifest.get("canonicalTagCommit") != "dbcdecf0003ac5a10ae963caf6babdcf5c22128d":
        raise SystemExit("projection manifest lost the immutable v1.0.0 provenance anchor")

    print(
        "CLDF projection QA OK: "
        f"articles={len(articles)}; entries={len(actual_entries)}; senses={len(actual_senses)}; "
        f"historicalLanguageIdentityOnly=true"
    )


if __name__ == "__main__":
    main()

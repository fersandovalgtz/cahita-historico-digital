#!/usr/bin/env python3
"""Generate a conservative CLDF Dictionary projection from CHD lexical articles.

This is a post-v1 derived representation. The canonical historical JSONL corpus
remains authoritative. The generator preserves printed Cahita forms verbatim,
uses the Spanish guide as the CLDF sense description, and deliberately avoids
assigning ISO 639-3 or Glottocode identifiers to historical source labels.
"""
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from pycldf import Dictionary, Source

ROOT = Path(__file__).resolve().parents[1]
ARTICLES_DIR = ROOT / "data" / "lexicon" / "articles"
SOURCE_METADATA = ROOT / "data" / "source" / "alc1737" / "metadata.json"
DEFAULT_OUTPUT = ROOT / "build" / "cldf"
LANGUAGE_ID = "cahita-historical-source"
PROJECTION_VERSION = "1.0.0-post-v1-cldf.1"
CANONICAL_TAG = "v1.0.0"
CANONICAL_TAG_COMMIT = "dbcdecf0003ac5a10ae963caf6babdcf5c22128d"


def load_articles() -> list[dict]:
    articles: list[dict] = []
    seen: set[str] = set()
    files = sorted(ARTICLES_DIR.glob("*.jsonl"))
    if not files:
        raise SystemExit(f"no lexical article JSONL files found in {ARTICLES_DIR}")

    for path in files:
        with path.open("r", encoding="utf-8") as handle:
            for line_number, raw in enumerate(handle, start=1):
                line = raw.strip()
                if not line:
                    continue
                try:
                    article = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise SystemExit(
                        f"invalid JSON in {path.relative_to(ROOT)}:{line_number}: {exc}"
                    ) from exc
                article_id = article.get("articleId")
                if not isinstance(article_id, str) or not article_id:
                    raise SystemExit(
                        f"missing articleId in {path.relative_to(ROOT)}:{line_number}"
                    )
                if article_id in seen:
                    raise SystemExit(f"duplicate articleId encountered during CLDF build: {article_id}")
                seen.add(article_id)
                articles.append(article)

    articles.sort(key=lambda item: item["articleId"])
    return articles


def clean_output(path: Path, force: bool) -> None:
    if path.exists():
        if any(path.iterdir()):
            if not force:
                raise SystemExit(
                    f"output directory is not empty: {path}; use --force to replace generated output"
                )
            shutil.rmtree(path)
        else:
            path.rmdir()
    path.mkdir(parents=True, exist_ok=False)


def source_reference(page: object) -> list[str]:
    if isinstance(page, int):
        return [f"ALC1737[{page}]"]
    return ["ALC1737"]


def historical_variety(form: dict) -> str:
    value = form.get("historicalVariety")
    return value if isinstance(value, str) and value else "unspecified"


def build_projection(articles: list[dict], output: Path) -> dict:
    source_meta = json.loads(SOURCE_METADATA.read_text(encoding="utf-8"))

    dataset = Dictionary.in_dir(output)
    dataset.add_component("LanguageTable")
    dataset.add_columns(
        "EntryTable",
        {
            "name": "Article_ID",
            "datatype": "string",
            "dc:description": "Canonical CHD historical article identifier.",
        },
        {
            "name": "Form_Index",
            "datatype": "integer",
            "dc:description": "1-based order of the form inside cahitaFormsRaw.",
        },
        {
            "name": "Historical_Variety_Label",
            "datatype": "string",
            "dc:description": (
                "Historical source label preserved verbatim as a documentary category; "
                "not automatically equated with a contemporary linguistic identity."
            ),
        },
        {
            "name": "Source_Qualifier_Raw",
            "datatype": "string",
            "dc:description": "Source-side qualifier preserved without modernization.",
        },
        {
            "name": "Source_Page_Digital",
            "datatype": "integer",
            "dc:description": "Digital witness page used by CHD.",
        },
        {
            "name": "Source_Column",
            "datatype": "string",
            "dc:description": "Source column recorded by CHD (left/right).",
        },
        {
            "name": "Article_Type",
            "datatype": "string",
            "dc:description": "CHD historical article type.",
        },
        {
            "name": "Review_Status",
            "datatype": "string",
            "dc:description": "CHD authority/review state; does not imply human verification.",
        },
        {
            "name": "Human_Verified",
            "datatype": "boolean",
            "dc:description": "True only when CHD explicitly records independent human verification.",
        },
        {
            "name": "Transcription_Raw",
            "datatype": "string",
            "dc:description": "Source-faithful CHD article transcription.",
        },
        {
            "name": "Source",
            "propertyUrl": "http://cldf.clld.org/v1.0/terms.rdf#source",
            "separator": ";",
        },
    )
    dataset.add_columns(
        "SenseTable",
        {
            "name": "Article_ID",
            "datatype": "string",
            "dc:description": "Canonical CHD historical article identifier.",
        },
        {
            "name": "Source_Grouping_Raw",
            "datatype": "string",
            "dc:description": "Historical grouping/section label when recorded in the source.",
        },
    )

    dataset.properties.update(
        {
            "dc:title": "Cahíta Histórico Digital — CLDF Dictionary projection",
            "dc:description": (
                "Reproducible post-v1 CLDF Dictionary projection of the historical vocabulary. "
                "Printed forms and historical variety labels are preserved as documentary data; "
                "the projection does not assign modern language identities or human verification."
            ),
            "dc:license": "https://creativecommons.org/licenses/by/4.0/",
            "dc:version": PROJECTION_VERSION,
            "dcat:accessURL": "https://github.com/fersandovalgtz/cahita-historico-digital",
        }
    )

    dataset.add_sources(
        Source(
            "book",
            "ALC1737",
            title=source_meta["title"],
            year=str(source_meta["datePublished"]),
            address=source_meta["placePublished"],
            publisher=source_meta["printer"],
            note=(
                "Anonymous on the title page; later attributions are disputed. "
                "CHD preserves the 1737 witness as the transcription authority."
            ),
        )
    )

    languages = [
        {
            "ID": LANGUAGE_ID,
            "Name": "Cahita (historical source label)",
            "Glottocode": None,
            "ISO639P3code": None,
        }
    ]
    entries: list[dict] = []
    senses: list[dict] = []
    articles_with_forms = 0
    articles_without_forms = 0
    human_verified_entries = 0

    for article in articles:
        forms = article.get("cahitaFormsRaw") or []
        if not forms:
            articles_without_forms += 1
            continue
        articles_with_forms += 1

        article_id = article["articleId"]
        description = article.get("spanishGuideRaw") or article.get("transcriptionRaw")
        if not isinstance(description, str) or not description:
            raise SystemExit(f"article {article_id} has forms but no usable CLDF sense description")

        for index, form in enumerate(forms, start=1):
            raw_form = form.get("formRaw")
            if not isinstance(raw_form, str) or not raw_form:
                raise SystemExit(f"article {article_id} form {index} has no formRaw")

            entry_id = f"{article_id}-f{index:02d}"
            sense_id = f"{entry_id}-s01"
            verified = article.get("humanVerified") is True
            if verified:
                human_verified_entries += 1

            entries.append(
                {
                    "ID": entry_id,
                    "Language_ID": LANGUAGE_ID,
                    "Headword": raw_form,
                    "Part_Of_Speech": None,
                    "Article_ID": article_id,
                    "Form_Index": index,
                    "Historical_Variety_Label": historical_variety(form),
                    "Source_Qualifier_Raw": form.get("sourceQualifierRaw"),
                    "Source_Page_Digital": article.get("sourcePageDigital"),
                    "Source_Column": article.get("column"),
                    "Article_Type": article.get("articleType"),
                    "Review_Status": article.get("reviewStatus"),
                    "Human_Verified": verified,
                    "Transcription_Raw": article.get("transcriptionRaw"),
                    "Source": source_reference(article.get("sourcePageDigital")),
                }
            )
            senses.append(
                {
                    "ID": sense_id,
                    "Description": description,
                    "Entry_ID": entry_id,
                    "Article_ID": article_id,
                    "Source_Grouping_Raw": article.get("sourceGroupingRaw"),
                }
            )

    dataset.write(EntryTable=entries, SenseTable=senses, LanguageTable=languages)

    manifest = {
        "projection": "CHD CLDF Dictionary",
        "projectionVersion": PROJECTION_VERSION,
        "cldfModule": "Dictionary",
        "canonicalDatasetVersion": "1.0.0",
        "canonicalTag": CANONICAL_TAG,
        "canonicalTagCommit": CANONICAL_TAG_COMMIT,
        "canonicalAuthority": "data/lexicon/articles/*.jsonl",
        "articleCount": len(articles),
        "articlesWithCahitaForms": articles_with_forms,
        "articlesWithoutCahitaForms": articles_without_forms,
        "entryCount": len(entries),
        "senseCount": len(senses),
        "humanVerifiedEntryCount": human_verified_entries,
        "languageIdentityPolicy": (
            "All EntryTable rows use a documentary historical Cahita Language_ID. "
            "Historical variety labels remain custom source labels; no ISO or Glottocode is inferred."
        ),
        "mappingPolicy": (
            "Each cahitaFormsRaw item becomes one EntryTable row; each generated entry receives "
            "one SenseTable row whose Description is spanishGuideRaw, falling back to transcriptionRaw."
        ),
        "excludedFromEntryTable": (
            "Historical articles without cahitaFormsRaw remain canonical CHD data but are not coerced "
            "into lexical entries in this Dictionary projection."
        ),
    }
    (output / "projection-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Output directory (default: {DEFAULT_OUTPUT.relative_to(ROOT)})",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace a non-empty output directory that contains only generated work.",
    )
    args = parser.parse_args()

    output = args.output if args.output.is_absolute() else ROOT / args.output
    clean_output(output, args.force)
    manifest = build_projection(load_articles(), output)
    print(
        "CLDF Dictionary projection generated: "
        f"articles={manifest['articleCount']}; entries={manifest['entryCount']}; "
        f"senses={manifest['senseCount']}; humanVerifiedEntries={manifest['humanVerifiedEntryCount']}"
    )
    print(f"metadata: {output / 'Dictionary-metadata.json'}")


if __name__ == "__main__":
    main()

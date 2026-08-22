#!/usr/bin/env python3
"""Export a deterministic TEI Lex-0 0.9.5 lexical view of ALC1737.

This is a conservative interoperability layer. Historical Cahita forms remain
xml:lang="und" because CHD does not infer a modern ISO language identity from
the 1737 source label. Only strict normalized-exact `Buſca` resolutions receive
@target pointers; editorial source-review edges remain outside this canonical
projection.

Schema conformance is enforced separately in CI against the archived official
TEI Lex-0 0.9.5 Relax NG schema pinned by URL and SHA-256.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

from export_lexicon_crossreference_graph import build_resolution, load_articles

ROOT = Path(__file__).resolve().parents[1]
SOURCE_METADATA = ROOT / "data/source/alc1737/metadata.json"

XML_NAME = "chd_lexicon_tei.xml"
MANIFEST_NAME = "manifest.json"
TEI_NS = "http://www.tei-c.org/ns/1.0"
XML_NS = "http://www.w3.org/XML/1998/namespace"
LEX0_VERSION = "0.9.5"
LEX0_SCHEMA_URL = "https://lex-0.org/releases/v0.9.5/schema/lex-0.rng"
LEX0_SCHEMA_SHA256 = "35e73fef48526634714bdf3d16b924f958fca078a903d0bdc2dd4d7d116d1aaa"

ET.register_namespace("", TEI_NS)


def q(local: str) -> str:
    return f"{{{TEI_NS}}}{local}"


def xml_attr(local: str) -> str:
    return f"{{{XML_NS}}}{local}"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def text_element(parent: ET.Element, tag: str, text: str | None, **attrs: str) -> ET.Element:
    element = ET.SubElement(parent, q(tag), attrs)
    if text is not None:
        element.text = str(text)
    return element


def strict_target_map() -> dict[tuple[str, int], str]:
    rows, _graph, _count, _files = build_resolution()
    result: dict[tuple[str, int], str] = {}
    for row in rows:
        target = row.get("exactUniqueTargetArticleId")
        if row.get("resolutionStatus") == "exact_unique" and isinstance(target, str):
            result[(row["sourceArticleId"], int(row["crossReferenceIndex"]))] = target
    return result


def build_header(root: ET.Element, metadata: dict[str, Any], article_count: int) -> None:
    header = ET.SubElement(root, q("teiHeader"))
    file_desc = ET.SubElement(header, q("fileDesc"))

    title_stmt = ET.SubElement(file_desc, q("titleStmt"))
    text_element(title_stmt, "title", "Cahíta Histórico Digital: vocabulario histórico ALC1737 — vista TEI")
    resp_stmt = ET.SubElement(title_stmt, q("respStmt"))
    text_element(resp_stmt, "resp", "Estructuración histórico-digital y exportación derivada")
    text_element(resp_stmt, "name", "Cahíta Histórico Digital")

    publication_stmt = ET.SubElement(file_desc, q("publicationStmt"))
    text_element(publication_stmt, "publisher", "Cahíta Histórico Digital")
    availability = ET.SubElement(publication_stmt, q("availability"))
    licence = ET.SubElement(
        availability,
        q("licence"),
        {"target": "https://creativecommons.org/licenses/by/4.0/"},
    )
    licence.text = "Structured data, metadata, annotations and original editorial layers: CC BY 4.0; historical source reproductions are not relicensed by CHD."

    source_desc = ET.SubElement(file_desc, q("sourceDesc"))
    list_bibl = ET.SubElement(source_desc, q("listBibl"), {"type": "dictionaries"})
    bibl = ET.SubElement(list_bibl, q("biblStruct"), {xml_attr("id"): metadata["id"]})
    monogr = ET.SubElement(bibl, q("monogr"))
    text_element(monogr, "title", metadata["title"], level="m")
    text_element(monogr, "idno", metadata["digitalWitness"]["identifier"], type="InternetArchive")
    imprint = ET.SubElement(monogr, q("imprint"))
    text_element(imprint, "pubPlace", metadata["placePublished"])
    text_element(imprint, "publisher", metadata["printer"])
    text_element(imprint, "date", metadata["datePublished"], when=metadata["datePublished"])

    encoding_desc = ET.SubElement(header, q("encodingDesc"))
    project_desc = ET.SubElement(encoding_desc, q("projectDesc"))
    text_element(
        project_desc,
        "p",
        f"Derived TEI lexical view generated deterministically from {article_count} canonical CHD historical article objects. The projection preserves source spellings and CHD authority boundaries.",
    )
    editorial_decl = ET.SubElement(encoding_desc, q("editorialDecl"))
    text_element(
        editorial_decl,
        "p",
        "Historical labels and forms are preserved as source data. Strict Buſca targets use normalized exact equality only. Editorial review edges, fuzzy matches, modern language identity, borrowing and semantic equivalence are not inferred in this projection.",
    )

    profile_desc = ET.SubElement(header, q("profileDesc"))
    lang_usage = ET.SubElement(profile_desc, q("langUsage"))
    text_element(
        lang_usage,
        "language",
        "Spanish as the historical guide and project working language",
        ident="es",
        role="workingLanguage",
    )
    text_element(
        lang_usage,
        "language",
        "Historical language labelled Cahita in the 1737 source; no modern ISO identity asserted by this export",
        ident="und",
        role="targetLanguage",
    )

    revision_desc = ET.SubElement(header, q("revisionDesc"))
    text_element(
        revision_desc,
        "change",
        "Deterministic CHD lexical projection aligned to TEI Lex-0 0.9.5; external archived-schema validation is enforced by CHD QA.",
        when="2026-08-21",
    )


def add_article(
    parent: ET.Element,
    article: dict[str, Any],
    targets: dict[tuple[str, int], str],
) -> tuple[int, int, int]:
    article_id = article["articleId"]
    guide = article.get("spanishGuideRaw")
    if not isinstance(guide, str) or not guide.strip():
        raise SystemExit(f"TEI export requires a non-empty spanishGuideRaw: {article_id}")

    entry = ET.SubElement(
        parent,
        q("entry"),
        {
            xml_attr("id"): article_id,
            xml_attr("lang"): "es",
            "type": "mainEntry",
        },
    )
    form = ET.SubElement(entry, q("form"), {"type": "lemma"})
    text_element(form, "orth", guide)

    sense = ET.SubElement(entry, q("sense"), {xml_attr("id"): f"{article_id}-sense-1"})

    form_count = 0
    for form_obj in article.get("cahitaFormsRaw") or []:
        raw = form_obj.get("formRaw")
        if not isinstance(raw, str) or not raw.strip():
            continue
        cit = ET.SubElement(sense, q("cit"), {"type": "translation"})
        quote = text_element(cit, "quote", raw)
        quote.set(xml_attr("lang"), "und")
        qualifier = form_obj.get("sourceQualifierRaw")
        if isinstance(qualifier, str) and qualifier.strip():
            text_element(cit, "lbl", qualifier)
        variety = form_obj.get("historicalVariety")
        if isinstance(variety, str) and variety not in {"", "unspecified"}:
            text_element(cit, "note", variety, type="historicalVarietyLabel")
        form_count += 1

    reference_count = 0
    targeted_count = 0
    for ref_index, ref_obj in enumerate(article.get("crossReferences") or []):
        marker = ref_obj.get("markerRaw")
        target_raw = ref_obj.get("targetRaw")
        if not isinstance(marker, str) or not isinstance(target_raw, str):
            continue
        xr = ET.SubElement(sense, q("xr"), {"type": "related"})
        text_element(xr, "lbl", marker)
        ref = ET.SubElement(xr, q("ref"), {"type": "entry"})
        ref.text = target_raw
        strict_target = targets.get((article_id, ref_index))
        if strict_target is not None:
            ref.set("target", f"#{strict_target}")
            targeted_count += 1
        reference_count += 1

    location_bits = [f"digital-page-{article.get('sourcePageDigital')}"]
    if article.get("column"):
        location_bits.append(f"column-{article['column']}")
    text_element(sense, "note", "; ".join(location_bits), type="sourceLocation")

    transcription = article.get("transcriptionRaw")
    if isinstance(transcription, str) and transcription.strip():
        text_element(sense, "note", transcription, type="sourceTranscription")

    review_status = article.get("reviewStatus")
    if isinstance(review_status, str):
        text_element(sense, "note", review_status, type="chdReviewStatus")

    return form_count, reference_count, targeted_count


def build_tree() -> tuple[ET.ElementTree, dict[str, Any]]:
    metadata = json.loads(SOURCE_METADATA.read_text(encoding="utf-8"))
    articles, source_files = load_articles()
    targets = strict_target_map()

    root = ET.Element(
        q("TEI"),
        {
            "type": "lex-0",
            xml_attr("lang"): "es",
        },
    )
    build_header(root, metadata, len(articles))
    text = ET.SubElement(root, q("text"))
    body = ET.SubElement(text, q("body"))
    dictionary = ET.SubElement(body, q("div"), {"type": "dictionary"})

    translation_count = 0
    crossref_count = 0
    targeted_crossref_count = 0
    for article in articles:
        forms, refs, targeted = add_article(dictionary, article, targets)
        translation_count += forms
        crossref_count += refs
        targeted_crossref_count += targeted

    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")
    stats = {
        "articleCount": len(articles),
        "translationCitationCount": translation_count,
        "crossReferenceCount": crossref_count,
        "strictTargetedCrossReferenceCount": targeted_crossref_count,
        "canonicalInputFileCount": len(source_files),
        "canonicalInputs": source_files,
    }
    return tree, stats


def serialize(tree: ET.ElementTree) -> bytes:
    return ET.tostring(tree.getroot(), encoding="utf-8", xml_declaration=True, short_empty_elements=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=ROOT / "build/lexicon-tei",
        help="Directory for the derived TEI lexical view.",
    )
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    tree, stats = build_tree()
    xml_bytes = serialize(tree)
    xml_path = args.out_dir / XML_NAME
    xml_path.write_bytes(xml_bytes)

    ET.fromstring(xml_bytes)

    manifest = {
        "sourceId": "ALC1737",
        "dataset": "historical_lexicon_tei_projection",
        "profileStatus": "tei_lex0_0_9_5_projection_with_external_ci_gate",
        "teiNamespace": TEI_NS,
        "teiLex0AlignmentTarget": LEX0_VERSION,
        "teiLex0ConformanceClaimed": True,
        "externalLex0SchemaValidationEnforcedInCI": True,
        "externalLex0SchemaValidationPerformedByExporter": False,
        "externalLex0SchemaUrl": LEX0_SCHEMA_URL,
        "externalLex0SchemaSha256": LEX0_SCHEMA_SHA256,
        "historicalTargetLanguageXmlLang": "und",
        "modernLanguageIdentityInferred": False,
        "editorialCrossReferenceEdgesIncluded": False,
        "strictExactTargetsIncluded": True,
        "fuzzyCrossReferenceTargetsIncluded": False,
        "semanticEquivalenceInferred": False,
        "borrowingInferred": False,
        "sourceTranscriptionPreserved": True,
        "deterministic": True,
        **stats,
        "formats": {
            XML_NAME: {
                "bytes": len(xml_bytes),
                "sha256": sha256_bytes(xml_bytes),
            }
        },
    }
    (args.out_dir / MANIFEST_NAME).write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )

    print(
        "exported TEI Lex-0 0.9.5 lexical projection: "
        f"{stats['articleCount']} entries; {stats['translationCitationCount']} translation citations; "
        f"{stats['crossReferenceCount']} source cross-references; "
        f"{stats['strictTargetedCrossReferenceCount']} strict @target pointers"
    )
    print(f"  {XML_NAME}: {len(xml_bytes)} bytes; sha256 {sha256_bytes(xml_bytes)}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Validate the public/reuse-facing scientific surface of CHD.

This gate complements corpus QA. It prevents documentation, machine-readable
metadata and the stable-release description from drifting away from canonical
v1 facts. It intentionally does not claim human philological verification.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "README.en.md",
    "CITATION.cff",
    "codemeta.json",
    "project-metadata.json",
    "metadata/fair-dataset.jsonld",
    "DATASHEET.md",
    "QUALITY_REPORT.md",
    "FAIR_ASSESSMENT.md",
    "GOVERNANCE.md",
    "CONTRIBUTORS.md",
    "CONTRIBUTING.md",
    "SCHEMA.md",
    "SCIENTIFIC_REPOSITORY_STANDARD.md",
    "SOURCES.md",
    "PROVENANCE.md",
    "DATA_LICENSE.md",
    "docs/DATA_PRODUCTS.md",
    "docs/ECOSYSTEM.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/CODEOWNERS",
    ".github/ISSUE_TEMPLATE/textual-correction.md",
    ".github/ISSUE_TEMPLATE/data-or-software-bug.md",
    ".github/ISSUE_TEMPLATE/research-or-interoperability.md",
    "scripts/query_lexicon.py",
]

EXPECTED = {
    "version": "1.0.0",
    "tag": "v1.0.0",
    "release_commit": "dbcdecf0003ac5a10ae963caf6babdcf5c22128d",
    "zip_sha256": "583183eabb90080dccd1ea63a069e248b28cd3ce41e99ba754ac71ce26586158",
    "articles": 2302,
    "candidate_count": 2072,
    "grammar_objects": 302,
    "grammar_evidence": 1215,
    "busca": 150,
    "open_recollations": 22,
    "human_verified": 0,
}


def load_json(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def require_text(rel: str, fragments: list[str]) -> None:
    text = (ROOT / rel).read_text(encoding="utf-8")
    for fragment in fragments:
        if fragment not in text:
            raise SystemExit(f"{rel}: required fragment missing: {fragment!r}")


def count_canonical_articles() -> tuple[int, int, int]:
    article_dir = ROOT / "data/lexicon/articles"
    files = sorted(article_dir.glob("*.jsonl"))
    total = 0
    human = 0
    for path in files:
        for raw in path.read_text(encoding="utf-8").splitlines():
            if not raw.strip():
                continue
            row = json.loads(raw)
            total += 1
            human += int(bool(row.get("humanVerified")))
    return len(files), total, human


def main() -> None:
    missing = [rel for rel in REQUIRED_FILES if not (ROOT / rel).exists()]
    if missing:
        raise SystemExit(f"public repository surface is incomplete: missing {missing}")

    metadata = load_json("project-metadata.json")
    if metadata["dataset_version"] != EXPECTED["version"]:
        raise SystemExit("project-metadata dataset_version drift")
    release = metadata["release"]
    if release["tag"] != EXPECTED["tag"] or release["commit"] != EXPECTED["release_commit"]:
        raise SystemExit("project-metadata release identity drift")
    if release["zip_sha256"] != EXPECTED["zip_sha256"]:
        raise SystemExit("project-metadata release ZIP digest drift")

    metrics = metadata["metrics"]
    checks = {
        "canonical_candidates": EXPECTED["candidate_count"],
        "historical_lexical_articles": EXPECTED["articles"],
        "grammar_objects": EXPECTED["grammar_objects"],
        "grammar_evidence_rows": EXPECTED["grammar_evidence"],
        "busca_crossreferences": EXPECTED["busca"],
        "open_recollation_uncertainties": EXPECTED["open_recollations"],
        "human_verified_count": EXPECTED["human_verified"],
    }
    for key, expected in checks.items():
        if metrics.get(key) != expected:
            raise SystemExit(f"project-metadata metric drift: {key}={metrics.get(key)!r}, expected {expected!r}")

    if metadata["language_object"].get("iso_639_3") is not None:
        raise SystemExit("historical Cahita must not be assigned a single ISO 639-3 code by this metadata layer")
    if metadata["persistent_identifiers"].get("doi") is not None:
        raise SystemExit("DOI must remain null until archival deposit is actually assigned")

    fair = load_json("metadata/fair-dataset.jsonld")
    if fair.get("version") != EXPECTED["version"]:
        raise SystemExit("FAIR JSON-LD version drift")
    if fair.get("license") != "https://creativecommons.org/licenses/by/4.0/":
        raise SystemExit("FAIR JSON-LD data license drift")

    contract_manifest = load_json("release/v1_contract_manifest.json")
    if contract_manifest.get("schemaContractCount") != 22 or contract_manifest.get("contractCount") != 26:
        raise SystemExit("v1 contract count drift")

    article_files, article_count, human_count = count_canonical_articles()
    if article_files != 211 or article_count != EXPECTED["articles"] or human_count != 0:
        raise SystemExit(
            "canonical lexical corpus drift: "
            f"files={article_files}, articles={article_count}, humanVerified={human_count}"
        )

    require_text(
        "README.md",
        [
            "v1.0.0",
            "2,302",
            "TEI Lex-0 0.9.5",
            "humanVerified=0",
            "583183eabb90080dccd1ea63a069e248b28cd3ce41e99ba754ac71ce26586158",
        ],
    )
    require_text(
        "README.en.md",
        ["v1.0.0", "2,302", "humanVerified=0", "DOI"],
    )
    require_text("GOVERNANCE.md", ["No equivalencia automática", "CARE"])
    require_text("CONTRIBUTORS.md", ["CRediT", "Fernando Sandoval Gutierrez"])
    require_text("FAIR_ASSESSMENT.md", ["No constituye certificación FAIR", "DOI"])

    print(
        "repository surface QA OK: "
        "requiredFiles=%d; articles=%d; articleFiles=%d; humanVerified=0; "
        "version=1.0.0; DOI=pending; historicalISO6393=null"
        % (len(REQUIRED_FILES), article_count, article_files)
    )


if __name__ == "__main__":
    main()

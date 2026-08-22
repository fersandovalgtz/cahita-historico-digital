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
    "SECURITY.md",
    "SOURCES.md",
    "PROVENANCE.md",
    "LICENSE",
    "DATA_LICENSE.md",
    "LICENSING.md",
    "references.bib",
    "docs/README.md",
    "docs/DATA_PRODUCTS.md",
    "docs/REPRODUCIBILITY.md",
    "docs/ECOSYSTEM.md",
    "docs/PRESERVATION.md",
    "docs/RELEASE_PUBLICATION_2026-08-22.md",
    "release/archival_deposit_v1.0.0.json",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/CODEOWNERS",
    ".github/ISSUE_TEMPLATE/textual-correction.md",
    ".github/ISSUE_TEMPLATE/data-or-software-bug.md",
    ".github/ISSUE_TEMPLATE/research-or-interoperability.md",
    "scripts/query_lexicon.py",
    "scripts/validate_repository_surface.py",
    "scripts/validate_documentation_links.py",
    "scripts/validate_published_v1.py",
    "scripts/validate_persistent_identifiers.py",
    "Makefile",
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
    "persistent_status": "archived with DOI",
    "version_doi": "10.5281/zenodo.22061986",
    "concept_doi": "10.5281/zenodo.22061985",
    "record_url": "https://zenodo.org/records/22061986",
    "provider": "Zenodo",
    "deposited_at": "2026-08-22",
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

    persistent = metadata.get("persistent_identifiers", {})
    persistent_expected = {
        "status": EXPECTED["persistent_status"],
        "doi": EXPECTED["version_doi"],
        "concept_doi": EXPECTED["concept_doi"],
        "provider": EXPECTED["provider"],
        "record_url": EXPECTED["record_url"],
        "deposited_at": EXPECTED["deposited_at"],
    }
    for key, expected in persistent_expected.items():
        if persistent.get(key) != expected:
            raise SystemExit(
                f"project-metadata persistent identifier drift: {key}={persistent.get(key)!r}, expected {expected!r}"
            )

    fair = load_json("metadata/fair-dataset.jsonld")
    if fair.get("version") != EXPECTED["version"]:
        raise SystemExit("FAIR JSON-LD version drift")
    if fair.get("license") != "https://creativecommons.org/licenses/by/4.0/":
        raise SystemExit("FAIR JSON-LD data license drift")
    expected_doi_url = f"https://doi.org/{EXPECTED['version_doi']}"
    if fair.get("@id") != expected_doi_url or fair.get("identifier") != expected_doi_url:
        raise SystemExit("FAIR JSON-LD persistent identifier drift")

    attestation = load_json("release/github_release_attestation_v1.0.0.json")
    if attestation.get("tagCommit") != EXPECTED["release_commit"]:
        raise SystemExit("durable release attestation commit drift")
    if (attestation.get("releaseZip") or {}).get("sha256") != EXPECTED["zip_sha256"]:
        raise SystemExit("durable release attestation ZIP digest drift")
    if attestation.get("verificationMode") != "deterministic_rebuild_from_immutable_tag":
        raise SystemExit("durable release attestation verification mode drift")

    archival = load_json("release/archival_deposit_v1.0.0.json")
    archived_release = archival.get("publishedRelease", {})
    if archived_release.get("tag") != EXPECTED["tag"]:
        raise SystemExit("archival attestation tag drift")
    if archived_release.get("tagCommit") != EXPECTED["release_commit"]:
        raise SystemExit("archival attestation commit drift")
    if archived_release.get("zipSha256") != EXPECTED["zip_sha256"]:
        raise SystemExit("archival attestation ZIP digest drift")
    deposit = archival.get("archivalDeposit", {})
    archival_expected = {
        "provider": EXPECTED["provider"],
        "recordUrl": EXPECTED["record_url"],
        "versionDoi": EXPECTED["version_doi"],
        "conceptDoi": EXPECTED["concept_doi"],
        "depositedAt": EXPECTED["deposited_at"],
    }
    for key, expected in archival_expected.items():
        if deposit.get(key) != expected:
            raise SystemExit(f"archival attestation drift: {key}={deposit.get(key)!r}, expected {expected!r}")
    policy = archival.get("policy", {})
    if policy.get("doiInferred") is not False or policy.get("tagModified") is not False:
        raise SystemExit("archival attestation must preserve doiInferred=false and tagModified=false")

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
            EXPECTED["zip_sha256"],
            EXPECTED["version_doi"],
            EXPECTED["concept_doi"],
        ],
    )
    require_text(
        "README.en.md",
        ["v1.0.0", "2,302", "humanVerified=0", EXPECTED["version_doi"], EXPECTED["concept_doi"]],
    )
    require_text("DATASHEET.md", ["2,302", "267 archivos científicos", EXPECTED["zip_sha256"], "DOI"])
    require_text("QUALITY_REPORT.md", ["371/371", "TEI Lex-0 0.9.5", EXPECTED["zip_sha256"], "humanVerified=0"])
    require_text("GOVERNANCE.md", ["No equivalencia automática", "CARE"])
    require_text("CONTRIBUTORS.md", ["CRediT", "Fernando Sandoval Gutierrez"])
    require_text("FAIR_ASSESSMENT.md", ["No constituye certificación FAIR", EXPECTED["version_doi"]])
    require_text("docs/PRESERVATION.md", [EXPECTED["version_doi"], EXPECTED["concept_doi"], EXPECTED["record_url"]])
    require_text("CITATION.cff", [f'doi: "{EXPECTED["version_doi"]}"'])
    require_text("SCHEMA.md", ["26 contratos", "TEI Lex-0 0.9.5"])
    require_text("SECURITY.md", ["integridad científica", "v1.0.0"])
    require_text("LICENSING.md", ["MIT", "CC BY 4.0", "No relicenciados"])
    require_text("docs/DATA_PRODUCTS.md", [EXPECTED["zip_sha256"], "query_lexicon.py"])
    require_text(
        "docs/REPRODUCIBILITY.md",
        [EXPECTED["release_commit"], EXPECTED["zip_sha256"], "make qa-full", "validate_published_v1.py"],
    )
    require_text("scripts/build_v1_release.py", [EXPECTED["release_commit"], "pinned to the immutable published v1.0.0"])

    print(
        "repository surface QA OK: "
        "requiredFiles=%d; articles=%d; articleFiles=%d; humanVerified=0; "
        "version=1.0.0; DOI=%s; conceptDOI=%s; historicalISO6393=null; publishedV1=immutable_tag_rebuild"
        % (
            len(REQUIRED_FILES),
            article_count,
            article_files,
            EXPECTED["version_doi"],
            EXPECTED["concept_doi"],
        )
    )


if __name__ == "__main__":
    main()

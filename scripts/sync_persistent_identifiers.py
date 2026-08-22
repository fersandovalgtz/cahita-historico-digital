#!/usr/bin/env python3
"""Synchronize real archival identifiers across CHD post-release metadata.

The script never creates, reserves, guesses or queries a DOI. It only accepts
identifiers already assigned by an archival repository and refuses to rewrite
a different DOI once an archived state has been recorded.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

from validate_persistent_identifiers import (
    ARCHIVAL_ATTESTATION,
    ARCHIVED_STATUS,
    CITATION,
    CODEMETA,
    FAIR_DATASET,
    PENDING_STATUS,
    PROJECT_METADATA,
    RELEASE_URL,
    ROOT,
    TAG,
    TAG_COMMIT,
    VERSION,
    ZIP_NAME,
    ZIP_SHA256,
    doi_url,
    normalize_doi,
    require_iso_date,
    require_https_url,
)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def upsert_property(dataset: dict, name: str, value: object) -> None:
    properties = dataset.setdefault("additionalProperty", [])
    for item in properties:
        if isinstance(item, dict) and item.get("name") == name:
            item["value"] = value
            return
    properties.append({"@type": "PropertyValue", "name": name, "value": value})


def update_citation(text: str, version_doi: str) -> str:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("doi:"):
            lines[index] = f'doi: "{version_doi}"'
            return "\n".join(lines) + "\n"

    insert_after = None
    for index, line in enumerate(lines):
        if line.startswith("date-released:"):
            insert_after = index
            break
    if insert_after is None:
        raise SystemExit("CITATION.cff has no date-released field; refusing implicit structural rewrite")
    lines.insert(insert_after + 1, f'doi: "{version_doi}"')
    return "\n".join(lines) + "\n"


def same_archival_identity(persistent: dict, version_doi: str, concept_doi: str | None) -> bool:
    try:
        existing_version = normalize_doi(persistent.get("doi"))
        existing_concept = normalize_doi(persistent.get("concept_doi")) if persistent.get("concept_doi") else None
    except SystemExit:
        return False
    return existing_version == version_doi and existing_concept == concept_doi


def build_attestation(
    *,
    provider: str,
    record_url: str,
    version_doi: str,
    concept_doi: str | None,
    deposited_at: str,
) -> dict:
    return {
        "attestationType": "CHD archival deposit and persistent identifier record",
        "project": "Cahíta Histórico Digital",
        "publishedRelease": {
            "version": VERSION,
            "tag": TAG,
            "tagCommit": TAG_COMMIT,
            "releaseUrl": RELEASE_URL,
            "zipName": ZIP_NAME,
            "zipSha256": ZIP_SHA256,
        },
        "archivalDeposit": {
            "provider": provider,
            "recordUrl": record_url,
            "versionDoi": version_doi,
            "conceptDoi": concept_doi,
            "depositedAt": deposited_at,
        },
        "policy": {
            "doiInferred": False,
            "doiMustBeAssignedExternally": True,
            "tagModified": False,
            "publishedReleaseRewritten": False,
            "postReleaseMetadataSynchronization": True,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Synchronize externally assigned DOI metadata without altering v1.0.0."
    )
    parser.add_argument("--version-doi", required=True, help="Real DOI assigned to v1.0.0")
    parser.add_argument("--concept-doi", help="Real concept DOI, if the archive provides one")
    parser.add_argument("--record-url", required=True, help="Published archival record HTTPS URL")
    parser.add_argument("--deposited-at", required=True, help="Archive publication/deposit date YYYY-MM-DD")
    parser.add_argument("--provider", required=True, help="Archival provider, e.g. Zenodo")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write changes. Without this flag the command performs a dry-run validation only.",
    )
    args = parser.parse_args()

    version_doi = normalize_doi(args.version_doi)
    if version_doi is None:
        raise SystemExit("--version-doi cannot be null")
    concept_doi = normalize_doi(args.concept_doi) if args.concept_doi else None
    record_url = require_https_url(args.record_url, "--record-url")
    deposited_at = require_iso_date(args.deposited_at, "--deposited-at")
    provider = args.provider.strip()
    if not provider:
        raise SystemExit("--provider cannot be empty")

    parsed = urlparse(record_url)
    if parsed.hostname in {"doi.org", "dx.doi.org"}:
        raise SystemExit("--record-url must be the archival record URL, not merely a DOI resolver URL")

    project = load_json(PROJECT_METADATA)
    persistent = project.setdefault("persistent_identifiers", {})
    current_status = persistent.get("status")
    if current_status not in {PENDING_STATUS, ARCHIVED_STATUS}:
        raise SystemExit(f"unsupported current persistent identifier status: {current_status!r}")
    if current_status == ARCHIVED_STATUS and not same_archival_identity(persistent, version_doi, concept_doi):
        raise SystemExit(
            "an archived DOI is already recorded and differs from the supplied identifier; "
            "refusing to rewrite persistent identity automatically"
        )

    print("validated externally supplied archival identity")
    print(f"  version DOI: {version_doi}")
    print(f"  concept DOI: {concept_doi or '(not supplied)'}")
    print(f"  provider: {provider}")
    print(f"  record URL: {record_url}")
    print(f"  deposited at: {deposited_at}")
    print(f"  immutable tag: {TAG} -> {TAG_COMMIT}")

    if not args.apply:
        print("dry run only: no files changed; re-run with --apply after verifying the archive record")
        return

    persistent.update(
        {
            "doi": version_doi,
            "concept_doi": concept_doi,
            "status": ARCHIVED_STATUS,
            "provider": provider,
            "record_url": record_url,
            "deposited_at": deposited_at,
        }
    )
    write_json(PROJECT_METADATA, project)

    codemeta = load_json(CODEMETA)
    codemeta["identifier"] = doi_url(version_doi)
    links = codemeta.setdefault("relatedLink", [])
    if record_url not in links:
        links.append(record_url)
    write_json(CODEMETA, codemeta)

    dataset = load_json(FAIR_DATASET)
    dataset["@id"] = doi_url(version_doi)
    dataset["identifier"] = doi_url(version_doi)
    upsert_property(dataset, "doiStatus", "assigned")
    upsert_property(dataset, "versionDoi", version_doi)
    upsert_property(dataset, "conceptDoi", concept_doi)
    upsert_property(dataset, "archivalRecord", record_url)
    write_json(FAIR_DATASET, dataset)

    citation_text = CITATION.read_text(encoding="utf-8")
    CITATION.write_text(update_citation(citation_text, version_doi), encoding="utf-8")

    write_json(
        ARCHIVAL_ATTESTATION,
        build_attestation(
            provider=provider,
            record_url=record_url,
            version_doi=version_doi,
            concept_doi=concept_doi,
            deposited_at=deposited_at,
        ),
    )

    validator = ROOT / "scripts" / "validate_persistent_identifiers.py"
    subprocess.run([sys.executable, str(validator)], cwd=ROOT, check=True)
    print("persistent identifiers synchronized; documentation/README review remains an explicit post-deposit step")


if __name__ == "__main__":
    main()

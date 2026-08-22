#!/usr/bin/env python3
"""Validate CHD post-release preservation and persistent-identifier state.

This validator deliberately lives outside the frozen v1 scientific-data and
contract manifests. It protects the immutable v1.0.0 release while allowing
real archival identifiers to be added later on ``main``.
"""
from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
PROJECT_METADATA = ROOT / "project-metadata.json"
CODEMETA = ROOT / "codemeta.json"
FAIR_DATASET = ROOT / "metadata" / "fair-dataset.jsonld"
CITATION = ROOT / "CITATION.cff"
ARCHIVAL_ATTESTATION = ROOT / "release" / "archival_deposit_v1.0.0.json"

VERSION = "1.0.0"
TAG = "v1.0.0"
TAG_COMMIT = "dbcdecf0003ac5a10ae963caf6babdcf5c22128d"
RELEASE_URL = "https://github.com/fersandovalgtz/cahita-historico-digital/releases/tag/v1.0.0"
ZIP_NAME = "cahita-historico-digital-v1.0.0.zip"
ZIP_SHA256 = "583183eabb90080dccd1ea63a069e248b28cd3ce41e99ba754ac71ce26586158"
PENDING_STATUS = "pending archival deposit"
ARCHIVED_STATUS = "archived with DOI"
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$", re.IGNORECASE)
CFF_DOI_RE = re.compile(r'^doi:\s*["\']?([^"\'\s]+)["\']?\s*$', re.MULTILINE)


def load_json(path: Path) -> dict:
    if not path.is_file():
        raise SystemExit(f"missing required metadata file: {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_doi(value: object) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str):
        raise SystemExit(f"DOI must be string or null, got {type(value).__name__}")
    doi = value.strip()
    for prefix in ("https://doi.org/", "http://doi.org/", "http://dx.doi.org/", "https://dx.doi.org/"):
        if doi.lower().startswith(prefix):
            doi = doi[len(prefix):]
            break
    if not DOI_RE.fullmatch(doi):
        raise SystemExit(f"invalid DOI syntax: {value!r}")
    return doi


def doi_url(doi: str) -> str:
    return f"https://doi.org/{doi}"


def require_https_url(value: object, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise SystemExit(f"{field} must be a non-empty HTTPS URL")
    parsed = urlparse(value.strip())
    if parsed.scheme != "https" or not parsed.netloc:
        raise SystemExit(f"{field} must be an HTTPS URL: {value!r}")
    return value.strip()


def require_iso_date(value: object, field: str) -> str:
    if not isinstance(value, str):
        raise SystemExit(f"{field} must be an ISO date")
    try:
        date.fromisoformat(value)
    except ValueError as exc:
        raise SystemExit(f"{field} must be YYYY-MM-DD: {value!r}") from exc
    return value


def additional_property(dataset: dict, name: str) -> object | None:
    for item in dataset.get("additionalProperty", []):
        if isinstance(item, dict) and item.get("name") == name:
            return item.get("value")
    return None


def validate_release_identity(project: dict) -> None:
    if project.get("dataset_version") != VERSION:
        raise SystemExit("project metadata version drifted from v1.0.0")
    release = project.get("release", {})
    expected = {
        "tag": TAG,
        "commit": TAG_COMMIT,
        "url": RELEASE_URL,
        "zip_name": ZIP_NAME,
        "zip_sha256": ZIP_SHA256,
    }
    for key, value in expected.items():
        if release.get(key) != value:
            raise SystemExit(f"published v1 identity drifted in project-metadata.json: release.{key}")


def validate_pending(project: dict, codemeta: dict, dataset: dict, citation_text: str) -> None:
    persistent = project.get("persistent_identifiers", {})
    if persistent.get("status") != PENDING_STATUS:
        raise SystemExit(f"pending DOI state must use status={PENDING_STATUS!r}")
    if persistent.get("doi") is not None or persistent.get("concept_doi") is not None:
        raise SystemExit("pending DOI state must keep doi and concept_doi null")
    forbidden_pending_fields = ("record_url", "deposited_at", "provider")
    present = [field for field in forbidden_pending_fields if persistent.get(field)]
    if present:
        raise SystemExit(f"pending DOI state must not claim archival facts: {present}")

    if CFF_DOI_RE.search(citation_text):
        raise SystemExit("CITATION.cff claims a DOI while project metadata is pending")
    identifier = codemeta.get("identifier")
    if isinstance(identifier, str) and "doi.org/10." in identifier.lower():
        raise SystemExit("codemeta.json claims a DOI while project metadata is pending")
    if dataset.get("identifier") is not None:
        raise SystemExit("FAIR dataset identifier must remain absent while DOI is pending")
    if dataset.get("@id") != RELEASE_URL:
        raise SystemExit("FAIR dataset @id must remain the immutable GitHub Release URL while DOI is pending")
    if additional_property(dataset, "doiStatus") != PENDING_STATUS:
        raise SystemExit("FAIR dataset doiStatus must match pending archival deposit")
    if ARCHIVAL_ATTESTATION.exists():
        raise SystemExit("archival attestation exists although no real DOI is registered")


def validate_archived(project: dict, codemeta: dict, dataset: dict, citation_text: str) -> None:
    persistent = project.get("persistent_identifiers", {})
    version_doi = normalize_doi(persistent.get("doi"))
    if not version_doi:
        raise SystemExit("archived state requires a version DOI")
    concept_doi = normalize_doi(persistent.get("concept_doi")) if persistent.get("concept_doi") else None
    record_url = require_https_url(persistent.get("record_url"), "persistent_identifiers.record_url")
    deposited_at = require_iso_date(persistent.get("deposited_at"), "persistent_identifiers.deposited_at")
    provider = persistent.get("provider")
    if not isinstance(provider, str) or not provider.strip():
        raise SystemExit("archived state requires persistent_identifiers.provider")

    expected_url = doi_url(version_doi)
    cff_match = CFF_DOI_RE.search(citation_text)
    if not cff_match or normalize_doi(cff_match.group(1)) != version_doi:
        raise SystemExit("CITATION.cff DOI is absent or inconsistent with project-metadata.json")
    if codemeta.get("identifier") != expected_url:
        raise SystemExit("codemeta.json identifier must equal the version DOI URL")
    if dataset.get("@id") != expected_url or dataset.get("identifier") != expected_url:
        raise SystemExit("FAIR dataset @id and identifier must equal the version DOI URL")
    if additional_property(dataset, "doiStatus") != "assigned":
        raise SystemExit("FAIR dataset doiStatus must be assigned after archival publication")
    if additional_property(dataset, "versionDoi") != version_doi:
        raise SystemExit("FAIR dataset versionDoi is inconsistent")
    if additional_property(dataset, "conceptDoi") != concept_doi:
        raise SystemExit("FAIR dataset conceptDoi is inconsistent")

    attestation = load_json(ARCHIVAL_ATTESTATION)
    expected_release = {
        "version": VERSION,
        "tag": TAG,
        "tagCommit": TAG_COMMIT,
        "releaseUrl": RELEASE_URL,
        "zipName": ZIP_NAME,
        "zipSha256": ZIP_SHA256,
    }
    for key, value in expected_release.items():
        if attestation.get("publishedRelease", {}).get(key) != value:
            raise SystemExit(f"archival attestation release identity mismatch: {key}")
    archival = attestation.get("archivalDeposit", {})
    expected_archival = {
        "provider": provider,
        "recordUrl": record_url,
        "versionDoi": version_doi,
        "conceptDoi": concept_doi,
        "depositedAt": deposited_at,
    }
    for key, value in expected_archival.items():
        if archival.get(key) != value:
            raise SystemExit(f"archival attestation mismatch: {key}")
    policy = attestation.get("policy", {})
    if policy.get("doiInferred") is not False or policy.get("tagModified") is not False:
        raise SystemExit("archival attestation must forbid inferred DOI and tag modification")


def main() -> None:
    project = load_json(PROJECT_METADATA)
    codemeta = load_json(CODEMETA)
    dataset = load_json(FAIR_DATASET)
    citation_text = CITATION.read_text(encoding="utf-8")
    validate_release_identity(project)

    persistent = project.get("persistent_identifiers", {})
    status = persistent.get("status")
    if status == PENDING_STATUS:
        validate_pending(project, codemeta, dataset, citation_text)
        print("persistent identifier QA OK: state=pending; doiInferred=false; immutableRelease=true")
    elif status == ARCHIVED_STATUS:
        validate_archived(project, codemeta, dataset, citation_text)
        print(
            "persistent identifier QA OK: "
            f"state=archived; versionDoi={persistent.get('doi')}; "
            f"conceptDoi={persistent.get('concept_doi')}; immutableRelease=true"
        )
    else:
        raise SystemExit(
            "unsupported persistent identifier state; expected "
            f"{PENDING_STATUS!r} or {ARCHIVED_STATUS!r}, got {status!r}"
        )


if __name__ == "__main__":
    main()

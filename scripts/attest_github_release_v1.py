#!/usr/bin/env python3
"""Attest the published GitHub Release for Cahíta Histórico Digital v1.0.0.

This validator consumes release metadata and locally downloaded release assets. It
never creates, edits, or moves the release/tag; it only verifies identity and writes
an auditable JSON attestation when every invariant holds.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

EXPECTED_TAG = "v1.0.0"
EXPECTED_COMMIT = "dbcdecf0003ac5a10ae963caf6babdcf5c22128d"
EXPECTED_ZIP = "cahita-historico-digital-v1.0.0.zip"
EXPECTED_ZIP_BYTES = 1_076_296
EXPECTED_ZIP_SHA256 = "45ed1f5e4f6ce101c574dec8a91ffa3c4694050cd4366d70f20c644c40043903"
EXPECTED_ASSETS = {EXPECTED_ZIP, "RELEASE_MANIFEST.json", "SHA256SUMS.txt"}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_sha256sums(path: Path) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        parts = line.split(maxsplit=1)
        if len(parts) != 2:
            raise SystemExit(f"invalid SHA256SUMS line: {raw!r}")
        digest, name = parts
        name = name.lstrip("*")
        if len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest.lower()):
            raise SystemExit(f"invalid SHA-256 digest in SHA256SUMS: {digest!r}")
        rows.append((digest.lower(), name))
    if len(rows) != 2:
        raise SystemExit(f"expected exactly 2 SHA256SUMS rows, found {len(rows)}")
    return rows


def find_sum(rows: list[tuple[str, str]], suffix: str) -> str:
    matches = [digest for digest, name in rows if name.endswith(suffix)]
    if len(matches) != 1:
        raise SystemExit(f"expected one SHA256SUMS row ending with {suffix!r}, found {len(matches)}")
    return matches[0]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--release-json", type=Path, required=True)
    parser.add_argument("--asset-dir", type=Path, required=True)
    parser.add_argument("--tag-commit", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    release = load_json(args.release_json)
    asset_dir = args.asset_dir

    if args.tag_commit != EXPECTED_COMMIT:
        raise SystemExit(f"tag commit mismatch: {args.tag_commit} != {EXPECTED_COMMIT}")
    if release.get("tagName") != EXPECTED_TAG:
        raise SystemExit(f"release tag mismatch: {release.get('tagName')!r}")
    if release.get("isDraft") is not False:
        raise SystemExit("GitHub Release must not be a draft")
    if release.get("isPrerelease") is not False:
        raise SystemExit("GitHub Release must not be a prerelease")
    if not release.get("url"):
        raise SystemExit("GitHub Release URL is missing")

    local_assets = {p.name for p in asset_dir.iterdir() if p.is_file()}
    if local_assets != EXPECTED_ASSETS:
        raise SystemExit(f"unexpected release asset set: {sorted(local_assets)}")

    api_assets = release.get("assets") or []
    api_names = {str(item.get("name")) for item in api_assets}
    if api_names != EXPECTED_ASSETS:
        raise SystemExit(f"release metadata asset set mismatch: {sorted(api_names)}")

    for item in api_assets:
        name = str(item["name"])
        local_size = (asset_dir / name).stat().st_size
        api_size = item.get("size")
        if api_size is not None and int(api_size) != local_size:
            raise SystemExit(f"asset-size mismatch for {name}: API={api_size}, local={local_size}")

    zip_path = asset_dir / EXPECTED_ZIP
    if zip_path.stat().st_size != EXPECTED_ZIP_BYTES:
        raise SystemExit(
            f"v1 ZIP size mismatch: {zip_path.stat().st_size} != {EXPECTED_ZIP_BYTES}"
        )
    zip_sha = sha256_file(zip_path)
    if zip_sha != EXPECTED_ZIP_SHA256:
        raise SystemExit(f"v1 ZIP SHA-256 mismatch: {zip_sha} != {EXPECTED_ZIP_SHA256}")

    manifest_path = asset_dir / "RELEASE_MANIFEST.json"
    manifest = load_json(manifest_path)
    manifest_sha = sha256_file(manifest_path)
    if manifest.get("version") != "1.0.0" or manifest.get("tag") != EXPECTED_TAG:
        raise SystemExit("release manifest version/tag mismatch")
    if manifest.get("sourceCommit") != EXPECTED_COMMIT:
        raise SystemExit("release manifest sourceCommit mismatch")
    if manifest.get("githubReleasePayloadReady") is not True:
        raise SystemExit("release manifest does not mark GitHub payload ready")
    if manifest.get("archivalDepositStatus") != "pending":
        raise SystemExit("archival deposit must still be pending at GitHub-release attestation")
    if manifest.get("versionDoi") is not None or manifest.get("conceptDoi") is not None:
        raise SystemExit("DOI must not be invented before archival deposit")
    if int(manifest.get("humanVerifiedCount", -1)) != 0:
        raise SystemExit("humanVerifiedCount drifted from 0")

    sums_path = asset_dir / "SHA256SUMS.txt"
    sums = parse_sha256sums(sums_path)
    sums_zip = find_sum(sums, EXPECTED_ZIP)
    sums_manifest = find_sum(sums, "RELEASE_MANIFEST.json")
    if sums_zip != zip_sha:
        raise SystemExit("SHA256SUMS ZIP digest does not match downloaded ZIP")
    if sums_manifest != manifest_sha:
        raise SystemExit("SHA256SUMS manifest digest does not match downloaded manifest")

    assets = []
    for name in sorted(EXPECTED_ASSETS):
        path = asset_dir / name
        assets.append({"name": name, "bytes": path.stat().st_size, "sha256": sha256_file(path)})

    attestation = {
        "attestationType": "github_release_integrity",
        "attestationVersion": 1,
        "project": "Cahíta Histórico Digital",
        "version": "1.0.0",
        "tag": EXPECTED_TAG,
        "tagCommit": EXPECTED_COMMIT,
        "releaseName": release.get("name"),
        "releaseUrl": release.get("url"),
        "publishedAt": release.get("publishedAt"),
        "isDraft": False,
        "isPrerelease": False,
        "assets": assets,
        "checks": {
            "tagPointsToExpectedCommit": True,
            "releaseTagMatches": True,
            "stableRelease": True,
            "exactAssetSet": True,
            "apiAssetSizesMatchDownloadedBytes": True,
            "validatedV1ZipSha256Matches": True,
            "sha256SumsConsistent": True,
            "releaseManifestIdentityMatchesTag": True,
            "doiNotInferred": True,
        },
        "archivalDepositStatus": "pending",
        "versionDoi": None,
        "conceptDoi": None,
        "humanVerifiedCount": 0,
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(attestation, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        "GitHub Release attestation OK: "
        f"tag={EXPECTED_TAG}; commit={EXPECTED_COMMIT}; assets=3; "
        f"zipSha256={zip_sha}; archivalDepositStatus=pending; humanVerified=0"
    )


if __name__ == "__main__":
    main()

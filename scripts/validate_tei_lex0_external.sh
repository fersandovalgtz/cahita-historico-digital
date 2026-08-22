#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCHEMA_URL='https://lex-0.org/releases/v0.9.5/schema/lex-0.rng'
SCHEMA_SHA256='35e73fef48526634714bdf3d16b924f958fca078a903d0bdc2dd4d7d116d1aaa'

if ! command -v jing >/dev/null 2>&1; then
  echo 'jing is required for external TEI Lex-0 validation' >&2
  exit 2
fi

work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT
schema="$work/lex-0-0.9.5.rng"
out="$work/tei"

curl -L --fail --silent --show-error --retry 3 --connect-timeout 15 \
  -o "$schema" "$SCHEMA_URL"

echo "$SCHEMA_SHA256  $schema" | sha256sum -c -
python "$ROOT/scripts/export_lexicon_tei.py" --out-dir "$out"
jing "$schema" "$out/chd_lexicon_tei.xml"

xml_sha="$(sha256sum "$out/chd_lexicon_tei.xml" | awk '{print $1}')"
xml_bytes="$(wc -c < "$out/chd_lexicon_tei.xml" | tr -d ' ')"

echo "external TEI Lex-0 QA OK: version=0.9.5; schemaSha256=$SCHEMA_SHA256; xmlSha256=$xml_sha; xmlBytes=$xml_bytes; validator=jing"

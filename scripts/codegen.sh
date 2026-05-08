#!/usr/bin/env bash
# Regenerate the generated Python client from packages/app/openapi/openapi.yaml.
#
# Uses `uv tool run` to invoke openapi-python-client without requiring a
# global install. The generated tree lands at src/eigenpal/_generated/ and
# is committed; users of the `eigenpal` PyPI package never run codegen.
#
# Idempotent: safe to run repeatedly. Strips the generator's pyproject.toml
# / README / etc. — we only keep the actual Python package source.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
PKG_DIR="$ROOT/packages/sdk-python"
SPEC="$ROOT/packages/app/openapi/openapi.yaml"
OUT_DIR="$PKG_DIR/src/eigenpal/_generated"
TMP_DIR="$(mktemp -d)"

if [ ! -f "$SPEC" ]; then
  echo "✗ Spec not found at $SPEC. Run \`bun run --cwd packages/app build:openapi\` first."
  exit 1
fi

echo "→ Generating Python client from $SPEC"

# openapi-python-client emits a full project layout — pyproject, README, etc.
# We only want the package source. Generate to a tmp dir, then sync the
# package source into our existing tree.
cd "$TMP_DIR"
uv tool run --from openapi-python-client@0.28.3 openapi-python-client generate \
  --path "$SPEC" \
  --config "$PKG_DIR/openapi-python-client.config.yaml" \
  --overwrite

GENERATED_DIR="$TMP_DIR/_generated/_generated"
if [ ! -d "$GENERATED_DIR" ]; then
  echo "✗ Expected generated package at $GENERATED_DIR — generator output layout changed."
  ls -la "$TMP_DIR" || true
  exit 1
fi

rm -rf "$OUT_DIR"
mkdir -p "$OUT_DIR"
cp -R "$GENERATED_DIR"/. "$OUT_DIR/"
rm -rf "$TMP_DIR"

echo "✓ Wrote generated client to $OUT_DIR"

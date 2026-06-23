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

python3 - "$OUT_DIR" <<'PY'
from pathlib import Path
import sys

out_dir = Path(sys.argv[1])

def replace(path: Path, old: str, new: str) -> None:
    text = path.read_text()
    if old not in text:
        raise RuntimeError(f"expected snippet not found in {path}")
    path.write_text(text.replace(old, new))

for path in out_dir.rglob("*.py"):
    text = path.read_text()
    lines = [line.rstrip() for line in text.splitlines()]
    while lines and lines[-1] == "":
        lines.pop()
    updated = "\n".join(lines) + "\n"
    if (
        "Unset" in updated
        and "from ...types import" in updated
        and "from ...types import UNSET, Unset" not in updated
    ):
        updated = updated.replace(
            "from ...types import Response, UNSET",
            "from ...types import Response, UNSET, Unset",
        )
    if updated != text:
        path.write_text(updated)

for relative in [
    "api/evaluation/automations_dataset_export.py",
    "api/reviews/runs_reviews_expected_file_get.py",
]:
    path = out_dir / relative
    text = path.read_text()
    text = text.replace("from ...types import File, FileTypes\n", "")
    text = text.replace("from io import BytesIO\n", "")
    text = text.replace("ApiErrorEnvelope | File", "ApiErrorEnvelope | bytes")
    text = text.replace("Response[ApiErrorEnvelope | File]", "Response[ApiErrorEnvelope | bytes]")
    text = text.replace(
        """        response_200 = File(
             payload = BytesIO(response.content)
        )



        return response_200""",
        """        response_200 = response.content
        return response_200""",
    )
    path.write_text(text)

runs_artifacts = out_dir / "api/runs/runs_artifacts_list.py"
text = runs_artifacts.read_text()
text = text.replace(
    "def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | RunArtifactsResponse | None:",
    "def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | RunArtifactsResponse | bytes | None:",
)
text = text.replace(
    "Response[ApiErrorEnvelope | RunArtifactsResponse]",
    "Response[ApiErrorEnvelope | RunArtifactsResponse | bytes]",
)
text = text.replace(
    "ApiErrorEnvelope | RunArtifactsResponse | None:",
    "ApiErrorEnvelope | RunArtifactsResponse | bytes | None:",
)
text = text.replace(
    """    if response.status_code == 200:
        response_200 = RunArtifactsResponse.from_dict(response.json())



        return response_200""",
    """    if response.status_code == 200:
        if response.headers.get("content-type", "").split(";", 1)[0].strip() in {"application/zip", "application/octet-stream"}:
            return response.content
        response_200 = RunArtifactsResponse.from_dict(response.json())



        return response_200""",
)
runs_artifacts.write_text(text)

runs_expected_create = out_dir / "api/reviews/runs_reviews_expected_create.py"
replace(
    runs_expected_create,
    """

        headers["Content-Type"] = "multipart/form-data"
""",
    "",
)
PY

echo "✓ Wrote generated client to $OUT_DIR"

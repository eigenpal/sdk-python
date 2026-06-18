"""Run with: ``EIGENPAL_API_KEY=eg_… python examples/quickstart.py``

Lists automations, picks the first one, triggers a run, and polls until the
run reaches a terminal state.
"""

from __future__ import annotations

import json
import os
import sys

from eigenpal import EigenpalClient, EigenpalError


def main() -> None:
    client = EigenpalClient(
        api_key=os.environ["EIGENPAL_API_KEY"],
        # For self-hosted deployments; defaults to https://studio.eigenpal.com.
        base_url=os.environ.get("EIGENPAL_BASE_URL"),
    )

    listing = client.automations.list(limit=1)
    automations = getattr(listing, "data", [])
    if not automations:
        print("No automations yet. Create one in the dashboard, then re-run.")
        return
    automation = automations[0]
    slug = automation.slug  # type: ignore[union-attr]
    run_type = automation.type  # type: ignore[union-attr]
    target = f"{run_type}s.{slug}"
    print(f"Triggering {target}")

    result = client.run_and_wait(
        target,
        input={},
        timeout_seconds=5 * 60,
    )
    print("finished:", result.finished)
    if result.finished:
        print("output:", json.dumps(result.output, indent=2, default=str))
    else:
        print(
            f"Run {result.id} still in flight; fetch it later with client.runs.get('{result.id}')."
        )


if __name__ == "__main__":
    try:
        main()
    except EigenpalError as e:
        print(f"✗ {type(e).__name__} ({e.status}): {e}", file=sys.stderr)
        if e.envelope:
            print(json.dumps(e.envelope, indent=2), file=sys.stderr)
        sys.exit(1)

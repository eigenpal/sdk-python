"""Run with: ``EIGENPAL_API_KEY=eg_… python examples/quickstart.py``

Lists workflows, picks the first one, triggers a run, and polls until
the execution reaches a terminal state.
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

    listing = client.workflows.list(limit=1)
    workflows = getattr(listing, "data", [])
    if not workflows:
        print("No workflows yet. Create one in the dashboard, then re-run.")
        return
    workflow = workflows[0]
    workflow_id = workflow.id  # type: ignore[union-attr]
    print(f"Triggering {workflow_id}")

    result = client.workflows.executions.run_and_wait(
        workflow_id,
        input={},
        timeout_seconds=5 * 60,
    )
    print("status:", result["status"])
    print("output:", json.dumps(result["output"], indent=2, default=str))


if __name__ == "__main__":
    try:
        main()
    except EigenpalError as e:
        print(f"✗ {type(e).__name__} ({e.status}): {e}", file=sys.stderr)
        if e.envelope:
            print(json.dumps(e.envelope, indent=2), file=sys.stderr)
        sys.exit(1)

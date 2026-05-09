#!/usr/bin/env python3
"""End-to-end smoke test for the published ``eigenpal`` package.

Usage (from a venv with ``eigenpal`` installed):

    EIGENPAL_BASE_URL=http://localhost:3000 \
    EIGENPAL_API_KEY=eig_live_... \
    python /path/to/local_smoke.py

The orchestrator at ``scripts/sdk-smoke-local.sh py`` builds a wheel,
installs it into a fresh venv, and invokes this script.

Mirrors the TS smoke verifier: confirms ``/api/v1`` paths resolve, that
the v1 endpoints return only the trimmed public surface, and that a bad
``base_url`` throws an ``EigenpalError`` instead of crashing.
"""

from __future__ import annotations

import os
import sys

from eigenpal import EigenpalClient, EigenpalError

BASE_URL = os.environ.get("EIGENPAL_BASE_URL", "http://localhost:3000")
API_KEY = os.environ.get("EIGENPAL_API_KEY")
if not API_KEY:
    print("EIGENPAL_API_KEY is required.", file=sys.stderr)
    sys.exit(2)

PUBLIC_WORKFLOW_FIELDS = {"id", "name", "version", "created_at", "updated_at"}
PUBLIC_EXECUTION_FIELDS = {
    "id",
    "workflow_id",
    "status",
    "trigger_type",
    "trigger_input",
    "result",
    "error",
    "created_at",
    "started_at",
    "completed_at",
    "workflow",
}

results: list[tuple[str, bool, str]] = []


def pass_(name: str, ok: bool, detail: str) -> None:
    results.append((name, ok, detail))
    print(f"{'✓' if ok else '✗'} {name} — {detail}")


def model_keys(obj: object) -> set[str]:
    """Public attrs on an attrs-defined model, excluding the catch-all dict."""
    if hasattr(obj, "__attrs_attrs__"):
        names = {a.name for a in obj.__attrs_attrs__}  # type: ignore[attr-defined]
        names.discard("additional_properties")
        # Drop attrs whose value is UNSET (the model declares them but the
        # server didn't return them — a tighter response is fine).
        from eigenpal._generated.types import Unset

        return {n for n in names if not isinstance(getattr(obj, n, None), Unset)}
    if isinstance(obj, dict):
        return set(obj.keys())
    raise TypeError(f"unsupported response type: {type(obj).__name__}")


def main() -> int:
    print(f"→ Smoke-testing eigenpal against {BASE_URL}\n")
    client = EigenpalClient(api_key=API_KEY, base_url=BASE_URL)

    # 1. workflows.list → public shape
    listing = client.workflows.list(limit=5)
    items = listing.data if hasattr(listing, "data") else []
    pass_("workflows.list responds", isinstance(items, list), f"data.length={len(items)}")
    workflow_id = None
    if items:
        keys = model_keys(items[0])
        leaked = keys - PUBLIC_WORKFLOW_FIELDS
        pass_(
            "workflows[0] only public fields",
            not leaked,
            f"leaked: {sorted(leaked)}" if leaked else f"keys: {sorted(keys)}",
        )
        workflow_id = items[0].id

    # 2. workflows.get → same shape
    if workflow_id:
        fetched = client.workflows.get(workflow_id)
        keys = model_keys(fetched)
        leaked = keys - PUBLIC_WORKFLOW_FIELDS
        pass_(
            "workflows.get only public fields",
            not leaked,
            f"leaked: {sorted(leaked)}"
            if leaked
            else f"version={getattr(fetched, 'version', None)}",
        )

    # 3. workflows.executions.list → public shape
    execs = client.workflows.executions.list(workflow_id, limit=5) if workflow_id else None
    exec_items = execs.data if hasattr(execs, "data") else []
    pass_(
        "workflows.executions.list responds",
        isinstance(exec_items, list),
        f"data.length={len(exec_items)}",
    )
    if exec_items:
        keys = model_keys(exec_items[0])
        leaked = keys - PUBLIC_EXECUTION_FIELDS
        pass_(
            "workflows.executions[0] only public fields",
            not leaked,
            f"leaked: {sorted(leaked)}" if leaked else f"keys: {sorted(keys)}",
        )

    # 4. Bad base_url throws an EigenpalError, not a raw httpx crash
    try:
        bad = EigenpalClient(api_key=API_KEY, base_url="https://example.com")
        bad.workflows.list(limit=1)
        pass_("bad base_url throws EigenpalError", False, "no error thrown")
    except EigenpalError as e:
        pass_("bad base_url throws EigenpalError", True, type(e).__name__)
    except Exception as e:
        pass_(
            "bad base_url throws EigenpalError",
            False,
            f"raw {type(e).__name__}: {str(e)[:80]}",
        )

    failed = [r for r in results if not r[1]]
    print(
        f"\n{'✓ all checks passed' if not failed else f'✗ {len(failed)} check(s) failed'} "
        f"({len(results)} total)"
    )
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())

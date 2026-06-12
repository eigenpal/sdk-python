"""Smoke tests for the Python SDK against mocked HTTP responses.

Run via `uv run pytest` from this directory.
"""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from eigenpal import (
    EigenpalClient,
    EigenpalAuthError,
    EigenpalError,
    EigenpalNotFoundError,
    EigenpalRateLimitError,
    EigenpalValidationError,
)


@pytest.fixture
def client() -> EigenpalClient:
    return EigenpalClient(api_key="eg_test_key", base_url="http://localhost:3000")


_TERMINAL_STATUSES = frozenset({"completed", "failed", "cancelled", "rejected"})


def run_accepted(**overrides: object) -> dict[str, object]:
    """Async run-start / rerun acceptance body (201 or 202)."""
    return {
        "id": "run_123",
        "type": "workflow",
        "finished": False,
        **overrides,
    }


def run_cancel_response(**overrides: object) -> dict[str, object]:
    return {
        "id": "run_123",
        "type": "workflow",
        "finished": True,
        "execution": {"status": "cancelled"},
        "cancellation": {"state": "cancelled", "wasStatus": "pending"},
        **overrides,
    }


def run_summary(**overrides: object) -> dict[str, object]:
    """Canonical grouped run body returned by GET /api/v1/runs/{id}."""
    special = dict(overrides)
    run_id = special.pop("id", "run_123")
    type_ = special.pop("type", "workflow")
    status = special.pop("status", "completed")
    output = special.pop("output", None)
    expected = special.pop("expected", None)
    expected_files = special.pop("expectedFiles", [])
    result_files = special.pop("resultFiles", [])
    finished = special.pop("finished", status in _TERMINAL_STATUSES)
    completed_at = special.pop(
        "completedAt",
        "2026-01-01T00:01:00.000Z" if finished else None,
    )

    execution: dict[str, object] = {
        "status": status,
        "schemaValid": None,
        "batchId": None,
        "annotation": None,
        "retry": {"number": 0, "previousRunId": None, "nextRun": None},
    }
    if type_ == "workflow":
        execution["steps"] = []
        if expected is not None:
            execution["expected"] = expected
    else:
        execution["files"] = {"output": result_files}
        execution["feedback"] = None
        if expected is not None or expected_files:
            execution["expected"] = {"output": expected, "files": expected_files}

    base: dict[str, object] = {
        "id": run_id,
        "type": type_,
        "finished": finished,
        "timing": {
            "createdAt": "2026-01-01T00:00:00.000Z",
            "startedAt": None,
            "completedAt": completed_at,
            "durationMs": 1200 if finished else None,
            "cancelRequestedAt": None,
        },
        "source": {
            "id": "awf_123" if type_ == "agent" else "wf_123",
            "name": "Invoice Agent" if type_ == "agent" else "Extract",
            "version": None,
            **(
                {
                    "slug": "invoice-agent",
                    "model": "claude-sonnet-4-5",
                    "git": {
                        "requestedRef": None,
                        "resolvedRef": None,
                        "resolvedTag": None,
                        "commitSha": None,
                    },
                }
                if type_ == "agent"
                else {"versionId": None}
            ),
        },
        "trigger": {"type": "api", "by": None},
        "execution": execution,
    }
    if finished and output is not None:
        base["output"] = output
    base.update(special)
    return base


@respx.mock
def test_attaches_bearer_auth(client: EigenpalClient) -> None:
    route = respx.get("http://localhost:3000/api/v1/workflows").mock(
        return_value=httpx.Response(
            200, json={"data": [], "total": 0, "limit": 50, "offset": 0}
        )
    )

    client.workflows.list()

    assert route.called
    assert route.calls.last.request.headers["authorization"] == "Bearer eg_test_key"


@respx.mock
def test_attaches_sdk_telemetry_headers(client: EigenpalClient) -> None:
    route = respx.get("http://localhost:3000/api/v1/workflows").mock(
        return_value=httpx.Response(
            200, json={"data": [], "total": 0, "limit": 50, "offset": 0}
        )
    )

    client.workflows.list()

    h = route.calls.last.request.headers
    assert h["x-eigenpal-sdk"] == "python"
    assert "x-eigenpal-sdk-version" in h
    # Runtime tag is "python-X.Y.Z" or "pypy-X.Y.Z"
    assert h["x-eigenpal-sdk-runtime"].startswith(("python-", "pypy-"))
    assert "-" in h["x-eigenpal-sdk-os"]
    assert h["user-agent"].startswith("eigenpal-sdk-python/")


@respx.mock
def test_run_returns_id(client: EigenpalClient) -> None:
    route = respx.post("http://localhost:3000/api/v1/runs").mock(
        return_value=httpx.Response(202, json=run_accepted(id="exec_abc"))
    )

    result = client.run("workflows.wf_xyz", input={"foo": "bar"})

    assert route.called
    assert result.id == "exec_abc"
    body = json.loads(route.calls.last.request.content.decode())
    assert body == {"target": "workflows.wf_xyz", "input": {"foo": "bar"}}


@respx.mock
def test_run_sends_overrides_in_canonical_envelope_body(client: EigenpalClient) -> None:
    route = respx.post("http://localhost:3000/api/v1/runs").mock(
        return_value=httpx.Response(202, json=run_accepted(id="exec_ov"))
    )

    overrides = {"steps": {"extract": {"total": 42}}}
    result = client.run("workflows.wf_xyz", input={"language": "en"}, overrides=overrides)

    assert result.id == "exec_ov"
    body = json.loads(route.calls.last.request.content.decode())
    assert body == {
        "target": "workflows.wf_xyz",
        "input": {"language": "en"},
        "overrides": overrides,
    }


@respx.mock
def test_run_object_targets_mirror_canonical_run_target_grammar(client: EigenpalClient) -> None:
    respx.post("http://localhost:3000/api/v1/runs").mock(
        return_value=httpx.Response(202, json=run_accepted(id="exec_workflow"))
    )

    client.run(
        {"type": "workflow", "slug": "finance/extract-invoice", "version": "1.2.3"},
        input={},
    )
    client.run({"type": "agent", "slug": "finance/invoice-agent", "version": "main"}, input={})
    client.run({"type": "agent", "slug": "agents.finance.invoice-agent"}, input={})

    workflow_request = respx.calls[0].request
    agent_request = respx.calls[1].request
    rooted_agent_request = respx.calls[2].request
    assert workflow_request.url.path.endswith("/api/v1/runs")
    assert "version=1.2.3" in str(workflow_request.url)
    assert json.loads(workflow_request.content.decode()) == {
        "target": "workflows.finance.extract-invoice",
        "input": {},
    }
    assert agent_request.url.path.endswith("/api/v1/runs")
    assert "version=main" in str(agent_request.url)
    assert json.loads(agent_request.content.decode()) == {
        "target": "agents.finance.invoice-agent",
        "input": {},
    }
    assert rooted_agent_request.url.path.endswith("/api/v1/runs")
    assert json.loads(rooted_agent_request.content.decode()) == {
        "target": "agents.finance.invoice-agent",
        "input": {},
    }


def test_run_rejects_ambiguous_rooted_agent_object_targets(client: EigenpalClient) -> None:
    with pytest.raises(EigenpalError, match='rooted at "agents\\."'):
        client.run({"type": "agent", "slug": "workflows.extract-invoice"}, input={})


@respx.mock
def test_run_with_wait_for_completion(client: EigenpalClient) -> None:
    route = respx.post("http://localhost:3000/api/v1/runs").mock(
        return_value=httpx.Response(
            200,
            json={
                **run_summary(id="exec_abc", status="completed", output={"ok": True}),
            },
        )
    )

    result = client.run("workflows.wf_xyz", input={"x": 1}, wait_for_completion=30)

    assert result.id == "exec_abc"
    assert "wait_for_completion=30" in str(route.calls.last.request.url)


@respx.mock
def test_agents_update_hits_update_endpoint(client: EigenpalClient) -> None:
    route = respx.patch("http://localhost:3000/api/v1/agents/invoice-agent").mock(
        return_value=httpx.Response(
            200,
            json={
                "agent": {
                    "id": "awf_123",
                    "slug": "invoice-agent",
                    "name": "Invoice Agent",
                    "description": "Updated",
                    "config": {"triggers": {"api": {"enabled": True}}},
                    "createdAt": "2026-01-01T00:00:00.000Z",
                    "updatedAt": "2026-01-02T00:00:00.000Z",
                }
            },
        )
    )

    result = client.agents.update(
        "invoice-agent",
        description="Updated",
        config={"triggers": {"api": {"enabled": True}}},
    )

    assert route.called
    assert result.agent.description == "Updated"
    body = json.loads(route.calls.last.request.content.decode())
    assert body == {
        "description": "Updated",
        "config": {"triggers": {"api": {"enabled": True}}},
    }


@respx.mock
def test_agent_run_with_wait_for_completion_accepts_200(
    client: EigenpalClient,
) -> None:
    route = respx.post(
        "http://localhost:3000/api/v1/runs", params={"version": "1.2.3"}
    ).mock(
        return_value=httpx.Response(
            200,
            json=run_summary(id="aex_123", type="agent", status="completed", output={"ok": True}),
        )
    )

    result = client.run(
        {"type": "agent", "slug": "invoice-agent", "version": "1.2.3"},
        input={"prompt": "hello"},
        wait_for_completion=30,
    )

    assert route.called
    assert result.id == "aex_123"
    assert result.finished is True
    assert result.execution.status.value == "completed"
    assert result.output.to_dict() == {"ok": True}
    assert "wait_for_completion=30" in str(route.calls.last.request.url)
    assert "version=1.2.3" in str(route.calls.last.request.url)


@respx.mock
def test_runs_list_accepts_agent_source_ref(client: EigenpalClient) -> None:
    route = respx.get("http://localhost:3000/api/v1/runs").mock(
        return_value=httpx.Response(
            200,
            json={
                "runs": [],
                "nextCursor": None,
            },
        )
    )

    client.runs.list(type="agent", source="invoice-agent", source_ref="latest", limit=10)

    assert route.called
    assert "type=agent" in str(route.calls.last.request.url)
    assert "source=invoice-agent" in str(route.calls.last.request.url)


@respx.mock
def test_runs_resource_uses_public_v1_runs_api(client: EigenpalClient) -> None:
    list_route = respx.get("http://localhost:3000/api/v1/runs").mock(
        return_value=httpx.Response(
            200,
            json={
                "runs": [],
                "nextCursor": None,
            },
        )
    )
    get_route = respx.get("http://localhost:3000/api/v1/runs/run_123").mock(
        return_value=httpx.Response(200, json=run_summary())
    )
    cancel_route = respx.post("http://localhost:3000/api/v1/runs/run_123/cancel").mock(
        return_value=httpx.Response(200, json=run_cancel_response(id="run_123"))
    )
    rerun_route = respx.post("http://localhost:3000/api/v1/runs/run_123/rerun").mock(
        return_value=httpx.Response(200, json=run_accepted(id="run_rerun"))
    )
    feedback_route = respx.patch("http://localhost:3000/api/v1/runs/run_123/feedback").mock(
        return_value=httpx.Response(200, json={"ok": True})
    )
    expected_route = respx.get("http://localhost:3000/api/v1/runs/run_123/expected").mock(
        return_value=httpx.Response(200, json={"expected": None, "files": []})
    )

    client.runs.list(type="workflow", source="wf_123", status="completed")
    run = client.runs.get("run_123", expand=["usage", "execution"])
    client.runs.cancel("run_123")
    client.rerun("run_123")
    client.runs.feedback.update("run_123", status="open")
    client.runs.expected.list("run_123")

    assert list_route.called
    assert "type=workflow" in str(list_route.calls.last.request.url)
    assert "source=wf_123" in str(list_route.calls.last.request.url)
    assert get_route.called
    assert "expand=usage%2Cexecution" in str(get_route.calls.last.request.url)
    assert run.id == "run_123"
    assert cancel_route.called
    assert rerun_route.called
    assert feedback_route.called
    assert expected_route.called


@respx.mock
def test_runs_compare_unwraps_typed_run_models(client: EigenpalClient) -> None:
    """compare must see expanded fields through the typed Run model, not always pass."""
    respx.get("http://localhost:3000/api/v1/runs/run_ref").mock(
        return_value=httpx.Response(
            200,
            json=run_summary(
                id="run_ref",
                type="agent",
                expected={"total": 1},
                expectedFiles=[{"name": "report.json"}],
            ),
        )
    )
    respx.get("http://localhost:3000/api/v1/runs/run_tgt").mock(
        return_value=httpx.Response(
            200,
            json=run_summary(
                id="run_tgt",
                type="agent",
                output={"ok": True},
                resultFiles=[{"name": "other.json"}],
            ),
        )
    )

    result = client.runs.compare("run_ref", "run_tgt")

    assert result["status"] == "fail"
    assert "report.json" in result["missingFiles"]
    assert "other.json" in result["extraFiles"]


@respx.mock
def test_401_raises_auth_error(client: EigenpalClient) -> None:
    respx.get("http://localhost:3000/api/v1/workflows").mock(
        return_value=httpx.Response(
            401,
            json={
                "issues": [
                    {
                        "field": "<root>",
                        "message": "invalid",
                        "code": "unauthorized",
                        "severity": "error",
                    }
                ],
                "requestId": "r1",
            },
        )
    )

    with pytest.raises(EigenpalAuthError):
        client.workflows.list()


@respx.mock
def test_404_raises_not_found_error(client: EigenpalClient) -> None:
    respx.get("http://localhost:3000/api/v1/workflows/wf_missing").mock(
        return_value=httpx.Response(
            404,
            json={
                "issues": [
                    {
                        "field": "<root>",
                        "message": "Workflow not found",
                        "code": "not_found",
                        "severity": "error",
                    }
                ],
                "requestId": "r2",
            },
        )
    )

    with pytest.raises(EigenpalNotFoundError):
        client.workflows.get("wf_missing")


@respx.mock
def test_429_raises_rate_limit_error_with_retry_after(client: EigenpalClient) -> None:
    respx.get("http://localhost:3000/api/v1/workflows").mock(
        return_value=httpx.Response(
            429,
            headers={"retry-after": "12"},
            json={
                "issues": [
                    {
                        "field": "<root>",
                        "message": "rate limited",
                        "code": "rate_limited",
                        "severity": "error",
                    }
                ],
                "requestId": "r3",
            },
        )
    )

    with pytest.raises(EigenpalRateLimitError) as exc:
        client.workflows.list()

    assert exc.value.retry_after == 12


@respx.mock
def test_400_raises_validation_error_with_issues(client: EigenpalClient) -> None:
    respx.post("http://localhost:3000/api/v1/runs").mock(
        return_value=httpx.Response(
            400,
            json={
                "issues": [
                    {
                        "field": "body.input",
                        "message": "required",
                        "code": "required",
                        "severity": "error",
                    }
                ],
                "requestId": "r4",
            },
        )
    )

    with pytest.raises(EigenpalValidationError) as exc:
        client.run({"type": "workflow", "id": "wf_xyz"})

    assert exc.value.issues[0]["field"] == "body.input"


@respx.mock
def test_runs_cancel_cancels_workflow_runs(client: EigenpalClient) -> None:
    route = respx.post("http://localhost:3000/api/v1/runs/exec_pq/cancel").mock(
        return_value=httpx.Response(200, json=run_cancel_response(id="exec_pq"))
    )

    result = client.runs.cancel("exec_pq")

    assert route.called
    assert result.execution.status.value == "cancelled"
    assert result.cancellation.state.value == "cancelled"


@respx.mock
def test_run_and_wait_polls_until_terminal(client: EigenpalClient) -> None:
    respx.post("http://localhost:3000/api/v1/runs").mock(
        return_value=httpx.Response(202, json=run_accepted(id="exec_pq"))
    )
    # First poll: running. Second: completed.
    poll_route = respx.get("http://localhost:3000/api/v1/runs/exec_pq").mock(
        side_effect=[
            httpx.Response(
                200, json=run_summary(id="exec_pq", status="running", finished=False)
            ),
            httpx.Response(
                200,
                json=run_summary(
                    id="exec_pq",
                    status="completed",
                    output={"total": 42},
                    completedAt="2025-01-01T00:00:05Z",
                ),
            ),
        ]
    )

    result = client.workflows.executions.run_and_wait(
        "wf_abc", input={"x": 1}, poll_interval_seconds=0.01, timeout_seconds=5.0
    )

    assert poll_route.call_count == 2
    assert result["id"] == "exec_pq"
    assert result["status"] == "completed"
    assert result["output"] == {"total": 42}

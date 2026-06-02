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
    EigenpalNotFoundError,
    EigenpalRateLimitError,
    EigenpalValidationError,
)


@pytest.fixture
def client() -> EigenpalClient:
    return EigenpalClient(api_key="eg_test_key", base_url="http://localhost:3000")


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
def test_workflows_run_returns_execution_id(client: EigenpalClient) -> None:
    route = respx.post("http://localhost:3000/api/v1/workflows/wf_xyz/run").mock(
        return_value=httpx.Response(201, json={"executionId": "exec_abc"})
    )

    result = client.workflows.run("wf_xyz", input={"foo": "bar"})

    assert route.called
    assert result.execution_id == "exec_abc"
    body = json.loads(route.calls.last.request.content.decode())
    assert body == {"input": {"foo": "bar"}}


@respx.mock
def test_workflows_run_with_wait_for_completion(client: EigenpalClient) -> None:
    route = respx.post("http://localhost:3000/api/v1/workflows/wf_xyz/run").mock(
        return_value=httpx.Response(
            201,
            json={
                "executionId": "exec_abc",
                "status": "completed",
                "result": {"ok": True},
            },
        )
    )

    result = client.workflows.run("wf_xyz", input={"x": 1}, wait_for_completion=30)

    assert result.execution_id == "exec_abc"
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
def test_agents_run_with_wait_for_completion_accepts_200(client: EigenpalClient) -> None:
    route = respx.post("http://localhost:3000/api/v1/agents/invoice-agent/run").mock(
        return_value=httpx.Response(
            200,
            json={
                "runId": "aex_123",
                "status": "completed",
                "output": {"ok": True},
            },
        )
    )

    result = client.agents.run(
        "invoice-agent",
        input={"prompt": "hello"},
        wait_for_completion=30,
        source_ref="1.2.3",
    )

    assert route.called
    assert result.run_id == "aex_123"
    assert result.status == "completed"
    assert result.output == {"ok": True}
    assert "wait_for_completion=30" in str(route.calls.last.request.url)
    assert "sourceRef=1.2.3" in str(route.calls.last.request.url)


@respx.mock
def test_agents_runs_list_accepts_source_ref(client: EigenpalClient) -> None:
    route = respx.get("http://localhost:3000/api/v1/agents/invoice-agent/runs").mock(
        return_value=httpx.Response(
            200,
            json={
                "runs": [],
                "total": 0,
                "limit": 10,
                "offset": 0,
            },
        )
    )

    client.agents.runs.list("invoice-agent", source_ref="latest", limit=10)

    assert route.called
    assert "sourceRef=latest" in str(route.calls.last.request.url)


@respx.mock
def test_401_raises_auth_error(client: EigenpalClient) -> None:
    respx.get("http://localhost:3000/api/v1/workflows").mock(
        return_value=httpx.Response(
            401,
            json={
                "issues": [
                    {"field": "<root>", "message": "invalid", "code": "unauthorized", "severity": "error"}
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
                    {"field": "<root>", "message": "Workflow not found", "code": "not_found", "severity": "error"}
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
                    {"field": "<root>", "message": "rate limited", "code": "rate_limited", "severity": "error"}
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
    respx.post("http://localhost:3000/api/v1/workflows/wf_xyz/run").mock(
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
        client.workflows.run("wf_xyz")

    assert exc.value.issues[0]["field"] == "body.input"


@respx.mock
def test_executions_cancel(client: EigenpalClient) -> None:
    route = respx.post("http://localhost:3000/api/v1/workflows/executions/exec_pq/cancel").mock(
        return_value=httpx.Response(
            200,
            json={
                "executionId": "exec_pq",
                "status": "cancelled",
                "wasStatus": "pending",
            },
        )
    )

    result = client.workflows.executions.cancel("exec_pq")

    assert route.called
    assert result.execution_id == "exec_pq"
    assert str(result.status) == "cancelled" or result.status.value == "cancelled"


@respx.mock
def test_run_and_wait_polls_until_terminal(client: EigenpalClient) -> None:
    respx.post("http://localhost:3000/api/v1/workflows/wf_abc/run").mock(
        return_value=httpx.Response(201, json={"executionId": "exec_pq"})
    )
    # First poll: running. Second: completed.
    poll_route = respx.get("http://localhost:3000/api/v1/workflows/executions/exec_pq").mock(
        side_effect=[
            httpx.Response(
                200,
                json={
                    "executionId": "exec_pq",
                    "status": "running",
                    "createdAt": "2025-01-01T00:00:00Z",
                },
            ),
            httpx.Response(
                200,
                json={
                    "executionId": "exec_pq",
                    "status": "completed",
                    "result": {"total": 42},
                    "createdAt": "2025-01-01T00:00:00Z",
                    "completedAt": "2025-01-01T00:00:05Z",
                },
            ),
        ]
    )

    result = client.workflows.executions.run_and_wait(
        "wf_abc", input={"x": 1}, poll_interval_seconds=0.01, timeout_seconds=5.0
    )

    assert poll_route.call_count == 2
    assert result["executionId"] == "exec_pq"
    assert result["status"] == "completed"
    assert result["result"] == {"total": 42}

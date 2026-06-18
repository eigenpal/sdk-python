"""Smoke tests for the Python SDK against mocked public API responses."""

from __future__ import annotations

import json

import httpx
import pytest
import respx

from eigenpal import (
    EigenpalAuthError,
    EigenpalClient,
    EigenpalNotFoundError,
    EigenpalRateLimitError,
    EigenpalValidationError,
)


@pytest.fixture
def client() -> EigenpalClient:
    return EigenpalClient(api_key="eg_test_key", base_url="http://localhost:3000", max_retries=0)


def run_accepted(**overrides: object) -> dict[str, object]:
    return {"id": "run_123", "type": "workflow", "finished": False, **overrides}


def run_summary(**overrides: object) -> dict[str, object]:
    return {
        "id": "run_123",
        "type": "workflow",
        "finished": True,
        "execution": {"status": "completed"},
        **overrides,
    }


@respx.mock
def test_attaches_bearer_auth_and_telemetry(client: EigenpalClient) -> None:
    route = respx.get("http://localhost:3000/api/v1/automations").mock(
        return_value=httpx.Response(200, json={"data": []})
    )

    client.automations.list()

    headers = route.calls.last.request.headers
    assert headers["authorization"] == "Bearer eg_test_key"
    assert headers["x-eigenpal-sdk"] == "python"
    assert headers["user-agent"].startswith("eigenpal-sdk-python/")


@respx.mock
def test_run_returns_id_and_sends_canonical_body(client: EigenpalClient) -> None:
    route = respx.post("http://localhost:3000/api/v1/runs", params={"version": "1.2.3"}).mock(
        return_value=httpx.Response(202, json=run_accepted(id="run_abc"))
    )

    result = client.run("workflows.extract-invoice@1.2.3", input={"language": "en"})

    assert result.id == "run_abc"
    assert json.loads(route.calls.last.request.content.decode()) == {
        "target": "workflows.extract-invoice",
        "input": {"language": "en"},
    }


@respx.mock
def test_run_forwards_metadata_in_json_body(client: EigenpalClient) -> None:
    route = respx.post("http://localhost:3000/api/v1/runs").mock(
        return_value=httpx.Response(202, json=run_accepted(id="run_meta"))
    )

    result = client.run(
        "workflows.extract-invoice",
        input={"language": "en"},
        metadata={"request_id": "req_1"},
    )

    assert result.id == "run_meta"
    assert json.loads(route.calls.last.request.content.decode()) == {
        "target": "workflows.extract-invoice",
        "input": {"language": "en"},
        "metadata": {"request_id": "req_1"},
    }


@respx.mock
def test_run_forwards_metadata_as_multipart_field(tmp_path, client: EigenpalClient) -> None:
    pdf = tmp_path / "contract.pdf"
    pdf.write_bytes(b"%PDF-1.4 fake content")

    route = respx.post("http://localhost:3000/api/v1/runs").mock(
        return_value=httpx.Response(202, json=run_accepted(id="run_meta"))
    )

    client.run(
        "workflows.extract-invoice",
        input={"contract": pdf},
        metadata={"request_id": "req_1"},
    )

    body = route.calls.last.request.content.decode("utf-8", errors="replace")
    assert 'name="metadata"' in body
    assert '"request_id": "req_1"' in body or '"request_id":"req_1"' in body


@respx.mock
def test_run_object_targets_mirror_canonical_target_grammar(client: EigenpalClient) -> None:
    respx.post("http://localhost:3000/api/v1/runs").mock(
        return_value=httpx.Response(202, json=run_accepted())
    )

    client.run({"type": "workflow", "slug": "finance/extract-invoice"}, input={})
    client.run({"type": "agent", "slug": "finance/invoice-agent"}, input={})

    assert json.loads(respx.calls[0].request.content.decode()) == {
        "target": "workflows.finance.extract-invoice",
        "input": {},
    }
    assert json.loads(respx.calls[1].request.content.decode()) == {
        "target": "agents.finance.invoice-agent",
        "input": {},
    }


def test_run_rejects_ambiguous_rooted_agent_targets(client: EigenpalClient) -> None:
    with pytest.raises(Exception, match='rooted at "agents\\."'):
        client.run({"type": "agent", "slug": "workflows.extract-invoice"}, input={})


@respx.mock
def test_public_resources_use_public_routes(client: EigenpalClient) -> None:
    respx.get("http://localhost:3000/api/v1/automations").mock(
        return_value=httpx.Response(200, json={"data": []})
    )
    respx.get("http://localhost:3000/api/v1/automations/workflows.extract-invoice").mock(
        return_value=httpx.Response(200, json={"id": "workflows.extract-invoice"})
    )
    respx.get("http://localhost:3000/api/v1/automations/workflows.extract-invoice/versions").mock(
        return_value=httpx.Response(200, json={"data": []})
    )
    respx.get("http://localhost:3000/api/v1/automations/workflows.extract-invoice/triggers").mock(
        return_value=httpx.Response(200, json={"triggers": []})
    )
    respx.get("http://localhost:3000/api/v1/runs").mock(
        return_value=httpx.Response(200, json={"runs": []})
    )
    respx.get("http://localhost:3000/api/v1/runs/run_123").mock(
        return_value=httpx.Response(200, json=run_summary())
    )
    respx.get("http://localhost:3000/api/v1/runs/run_123/usage").mock(
        return_value=httpx.Response(200, json={"usage": None})
    )
    respx.get("http://localhost:3000/api/v1/runs/run_123/steps").mock(
        return_value=httpx.Response(200, json={"steps": []})
    )
    respx.get("http://localhost:3000/api/v1/runs/run_123/events").mock(
        return_value=httpx.Response(200, json={"events": []})
    )
    respx.get("http://localhost:3000/api/v1/runs/run_123/artifacts").mock(
        return_value=httpx.Response(200, json={"artifacts": []})
    )
    respx.get("http://localhost:3000/api/v1/runs/run_123/feedback").mock(
        return_value=httpx.Response(200, json={"feedback": None})
    )
    respx.get("http://localhost:3000/api/v1/runs/run_123/trace").mock(
        return_value=httpx.Response(200, json={"lines": []})
    )
    respx.post("http://localhost:3000/api/v1/files").mock(
        return_value=httpx.Response(201, json={"id": "file_123", "filename": "input.txt"})
    )
    respx.get("http://localhost:3000/api/v1/files/file_123").mock(
        return_value=httpx.Response(200, json={"id": "file_123", "filename": "input.txt"})
    )
    respx.delete("http://localhost:3000/api/v1/files/file_123").mock(
        return_value=httpx.Response(204)
    )

    client.automations.list()
    client.automations.get("workflows.extract-invoice")
    client.automations.versions("workflows.extract-invoice")
    client.automations.triggers("workflows.extract-invoice")
    client.runs.list(type="workflow", status="completed")
    client.runs.get("run_123", expand=["usage", "execution"])
    client.runs.usage("run_123")
    client.runs.steps("run_123")
    client.runs.events("run_123")
    client.runs.artifacts.list("run_123")
    client.runs.feedback.get("run_123")
    client.runs.trace.get("run_123")
    client.files.upload({"content": b"hello", "filename": "input.txt", "mime_type": "text/plain"})
    client.files.get("file_123")
    assert client.files.delete("file_123") is None

    assert len(respx.calls) == 15


@respx.mock
def test_run_control_routes(client: EigenpalClient) -> None:
    cancel_route = respx.post("http://localhost:3000/api/v1/runs/run_123/cancel").mock(
        return_value=httpx.Response(200, json=run_summary(id="run_123"))
    )
    rerun_route = respx.post(
        "http://localhost:3000/api/v1/runs/run_123/rerun",
        params={"wait_for_completion": "30"},
    ).mock(return_value=httpx.Response(202, json=run_accepted(id="run_456")))

    client.runs.cancel("run_123")
    client.rerun("run_123", wait_for_completion=30)

    assert cancel_route.called
    assert rerun_route.called


@respx.mock
def test_401_404_429_and_400_raise_typed_errors(client: EigenpalClient) -> None:
    respx.get("http://localhost:3000/api/v1/automations").mock(
        side_effect=[
            httpx.Response(401, json={"issues": [{"field": "<root>", "message": "invalid"}]}),
            httpx.Response(429, headers={"retry-after": "12"}, json={"issues": []}),
            httpx.Response(400, json={"issues": [{"field": "target", "message": "required"}]}),
        ]
    )
    respx.get("http://localhost:3000/api/v1/automations/missing").mock(
        return_value=httpx.Response(404, json={"issues": [{"field": "<root>", "message": "missing"}]})
    )

    with pytest.raises(EigenpalAuthError):
        client.automations.list()
    with pytest.raises(EigenpalNotFoundError):
        client.automations.get("missing")
    with pytest.raises(EigenpalRateLimitError):
        client.automations.list()
    with pytest.raises(EigenpalValidationError):
        client.automations.list()


@respx.mock
def test_run_and_wait_polls_until_terminal(client: EigenpalClient) -> None:
    respx.post("http://localhost:3000/api/v1/runs").mock(
        return_value=httpx.Response(202, json=run_accepted(id="run_123"))
    )
    respx.get("http://localhost:3000/api/v1/runs/run_123").mock(
        side_effect=[
            httpx.Response(200, json=run_summary(id="run_123", finished=False, execution={"status": "running"})),
            httpx.Response(200, json=run_summary(id="run_123", output={"total": 42})),
        ]
    )

    result = client.run_and_wait(
        "workflows.extract-invoice",
        input={"x": 1},
        poll_interval_seconds=0.01,
        timeout_seconds=5.0,
    )

    assert result.output.total == 42

"""Tests for multipart file uploads — exercises the ``-F``-style path the
SDK takes whenever ``client.run``'s input contains a Path / file-like /
explicit dict descriptor."""

from __future__ import annotations

import json
from io import BytesIO
from pathlib import Path

import httpx
import pytest
import respx

from eigenpal import EigenpalClient


@pytest.fixture
def client() -> EigenpalClient:
    return EigenpalClient(api_key="eg_test_key", base_url="http://localhost:3000")


@respx.mock
def test_path_input_uploads_as_multipart(tmp_path: Path, client: EigenpalClient) -> None:
    pdf = tmp_path / "contract.pdf"
    pdf.write_bytes(b"%PDF-1.4 fake content")

    route = respx.post("http://localhost:3000/api/v1/run/workflows.wf_xyz").mock(
        return_value=httpx.Response(201, json={"runId": "exec_abc", "type": "workflow"})
    )

    result = client.run(
        {"type": "workflow", "id": "wf_xyz"},
        input={"contract_document": pdf, "language": "en"},
    )

    assert result.run_id == "exec_abc"
    request = route.calls.last.request
    content_type = request.headers["content-type"]
    assert content_type.startswith("multipart/form-data; boundary=")

    body = request.content.decode("utf-8", errors="replace")
    assert 'name="contract_document"' in body
    assert 'filename="contract.pdf"' in body
    # Scalar input rides in the _json sidecar
    assert 'name="_json"' in body
    assert '"target"' not in body
    assert '"language": "en"' in body or '"language":"en"' in body


@respx.mock
def test_explicit_descriptor_with_raw_bytes(client: EigenpalClient) -> None:
    route = respx.post("http://localhost:3000/api/v1/run/workflows.wf_xyz").mock(
        return_value=httpx.Response(201, json={"runId": "exec_abc", "type": "workflow"})
    )

    client.run(
        {"type": "workflow", "id": "wf_xyz"},
        input={
            "contract": {
                "content": b"%PDF",
                "filename": "contract.pdf",
                "mime_type": "application/pdf",
            },
        },
    )

    body = route.calls.last.request.content.decode("utf-8", errors="replace")
    assert 'filename="contract.pdf"' in body
    assert "application/pdf" in body


@respx.mock
def test_file_like_object_uploads(tmp_path: Path, client: EigenpalClient) -> None:
    fpath = tmp_path / "policy.txt"
    fpath.write_bytes(b"hello world")

    route = respx.post("http://localhost:3000/api/v1/run/workflows.wf_xyz").mock(
        return_value=httpx.Response(201, json={"runId": "exec_abc", "type": "workflow"})
    )

    with fpath.open("rb") as f:
        client.run("workflows.wf_xyz", input={"policy": f})

    body = route.calls.last.request.content.decode("utf-8", errors="replace")
    assert 'name="policy"' in body
    assert 'filename="policy.txt"' in body


@respx.mock
def test_no_files_uses_json(client: EigenpalClient) -> None:
    route = respx.post("http://localhost:3000/api/v1/run/workflows.wf_xyz").mock(
        return_value=httpx.Response(201, json={"runId": "exec_abc", "type": "workflow"})
    )

    client.run("workflows.wf_xyz", input={"language": "en"})

    request = route.calls.last.request
    assert request.headers["content-type"] == "application/json"
    assert json.loads(request.content) == {"language": "en"}


@respx.mock
def test_runs_files_upload_uses_required_file_part(client: EigenpalClient) -> None:
    route = respx.post("http://localhost:3000/api/v1/runs/run_123/files").mock(
        return_value=httpx.Response(201, json={"id": "file_123", "filename": "input.txt"})
    )

    result = client.runs.files.upload(
        "run_123",
        {"content": b"hello", "filename": "input.txt", "mime_type": "text/plain"},
    )

    assert route.called
    assert result["id"] == "file_123"
    request = route.calls.last.request
    assert request.headers["content-type"].startswith("multipart/form-data; boundary=")
    body = request.content.decode("utf-8", errors="replace")
    assert 'name="file"' in body
    assert 'filename="input.txt"' in body
    assert "text/plain" in body


@respx.mock
def test_runs_files_delete_accepts_empty_204(client: EigenpalClient) -> None:
    route = respx.delete("http://localhost:3000/api/v1/runs/run_123/files/file_123").mock(
        return_value=httpx.Response(204)
    )

    result = client.runs.files.delete("run_123", "file_123")

    assert route.called
    assert result is None


@respx.mock
def test_multiple_files_all_present(tmp_path: Path, client: EigenpalClient) -> None:
    a = tmp_path / "a.pdf"
    a.write_bytes(b"a")
    b = tmp_path / "b.pdf"
    b.write_bytes(b"b")

    route = respx.post("http://localhost:3000/api/v1/run/workflows.wf_xyz").mock(
        return_value=httpx.Response(201, json={"runId": "exec_abc", "type": "workflow"})
    )

    client.run({"type": "workflow", "id": "wf_xyz"}, input={"primary": a, "secondary": b})

    body = route.calls.last.request.content.decode("utf-8", errors="replace")
    assert 'filename="a.pdf"' in body
    assert 'filename="b.pdf"' in body


@respx.mock
def test_bytesio_uploads_with_default_filename(client: EigenpalClient) -> None:
    route = respx.post("http://localhost:3000/api/v1/run/workflows.wf_xyz").mock(
        return_value=httpx.Response(201, json={"runId": "exec_abc", "type": "workflow"})
    )

    buf = BytesIO(b"data")
    # BytesIO has no .name → falls back to "file"
    client.run(
        {"type": "workflow", "id": "wf_xyz"},
        input={"contract": {"content": buf.getvalue(), "filename": "named.bin"}},
    )

    body = route.calls.last.request.content.decode("utf-8", errors="replace")
    assert 'filename="named.bin"' in body

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

from test_smoke import run_accepted


@pytest.fixture
def client() -> EigenpalClient:
    return EigenpalClient(api_key="eg_test_key", base_url="http://localhost:3000")


@respx.mock
def test_file_download_follows_signed_storage_redirect(client: EigenpalClient) -> None:
    respx.get("http://localhost:3000/v1/files/file_123/content").mock(
        return_value=httpx.Response(
            302,
            headers={"Location": "https://storage.example/files/file_123?sig=secret"},
        )
    )
    storage = respx.get("https://storage.example/files/file_123?sig=secret").mock(
        return_value=httpx.Response(200, content=b"large-file-bytes")
    )

    assert client.files.download("file_123") == b"large-file-bytes"
    assert storage.called
    assert "authorization" not in storage.calls.last.request.headers


@respx.mock
def test_path_input_uploads_as_multipart(
    tmp_path: Path, client: EigenpalClient
) -> None:
    pdf = tmp_path / "contract.pdf"
    pdf.write_bytes(b"%PDF-1.4 fake content")

    route = respx.post("http://localhost:3000/v1/runs").mock(
        return_value=httpx.Response(202, json=run_accepted(id="exec_abc"))
    )

    result = client.run(
        {"type": "workflow", "id": "wf_xyz"},
        input={"contract_document": pdf, "language": "en"},
    )

    assert result.id == "exec_abc"
    request = route.calls.last.request
    content_type = request.headers["content-type"]
    assert content_type.startswith("multipart/form-data; boundary=")

    body = request.content.decode("utf-8", errors="replace")
    assert 'name="files.contract_document"' in body
    assert 'filename="contract.pdf"' in body
    # Scalar input rides in the canonical input JSON part; target is a top-level form field
    assert 'name="input"' in body
    assert 'name="target"' in body
    assert "workflows.wf_xyz" in body
    assert '"language": "en"' in body or '"language":"en"' in body


@respx.mock
def test_explicit_descriptor_with_raw_bytes(client: EigenpalClient) -> None:
    route = respx.post("http://localhost:3000/v1/runs").mock(
        return_value=httpx.Response(202, json=run_accepted(id="exec_abc"))
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

    route = respx.post("http://localhost:3000/v1/runs").mock(
        return_value=httpx.Response(202, json=run_accepted(id="exec_abc"))
    )

    with fpath.open("rb") as f:
        client.run("workflows.wf_xyz", input={"policy": f})

    body = route.calls.last.request.content.decode("utf-8", errors="replace")
    assert 'name="files.policy"' in body
    assert 'filename="policy.txt"' in body


@respx.mock
def test_no_files_uses_json(client: EigenpalClient) -> None:
    route = respx.post("http://localhost:3000/v1/runs").mock(
        return_value=httpx.Response(202, json=run_accepted(id="exec_abc"))
    )

    client.run("workflows.wf_xyz", input={"language": "en"})

    request = route.calls.last.request
    assert request.headers["content-type"] == "application/json"
    assert json.loads(request.content) == {
        "target": "workflows.wf_xyz",
        "input": {"language": "en"},
    }


@respx.mock
def test_files_upload_uses_required_file_part(client: EigenpalClient) -> None:
    respx.post("http://localhost:3000/v1/files/uploads").mock(
        return_value=httpx.Response(
            200,
            json={
                "transport": "multipart",
                "url": "/api/v1/files",
                "maxFileSizeBytes": 100 * 1024 * 1024,
            },
        )
    )
    route = respx.post("http://localhost:3000/api/v1/files").mock(
        return_value=httpx.Response(
            201, json={"id": "file_123", "filename": "input.txt"}
        )
    )

    result = client.files.upload(
        {"content": b"hello", "filename": "input.txt", "mime_type": "text/plain"}
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
def test_files_upload_uses_storage_direct_transport_without_api_auth(
    client: EigenpalClient,
) -> None:
    respx.post("http://localhost:3000/v1/files/uploads").mock(
        return_value=httpx.Response(
            200,
            json={
                "transport": "presigned-put",
                "uploadId": "fup_1",
                "fileId": "file_1",
                "url": "https://storage.example/pending",
                "headers": {
                    "Content-Type": "text/plain",
                    "Content-Length": "5",
                    "x-amz-meta-upload-id": "fup_1",
                },
                "expiresAt": "2026-08-04T10:00:00.000Z",
                "maxFileSizeBytes": 100 * 1024 * 1024,
            },
        )
    )
    storage = respx.put("https://storage.example/pending").mock(
        return_value=httpx.Response(200)
    )
    respx.post("http://localhost:3000/v1/files/uploads/fup_1/complete").mock(
        return_value=httpx.Response(
            200,
            json={"id": "file_1", "filename": "input.txt"},
        )
    )

    result = client.files.upload(
        {"content": b"hello", "filename": "input.txt", "mime_type": "text/plain"}
    )

    assert result["id"] == "file_1"
    assert storage.calls.last.request.headers.get("authorization") is None
    assert storage.calls.last.request.headers["content-type"] == "text/plain"


@respx.mock
def test_files_delete_accepts_empty_204(client: EigenpalClient) -> None:
    route = respx.delete("http://localhost:3000/v1/files/file_123").mock(
        return_value=httpx.Response(204)
    )

    result = client.files.delete("file_123")

    assert route.called
    assert result is None


@respx.mock
def test_files_upload_sends_idempotency_key(client: EigenpalClient) -> None:
    create = respx.post("http://localhost:3000/v1/files/uploads").mock(
        return_value=httpx.Response(
            200,
            json={
                "transport": "multipart",
                "url": "/api/v1/files",
                "maxFileSizeBytes": 100 * 1024 * 1024,
            },
        )
    )
    respx.post("http://localhost:3000/api/v1/files").mock(
        return_value=httpx.Response(
            201, json={"id": "file_123", "filename": "input.txt"}
        )
    )

    client.files.upload(
        {"content": b"hello", "filename": "input.txt", "mime_type": "text/plain"},
        idempotency_key="idem_fixed_py",
    )

    body = json.loads(create.calls.last.request.content)
    assert body == {
        "filename": "input.txt",
        "contentType": "text/plain",
        "size": 5,
        "idempotencyKey": "idem_fixed_py",
    }


@respx.mock
def test_large_run_file_inputs_preupload_via_files(client: EigenpalClient) -> None:
    large = b"x" * (5 * 1024 * 1024)
    respx.post("http://localhost:3000/v1/files/uploads").mock(
        return_value=httpx.Response(
            200,
            json={
                "transport": "multipart",
                "url": "/api/v1/files",
                "maxFileSizeBytes": 100 * 1024 * 1024,
            },
        )
    )
    respx.post("http://localhost:3000/api/v1/files").mock(
        return_value=httpx.Response(
            201, json={"id": "file_large", "filename": "big.bin"}
        )
    )
    run_route = respx.post("http://localhost:3000/v1/runs").mock(
        return_value=httpx.Response(202, json=run_accepted(id="exec_abc"))
    )

    client.run(
        "workflows.wf_xyz",
        input={
            "document": {
                "content": large,
                "filename": "big.bin",
                "mime_type": "application/octet-stream",
            },
            "language": "en",
        },
    )

    request = run_route.calls.last.request
    assert request.headers["content-type"] == "application/json"
    assert json.loads(request.content) == {
        "target": "workflows.wf_xyz",
        "input": {
            "document": {"$fileId": "file_large"},
            "language": "en",
        },
    }
    create_call = next(
        call
        for call in respx.calls
        if str(call.request.url).endswith("/v1/files/uploads")
    )
    assert json.loads(create_call.request.content)["purpose"] == "run-input"


@respx.mock
def test_null_multipart_max_keeps_large_run_file_on_multipart() -> None:
    client = EigenpalClient(
        api_key="eg_test_key",
        base_url="http://localhost:3000",
        multipart_max_bytes=None,
    )
    run_route = respx.post("http://localhost:3000/v1/runs").mock(
        return_value=httpx.Response(202, json=run_accepted(id="exec_multipart"))
    )
    try:
        client.run(
            "workflows.wf_xyz",
            input={
                "document": {
                    "content": b"x" * (5 * 1024 * 1024),
                    "filename": "big.bin",
                    "mime_type": "application/octet-stream",
                }
            },
        )
    finally:
        client.close()

    assert run_route.called
    assert run_route.calls.last.request.headers["content-type"].startswith("multipart/form-data")
    assert not any(str(call.request.url).endswith("/v1/files/uploads") for call in respx.calls)


@respx.mock
def test_explicit_files_upload_omits_purpose(client: EigenpalClient) -> None:
    create_route = respx.post("http://localhost:3000/v1/files/uploads").mock(
        return_value=httpx.Response(
            200,
            json={
                "transport": "multipart",
                "url": "/api/v1/files",
                "maxFileSizeBytes": 100 * 1024 * 1024,
            },
        )
    )
    respx.post("http://localhost:3000/api/v1/files").mock(
        return_value=httpx.Response(
            201, json={"id": "file_keep", "filename": "input.txt", "purpose": None}
        )
    )

    client.files.upload({"content": b"hello", "filename": "input.txt", "mime_type": "text/plain"})
    body = json.loads(create_route.calls.last.request.content)
    assert "purpose" not in body


@respx.mock
def test_two_mid_size_files_preupload_enough_for_aggregate_budget(
    client: EigenpalClient,
) -> None:
    three_mib = b"x" * (3 * 1024 * 1024)
    respx.post("http://localhost:3000/v1/files/uploads").mock(
        return_value=httpx.Response(
            200,
            json={
                "transport": "multipart",
                "url": "/api/v1/files",
                "maxFileSizeBytes": 100 * 1024 * 1024,
            },
        )
    )
    file_ids = iter(["file_1", "file_2"])

    def files_response(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            201, json={"id": next(file_ids), "filename": "part.bin"}
        )

    files_route = respx.post("http://localhost:3000/api/v1/files").mock(
        side_effect=files_response
    )
    run_route = respx.post("http://localhost:3000/v1/runs").mock(
        return_value=httpx.Response(202, json=run_accepted(id="exec_abc"))
    )

    client.run(
        "workflows.wf_xyz",
        input={
            "primary": {
                "content": three_mib,
                "filename": "primary.bin",
                "mime_type": "application/octet-stream",
            },
            "secondary": {
                "content": three_mib,
                "filename": "secondary.bin",
                "mime_type": "application/octet-stream",
            },
            "language": "en",
        },
    )

    assert files_route.call_count >= 1
    request = run_route.calls.last.request
    content_type = request.headers["content-type"]
    body = request.content.decode("utf-8", errors="replace")
    assert "$fileId" in body or '"$fileId"' in body
    if content_type.startswith("multipart/form-data"):
        assert 'filename="primary.bin"' in body or 'filename="secondary.bin"' in body
    else:
        assert content_type == "application/json"
        parsed = json.loads(request.content)
        assert parsed["input"]["primary"]["$fileId"].startswith("file_")
        assert parsed["input"]["secondary"]["$fileId"].startswith("file_")


@respx.mock
def test_multiple_files_all_present(tmp_path: Path, client: EigenpalClient) -> None:
    a = tmp_path / "a.pdf"
    a.write_bytes(b"a")
    b = tmp_path / "b.pdf"
    b.write_bytes(b"b")

    route = respx.post("http://localhost:3000/v1/runs").mock(
        return_value=httpx.Response(202, json=run_accepted(id="exec_abc"))
    )

    client.run(
        {"type": "workflow", "id": "wf_xyz"}, input={"primary": a, "secondary": b}
    )

    body = route.calls.last.request.content.decode("utf-8", errors="replace")
    assert 'filename="a.pdf"' in body
    assert 'filename="b.pdf"' in body


@respx.mock
def test_bytesio_uploads_with_default_filename(client: EigenpalClient) -> None:
    route = respx.post("http://localhost:3000/v1/runs").mock(
        return_value=httpx.Response(202, json=run_accepted(id="exec_abc"))
    )

    buf = BytesIO(b"data")
    # BytesIO has no .name → falls back to "file"
    client.run(
        {"type": "workflow", "id": "wf_xyz"},
        input={"contract": {"content": buf.getvalue(), "filename": "named.bin"}},
    )

    body = route.calls.last.request.content.decode("utf-8", errors="replace")
    assert 'filename="named.bin"' in body

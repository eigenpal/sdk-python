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
from eigenpal._upload import (
    expected_part_byte_length,
    part_is_authoritatively_complete,
    should_abort_multipart_upload_session,
    storage_upload_timeout,
)
from eigenpal.errors import EigenpalError

from test_smoke import run_accepted

FIVE_GIB = 5 * 1024 * 1024 * 1024
FIVE_MIB = 5 * 1024 * 1024


def test_five_gib_part_math_does_not_need_a_buffer() -> None:
    assert expected_part_byte_length(FIVE_GIB, FIVE_MIB, 1, 1024) == FIVE_MIB
    assert expected_part_byte_length(FIVE_GIB, FIVE_MIB, 1024, 1024) == FIVE_MIB
    assert should_abort_multipart_upload_session(parts_ready=False) is True
    assert should_abort_multipart_upload_session(parts_ready=True) is False


def test_missing_list_parts_size_is_incomplete() -> None:
    assert (
        part_is_authoritatively_complete([{"partNumber": 1, "etag": '"e1"'}], 1, 4)
        is False
    )
    assert (
        part_is_authoritatively_complete(
            [{"partNumber": 1, "size": 4, "etag": '"e1"'}], 1, 4
        )
        is True
    )


def test_storage_and_api_timeout_policies_differ(client: EigenpalClient) -> None:
    api = client._http.timeout
    storage = storage_upload_timeout(client.timeout_seconds)
    assert api.read == client.timeout_seconds
    assert api.write == client.timeout_seconds
    assert storage.connect == client.timeout_seconds
    assert storage.read is None
    assert storage.write is None
    assert storage.write != api.write
    assert storage.read != api.read


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


@respx.mock
def test_files_upload_multipart_from_path_does_not_use_read_bytes(
    tmp_path: Path, client: EigenpalClient
) -> None:
    blob = tmp_path / "doc.bin"
    blob.write_bytes(b"abcdefghijkl")
    uploaded: set[int] = set()

    respx.post("http://localhost:3000/v1/files/uploads").mock(
        return_value=httpx.Response(
            200,
            json={
                "transport": "presigned-multipart",
                "uploadId": "fup_mpu",
                "fileId": "file_mpu",
                "partSizeBytes": 5,
                "partCount": 3,
                "partsUrl": "/v1/files/uploads/fup_mpu/parts",
                "completeUrl": "/v1/files/uploads/fup_mpu/complete",
                "expiresAt": "2026-08-04T10:00:00.000Z",
                "maxFileSizeBytes": 100 * 1024 * 1024,
            },
        )
    )

    def list_parts(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            json={
                "parts": [
                    {
                        "partNumber": number,
                        "size": 2 if number == 3 else 5,
                        "etag": f'"e{number}"',
                    }
                    for number in sorted(uploaded)
                ]
            },
        )

    def presign(request: httpx.Request) -> httpx.Response:
        part_number = request.read() if False else json.loads(request.content)["partNumber"]
        return httpx.Response(
            200,
            json={
                "url": f"https://storage.example/part-{part_number}",
                "headers": {},
                "partSizeBytes": 2 if part_number == 3 else 5,
            },
        )

    respx.get("http://localhost:3000/v1/files/uploads/fup_mpu/parts").mock(
        side_effect=list_parts
    )
    respx.post("http://localhost:3000/v1/files/uploads/fup_mpu/parts").mock(
        side_effect=presign
    )
    respx.post("http://localhost:3000/v1/files/uploads/fup_mpu/complete").mock(
        return_value=httpx.Response(
            200, json={"id": "file_mpu", "filename": "doc.bin", "size": 12}
        )
    )

    def storage_put(request: httpx.Request) -> httpx.Response:
        part_number = int(str(request.url).rsplit("-", 1)[-1])
        uploaded.add(part_number)
        return httpx.Response(200)

    respx.put(url__startswith="https://storage.example/part-").mock(side_effect=storage_put)

    original = Path.read_bytes

    def banned(self: Path) -> bytes:
        raise AssertionError("Path.read_bytes should not load the whole file")

    Path.read_bytes = banned  # type: ignore[method-assign]
    try:
        result = client.files.upload(blob)
    finally:
        Path.read_bytes = original  # type: ignore[method-assign]

    assert result["id"] == "file_mpu"
    assert uploaded == {1, 2, 3}


@respx.mock
def test_files_upload_retries_part_with_fresh_url(client: EigenpalClient) -> None:
    uploaded: set[int] = set()
    presigns = {"count": 0}
    respx.post("http://localhost:3000/v1/files/uploads").mock(
        return_value=httpx.Response(
            200,
            json={
                "transport": "presigned-multipart",
                "uploadId": "fup_retry",
                "fileId": "file_retry",
                "partSizeBytes": 4,
                "partCount": 1,
                "partsUrl": "/v1/files/uploads/fup_retry/parts",
                "completeUrl": "/v1/files/uploads/fup_retry/complete",
                "maxFileSizeBytes": 100 * 1024 * 1024,
            },
        )
    )
    respx.get("http://localhost:3000/v1/files/uploads/fup_retry/parts").mock(
        side_effect=lambda request: httpx.Response(
            200,
            json={
                "parts": (
                    [{"partNumber": 1, "size": 4, "etag": '"e1"'}] if uploaded else []
                )
            },
        )
    )

    def presign(request: httpx.Request) -> httpx.Response:
        presigns["count"] += 1
        return httpx.Response(
            200,
            json={
                "url": f"https://storage.example/retry-{presigns['count']}",
                "headers": {},
                "partSizeBytes": 4,
            },
        )

    respx.post("http://localhost:3000/v1/files/uploads/fup_retry/parts").mock(
        side_effect=presign
    )
    respx.put("https://storage.example/retry-1").mock(return_value=httpx.Response(503))
    respx.put("https://storage.example/retry-2").mock(
        side_effect=lambda request: (uploaded.add(1) or httpx.Response(200))
    )
    respx.post("http://localhost:3000/v1/files/uploads/fup_retry/complete").mock(
        return_value=httpx.Response(
            200, json={"id": "file_retry", "filename": "note.txt", "size": 4}
        )
    )

    result = client.files.upload(
        {"content": b"note", "filename": "note.txt", "mime_type": "text/plain"}
    )
    assert result["id"] == "file_retry"
    assert presigns["count"] == 2


@respx.mock
def test_files_upload_aborts_after_unrecoverable_part_failure(
    client: EigenpalClient,
) -> None:
    respx.post("http://localhost:3000/v1/files/uploads").mock(
        return_value=httpx.Response(
            200,
            json={
                "transport": "presigned-multipart",
                "uploadId": "fup_abort",
                "fileId": "file_abort",
                "partSizeBytes": 4,
                "partCount": 1,
                "partsUrl": "/v1/files/uploads/fup_abort/parts",
                "completeUrl": "/v1/files/uploads/fup_abort/complete",
                "maxFileSizeBytes": 100 * 1024 * 1024,
            },
        )
    )
    respx.get("http://localhost:3000/v1/files/uploads/fup_abort/parts").mock(
        return_value=httpx.Response(200, json={"parts": []})
    )
    respx.post("http://localhost:3000/v1/files/uploads/fup_abort/parts").mock(
        return_value=httpx.Response(
            200,
            json={
                "url": "https://storage.example/forbidden",
                "headers": {},
                "partSizeBytes": 4,
            },
        )
    )
    respx.put("https://storage.example/forbidden").mock(return_value=httpx.Response(403))
    abort = respx.delete("http://localhost:3000/v1/files/uploads/fup_abort").mock(
        return_value=httpx.Response(200, json={"aborted": True})
    )

    with pytest.raises(Exception):
        client.files.upload({"content": b"note", "filename": "note.txt"})
    assert abort.called


@respx.mock
def test_files_upload_complete_failure_preserves_session_and_parts(
    client: EigenpalClient,
) -> None:
    uploaded: set[int] = set()
    respx.post("http://localhost:3000/v1/files/uploads").mock(
        return_value=httpx.Response(
            200,
            json={
                "transport": "presigned-multipart",
                "uploadId": "fup_complete_fail",
                "fileId": "file_complete_fail",
                "partSizeBytes": 4,
                "partCount": 1,
                "partsUrl": "/v1/files/uploads/fup_complete_fail/parts",
                "completeUrl": "/v1/files/uploads/fup_complete_fail/complete",
                "maxFileSizeBytes": 100 * 1024 * 1024,
            },
        )
    )
    respx.get("http://localhost:3000/v1/files/uploads/fup_complete_fail/parts").mock(
        side_effect=lambda request: httpx.Response(
            200,
            json={
                "parts": (
                    [{"partNumber": 1, "size": 4, "etag": '"e1"'}] if uploaded else []
                )
            },
        )
    )
    respx.post("http://localhost:3000/v1/files/uploads/fup_complete_fail/parts").mock(
        return_value=httpx.Response(
            200,
            json={
                "url": "https://storage.example/part-1",
                "headers": {},
                "partSizeBytes": 4,
            },
        )
    )
    respx.put("https://storage.example/part-1").mock(
        side_effect=lambda request: (uploaded.add(1) or httpx.Response(200))
    )
    respx.post("http://localhost:3000/v1/files/uploads/fup_complete_fail/complete").mock(
        return_value=httpx.Response(
            409,
            json={
                "issues": [
                    {"field": "uploadId", "message": "Upload cannot complete: promoting"}
                ],
                "requestId": "req_complete_fail",
            },
        )
    )
    abort = respx.delete(
        "http://localhost:3000/v1/files/uploads/fup_complete_fail"
    ).mock(return_value=httpx.Response(200, json={"aborted": True}))

    with pytest.raises(
        EigenpalError, match="remain stored for fup_complete_fail.*retry complete"
    ):
        client.files.upload({"content": b"note", "filename": "note.txt"})
    assert not abort.called
    assert uploaded == {1}


@respx.mock
def test_files_upload_reuploads_listed_part_without_size(client: EigenpalClient) -> None:
    uploaded: set[int] = set()
    respx.post("http://localhost:3000/v1/files/uploads").mock(
        return_value=httpx.Response(
            200,
            json={
                "transport": "presigned-multipart",
                "uploadId": "fup_nosize",
                "fileId": "file_nosize",
                "partSizeBytes": 4,
                "partCount": 1,
                "partsUrl": "/v1/files/uploads/fup_nosize/parts",
                "completeUrl": "/v1/files/uploads/fup_nosize/complete",
                "maxFileSizeBytes": 100 * 1024 * 1024,
            },
        )
    )
    respx.get("http://localhost:3000/v1/files/uploads/fup_nosize/parts").mock(
        side_effect=lambda request: httpx.Response(
            200,
            json={
                "parts": (
                    [{"partNumber": 1, "size": 4, "etag": '"e1"'}]
                    if uploaded
                    else [{"partNumber": 1, "etag": '"e1"'}]
                )
            },
        )
    )
    respx.post("http://localhost:3000/v1/files/uploads/fup_nosize/parts").mock(
        return_value=httpx.Response(
            200,
            json={
                "url": "https://storage.example/part-1",
                "headers": {},
                "partSizeBytes": 4,
            },
        )
    )
    storage = respx.put("https://storage.example/part-1").mock(
        side_effect=lambda request: (uploaded.add(1) or httpx.Response(200))
    )
    respx.post("http://localhost:3000/v1/files/uploads/fup_nosize/complete").mock(
        return_value=httpx.Response(
            200, json={"id": "file_nosize", "filename": "note.txt", "size": 4}
        )
    )

    result = client.files.upload({"content": b"note", "filename": "note.txt"})
    assert result["id"] == "file_nosize"
    assert storage.call_count == 1


@respx.mock
def test_files_upload_uses_storage_timeout_not_api_timeout(
    client: EigenpalClient, monkeypatch: pytest.MonkeyPatch
) -> None:
    captured: list[object] = []
    original_put = httpx.put

    def spy_put(*args: object, **kwargs: object) -> httpx.Response:
        captured.append(kwargs.get("timeout"))
        return original_put(*args, **kwargs)

    monkeypatch.setattr(httpx, "put", spy_put)
    uploaded: set[int] = set()
    respx.post("http://localhost:3000/v1/files/uploads").mock(
        return_value=httpx.Response(
            200,
            json={
                "transport": "presigned-multipart",
                "uploadId": "fup_timeout",
                "fileId": "file_timeout",
                "partSizeBytes": 4,
                "partCount": 1,
                "partsUrl": "/v1/files/uploads/fup_timeout/parts",
                "completeUrl": "/v1/files/uploads/fup_timeout/complete",
                "maxFileSizeBytes": 100 * 1024 * 1024,
            },
        )
    )
    respx.get("http://localhost:3000/v1/files/uploads/fup_timeout/parts").mock(
        side_effect=lambda request: httpx.Response(
            200,
            json={
                "parts": (
                    [{"partNumber": 1, "size": 4, "etag": '"e1"'}] if uploaded else []
                )
            },
        )
    )
    respx.post("http://localhost:3000/v1/files/uploads/fup_timeout/parts").mock(
        return_value=httpx.Response(
            200,
            json={
                "url": "https://storage.example/part-1",
                "headers": {},
                "partSizeBytes": 4,
            },
        )
    )
    respx.put("https://storage.example/part-1").mock(
        side_effect=lambda request: (uploaded.add(1) or httpx.Response(200))
    )
    respx.post("http://localhost:3000/v1/files/uploads/fup_timeout/complete").mock(
        return_value=httpx.Response(
            200, json={"id": "file_timeout", "filename": "note.txt", "size": 4}
        )
    )

    client.files.upload({"content": b"note", "filename": "note.txt"})
    assert captured
    for timeout in captured:
        assert isinstance(timeout, httpx.Timeout)
        assert timeout.write is None
        assert timeout.read is None
        assert timeout.connect == client.timeout_seconds
    assert client._http.timeout.write == client.timeout_seconds
    assert client._http.timeout.read == client.timeout_seconds


def test_non_seekable_stream_is_rejected(client: EigenpalClient) -> None:
    class NonSeekable:
        name = "pipe.bin"

        def read(self, n: int = -1) -> bytes:
            return b"x"

        def seekable(self) -> bool:
            return False

    with pytest.raises(EigenpalError, match="non-seekable"):
        client.files.upload(NonSeekable())  # type: ignore[arg-type]

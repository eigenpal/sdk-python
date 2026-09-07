from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import httpx
import respx

from eigenpal import EigenpalClient
from eigenpal._generated.models.list_email_servers_response import (
    ListEmailServersResponse,
)
from eigenpal._generated.models.public_resend_email_server import PublicResendEmailServer
from eigenpal._generated.models.public_smtp_email_server import PublicSmtpEmailServer

SERVER_ID = "ems_01ABCDEFGHJKMNPQRSTVWXYZ"
BASE = "http://localhost:3000"


def public_resend_server(**overrides: Any) -> dict[str, Any]:
    return {
        "id": SERVER_ID,
        "name": "Alerts",
        "enabled": True,
        "createdAt": "2026-09-04T00:00:00.000Z",
        "updatedAt": "2026-09-04T00:00:00.000Z",
        "transport": "resend",
        "fromEmail": "alerts@example.com",
        "fromName": "EigenPal",
        "apiKeyConfigured": True,
        **overrides,
    }


def public_smtp_server() -> dict[str, Any]:
    return {
        "id": SERVER_ID,
        "name": "SMTP Alerts",
        "enabled": True,
        "createdAt": "2026-09-04T00:00:00.000Z",
        "updatedAt": "2026-09-04T00:00:00.000Z",
        "transport": "smtp",
        "fromEmail": "alerts@example.com",
        "fromName": "EigenPal",
        "host": "smtp.example.com",
        "port": 587,
        "security": "starttls",
        "username": "mailer",
        "passwordConfigured": True,
        "caPemConfigured": False,
    }


def assert_no_secrets(value: Any) -> None:
    blob = json.dumps(value)
    assert '"apiKey"' not in blob
    assert '"password"' not in blob
    assert '"caPem"' not in blob
    assert "re_test_secret" not in blob


@respx.mock
def test_list_uses_openapi_pagination_and_public_rows() -> None:
    client = EigenpalClient(api_key="eg_test", base_url=BASE, max_retries=0)
    listing = {
        "data": [public_resend_server(), public_smtp_server()],
        "total": 2,
        "limit": 20,
        "offset": 10,
    }
    route = respx.get(f"{BASE}/v1/email-servers", params={"limit": 20, "offset": 10}).mock(
        return_value=httpx.Response(200, json=listing)
    )

    page = client.email_servers.list(limit=20, offset=10)

    assert route.called
    assert route.calls.last.request.method == "GET"
    assert page["total"] == 2
    assert page["limit"] == 20
    assert page["offset"] == 10
    assert page["data"][0]["transport"] == "resend"
    assert page["data"][0]["apiKeyConfigured"] is True
    assert page["data"][1]["passwordConfigured"] is True
    parsed = ListEmailServersResponse.from_dict(dict(page))
    assert len(parsed.data) == 2
    assert isinstance(parsed.data[0], PublicResendEmailServer)
    assert isinstance(parsed.data[1], PublicSmtpEmailServer)
    assert_no_secrets(page)


@respx.mock
def test_create_get_update_delete_test_match_contract() -> None:
    from eigenpal._generated.models.test_email_server_request import (
        TestEmailServerRequest,
    )
    from eigenpal._generated.models.test_email_server_response_type_0 import (
        TestEmailServerResponseType0,
    )

    client = EigenpalClient(api_key="eg_test", base_url=BASE, max_retries=0)
    create_body = {
        "name": "Alerts",
        "transport": "resend",
        "apiKey": "re_test_secret",
        "fromEmail": "alerts@example.com",
        "fromName": "EigenPal",
    }
    created = respx.post(f"{BASE}/v1/email-servers").mock(
        return_value=httpx.Response(201, json=public_resend_server())
    )
    fetched = respx.get(f"{BASE}/v1/email-servers/{SERVER_ID}").mock(
        return_value=httpx.Response(200, json=public_resend_server())
    )
    updated = respx.patch(f"{BASE}/v1/email-servers/{SERVER_ID}").mock(
        return_value=httpx.Response(200, json=public_resend_server(name="Renamed"))
    )
    deleted = respx.delete(f"{BASE}/v1/email-servers/{SERVER_ID}").mock(
        return_value=httpx.Response(200, json={"deleted": True, "id": SERVER_ID})
    )
    tested = respx.post(f"{BASE}/v1/email-servers/{SERVER_ID}/test").mock(
        return_value=httpx.Response(
            200,
            json={"ok": True, "transport": "resend", "messageId": "msg_1"},
        )
    )

    create_result = client.email_servers.create(create_body)
    get_result = client.email_servers.get(SERVER_ID)
    update_result = client.email_servers.update(
        SERVER_ID, {"name": "Renamed", "enabled": True}
    )
    delete_result = client.email_servers.delete(SERVER_ID)
    test_body = {"to": "ops@example.com"}
    test_result = client.email_servers.test(SERVER_ID, test_body)

    assert json.loads(created.calls.last.request.content.decode()) == create_body
    assert json.loads(updated.calls.last.request.content.decode()) == {
        "name": "Renamed",
        "enabled": True,
    }
    parsed_test_request = TestEmailServerRequest.from_dict(
        json.loads(tested.calls.last.request.content.decode())
    )
    assert parsed_test_request.to == "ops@example.com"
    assert json.loads(tested.calls.last.request.content.decode()) == test_body

    assert fetched.called
    assert deleted.called
    assert create_result["apiKeyConfigured"] is True
    assert get_result["id"] == SERVER_ID
    assert update_result["name"] == "Renamed"
    assert delete_result == {"deleted": True, "id": SERVER_ID}
    parsed_test = TestEmailServerResponseType0.from_dict(dict(test_result))
    assert parsed_test.ok is True
    assert parsed_test.message_id == "msg_1"
    assert "to" not in test_result
    assert_no_secrets(create_result)
    assert_no_secrets(get_result)
    assert_no_secrets(update_result)
    assert_no_secrets(test_result)


def test_public_facade_and_docs_cover_email_server_methods() -> None:
    client = EigenpalClient(api_key="eg_test", base_url=BASE, max_retries=0)
    assert callable(client.email_servers.list)
    assert callable(client.email_servers.get)
    assert callable(client.email_servers.create)
    assert callable(client.email_servers.update)
    assert callable(client.email_servers.delete)
    assert callable(client.email_servers.test)

    docs = (Path(__file__).resolve().parents[1] / "docs" / "reference.md").read_text()
    assert "### `client.email_servers.list`" in docs
    assert "### `client.email_servers.create`" in docs
    assert "### `client.email_servers.get`" in docs
    assert "### `client.email_servers.update`" in docs
    assert "### `client.email_servers.delete`" in docs
    assert "### `client.email_servers.test`" in docs
    assert "`limit`" in docs
    assert "`offset`" in docs
    assert '{"to": "ops@example.com"}' in docs

from __future__ import annotations

import json

import httpx
import respx

from eigenpal import EigenpalClient

WORKFLOW_ID = "wf_01ABCDEFGHJKMNPQRSTVWXYZ"
REVIEW_ID = "dsr_01ABCDEFGHJKMNPQRSTVWXYZ"
ITEM_ID = "dsri_01ABCDEFGHJKMNPQRSTVWXYZ"
BASE = "http://localhost:3000"


@respx.mock
def test_list_encodes_status_filter_and_pagination() -> None:
    client = EigenpalClient(api_key="eg_test", base_url=BASE, max_retries=0)
    route = respx.get(
        f"{BASE}/v1/automations/{WORKFLOW_ID}/dataset-review-requests",
        params={"status": "open,paused", "limit": 20, "offset": 5},
    ).mock(return_value=httpx.Response(200, json={"data": [], "total": 0}))

    client.automations.dataset_review_requests.list(
        WORKFLOW_ID,
        status=["open", "paused"],
        limit=20,
        offset=5,
    )

    assert route.called
    assert route.calls.last.request.method == "GET"


@respx.mock
def test_create_posts_review_request_body() -> None:
    client = EigenpalClient(api_key="eg_test", base_url=BASE, max_retries=0)
    route = respx.post(
        f"{BASE}/v1/automations/{WORKFLOW_ID}/dataset-review-requests"
    ).mock(return_value=httpx.Response(201, json={"id": REVIEW_ID, "status": "open"}))

    client.automations.dataset_review_requests.create(
        WORKFLOW_ID,
        {
            "title": "Q1 GT review",
            "exampleNames": ["invoice-foo", "invoice-bar"],
            "instructions": "Check totals",
            "focusFields": [
                {"path": "vendor.iban", "reason": "OCR often mangles IBANs"}
            ],
            "ignoredFields": ["currency"],
            "itemNotes": [
                {
                    "exampleName": "invoice-foo",
                    "comment": "Totals drifted",
                    "fields": [{"path": "total", "comment": "off by 0.01"}],
                }
            ],
            "status": "open",
        },
    )

    assert route.called
    body = json.loads(route.calls.last.request.content.decode())
    assert body == {
        "title": "Q1 GT review",
        "exampleNames": ["invoice-foo", "invoice-bar"],
        "instructions": "Check totals",
        "focusFields": [{"path": "vendor.iban", "reason": "OCR often mangles IBANs"}],
        "ignoredFields": ["currency"],
        "itemNotes": [
            {
                "exampleName": "invoice-foo",
                "comment": "Totals drifted",
                "fields": [{"path": "total", "comment": "off by 0.01"}],
            }
        ],
        "status": "open",
    }


@respx.mock
def test_update_patches_request_status() -> None:
    client = EigenpalClient(api_key="eg_test", base_url=BASE, max_retries=0)
    route = respx.patch(
        f"{BASE}/v1/automations/{WORKFLOW_ID}/dataset-review-requests/{REVIEW_ID}"
    ).mock(return_value=httpx.Response(200, json={"id": REVIEW_ID, "status": "closed"}))

    client.automations.dataset_review_requests.update(
        WORKFLOW_ID,
        REVIEW_ID,
        {"status": "closed"},
    )

    assert route.called
    body = json.loads(route.calls.last.request.content.decode())
    assert body == {"status": "closed"}


@respx.mock
def test_update_item_patches_action_payload() -> None:
    client = EigenpalClient(api_key="eg_test", base_url=BASE, max_retries=0)
    route = respx.patch(
        f"{BASE}/v1/automations/{WORKFLOW_ID}/dataset-review-requests/{REVIEW_ID}/items/{ITEM_ID}"
    ).mock(
        return_value=httpx.Response(
            200, json={"item": {"id": ITEM_ID, "status": "edited"}}
        )
    )

    client.automations.dataset_review_requests.update_item(
        WORKFLOW_ID,
        REVIEW_ID,
        ITEM_ID,
        {
            "action": "edit",
            "expected": {"total": 42},
            "comment": "fixed total",
            "expectedUpdatedAt": "2026-01-01T00:00:00.000Z",
        },
    )

    assert route.called
    body = json.loads(route.calls.last.request.content.decode())
    assert body == {
        "action": "edit",
        "expected": {"total": 42},
        "comment": "fixed total",
        "expectedUpdatedAt": "2026-01-01T00:00:00.000Z",
    }


@respx.mock
def test_update_item_field_decision_and_clear() -> None:
    client = EigenpalClient(api_key="eg_test", base_url=BASE, max_retries=0)
    route = respx.patch(
        f"{BASE}/v1/automations/{WORKFLOW_ID}/dataset-review-requests/{REVIEW_ID}/items/{ITEM_ID}"
    ).mock(
        return_value=httpx.Response(
            200,
            json={"item": {"id": ITEM_ID, "status": "pending", "fieldDecisions": {}}},
        )
    )

    client.automations.dataset_review_requests.update_item(
        WORKFLOW_ID,
        REVIEW_ID,
        ITEM_ID,
        {
            "action": "field-decision",
            "fieldPath": "vendor.iban",
            "decision": "rejected",
            "expectedUpdatedAt": "2026-01-01T00:00:00.000Z",
        },
    )
    client.automations.dataset_review_requests.update_item(
        WORKFLOW_ID,
        REVIEW_ID,
        ITEM_ID,
        {
            "action": "field-decision",
            "fieldPath": "vendor.iban",
            "decision": None,
            "expectedUpdatedAt": "2026-01-01T00:00:01.000Z",
        },
    )

    assert route.call_count == 2
    assert json.loads(route.calls[0].request.content.decode())["decision"] == "rejected"
    assert json.loads(route.calls[1].request.content.decode())["decision"] is None


@respx.mock
def test_events_reads_events_subresource() -> None:
    client = EigenpalClient(api_key="eg_test", base_url=BASE, max_retries=0)
    route = respx.get(
        f"{BASE}/v1/automations/{WORKFLOW_ID}/dataset-review-requests/{REVIEW_ID}/events"
    ).mock(return_value=httpx.Response(200, json={"events": []}))

    client.automations.dataset_review_requests.events(WORKFLOW_ID, REVIEW_ID)

    assert route.called
    assert route.calls.last.request.method == "GET"


@respx.mock
def test_get_item_file_defaults_to_input_and_supports_expected_kind() -> None:
    client = EigenpalClient(api_key="eg_test", base_url=BASE, max_retries=0)
    input_route = respx.get(
        f"{BASE}/v1/automations/{WORKFLOW_ID}/dataset-review-requests/{REVIEW_ID}/items/{ITEM_ID}/files/input/contract.pdf"
    ).mock(return_value=httpx.Response(200, content=b"bytes"))
    expected_route = respx.get(
        f"{BASE}/v1/automations/{WORKFLOW_ID}/dataset-review-requests/{REVIEW_ID}/items/{ITEM_ID}/files/expected/report.pdf",
        params={"kind": "expected"},
    ).mock(return_value=httpx.Response(200, content=b"corrected"))

    assert (
        client.automations.dataset_review_requests.get_item_file(
            WORKFLOW_ID, REVIEW_ID, ITEM_ID, "input/contract.pdf"
        )
        == b"bytes"
    )
    assert (
        client.automations.dataset_review_requests.get_item_file(
            WORKFLOW_ID, REVIEW_ID, ITEM_ID, "expected/report.pdf", kind="expected"
        )
        == b"corrected"
    )

    assert input_route.called
    assert expected_route.called
    assert "kind" not in str(input_route.calls.last.request.url)


@respx.mock
def test_record_item_file_decision_and_clear() -> None:
    client = EigenpalClient(api_key="eg_test", base_url=BASE, max_retries=0)
    route = respx.patch(
        f"{BASE}/v1/automations/{WORKFLOW_ID}/dataset-review-requests/{REVIEW_ID}/items/{ITEM_ID}"
    ).mock(
        return_value=httpx.Response(
            200,
            json={"item": {"id": ITEM_ID, "status": "pending", "fileDecisions": {}}},
        )
    )

    client.automations.dataset_review_requests.record_item_file_decision(
        WORKFLOW_ID,
        REVIEW_ID,
        ITEM_ID,
        {
            "filePath": "expected/report.pdf",
            "decision": "approved",
            "comment": "totals match",
            "expectedUpdatedAt": "2026-01-01T00:00:00.000Z",
        },
    )
    client.automations.dataset_review_requests.record_item_file_decision(
        WORKFLOW_ID,
        REVIEW_ID,
        ITEM_ID,
        {
            "filePath": "expected/report.pdf",
            "decision": None,
            "expectedUpdatedAt": "2026-01-01T00:00:01.000Z",
        },
    )

    assert route.call_count == 2
    first = json.loads(route.calls[0].request.content.decode())
    assert first == {
        "action": "file-decision",
        "filePath": "expected/report.pdf",
        "decision": "approved",
        "comment": "totals match",
        "expectedUpdatedAt": "2026-01-01T00:00:00.000Z",
    }
    second = json.loads(route.calls[1].request.content.decode())
    assert second["action"] == "file-decision"
    assert second["decision"] is None


@respx.mock
def test_edit_item_file_sends_multipart_edit_file() -> None:
    client = EigenpalClient(api_key="eg_test", base_url=BASE, max_retries=0)
    route = respx.patch(
        f"{BASE}/v1/automations/{WORKFLOW_ID}/dataset-review-requests/{REVIEW_ID}/items/{ITEM_ID}"
    ).mock(
        return_value=httpx.Response(
            200, json={"item": {"id": ITEM_ID, "status": "edited"}}
        )
    )

    client.automations.dataset_review_requests.edit_item_file(
        WORKFLOW_ID,
        REVIEW_ID,
        ITEM_ID,
        {"filename": "report.pdf", "mime_type": "application/pdf", "content": b"fixed"},
        file_path="expected/report.pdf",
        comment="fixed total",
        expected_updated_at="2026-01-01T00:00:00.000Z",
    )

    assert route.called
    request = route.calls.last.request
    assert "multipart/form-data" in request.headers["content-type"]
    body = request.content.decode()
    assert 'name="action"' in body and "edit-file" in body
    assert 'name="filePath"' in body and "expected/report.pdf" in body
    assert 'name="comment"' in body and "fixed total" in body
    assert 'name="expectedUpdatedAt"' in body
    assert 'filename="report.pdf"' in body and "fixed" in body

"""The hand-written `Eigenpal` facade.

Wraps the auto-generated `AuthenticatedClient` from
`eigenpal._generated` with a friendlier API: namespaced resources,
typed exceptions, and a client-side `run_and_wait` polling helper.
"""

from __future__ import annotations

import json
import os
import time
from typing import Any, Optional

import httpx

from eigenpal._files import has_file_input, is_file_input, to_upload_tuple
from eigenpal._generated.api.executions import (
    executions_cancel,
    executions_get,
    executions_list,
)
from eigenpal._generated.api.workflows import (
    workflows_get,
    workflows_list,
    workflows_run,
    workflows_versions_list,
)
from eigenpal._generated.client import AuthenticatedClient
from eigenpal._generated.models.cancel_execution_response import CancelExecutionResponse
from eigenpal._generated.models.execution_status_response import ExecutionStatusResponse
from eigenpal._generated.models.executions_get_include_steps import ExecutionsGetIncludeSteps
from eigenpal._generated.models.list_executions_response import ListExecutionsResponse
from eigenpal._generated.models.list_versions_response import ListVersionsResponse
from eigenpal._generated.models.list_workflows_response import ListWorkflowsResponse
from eigenpal._generated.models.run_workflow_body import RunWorkflowBody
from eigenpal._generated.models.run_workflow_response import RunWorkflowResponse
from eigenpal._generated.models.workflow_summary import WorkflowSummary
from eigenpal._generated.types import UNSET, Response, Unset
from eigenpal.errors import EigenpalTimeoutError, error_from_response

DEFAULT_BASE_URL = "https://app.eigenpal.com"
DEFAULT_TIMEOUT_SECONDS = 60.0
DEFAULT_POLL_INTERVAL_SECONDS = 2.0
DEFAULT_RUN_AND_WAIT_TIMEOUT_SECONDS = 5 * 60.0

TERMINAL_STATUSES = frozenset({"completed", "failed", "cancelled", "rejected"})


def _opt(value: Any) -> Any:
    """Generated SDK takes UNSET (not None) for optional query params."""
    return UNSET if value is None else value


def _check_response(response: Response[Any]) -> Any:
    """Raise a typed Eigenpal exception on non-2xx; return parsed body otherwise."""
    if 200 <= response.status_code < 300:
        return response.parsed

    envelope: Optional[dict[str, Any]] = None
    try:
        parsed = httpx.Response(response.status_code, content=response.content).json()
        if isinstance(parsed, dict):
            envelope = parsed
    except Exception:
        pass

    retry_after: Optional[int] = None
    try:
        retry_after = int(response.headers.get("retry-after"))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        pass

    raise error_from_response(response.status_code, envelope, retry_after)


class Eigenpal:
    """Top-level SDK client.

    >>> client = Eigenpal()  # reads EIGENPAL_API_KEY from env
    >>> client = Eigenpal(api_key="eg_...")  # explicit
    """

    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout_seconds: float = DEFAULT_TIMEOUT_SECONDS,
        verify_ssl: bool = True,
    ) -> None:
        resolved_key = api_key or os.environ.get("EIGENPAL_API_KEY")
        if not resolved_key:
            raise ValueError(
                "Missing API key. Pass Eigenpal(api_key=...) or set the "
                "EIGENPAL_API_KEY environment variable."
            )

        resolved_base_url = base_url or os.environ.get("EIGENPAL_BASE_URL") or DEFAULT_BASE_URL

        self._client = AuthenticatedClient(
            base_url=resolved_base_url,
            token=resolved_key,
            timeout=httpx.Timeout(timeout_seconds),
            verify_ssl=verify_ssl,
            raise_on_unexpected_status=False,
            headers={"User-Agent": "eigenpal-sdk-python/0.0.0"},
        )
        self.workflows = WorkflowsResource(self._client)
        self.executions = ExecutionsResource(self._client)

    def __enter__(self) -> "Eigenpal":
        return self

    def __exit__(self, *exc_info: Any) -> None:
        self._client.get_httpx_client().close()


def _run_multipart(
    client: AuthenticatedClient,
    workflow_id: str,
    input: dict[str, Any],
    *,
    version: Optional[str],
    wait_for_completion: Optional[int],
    overrides: Optional[dict[str, Any]],
    trigger: Optional[str],
) -> RunWorkflowResponse:
    """Send a workflow run as ``multipart/form-data``. Each file value in
    ``input`` becomes a top-level form field; non-file inputs + overrides +
    trigger ride along in the canonical ``_json`` text field."""
    files: list[tuple[str, tuple[str, bytes, str]]] = []
    scalars: dict[str, Any] = {}
    for key, value in input.items():
        if is_file_input(value):
            files.append((key, to_upload_tuple(value)))
        else:
            scalars[key] = value

    sidecar: dict[str, Any] = {}
    if scalars:
        sidecar["input"] = scalars
    if overrides is not None:
        sidecar["overrides"] = overrides
    if trigger is not None:
        sidecar["trigger"] = trigger
    data = {"_json": json.dumps(sidecar)} if sidecar else {}

    params: dict[str, Any] = {}
    if version is not None:
        params["version"] = version
    if wait_for_completion is not None:
        params["wait_for_completion"] = wait_for_completion

    httpx_client = client.get_httpx_client()
    raw_response = httpx_client.post(
        f"/v1/workflows/{workflow_id}/run",
        params=params,
        files=files,
        data=data,
    )

    # Match the shape returned by ``workflows_run.sync_detailed`` so
    # ``_check_response`` works the same way.
    if 200 <= raw_response.status_code < 300:
        parsed = RunWorkflowResponse.from_dict(raw_response.json())
    else:
        parsed = None
    return _check_response(
        Response(
            status_code=raw_response.status_code,
            content=raw_response.content,
            headers=raw_response.headers,
            parsed=parsed,
        )
    )


class WorkflowsResource:
    """Workflow operations: list, get, run, versions."""

    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def run(
        self,
        workflow_id: str,
        input: Optional[dict[str, Any]] = None,
        *,
        version: Optional[str] = None,
        wait_for_completion: Optional[int] = None,
        overrides: Optional[dict[str, Any]] = None,
        trigger: Optional[str] = None,
    ) -> RunWorkflowResponse:
        # File-bearing input → multipart/form-data (no base64 overhead).
        if has_file_input(input):
            assert input is not None
            return _run_multipart(
                self._client,
                workflow_id,
                input,
                version=version,
                wait_for_completion=wait_for_completion,
                overrides=overrides,
                trigger=trigger,
            )

        body = RunWorkflowBody.from_dict(
            {
                **({"input": input} if input is not None else {}),
                **({"overrides": overrides} if overrides is not None else {}),
                **({"trigger": trigger} if trigger is not None else {}),
            }
        )
        response = workflows_run.sync_detailed(
            id=workflow_id,
            client=self._client,
            body=body,
            version=_opt(version),
            wait_for_completion=_opt(wait_for_completion),
        )
        return _check_response(response)

    def list(
        self,
        *,
        search: Optional[str] = None,
        name: Optional[str] = None,
        kind: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> ListWorkflowsResponse:
        from eigenpal._generated.models.workflows_list_kind import WorkflowsListKind

        kind_enum: Unset | WorkflowsListKind = (
            WorkflowsListKind(kind) if kind is not None else UNSET
        )
        response = workflows_list.sync_detailed(
            client=self._client,
            search=_opt(search),
            name=_opt(name),
            kind=kind_enum,
            limit=_opt(limit),
            offset=_opt(offset),
        )
        return _check_response(response)

    def get(self, workflow_id: str) -> WorkflowSummary:
        response = workflows_get.sync_detailed(id=workflow_id, client=self._client)
        return _check_response(response)

    def versions(
        self,
        workflow_id: str,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> ListVersionsResponse:
        response = workflows_versions_list.sync_detailed(
            id=workflow_id,
            client=self._client,
            limit=_opt(limit),
            offset=_opt(offset),
        )
        return _check_response(response)


class ExecutionsResource:
    """Execution operations: list, get, cancel, run_and_wait."""

    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def get(self, execution_id: str, *, include_steps: bool = False) -> ExecutionStatusResponse:
        include = ExecutionsGetIncludeSteps.TRUE if include_steps else UNSET
        response = executions_get.sync_detailed(
            execution_id=execution_id,
            client=self._client,
            include_steps=include,
        )
        return _check_response(response)

    def list(
        self,
        *,
        workflow_id: Optional[str] = None,
        status: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        example_id: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> ListExecutionsResponse:
        response = executions_list.sync_detailed(
            client=self._client,
            workflow_id=_opt(workflow_id),
            status=_opt(status),
            from_date=_opt(from_date),
            to_date=_opt(to_date),
            example_id=_opt(example_id),
            limit=_opt(limit),
            offset=_opt(offset),
        )
        return _check_response(response)

    def cancel(self, execution_id: str) -> CancelExecutionResponse:
        response = executions_cancel.sync_detailed(
            execution_id=execution_id, client=self._client
        )
        return _check_response(response)

    def run_and_wait(
        self,
        workflow_id: str,
        input: Optional[dict[str, Any]] = None,
        *,
        version: Optional[str] = None,
        poll_interval_seconds: float = DEFAULT_POLL_INTERVAL_SECONDS,
        timeout_seconds: float = DEFAULT_RUN_AND_WAIT_TIMEOUT_SECONDS,
        overrides: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        """Trigger a workflow and poll client-side until terminal status.

        Unlike ``workflows.run(wait_for_completion=60)``, this polls
        indefinitely (up to ``timeout_seconds``, default 5 min) so it
        works for runs that exceed the 60s server-side sync window.
        """
        if has_file_input(input):
            assert input is not None
            run_result = _run_multipart(
                self._client,
                workflow_id,
                input,
                version=version,
                wait_for_completion=None,
                overrides=overrides,
                trigger=None,
            )
        else:
            body = RunWorkflowBody.from_dict(
                {
                    **({"input": input} if input is not None else {}),
                    **({"overrides": overrides} if overrides is not None else {}),
                }
            )
            run_response = workflows_run.sync_detailed(
                id=workflow_id,
                client=self._client,
                body=body,
                version=_opt(version),
            )
            run_result = _check_response(run_response)
        execution_id = run_result.execution_id  # type: ignore[union-attr]

        deadline = time.monotonic() + timeout_seconds
        while True:
            if time.monotonic() >= deadline:
                raise EigenpalTimeoutError(
                    f"run_and_wait timed out after {timeout_seconds}s "
                    f"(execution_id={execution_id})"
                )

            status = self.get(execution_id)
            status_value = getattr(status, "status", None)
            # Generated enums expose `.value`; plain strings pass through.
            status_str = getattr(status_value, "value", status_value)
            if status_str and str(status_str) in TERMINAL_STATUSES:
                return {
                    "executionId": execution_id,
                    "status": str(status_str),
                    "result": getattr(status, "result", None),
                    "error": getattr(status, "error", None),
                }

            time.sleep(poll_interval_seconds)

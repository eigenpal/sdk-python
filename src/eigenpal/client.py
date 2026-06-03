"""The hand-written `EigenpalClient` facade.

Wraps the auto-generated `AuthenticatedClient` from
`eigenpal._generated` with a friendlier API: namespaced resources,
typed exceptions, and a client-side `run_and_wait` polling helper.
"""

from __future__ import annotations

import json
import os
import time
from typing import Any, BinaryIO, Optional, Union
from urllib.parse import quote

import httpx

from eigenpal._files import has_file_input, is_file_input, to_upload_tuple
from eigenpal._generated.api.agents import (
    agents_create,
    agents_triggers_email_create_alias,
    agents_triggers_email_delete_alias,
    agents_triggers_email_get,
    agents_triggers_email_list,
    agents_triggers_email_update,
    agents_triggers_email_update_alias,
    agents_runs_cancel,
    agents_runs_rerun,
    agents_runs_expected_create,
    agents_runs_expected_delete,
    agents_runs_expected_list,
    agents_runs_expected_rename,
    agents_runs_feedback_delete,
    agents_runs_feedback_get,
    agents_runs_feedback_update,
    agents_runs_get,
    agents_runs_list,
    agents_files_list_or_get,
    agents_files_put,
    agents_files_upload_batch,
    agents_get,
    agents_list,
    agents_run,
    agents_update,
)
from eigenpal._generated.api.automations import automations_sync
from eigenpal._generated.api.source import (
    source_lockfile_preview,
    source_raw,
    source_releases,
    source_repository,
    source_secrets_decrypt,
    source_secrets_encrypt,
)
from eigenpal._generated.api.workflows import (
    workflows_get,
    workflows_executions_cancel,
    workflows_executions_get,
    workflows_executions_list,
    workflows_list,
    workflows_run,
    workflows_versions_list,
)
from eigenpal._generated.client import AuthenticatedClient
from eigenpal._generated.models.agent_run_response import AgentRunResponse
from eigenpal._generated.models.agents_triggers_email_create_alias_body import (
    AgentsTriggersEmailCreateAliasBody,
)
from eigenpal._generated.models.agents_triggers_email_create_alias_response_201 import (
    AgentsTriggersEmailCreateAliasResponse201,
)
from eigenpal._generated.models.agents_triggers_email_delete_alias_response_200 import (
    AgentsTriggersEmailDeleteAliasResponse200,
)
from eigenpal._generated.models.agents_triggers_email_get_response_200 import (
    AgentsTriggersEmailGetResponse200,
)
from eigenpal._generated.models.agents_triggers_email_list_response_200 import (
    AgentsTriggersEmailListResponse200,
)
from eigenpal._generated.models.agents_triggers_email_update_alias_body import (
    AgentsTriggersEmailUpdateAliasBody,
)
from eigenpal._generated.models.agents_triggers_email_update_alias_response_200 import (
    AgentsTriggersEmailUpdateAliasResponse200,
)
from eigenpal._generated.models.agents_triggers_email_update_body import (
    AgentsTriggersEmailUpdateBody,
)
from eigenpal._generated.models.agents_triggers_email_update_response_200 import (
    AgentsTriggersEmailUpdateResponse200,
)
from eigenpal._generated.models.agents_files_put_body import AgentsFilesPutBody
from eigenpal._generated.models.agents_files_upload_batch_body import AgentsFilesUploadBatchBody
from eigenpal._generated.models.agent_execution_expected_artifacts import (
    AgentExecutionExpectedArtifacts,
)
from eigenpal._generated.models.agent_execution_feedback_detail import AgentExecutionFeedbackDetail
from eigenpal._generated.models.agents_runs_list_feedback_rating import AgentsRunsListFeedbackRating
from eigenpal._generated.models.agents_runs_list_feedback_status import AgentsRunsListFeedbackStatus
from eigenpal._generated.models.agents_runs_list_order import AgentsRunsListOrder
from eigenpal._generated.models.agents_runs_list_sort import AgentsRunsListSort
from eigenpal._generated.models.cancel_agent_execution_response import CancelAgentExecutionResponse
from eigenpal._generated.models.cancel_workflow_execution_response import (
    CancelWorkflowExecutionResponse,
)
from eigenpal._generated.models.source_secrets_decrypt_body import SourceSecretsDecryptBody
from eigenpal._generated.models.source_secrets_encrypt_body import SourceSecretsEncryptBody
from eigenpal._generated.models.source_secrets_encrypt_response import SourceSecretsEncryptResponse
from eigenpal._generated.models.create_agent_body import CreateAgentBody
from eigenpal._generated.models.create_agent_response import CreateAgentResponse
from eigenpal._generated.models.get_agent_response import GetAgentResponse
from eigenpal._generated.models.list_agent_runs_response import ListAgentRunsResponse
from eigenpal._generated.models.list_agents_response import ListAgentsResponse
from eigenpal._generated.models.list_versions_response import ListVersionsResponse
from eigenpal._generated.models.list_workflow_executions_response import (
    ListWorkflowExecutionsResponse,
)
from eigenpal._generated.models.list_workflows_response import ListWorkflowsResponse
from eigenpal._generated.models.patch_agent_body import PatchAgentBody
from eigenpal._generated.models.patch_agent_response import PatchAgentResponse
from eigenpal._generated.models.copy_agent_execution_output_to_expected_body import (
    CopyAgentExecutionOutputToExpectedBody,
)
from eigenpal._generated.models.rename_expected_file_body import RenameExpectedFileBody
from eigenpal._generated.models.rerun_agent_run_response import RerunAgentRunResponse
from eigenpal._generated.models.run_agent_body import RunAgentBody
from eigenpal._generated.models.run_agent_response import RunAgentResponse
from eigenpal._generated.models.run_workflow_body import RunWorkflowBody
from eigenpal._generated.models.run_workflow_response import RunWorkflowResponse
from eigenpal._generated.models.update_agent_execution_feedback_body import (
    UpdateAgentExecutionFeedbackBody,
)
from eigenpal._generated.models.workflow_detail import WorkflowDetail
from eigenpal._generated.models.workflow_execution_status_response import (
    WorkflowExecutionStatusResponse,
)
from eigenpal._generated.models.workflow_summary import WorkflowSummary
from eigenpal._generated.models.workflows_executions_get_include_steps import (
    WorkflowsExecutionsGetIncludeSteps,
)
from eigenpal._generated.types import UNSET, Response, Unset
from eigenpal._telemetry import build_telemetry_headers
from eigenpal.errors import EigenpalError, EigenpalTimeoutError, error_from_response

DEFAULT_BASE_URL = "https://app.eigenpal.com"
DEFAULT_TIMEOUT_SECONDS = 60.0
DEFAULT_POLL_INTERVAL_SECONDS = 2.0
DEFAULT_RUN_AND_WAIT_TIMEOUT_SECONDS = 5 * 60.0

TERMINAL_STATUSES = frozenset({"completed", "failed", "cancelled", "rejected"})


def _assert_json_response(response: httpx.Response) -> None:
    """Raise EigenpalError when the response body isn't JSON.

    Mirrors the TS client's assertJsonResponse guard. Without this, a
    misconfigured ``base_url`` pointed at an HTML host (the marketing
    site, a misconfigured proxy) lets the auto-generated client crash
    with a raw ``JSONDecodeError`` when it tries to parse the body —
    the same footgun that hid the @eigenpal/sdk@0.4.10 ``/v1`` bug.

    Fires for both 2xx and error responses: a 4xx with HTML usually
    means the URL never reached the API at all (e.g. example.com 404
    page), and we want a typed error rather than a downstream
    JSONDecodeError surfaced to the user.

    Sync-only. Today no async API is exposed, so registering this on
    httpx.AsyncClient would fire a "coroutine was never awaited"
    warning. When we expose async, define an `async def` twin and stop
    forwarding httpx_args verbatim — register the right hook per
    client.
    """
    if response.status_code == 204:
        return
    content_type = (response.headers.get("content-type") or "").lower()
    # Empty Content-Type can come from minimal proxies; tolerate it.
    if content_type == "" or "json" in content_type or "octet-stream" in content_type:
        return
    raise EigenpalError(
        f'Expected a JSON response from the API but got Content-Type "{content_type}". '
        "This usually means `base_url` points at a non-API host (e.g. the marketing site or "
        'a misconfigured proxy). Set `base_url` to your EigenPal instance root, '
        'e.g. "https://app.eigenpal.com".',
        status=response.status_code,
    )


def _opt(value: Any) -> Any:
    """Generated SDK takes UNSET (not None) for optional query params."""
    return UNSET if value is None else value


def _csv(value: Optional[Union[str, list[str]]]) -> Optional[str]:
    """Accept ``str`` or ``list[str]``; emit a comma-separated string for
    the wire format (or ``None`` for "not provided")."""
    if value is None:
        return None
    if isinstance(value, list):
        return ",".join(value)
    return value


def _agent_artifact_path(kind: str, filename: str) -> str:
    if kind in {"issues", "trace", "lockfile"}:
        return filename
    return f"{kind}/{filename}"


def _quote_artifact_path(artifact_path: str) -> str:
    return "/".join(quote(segment, safe="") for segment in artifact_path.split("/"))


def _check_response(response: Response[Any]) -> Any:
    """Raise a typed EigenPal exception on non-2xx; return parsed body otherwise."""
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


class EigenpalClient:
    """Top-level SDK client.

    >>> client = EigenpalClient()  # reads EIGENPAL_API_KEY from env
    >>> client = EigenpalClient(api_key="eg_...")  # explicit
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
                "Missing API key. Pass EigenpalClient(api_key=...) or set the "
                "EIGENPAL_API_KEY environment variable."
            )

        resolved_base_url = base_url or os.environ.get("EIGENPAL_BASE_URL") or DEFAULT_BASE_URL

        self._client = AuthenticatedClient(
            base_url=resolved_base_url,
            token=resolved_key,
            timeout=httpx.Timeout(timeout_seconds),
            verify_ssl=verify_ssl,
            raise_on_unexpected_status=False,
            # SDK telemetry headers (X-Eigenpal-Sdk-*) + a richer User-Agent.
            # The server logs these per request so we can track adoption.
            headers=build_telemetry_headers(),
            # Sync-only event hook. ``httpx_args`` is forwarded to both
            # httpx.Client and httpx.AsyncClient by the generated wrapper,
            # but no async API surface is exposed today. See the docstring
            # on ``_assert_json_response`` for the path forward when async
            # ships.
            httpx_args={"event_hooks": {"response": [_assert_json_response]}},
        )
        self.workflows = WorkflowsResource(self._client)
        self.agents = AgentsResource(self._client)
        self.source = SourceResource(self._client)
        self.automations = AutomationsResource(self._client)

    def __enter__(self) -> "EigenpalClient":
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
        f"/api/v1/workflows/{workflow_id}/run",
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


def _run_agent_multipart(
    client: AuthenticatedClient,
    agent_id: str,
    input: dict[str, Any],
    *,
    wait_for_completion: Optional[int],
    source_ref: Optional[str],
) -> RunAgentResponse:
    """Send an agent execution as ``multipart/form-data``.

    Each file value in ``input`` becomes a top-level form field. Scalar inputs
    ride in the ``_json`` field as the input object itself.
    """
    files: list[tuple[str, tuple[str, bytes, str]]] = []
    scalars: dict[str, Any] = {}
    for key, value in input.items():
        if is_file_input(value):
            files.append((key, to_upload_tuple(value)))
        else:
            scalars[key] = value

    params: dict[str, Any] = {}
    if wait_for_completion is not None:
        params["wait_for_completion"] = wait_for_completion
    if source_ref is not None:
        params["sourceRef"] = source_ref

    data = {"_json": json.dumps(scalars)} if scalars else {}
    raw_response = client.get_httpx_client().post(
        f"/api/v1/agents/{agent_id}/run",
        params=params,
        files=files,
        data=data,
    )

    if 200 <= raw_response.status_code < 300:
        parsed = RunAgentResponse.from_dict(raw_response.json())
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


class SourceResource:
    """Source repository operations: repository metadata, raw files, releases, lockfiles, secrets."""

    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def repository(self) -> Any:
        response = source_repository.sync_detailed(client=self._client)
        return _check_response(response)

    def raw(self, path: str, *, ref: str = "main") -> Any:
        response = source_raw.sync_detailed(client=self._client, path=path, ref=ref)
        return _check_response(response)

    def releases(self, package_path: str, *, version: Optional[str] = None) -> Any:
        response = source_releases.sync_detailed(
            client=self._client,
            package_path=package_path,
            version=_opt(version),
        )
        return _check_response(response)

    def lockfile(self, package_ref: str) -> Any:
        response = source_lockfile_preview.sync_detailed(
            client=self._client,
            package_ref=package_ref,
        )
        return _check_response(response)

    def decrypt_secrets(self, body: dict[str, Any] | SourceSecretsDecryptBody) -> Any:
        payload = (
            body
            if isinstance(body, SourceSecretsDecryptBody)
            else SourceSecretsDecryptBody.from_dict(body)
        )
        response = source_secrets_decrypt.sync_detailed(client=self._client, body=payload)
        return _check_response(response)

    def encrypt_secrets(self, body: dict[str, Any] | SourceSecretsEncryptBody) -> SourceSecretsEncryptResponse:
        payload = (
            body
            if isinstance(body, SourceSecretsEncryptBody)
            else SourceSecretsEncryptBody.from_dict(body)
        )
        response = source_secrets_encrypt.sync_detailed(client=self._client, body=payload)
        return _check_response(response)


class AutomationsResource:
    """Automation operations: sync public automation metadata from source."""

    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def sync(self, automation: str) -> Any:
        response = automations_sync.sync_detailed(client=self._client, automation=automation)
        return _check_response(response)


class WorkflowsResource:
    """Workflow operations: list, get, run, versions."""

    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client
        self.executions = WorkflowExecutionsResource(client)

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

    def get(self, workflow_id: str) -> WorkflowDetail:
        """Get a single workflow by id. Includes the current version's YAML."""
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


class WorkflowExecutionsResource:
    """Workflow execution operations: list, get, cancel, run_and_wait."""

    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def get(self, execution_id: str, *, include_steps: bool = False) -> WorkflowExecutionStatusResponse:
        include = WorkflowsExecutionsGetIncludeSteps.TRUE if include_steps else UNSET
        response = workflows_executions_get.sync_detailed(
            execution_id=execution_id,
            client=self._client,
            include_steps=include,
        )
        return _check_response(response)

    def list(
        self,
        workflow_id: str,
        *,
        status: Optional[Union[str, list[str]]] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        example_id: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> ListWorkflowExecutionsResponse:
        response = workflows_executions_list.sync_detailed(
            id=workflow_id,
            client=self._client,
            status=_opt(_csv(status)),
            from_date=_opt(from_date),
            to_date=_opt(to_date),
            example_id=_opt(example_id),
            limit=_opt(limit),
            offset=_opt(offset),
        )
        return _check_response(response)

    def cancel(self, execution_id: str) -> CancelWorkflowExecutionResponse:
        response = workflows_executions_cancel.sync_detailed(
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


class AgentRunsResource:
    """Agent run operations: list, get, cancel, feedback, and expected artifacts."""

    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def list(
        self,
        agent_id: str,
        *,
        status: Optional[str] = None,
        batch_id: Optional[str] = None,
        example_id: Optional[str] = None,
        example_id_contains: Optional[str] = None,
        created_after: Optional[str] = None,
        created_before: Optional[str] = None,
        completed_after: Optional[str] = None,
        completed_before: Optional[str] = None,
        source_ref: Optional[str] = None,
        feedback_status: Optional[str] = None,
        feedback_rating: Optional[str] = None,
        has_feedback: Optional[bool] = None,
        no_feedback: Optional[bool] = None,
        has_expected: Optional[bool] = None,
        has_expected_json: Optional[bool] = None,
        has_expected_files: Optional[bool] = None,
        feedback_body_contains: Optional[str] = None,
        feedback_created_after: Optional[str] = None,
        feedback_created_before: Optional[str] = None,
        feedback_updated_after: Optional[str] = None,
        feedback_updated_before: Optional[str] = None,
        feedback_resolved_after: Optional[str] = None,
        feedback_resolved_before: Optional[str] = None,
        promoted_to_example: Optional[bool] = None,
        promoted_example_name: Optional[str] = None,
        since_last_resolved: Optional[bool] = None,
        include: Optional[str] = None,
        sort: Optional[str] = None,
        order: Optional[str] = None,
        scan_limit: Optional[int] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> ListAgentRunsResponse:
        response = agents_runs_list.sync_detailed(
            agent_id=agent_id,
            client=self._client,
            status=_opt(status),
            batch_id=_opt(batch_id),
            example_id=_opt(example_id),
            example_id_contains=_opt(example_id_contains),
            created_after=_opt(created_after),
            created_before=_opt(created_before),
            completed_after=_opt(completed_after),
            completed_before=_opt(completed_before),
            source_ref=_opt(source_ref),
            feedback_status=(
                _opt(None)
                if feedback_status is None
                else AgentsRunsListFeedbackStatus(feedback_status)
            ),
            feedback_rating=(
                _opt(None)
                if feedback_rating is None
                else AgentsRunsListFeedbackRating(feedback_rating)
            ),
            has_feedback=_opt(has_feedback),
            no_feedback=_opt(no_feedback),
            has_expected=_opt(has_expected),
            has_expected_json=_opt(has_expected_json),
            has_expected_files=_opt(has_expected_files),
            feedback_body_contains=_opt(feedback_body_contains),
            feedback_created_after=_opt(feedback_created_after),
            feedback_created_before=_opt(feedback_created_before),
            feedback_updated_after=_opt(feedback_updated_after),
            feedback_updated_before=_opt(feedback_updated_before),
            feedback_resolved_after=_opt(feedback_resolved_after),
            feedback_resolved_before=_opt(feedback_resolved_before),
            promoted_to_example=_opt(promoted_to_example),
            promoted_example_name=_opt(promoted_example_name),
            since_last_resolved=_opt(since_last_resolved),
            include=_opt(include),
            sort=_opt(None) if sort is None else AgentsRunsListSort(sort),
            order=_opt(None) if order is None else AgentsRunsListOrder(order),
            scan_limit=_opt(scan_limit),
            limit=_opt(limit),
            offset=_opt(offset),
        )
        return _check_response(response)

    def get(self, run_id: str, *, include: Optional[str] = None) -> AgentRunResponse:
        response = agents_runs_get.sync_detailed(
            run_id=run_id,
            client=self._client,
            include=_opt(include),
        )
        return _check_response(response)

    def cancel(self, run_id: str) -> CancelAgentExecutionResponse:
        response = agents_runs_cancel.sync_detailed(
            run_id=run_id,
            client=self._client,
        )
        return _check_response(response)

    def rerun(self, run_id: str) -> RerunAgentRunResponse:
        response = agents_runs_rerun.sync_detailed(
            run_id=run_id,
            client=self._client,
        )
        return _check_response(response)

    def get_feedback(self, run_id: str) -> AgentExecutionFeedbackDetail:
        response = agents_runs_feedback_get.sync_detailed(
            run_id=run_id,
            client=self._client,
        )
        return _check_response(response)

    def update_feedback(
        self,
        run_id: str,
        *,
        body: Optional[str] = None,
        feedback: Optional[str] = None,
        rating: Optional[str] = None,
        feedback_rating: Optional[str] = None,
        status: Optional[str] = None,
        feedback_status: Optional[str] = None,
        expected: Any | None | Unset = UNSET,
    ) -> AgentExecutionFeedbackDetail:
        payload = UpdateAgentExecutionFeedbackBody.from_dict(
            {
                **({ "body": body } if body is not None else {}),
                **({ "feedback": feedback } if feedback is not None else {}),
                **({ "rating": rating } if rating is not None else {}),
                **({ "feedbackRating": feedback_rating } if feedback_rating is not None else {}),
                **({ "status": status } if status is not None else {}),
                **({ "feedbackStatus": feedback_status } if feedback_status is not None else {}),
                **({ "expected": expected } if not isinstance(expected, Unset) else {}),
            }
        )
        response = agents_runs_feedback_update.sync_detailed(
            run_id=run_id,
            client=self._client,
            body=payload,
        )
        return _check_response(response)

    def clear_feedback(self, run_id: str) -> AgentExecutionFeedbackDetail:
        response = agents_runs_feedback_delete.sync_detailed(
            run_id=run_id,
            client=self._client,
        )
        return _check_response(response)

    def list_expected(self, run_id: str) -> AgentExecutionExpectedArtifacts:
        response = agents_runs_expected_list.sync_detailed(
            run_id=run_id,
            client=self._client,
        )
        return _check_response(response)

    def copy_output_to_expected(
        self,
        run_id: str,
        *,
        output_file_name: str,
        expected_name: Optional[str] = None,
    ) -> Any:
        response = agents_runs_expected_create.sync_detailed(
            run_id=run_id,
            client=self._client,
            body=CopyAgentExecutionOutputToExpectedBody(
                output_file_name=output_file_name,
                expected_name=_opt(expected_name),
            ),
        )
        return _check_response(response)

    def rename_expected(self, run_id: str, filename: str, *, name: str) -> Any:
        response = agents_runs_expected_rename.sync_detailed(
            run_id=run_id,
            filename=filename,
            client=self._client,
            body=RenameExpectedFileBody(name=name),
        )
        return _check_response(response)

    def delete_expected(self, run_id: str, filename: str) -> None:
        response = agents_runs_expected_delete.sync_detailed(
            run_id=run_id,
            filename=filename,
            client=self._client,
        )
        _check_response(response)
        return None

    def upload_expected(
        self,
        run_id: str,
        *,
        file: bytes | BinaryIO,
        filename: str,
        name: Optional[str] = None,
    ) -> Any:
        files = {"file": (filename, file)}
        data = {"name": name} if name is not None else None
        raw_response = self._client.get_httpx_client().post(
            f"/api/v1/agents/runs/{quote(run_id, safe='')}/expected",
            files=files,
            data=data,
        )
        if 200 <= raw_response.status_code < 300:
            return raw_response.json()
        return _check_response(Response(raw_response.status_code, raw_response.content, raw_response.headers, None))

    def download_expected(self, run_id: str, filename: str) -> bytes:
        raw_response = self._client.get_httpx_client().get(
            "/api/v1/agents/runs/"
            f"{quote(run_id, safe='')}/expected/{quote(filename, safe='')}"
        )
        if 200 <= raw_response.status_code < 300:
            return raw_response.content
        return _check_response(Response(raw_response.status_code, raw_response.content, raw_response.headers, None))

    def download_file(
        self,
        run_id: str,
        artifact_path_or_kind: str,
        filename: Optional[str] = None,
    ) -> bytes:
        artifact_path = (
            _agent_artifact_path(artifact_path_or_kind, filename)
            if filename is not None
            else artifact_path_or_kind
        )
        raw_response = self._client.get_httpx_client().get(
            "/api/v1/agents/runs/"
            f"{quote(run_id, safe='')}/files/{_quote_artifact_path(artifact_path)}"
        )
        if 200 <= raw_response.status_code < 300:
            return raw_response.content
        return _check_response(Response(raw_response.status_code, raw_response.content, raw_response.headers, None))


class AgentEmailTriggersResource:
    """Agent email trigger operations: list, get, update, create aliases, and remove aliases."""

    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def list(self) -> AgentsTriggersEmailListResponse200:
        response = agents_triggers_email_list.sync_detailed(client=self._client)
        return _check_response(response)

    def get(self, agent_id: str) -> AgentsTriggersEmailGetResponse200:
        response = agents_triggers_email_get.sync_detailed(
            agent_id=agent_id,
            client=self._client,
        )
        return _check_response(response)

    def update(
        self,
        agent_id: str,
        body: dict[str, Any] | AgentsTriggersEmailUpdateBody,
    ) -> AgentsTriggersEmailUpdateResponse200:
        payload = (
            body
            if isinstance(body, AgentsTriggersEmailUpdateBody)
            else AgentsTriggersEmailUpdateBody.from_dict(body)
        )
        response = agents_triggers_email_update.sync_detailed(
            agent_id=agent_id,
            client=self._client,
            body=payload,
        )
        return _check_response(response)

    def create_alias(
        self,
        agent_id: str,
        body: dict[str, Any] | AgentsTriggersEmailCreateAliasBody,
    ) -> AgentsTriggersEmailCreateAliasResponse201:
        payload = (
            body
            if isinstance(body, AgentsTriggersEmailCreateAliasBody)
            else AgentsTriggersEmailCreateAliasBody.from_dict(body)
        )
        response = agents_triggers_email_create_alias.sync_detailed(
            agent_id=agent_id,
            client=self._client,
            body=payload,
        )
        return _check_response(response)

    def update_alias(
        self,
        agent_id: str,
        email_id: str,
        body: dict[str, Any] | AgentsTriggersEmailUpdateAliasBody,
    ) -> AgentsTriggersEmailUpdateAliasResponse200:
        payload = (
            body
            if isinstance(body, AgentsTriggersEmailUpdateAliasBody)
            else AgentsTriggersEmailUpdateAliasBody.from_dict(body)
        )
        response = agents_triggers_email_update_alias.sync_detailed(
            agent_id=agent_id,
            email_id=email_id,
            client=self._client,
            body=payload,
        )
        return _check_response(response)

    def delete_alias(
        self,
        agent_id: str,
        email_id: str,
    ) -> AgentsTriggersEmailDeleteAliasResponse200:
        response = agents_triggers_email_delete_alias.sync_detailed(
            agent_id=agent_id,
            email_id=email_id,
            client=self._client,
        )
        return _check_response(response)


class AgentsResource:
    """Agent operations: list, get, create, run, runs, and email triggers."""

    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client
        self.runs = AgentRunsResource(client)
        self.email_triggers = AgentEmailTriggersResource(client)

    def list(
        self,
        *,
        search: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> ListAgentsResponse:
        response = agents_list.sync_detailed(
            client=self._client,
            search=_opt(search),
            limit=_opt(limit),
            offset=_opt(offset),
        )
        return _check_response(response)

    def get(self, agent_id: str, *, include: Optional[str] = None) -> GetAgentResponse:
        response = agents_get.sync_detailed(
            agent_id=agent_id,
            client=self._client,
            include=_opt(include),
        )
        return _check_response(response)

    def list_files(
        self,
        agent_id: str,
        *,
        path: Optional[str] = None,
        prefix: Optional[str] = None,
    ) -> Any:
        response = agents_files_list_or_get.sync_detailed(
            agent_id=agent_id,
            client=self._client,
            path=_opt(path),
            prefix=_opt(prefix),
        )
        return _check_response(response)

    def put_file(self, agent_id: str, path: str, *, content_base64: str) -> Any:
        response = agents_files_put.sync_detailed(
            agent_id=agent_id,
            client=self._client,
            path=path,
            body=AgentsFilesPutBody.from_dict({"contentBase64": content_base64}),
        )
        return _check_response(response)

    def upload_files(self, agent_id: str, files: list[dict[str, Any]]) -> Any:
        response = agents_files_upload_batch.sync_detailed(
            agent_id=agent_id,
            client=self._client,
            body=AgentsFilesUploadBatchBody.from_dict({"files": files}),
        )
        return _check_response(response)

    def create(
        self,
        *,
        name: str,
        slug: str,
        description: Optional[str] = None,
        config: Optional[dict[str, Any]] = None,
    ) -> CreateAgentResponse:
        body = CreateAgentBody.from_dict(
            {
                "name": name,
                "slug": slug,
                **({"description": description} if description is not None else {}),
                **({"config": config} if config is not None else {}),
            }
        )
        response = agents_create.sync_detailed(client=self._client, body=body)
        return _check_response(response)

    def update(
        self,
        agent_id: str,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
        config: Optional[dict[str, Any]] = None,
    ) -> PatchAgentResponse:
        body = PatchAgentBody.from_dict(
            {
                **({"name": name} if name is not None else {}),
                **({"description": description} if description is not None else {}),
                **({"config": config} if config is not None else {}),
            }
        )
        response = agents_update.sync_detailed(agent_id=agent_id, client=self._client, body=body)
        return _check_response(response)

    def run(
        self,
        agent_id: str,
        input: Optional[dict[str, Any]] = None,
        *,
        wait_for_completion: Optional[int] = None,
        source_ref: Optional[str] = None,
    ) -> RunAgentResponse:
        if has_file_input(input):
            assert input is not None
            return _run_agent_multipart(
                self._client,
                agent_id,
                input,
                wait_for_completion=wait_for_completion,
                source_ref=source_ref,
            )

        body = RunAgentBody.from_dict(
            {
                **({"input": input} if input is not None else {}),
                **({"sourceRef": source_ref} if source_ref is not None else {}),
            }
        )
        response = agents_run.sync_detailed(
            agent_id=agent_id,
            client=self._client,
            body=body,
            source_ref=_opt(source_ref),
            wait_for_completion=_opt(wait_for_completion),
        )
        return _check_response(response)

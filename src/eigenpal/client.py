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
    agents_versions_list,
    agents_files_list_or_get,
    agents_files_put,
    agents_files_upload_batch,
    agents_get,
    agents_list,
    agents_update,
)
from eigenpal._generated.api.runs import (
    runs_cancel,
    runs_expected_create,
    runs_expected_file_delete,
    runs_expected_file_get,
    runs_expected_file_update,
    runs_expected_get,
    runs_feedback_clear,
    runs_feedback_get,
    runs_feedback_update,
    runs_get,
    runs_list,
    runs_rerun,
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
    workflows_list,
    workflows_versions_list,
)
from eigenpal._generated.client import AuthenticatedClient
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
from eigenpal._generated.models.agents_files_upload_batch_body import (
    AgentsFilesUploadBatchBody,
)
from eigenpal._generated.models.source_secrets_decrypt_body import (
    SourceSecretsDecryptBody,
)
from eigenpal._generated.models.source_secrets_encrypt_body import (
    SourceSecretsEncryptBody,
)
from eigenpal._generated.models.source_secrets_encrypt_response import (
    SourceSecretsEncryptResponse,
)
from eigenpal._generated.models.create_agent_body import CreateAgentBody
from eigenpal._generated.models.create_agent_response import CreateAgentResponse
from eigenpal._generated.models.get_agent_response import GetAgentResponse
from eigenpal._generated.models.list_agent_versions_response import (
    ListAgentVersionsResponse,
)
from eigenpal._generated.models.list_agents_response import ListAgentsResponse
from eigenpal._generated.models.list_versions_response import ListVersionsResponse
from eigenpal._generated.models.list_workflows_response import ListWorkflowsResponse
from eigenpal._generated.models.patch_agent_body import PatchAgentBody
from eigenpal._generated.models.patch_agent_response import PatchAgentResponse
from eigenpal._generated.models.runs_cancel_response_200 import RunsCancelResponse200
from eigenpal._generated.models.runs_expected_file_update_body import (
    RunsExpectedFileUpdateBody,
)
from eigenpal._generated.models.runs_expected_file_update_response_200 import (
    RunsExpectedFileUpdateResponse200,
)
from eigenpal._generated.models.runs_expected_get_response_200 import (
    RunsExpectedGetResponse200,
)
from eigenpal._generated.models.runs_feedback_clear_response_200 import (
    RunsFeedbackClearResponse200,
)
from eigenpal._generated.models.runs_feedback_get_response_200 import (
    RunsFeedbackGetResponse200,
)
from eigenpal._generated.models.runs_feedback_update_response_200 import (
    RunsFeedbackUpdateResponse200,
)
from eigenpal._generated.models.runs_list_response import RunsListResponse
from eigenpal._generated.models.run_envelope import RunEnvelope
from eigenpal._generated.models.run_rerun_request import RunRerunRequest
from eigenpal._generated.models.run_rerun_response import RunRerunResponse
from eigenpal._generated.models.run_start_response import RunStartResponse
from eigenpal._generated.models.run_feedback_request import RunFeedbackRequest
from eigenpal._generated.models.workflow_detail import WorkflowDetail
from eigenpal._generated.models.workflow_summary import WorkflowSummary
from eigenpal._generated.types import UNSET, Response, Unset
from eigenpal._telemetry import build_telemetry_headers
from eigenpal.errors import EigenpalError, EigenpalTimeoutError, error_from_response

DEFAULT_BASE_URL = "https://studio.eigenpal.com"
DEFAULT_TIMEOUT_SECONDS = 60.0
DEFAULT_POLL_INTERVAL_SECONDS = 2.0
DEFAULT_RUN_AND_WAIT_TIMEOUT_SECONDS = 5 * 60.0

TERMINAL_STATUSES = frozenset({"completed", "failed", "cancelled", "rejected"})

UpdateAgentExecutionFeedbackBody = dict[str, Any]
CopyAgentExecutionOutputToExpectedBody = dict[str, Any]
RenameExpectedFileBody = dict[str, Any]


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
        "a misconfigured proxy). Set `base_url` to your EigenPal instance root, "
        'e.g. "https://studio.eigenpal.com".',
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


def _run_prop(run: Any, key: str, default: Any = None) -> Any:
    """Read fields from dicts, attrs models, or generated additional-property models."""
    if isinstance(run, dict):
        return run.get(key, default)
    if hasattr(run, "__contains__") and key in run:
        try:
            return run[key]
        except Exception:
            return default
    return getattr(run, key, default)


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

        resolved_base_url = (
            base_url or os.environ.get("EIGENPAL_BASE_URL") or DEFAULT_BASE_URL
        )

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
        self.runs = RunsResource(self._client)

    @property
    def raw_client(self) -> AuthenticatedClient:
        """Expose the generated authenticated client for advanced/generated API calls."""
        return self._client

    def run(
        self,
        target: Union[str, dict[str, Any]],
        input: Optional[dict[str, Any]] = None,
        *,
        wait_for_completion: Optional[int] = None,
        overrides: Optional[dict[str, Any]] = None,
    ) -> RunStartResponse:
        """Start a workflow or agent run via ``POST /api/v1/run/{target}``.

        ``overrides`` (workflow targets only) is sent under the reserved
        ``_overrides`` body key as ``{"steps": {<stepName>: <output>}}``.
        """
        path_target, version = _path_target_from_run_target(target)
        if has_file_input(input):
            assert input is not None
            return _run_multipart(
                self._client,
                input,
                path_target=path_target,
                version=version,
                wait_for_completion=wait_for_completion,
                overrides=overrides,
            )

        return _run_json(
            self._client,
            path_target=path_target,
            version=version,
            wait_for_completion=wait_for_completion,
            input=input,
            overrides=overrides,
        )

    def rerun(
        self, run_id: str, *, source_ref: Optional[str] = None
    ) -> RunRerunResponse:
        """Create a new run from a previous run's input snapshot."""
        return self.runs.rerun(run_id, source_ref=source_ref)

    def __enter__(self) -> "EigenpalClient":
        return self

    def __exit__(self, *exc_info: Any) -> None:
        self._client.get_httpx_client().close()


def _wrap_run_response(raw_response: Any) -> RunStartResponse:
    """Wrap a raw httpx run-start response in the generated ``Response``
    envelope and surface API errors through ``_check_response``."""
    if 200 <= raw_response.status_code < 300:
        parsed = RunStartResponse.from_dict(raw_response.json())
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


def _run_json(
    client: AuthenticatedClient,
    *,
    path_target: str,
    version: Optional[str],
    wait_for_completion: Optional[int],
    input: Optional[dict[str, Any]],
    overrides: Optional[dict[str, Any]] = None,
) -> RunStartResponse:
    """Send a JSON-body run. Per-step overrides ride in the reserved
    ``_overrides`` body key."""
    body: dict[str, Any] = dict(input or {})
    if overrides is not None:
        body["_overrides"] = overrides
    raw_response = client.get_httpx_client().post(
        f"/api/v1/run/{quote(path_target, safe='')}",
        params=_run_query(wait_for_completion=wait_for_completion, version=version),
        json=body,
    )
    return _wrap_run_response(raw_response)


def _run_multipart(
    client: AuthenticatedClient,
    input: dict[str, Any],
    *,
    path_target: str,
    version: Optional[str],
    wait_for_completion: Optional[int],
    overrides: Optional[dict[str, Any]] = None,
) -> RunStartResponse:
    """Send a run as ``multipart/form-data``. Each file value in
    ``input`` becomes a top-level form field; non-file inputs ride along
    in the canonical ``_json`` text field, and per-step overrides in the
    reserved ``_overrides`` text field."""
    files: list[tuple[str, tuple[str, bytes, str]]] = []
    scalars: dict[str, Any] = {}
    for key, value in input.items():
        if is_file_input(value):
            files.append((key, to_upload_tuple(value)))
        else:
            scalars[key] = value

    data = {"_json": json.dumps(scalars)}
    if overrides is not None:
        data["_overrides"] = json.dumps(overrides)

    httpx_client = client.get_httpx_client()
    raw_response = httpx_client.post(
        f"/api/v1/run/{quote(path_target, safe='')}",
        params=_run_query(wait_for_completion=wait_for_completion, version=version),
        files=files,
        data=data,
    )
    return _wrap_run_response(raw_response)


def _path_target_from_run_target(target: Union[str, dict[str, Any]]) -> tuple[str, Optional[str]]:
    if isinstance(target, str):
        parts = target.split("@")
        if len(parts) > 2 or not parts[0] or (len(parts) == 2 and not parts[1]):
            raise EigenpalError("Run target strings must be <target> or <target>@<version>.", status=0)
        version = parts[1] if len(parts) == 2 and parts[1] != "latest" else None
        return parts[0], version
    kind = target.get("type")
    id_or_slug = target.get("slug") or target.get("id")
    if kind not in {"workflow", "agent"} or not id_or_slug:
        raise EigenpalError("Run target objects require type plus slug or id.", status=0)
    root = "agents" if kind == "agent" else "workflows"
    name = id_or_slug if "." in id_or_slug else f"{root}.{id_or_slug.replace('/', '.')}"
    version = target.get("version")
    return name, version if version and version != "latest" else None


def _run_query(
    *, wait_for_completion: Optional[int], version: Optional[str]
) -> Optional[dict[str, Any]]:
    params: dict[str, Any] = {}
    if wait_for_completion is not None:
        params["wait_for_completion"] = wait_for_completion
    if version:
        params["version"] = version
    return params or None


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
        response = source_secrets_decrypt.sync_detailed(
            client=self._client, body=payload
        )
        return _check_response(response)

    def encrypt_secrets(
        self, body: dict[str, Any] | SourceSecretsEncryptBody
    ) -> SourceSecretsEncryptResponse:
        payload = (
            body
            if isinstance(body, SourceSecretsEncryptBody)
            else SourceSecretsEncryptBody.from_dict(body)
        )
        response = source_secrets_encrypt.sync_detailed(
            client=self._client, body=payload
        )
        return _check_response(response)


class AutomationsResource:
    """Automation operations: sync public automation metadata from source."""

    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def sync(self, automation: str) -> Any:
        response = automations_sync.sync_detailed(
            client=self._client, automation=automation
        )
        return _check_response(response)


class WorkflowsResource:
    """Workflow operations: list, get, versions."""

    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client
        self.executions = WorkflowExecutionsResource(client)

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
    """Workflow execution helper namespace; existing run retrieval lives on ``client.runs``."""

    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def _get_status(self, execution_id: str) -> Any:
        response = runs_get.sync_detailed(
            id=execution_id,
            client=self._client,
            include="detail",
        )
        return _check_response(response).run

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

        Unlike ``client.run(wait_for_completion=60)``, this polls
        indefinitely (up to ``timeout_seconds``, default 5 min) so it
        works for runs that exceed the 60s server-side sync window.
        """
        target = f"workflows.{workflow_id}"
        run_version = version if version and version != "latest" else None
        if has_file_input(input):
            assert input is not None
            run_result = _run_multipart(
                self._client,
                input,
                path_target=target,
                version=run_version,
                wait_for_completion=None,
                overrides=overrides,
            )
        else:
            run_result = _run_json(
                self._client,
                path_target=target,
                version=run_version,
                wait_for_completion=None,
                input=input,
                overrides=overrides,
            )
        execution_id = run_result.run_id  # type: ignore[union-attr]

        deadline = time.monotonic() + timeout_seconds
        while True:
            if time.monotonic() >= deadline:
                raise EigenpalTimeoutError(
                    f"run_and_wait timed out after {timeout_seconds}s "
                    f"(run_id={execution_id})"
                )

            status = self._get_status(execution_id)
            status_value = _run_prop(status, "status")
            # Generated enums expose `.value`; plain strings pass through.
            status_str = getattr(status_value, "value", status_value)
            if status_str and str(status_str) in TERMINAL_STATUSES:
                return {
                    "runId": execution_id,
                    "status": str(status_str),
                    "output": _run_prop(status, "output"),
                    "error": _run_prop(status, "error"),
                }

            time.sleep(poll_interval_seconds)


class RunsResource:
    """Tenant-wide run operations across workflow, agent, manual, and eval runs."""

    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client
        self.feedback = RunsFeedbackResource(client)
        self.expected = RunsExpectedResource(client)
        self.files = RunsFilesResource(client)
        self.artifacts = RunsArtifactsResource(client)
        self.comparison = RunsComparisonResource(client)
        self.trace = RunsTraceResource(client)

    def list(
        self,
        *,
        type: Optional[str] = None,
        source: Optional[str] = None,
        status: Optional[Union[str, list[str]]] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        batch_id: Optional[str] = None,
        example_id: Optional[str] = None,
        example_id_contains: Optional[str] = None,
        created_after: Optional[str] = None,
        created_before: Optional[str] = None,
        completed_after: Optional[str] = None,
        completed_before: Optional[str] = None,
        source_ref: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> RunsListResponse:
        response = runs_list.sync_detailed(
            client=self._client,
            type_=_opt(type),
            source=_opt(source),
            status=_opt(_csv(status)),
            from_=_opt(from_date),
            to=_opt(to_date),
            batch_id=_opt(batch_id),
            example_id=_opt(example_id),
            example_id_contains=_opt(example_id_contains),
            created_after=_opt(created_after),
            created_before=_opt(created_before),
            completed_after=_opt(completed_after),
            completed_before=_opt(completed_before),
            source_ref=_opt(source_ref),
            limit=_opt(limit),
            offset=_opt(offset),
        )
        return _check_response(response)

    def get(self, run_id: str, *, include: Optional[str] = None) -> Any:
        response = runs_get.sync_detailed(
            id=run_id,
            client=self._client,
            include=_opt(include),
        )
        return _check_response(response).run

    def cancel(self, run_id: str) -> RunsCancelResponse200:
        response = runs_cancel.sync_detailed(id=run_id, client=self._client)
        return _check_response(response)

    def rerun(
        self, run_id: str, *, source_ref: Optional[str] = None
    ) -> RunRerunResponse:
        response = runs_rerun.sync_detailed(
            id=run_id,
            client=self._client,
            body=RunRerunRequest(source_ref=_opt(source_ref)),
        )
        return _check_response(response)

    def compare(
        self,
        reference_run_id: str,
        run_id: str,
        *,
        baseline: bool = False,
        step: Optional[str] = None,
        normalize_dates: bool = False,
    ) -> dict[str, Any]:
        mode = "baseline" if baseline else "expected"
        reference = self.get(
            reference_run_id,
            include="detail,files,output" if baseline else "detail,expected",
        )
        target = self.get(run_id, include="detail,files,output")
        if _is_workflow_run(reference) and _is_workflow_run(target):
            return _compare_workflow_runs(reference_run_id, reference, run_id, target, step)
        if step:
            raise EigenpalError(
                "step is only supported when both runs are workflow runs. Agent runs do not have workflow steps.",
                status=400,
            )
        if _is_workflow_run(reference) or _is_workflow_run(target):
            raise EigenpalError(
                "Mixed workflow/agent comparisons are not supported. Compare two workflow runs or two agent runs.",
                status=400,
            )
        return _compare_artifact_runs(
            reference_run_id,
            reference,
            run_id,
            target,
            mode=mode,
            normalize_dates=normalize_dates,
        )

    def connect(self, run_id: str) -> Any:
        raw_response = self._client.get_httpx_client().post(
            f"/api/v1/runs/{quote(run_id, safe='')}/connect"
        )
        if 200 <= raw_response.status_code < 300:
            return raw_response.json()
        return _check_response(
            Response(
                raw_response.status_code,
                raw_response.content,
                raw_response.headers,
                None,
            )
        )


class RunsFeedbackResource:
    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def get(self, run_id: str) -> RunsFeedbackGetResponse200:
        response = runs_feedback_get.sync_detailed(id=run_id, client=self._client)
        return _check_response(response)

    def update(
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
    ) -> RunsFeedbackUpdateResponse200:
        payload = {
            **({"body": body} if body is not None else {}),
            **({"feedback": feedback} if feedback is not None else {}),
            **({"rating": rating} if rating is not None else {}),
            **(
                {"feedbackRating": feedback_rating}
                if feedback_rating is not None
                else {}
            ),
            **({"status": status} if status is not None else {}),
            **(
                {"feedbackStatus": feedback_status}
                if feedback_status is not None
                else {}
            ),
            **({"expected": expected} if not isinstance(expected, Unset) else {}),
        }
        response = runs_feedback_update.sync_detailed(
            id=run_id,
            client=self._client,
            body=RunFeedbackRequest.from_dict(payload),
        )
        return _check_response(response)

    def resolve(
        self,
        run_id: str,
        *,
        body: Optional[str] = None,
        feedback: Optional[str] = None,
    ) -> RunsFeedbackUpdateResponse200:
        return self.update(run_id, status="resolved", body=body, feedback=feedback)

    def clear(self, run_id: str) -> RunsFeedbackClearResponse200:
        response = runs_feedback_clear.sync_detailed(id=run_id, client=self._client)
        return _check_response(response)


class RunsExpectedResource:
    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def list(self, run_id: str) -> RunsExpectedGetResponse200:
        response = runs_expected_get.sync_detailed(id=run_id, client=self._client)
        return _check_response(response)

    def copy_output(
        self,
        run_id: str,
        *,
        output_file_name: str,
        expected_name: Optional[str] = None,
    ) -> Any:
        response = runs_expected_create.sync_detailed(
            id=run_id,
            client=self._client,
            body={
                "outputFileName": output_file_name,
                **(
                    {"expectedName": expected_name} if expected_name is not None else {}
                ),
            },
        )
        return _check_response(response)

    def upload(
        self,
        run_id: str,
        file: bytes | BinaryIO,
        *,
        filename: str = "expected.bin",
        name: Optional[str] = None,
    ) -> Any:
        raw_response = self._client.get_httpx_client().post(
            f"/api/v1/runs/{quote(run_id, safe='')}/expected",
            files={"file": (filename, file)},
            data={**({"name": name} if name is not None else {})},
        )
        if 200 <= raw_response.status_code < 300:
            return raw_response.json()
        return _check_response(
            Response(
                raw_response.status_code,
                raw_response.content,
                raw_response.headers,
                None,
            )
        )

    def rename(self, run_id: str, filename: str, *, name: str) -> Any:
        response = runs_expected_file_update.sync_detailed(
            id=run_id,
            filename=filename,
            client=self._client,
            body=RunsExpectedFileUpdateBody(name=name),
        )
        return _check_response(response)

    def delete(self, run_id: str, filename: str) -> None:
        response = runs_expected_file_delete.sync_detailed(
            id=run_id,
            filename=filename,
            client=self._client,
        )
        return _check_response(response)

    def download(self, run_id: str, filename: str) -> bytes:
        response = runs_expected_file_get.sync_detailed(
            id=run_id,
            filename=filename,
            client=self._client,
        )
        return _check_response(response)


class RunsFilesResource:
    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def list(self, run_id: str) -> Any:
        raw_response = self._client.get_httpx_client().get(
            f"/api/v1/runs/{quote(run_id, safe='')}/files"
        )
        if 200 <= raw_response.status_code < 300:
            return raw_response.json()
        return _check_response(
            Response(
                raw_response.status_code,
                raw_response.content,
                raw_response.headers,
                None,
            )
        )

    def upload(
        self,
        run_id: str,
        file: Any,
        *,
        filename: str = "file",
        mime_type: Optional[str] = None,
    ) -> Any:
        upload_file = (
            (filename, bytes(file), mime_type or "application/octet-stream")
            if isinstance(file, (bytes, bytearray))
            else to_upload_tuple(file)
        )
        raw_response = self._client.get_httpx_client().post(
            f"/api/v1/runs/{quote(run_id, safe='')}/files",
            files={"file": upload_file},
        )
        if 200 <= raw_response.status_code < 300:
            return raw_response.json()
        return _check_response(
            Response(
                raw_response.status_code,
                raw_response.content,
                raw_response.headers,
                None,
            )
        )

    def delete(self, run_id: str, file_id: str) -> Any:
        raw_response = self._client.get_httpx_client().delete(
            f"/api/v1/runs/{quote(run_id, safe='')}/files/{quote(file_id, safe='')}"
        )
        if 200 <= raw_response.status_code < 300:
            if raw_response.status_code == 204:
                return None
            return raw_response.json()
        return _check_response(
            Response(
                raw_response.status_code,
                raw_response.content,
                raw_response.headers,
                None,
            )
        )


class RunsComparisonResource:
    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def get(self, run_id: str) -> Any:
        raw_response = self._client.get_httpx_client().get(
            f"/api/v1/runs/{quote(run_id, safe='')}/comparison"
        )
        if 200 <= raw_response.status_code < 300:
            return raw_response.json()
        return _check_response(
            Response(
                raw_response.status_code,
                raw_response.content,
                raw_response.headers,
                None,
            )
        )


class RunsTraceResource:
    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def get(self, run_id: str) -> Any:
        raw_response = self._client.get_httpx_client().get(
            f"/api/v1/runs/{quote(run_id, safe='')}/trace"
        )
        if 200 <= raw_response.status_code < 300:
            return raw_response.json()
        return _check_response(
            Response(
                raw_response.status_code,
                raw_response.content,
                raw_response.headers,
                None,
            )
        )


class RunsArtifactsResource:
    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def download(self, run_id: str, artifact_path: str) -> bytes:
        raw_response = self._client.get_httpx_client().get(
            f"/api/v1/runs/{quote(run_id, safe='')}/artifact/{_quote_artifact_path(artifact_path)}"
        )
        if 200 <= raw_response.status_code < 300:
            return raw_response.content
        return _check_response(
            Response(
                raw_response.status_code,
                raw_response.content,
                raw_response.headers,
                None,
            )
        )

    def download_zip(
        self,
        run_id: str,
        *,
        files: Optional[str] = None,
        token: Optional[str] = None,
    ) -> bytes:
        params = {
            **({"files": files} if files is not None else {}),
            **({"token": token} if token is not None else {}),
        }
        raw_response = self._client.get_httpx_client().get(
            f"/api/v1/runs/{quote(run_id, safe='')}/files-zip",
            params=params,
        )
        if 200 <= raw_response.status_code < 300:
            return raw_response.content
        return _check_response(
            Response(
                raw_response.status_code,
                raw_response.content,
                raw_response.headers,
                None,
            )
        )


def _is_workflow_run(run: Any) -> bool:
    return isinstance(run, dict) and isinstance(run.get("stepExecutions"), list)


def _step_name(step: dict[str, Any]) -> str:
    return str(step.get("stepName") or step.get("name") or step.get("id") or "")


def _compare_workflow_runs(
    reference_run_id: str,
    reference: dict[str, Any],
    run_id: str,
    target: dict[str, Any],
    step: Optional[str],
) -> dict[str, Any]:
    wanted = [s.strip() for s in step.split(",") if s.strip()] if step else []
    target_steps = {
        _step_name(s): s for s in target.get("stepExecutions", []) if isinstance(s, dict)
    }
    steps = []
    for ref_step in reference.get("stepExecutions", []):
        if not isinstance(ref_step, dict):
            continue
        name = _step_name(ref_step)
        if wanted and name not in wanted:
            continue
        target_step = target_steps.get(name)
        ref_output = ref_step.get("outputData", ref_step.get("output"))
        target_output = (
            target_step.get("outputData", target_step.get("output"))
            if isinstance(target_step, dict)
            else None
        )
        steps.append(
            {
                "stepName": name,
                "referenceStatus": str(ref_step.get("status") or ""),
                "targetStatus": str(target_step.get("status") if target_step else "missing"),
                "outputState": "match" if ref_output == target_output else "diff",
            }
        )
    return {
        "status": (
            "pass"
            if all(s["targetStatus"] != "missing" and s["outputState"] == "match" for s in steps)
            else "fail"
        ),
        "runId": run_id,
        "comparedWithRunId": reference_run_id,
        "steps": steps,
    }


def _names(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    return [
        str(item.get("name"))
        for item in value
        if isinstance(item, dict) and item.get("name")
    ]


def _comparable_name(value: str, normalize_dates: bool) -> str:
    if not normalize_dates:
        return value
    import re

    return re.sub(r"\d{8}", "<date>", re.sub(r"\d{4}-\d{2}-\d{2}", "<date>", value))


def _diff_json(expected: Any, actual: Any, base_path: str = "$") -> list[dict[str, str]]:
    if expected is None or expected == actual:
        return []
    if isinstance(expected, dict) and isinstance(actual, dict):
        diffs: list[dict[str, str]] = []
        for key in sorted(set(expected.keys()) | set(actual.keys())):
            path = f"{base_path}.{key}"
            if key not in actual:
                diffs.append({"path": path, "type": "missing"})
            elif key not in expected:
                diffs.append({"path": path, "type": "extra"})
            else:
                diffs.extend(_diff_json(expected[key], actual[key], path))
        return diffs
    return [{"path": base_path, "type": "changed"}]


def _compare_artifact_runs(
    reference_run_id: str,
    reference: Any,
    run_id: str,
    target: Any,
    *,
    mode: str,
    normalize_dates: bool,
) -> dict[str, Any]:
    reference_run = reference if isinstance(reference, dict) else {}
    target_run = target if isinstance(target, dict) else {}
    expected_value = reference_run.get("output") if mode == "baseline" else reference_run.get("expected")
    expected_files = _names(
        reference_run.get("resultFiles") if mode == "baseline" else reference_run.get("expectedFiles")
    )
    output_files = _names(target_run.get("resultFiles"))
    missing = [
        name
        for name in expected_files
        if not any(
            _comparable_name(out, normalize_dates) == _comparable_name(name, normalize_dates)
            for out in output_files
        )
    ]
    extra = [
        name
        for name in output_files
        if not any(
            _comparable_name(exp, normalize_dates) == _comparable_name(name, normalize_dates)
            for exp in expected_files
        )
    ]
    matched = [
        {
            "expected": name,
            "actual": next(
                (
                    out
                    for out in output_files
                    if _comparable_name(out, normalize_dates)
                    == _comparable_name(name, normalize_dates)
                ),
                name,
            ),
        }
        for name in expected_files
        if name not in missing
    ]
    json_differences = _diff_json(expected_value, target_run.get("output"))
    return {
        "status": "pass" if not json_differences and not missing and not extra else "fail",
        "runId": run_id,
        "comparedWithRunId": reference_run_id,
        "mode": mode,
        "jsonDifferences": json_differences,
        "matchedFiles": matched,
        "missingFiles": missing,
        "extraFiles": extra,
    }


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
    """Agent operations: list, get, create, update, versions, files, and email triggers."""

    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client
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

    def versions(self, agent_id: str) -> ListAgentVersionsResponse:
        response = agents_versions_list.sync_detailed(
            agent_id=agent_id,
            client=self._client,
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
        response = agents_update.sync_detailed(
            agent_id=agent_id, client=self._client, body=body
        )
        return _check_response(response)


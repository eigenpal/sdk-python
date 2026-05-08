from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.run_workflow_body import RunWorkflowBody
from ...models.run_workflow_response import RunWorkflowResponse
from ...models.workflows_run_files_body import WorkflowsRunFilesBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body:    RunWorkflowBody  |     WorkflowsRunFilesBody  | Unset = UNSET,
    version: str | Unset = UNSET,
    wait_for_completion: int | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["version"] = version

    params["wait_for_completion"] = wait_for_completion


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/workflows/{id}/run".format(id=quote(str(id), safe=""),),
        "params": params,
    }

    if isinstance(body, RunWorkflowBody):
        _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"
    if isinstance(body, WorkflowsRunFilesBody):
        _kwargs["files"] = body.to_multipart()


        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | RunWorkflowResponse | None:
    if response.status_code == 201:
        response_201 = RunWorkflowResponse.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = ApiErrorEnvelope.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ApiErrorEnvelope.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ApiErrorEnvelope.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ApiErrorEnvelope.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = ApiErrorEnvelope.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = ApiErrorEnvelope.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | RunWorkflowResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body:    RunWorkflowBody  |     WorkflowsRunFilesBody  | Unset = UNSET,
    version: str | Unset = UNSET,
    wait_for_completion: int | Unset = UNSET,

) -> Response[ApiErrorEnvelope | RunWorkflowResponse]:
    """ Execute a workflow (async or sync)

     Enqueues a workflow execution. Returns 201 with `{ executionId }` by default. Pass
    `wait_for_completion=<seconds>` (max 60) to hold the connection until the run reaches a terminal
    state; the body then also includes `status`, `result`, and `error`. File inputs are uploaded as
    `multipart/form-data` (each file as a top-level form field; `_json` field carries scalar inputs).

    Args:
        id (str): Workflow id (e.g. `wf_abc123`) or slug (e.g. `extract-invoice`, the workflow
            `name`).
        version (str | Unset): Version id, or "latest" (default)
        wait_for_completion (int | Unset): Seconds to hold the connection waiting for completion
            (max 60). Omit for async.
        body (RunWorkflowBody):
        body (WorkflowsRunFilesBody): Multipart upload. Each file field becomes an input file; a
            `_json` text field provides scalar inputs as JSON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | RunWorkflowResponse]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
version=version,
wait_for_completion=wait_for_completion,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body:    RunWorkflowBody  |     WorkflowsRunFilesBody  | Unset = UNSET,
    version: str | Unset = UNSET,
    wait_for_completion: int | Unset = UNSET,

) -> ApiErrorEnvelope | RunWorkflowResponse | None:
    """ Execute a workflow (async or sync)

     Enqueues a workflow execution. Returns 201 with `{ executionId }` by default. Pass
    `wait_for_completion=<seconds>` (max 60) to hold the connection until the run reaches a terminal
    state; the body then also includes `status`, `result`, and `error`. File inputs are uploaded as
    `multipart/form-data` (each file as a top-level form field; `_json` field carries scalar inputs).

    Args:
        id (str): Workflow id (e.g. `wf_abc123`) or slug (e.g. `extract-invoice`, the workflow
            `name`).
        version (str | Unset): Version id, or "latest" (default)
        wait_for_completion (int | Unset): Seconds to hold the connection waiting for completion
            (max 60). Omit for async.
        body (RunWorkflowBody):
        body (WorkflowsRunFilesBody): Multipart upload. Each file field becomes an input file; a
            `_json` text field provides scalar inputs as JSON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | RunWorkflowResponse
     """


    return sync_detailed(
        id=id,
client=client,
body=body,
version=version,
wait_for_completion=wait_for_completion,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body:    RunWorkflowBody  |     WorkflowsRunFilesBody  | Unset = UNSET,
    version: str | Unset = UNSET,
    wait_for_completion: int | Unset = UNSET,

) -> Response[ApiErrorEnvelope | RunWorkflowResponse]:
    """ Execute a workflow (async or sync)

     Enqueues a workflow execution. Returns 201 with `{ executionId }` by default. Pass
    `wait_for_completion=<seconds>` (max 60) to hold the connection until the run reaches a terminal
    state; the body then also includes `status`, `result`, and `error`. File inputs are uploaded as
    `multipart/form-data` (each file as a top-level form field; `_json` field carries scalar inputs).

    Args:
        id (str): Workflow id (e.g. `wf_abc123`) or slug (e.g. `extract-invoice`, the workflow
            `name`).
        version (str | Unset): Version id, or "latest" (default)
        wait_for_completion (int | Unset): Seconds to hold the connection waiting for completion
            (max 60). Omit for async.
        body (RunWorkflowBody):
        body (WorkflowsRunFilesBody): Multipart upload. Each file field becomes an input file; a
            `_json` text field provides scalar inputs as JSON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | RunWorkflowResponse]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
version=version,
wait_for_completion=wait_for_completion,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body:    RunWorkflowBody  |     WorkflowsRunFilesBody  | Unset = UNSET,
    version: str | Unset = UNSET,
    wait_for_completion: int | Unset = UNSET,

) -> ApiErrorEnvelope | RunWorkflowResponse | None:
    """ Execute a workflow (async or sync)

     Enqueues a workflow execution. Returns 201 with `{ executionId }` by default. Pass
    `wait_for_completion=<seconds>` (max 60) to hold the connection until the run reaches a terminal
    state; the body then also includes `status`, `result`, and `error`. File inputs are uploaded as
    `multipart/form-data` (each file as a top-level form field; `_json` field carries scalar inputs).

    Args:
        id (str): Workflow id (e.g. `wf_abc123`) or slug (e.g. `extract-invoice`, the workflow
            `name`).
        version (str | Unset): Version id, or "latest" (default)
        wait_for_completion (int | Unset): Seconds to hold the connection waiting for completion
            (max 60). Omit for async.
        body (RunWorkflowBody):
        body (WorkflowsRunFilesBody): Multipart upload. Each file field becomes an input file; a
            `_json` text field provides scalar inputs as JSON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | RunWorkflowResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
version=version,
wait_for_completion=wait_for_completion,

    )).parsed

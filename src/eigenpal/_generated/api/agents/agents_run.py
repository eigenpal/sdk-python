from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agents_run_files_body import AgentsRunFilesBody
from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.run_agent_body import RunAgentBody
from ...models.run_agent_response import RunAgentResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    agent_id: str,
    *,
    body:    RunAgentBody  |     AgentsRunFilesBody  | Unset = UNSET,
    wait_for_completion: int | Unset = UNSET,
    source_ref: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["wait_for_completion"] = wait_for_completion

    params["sourceRef"] = source_ref


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/agents/{agent_id}/run".format(agent_id=quote(str(agent_id), safe=""),),
        "params": params,
    }

    if isinstance(body, RunAgentBody):
        _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"
    if isinstance(body, AgentsRunFilesBody):
        _kwargs["files"] = body.to_multipart()


        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | RunAgentResponse | None:
    if response.status_code == 200:
        response_200 = RunAgentResponse.from_dict(response.json())



        return response_200

    if response.status_code == 202:
        response_202 = RunAgentResponse.from_dict(response.json())



        return response_202

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | RunAgentResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body:    RunAgentBody  |     AgentsRunFilesBody  | Unset = UNSET,
    wait_for_completion: int | Unset = UNSET,
    source_ref: str | Unset = UNSET,

) -> Response[ApiErrorEnvelope | RunAgentResponse]:
    """ Run an agent

     Enqueues an agent run. Returns 202 with `{ runId }` by default. Pass `wait_for_completion=<seconds>`
    to hold the connection until the run reaches a terminal state. File inputs are uploaded as
    multipart/form-data.

    Args:
        agent_id (str): Agent id or slug
        wait_for_completion (int | Unset): Seconds to hold the connection waiting for completion
            (max 600). Omit for async.
        source_ref (str | Unset): Git source ref to resolve for this run. Defaults to latest.
            Supports latest, main, exact versions/tags such as 1.2.3, semver ranges such as 1.2.x or
            1.x, and exact commit SHAs. Example: latest.
        body (RunAgentBody):
        body (AgentsRunFilesBody): Multipart upload. Each file field becomes an input file;
            `_json` carries scalar inputs as JSON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | RunAgentResponse]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
body=body,
wait_for_completion=wait_for_completion,
source_ref=source_ref,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body:    RunAgentBody  |     AgentsRunFilesBody  | Unset = UNSET,
    wait_for_completion: int | Unset = UNSET,
    source_ref: str | Unset = UNSET,

) -> ApiErrorEnvelope | RunAgentResponse | None:
    """ Run an agent

     Enqueues an agent run. Returns 202 with `{ runId }` by default. Pass `wait_for_completion=<seconds>`
    to hold the connection until the run reaches a terminal state. File inputs are uploaded as
    multipart/form-data.

    Args:
        agent_id (str): Agent id or slug
        wait_for_completion (int | Unset): Seconds to hold the connection waiting for completion
            (max 600). Omit for async.
        source_ref (str | Unset): Git source ref to resolve for this run. Defaults to latest.
            Supports latest, main, exact versions/tags such as 1.2.3, semver ranges such as 1.2.x or
            1.x, and exact commit SHAs. Example: latest.
        body (RunAgentBody):
        body (AgentsRunFilesBody): Multipart upload. Each file field becomes an input file;
            `_json` carries scalar inputs as JSON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | RunAgentResponse
     """


    return sync_detailed(
        agent_id=agent_id,
client=client,
body=body,
wait_for_completion=wait_for_completion,
source_ref=source_ref,

    ).parsed

async def asyncio_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body:    RunAgentBody  |     AgentsRunFilesBody  | Unset = UNSET,
    wait_for_completion: int | Unset = UNSET,
    source_ref: str | Unset = UNSET,

) -> Response[ApiErrorEnvelope | RunAgentResponse]:
    """ Run an agent

     Enqueues an agent run. Returns 202 with `{ runId }` by default. Pass `wait_for_completion=<seconds>`
    to hold the connection until the run reaches a terminal state. File inputs are uploaded as
    multipart/form-data.

    Args:
        agent_id (str): Agent id or slug
        wait_for_completion (int | Unset): Seconds to hold the connection waiting for completion
            (max 600). Omit for async.
        source_ref (str | Unset): Git source ref to resolve for this run. Defaults to latest.
            Supports latest, main, exact versions/tags such as 1.2.3, semver ranges such as 1.2.x or
            1.x, and exact commit SHAs. Example: latest.
        body (RunAgentBody):
        body (AgentsRunFilesBody): Multipart upload. Each file field becomes an input file;
            `_json` carries scalar inputs as JSON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | RunAgentResponse]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
body=body,
wait_for_completion=wait_for_completion,
source_ref=source_ref,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body:    RunAgentBody  |     AgentsRunFilesBody  | Unset = UNSET,
    wait_for_completion: int | Unset = UNSET,
    source_ref: str | Unset = UNSET,

) -> ApiErrorEnvelope | RunAgentResponse | None:
    """ Run an agent

     Enqueues an agent run. Returns 202 with `{ runId }` by default. Pass `wait_for_completion=<seconds>`
    to hold the connection until the run reaches a terminal state. File inputs are uploaded as
    multipart/form-data.

    Args:
        agent_id (str): Agent id or slug
        wait_for_completion (int | Unset): Seconds to hold the connection waiting for completion
            (max 600). Omit for async.
        source_ref (str | Unset): Git source ref to resolve for this run. Defaults to latest.
            Supports latest, main, exact versions/tags such as 1.2.3, semver ranges such as 1.2.x or
            1.x, and exact commit SHAs. Example: latest.
        body (RunAgentBody):
        body (AgentsRunFilesBody): Multipart upload. Each file field becomes an input file;
            `_json` carries scalar inputs as JSON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | RunAgentResponse
     """


    return (await asyncio_detailed(
        agent_id=agent_id,
client=client,
body=body,
wait_for_completion=wait_for_completion,
source_ref=source_ref,

    )).parsed

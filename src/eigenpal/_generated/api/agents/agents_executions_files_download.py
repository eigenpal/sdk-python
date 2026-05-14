from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agents_executions_files_download_kind import AgentsExecutionsFilesDownloadKind
from ...models.api_error_envelope import ApiErrorEnvelope
from typing import cast



def _get_kwargs(
    execution_id: str,
    kind: AgentsExecutionsFilesDownloadKind,
    filename: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/agents/executions/{execution_id}/files/{kind}/{filename}".format(execution_id=quote(str(execution_id), safe=""),kind=quote(str(kind), safe=""),filename=quote(str(filename), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ApiErrorEnvelope | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ApiErrorEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    execution_id: str,
    kind: AgentsExecutionsFilesDownloadKind,
    filename: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | ApiErrorEnvelope]:
    """ Download an execution file

     Downloads an input file, output file, issues.md, or trace.jsonl attached to an agent execution.

    Args:
        execution_id (str):
        kind (AgentsExecutionsFilesDownloadKind):
        filename (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiErrorEnvelope]
     """


    kwargs = _get_kwargs(
        execution_id=execution_id,
kind=kind,
filename=filename,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    execution_id: str,
    kind: AgentsExecutionsFilesDownloadKind,
    filename: str,
    *,
    client: AuthenticatedClient | Client,

) -> Any | ApiErrorEnvelope | None:
    """ Download an execution file

     Downloads an input file, output file, issues.md, or trace.jsonl attached to an agent execution.

    Args:
        execution_id (str):
        kind (AgentsExecutionsFilesDownloadKind):
        filename (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiErrorEnvelope
     """


    return sync_detailed(
        execution_id=execution_id,
kind=kind,
filename=filename,
client=client,

    ).parsed

async def asyncio_detailed(
    execution_id: str,
    kind: AgentsExecutionsFilesDownloadKind,
    filename: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | ApiErrorEnvelope]:
    """ Download an execution file

     Downloads an input file, output file, issues.md, or trace.jsonl attached to an agent execution.

    Args:
        execution_id (str):
        kind (AgentsExecutionsFilesDownloadKind):
        filename (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiErrorEnvelope]
     """


    kwargs = _get_kwargs(
        execution_id=execution_id,
kind=kind,
filename=filename,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    execution_id: str,
    kind: AgentsExecutionsFilesDownloadKind,
    filename: str,
    *,
    client: AuthenticatedClient | Client,

) -> Any | ApiErrorEnvelope | None:
    """ Download an execution file

     Downloads an input file, output file, issues.md, or trace.jsonl attached to an agent execution.

    Args:
        execution_id (str):
        kind (AgentsExecutionsFilesDownloadKind):
        filename (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiErrorEnvelope
     """


    return (await asyncio_detailed(
        execution_id=execution_id,
kind=kind,
filename=filename,
client=client,

    )).parsed

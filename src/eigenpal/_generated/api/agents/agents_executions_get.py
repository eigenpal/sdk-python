from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agent_execution_response import AgentExecutionResponse
from ...models.api_error_envelope import ApiErrorEnvelope
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    execution_id: str,
    *,
    include: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["include"] = include


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/agents/executions/{execution_id}".format(execution_id=quote(str(execution_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentExecutionResponse | ApiErrorEnvelope | None:
    if response.status_code == 200:
        response_200 = AgentExecutionResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AgentExecutionResponse | ApiErrorEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    include: str | Unset = UNSET,

) -> Response[AgentExecutionResponse | ApiErrorEnvelope]:
    """ Get agent execution

     Returns one agent execution by id.

    Args:
        execution_id (str): Execution id
        include (str | Unset): Comma-separated optional sections, e.g. files

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentExecutionResponse | ApiErrorEnvelope]
     """


    kwargs = _get_kwargs(
        execution_id=execution_id,
include=include,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    include: str | Unset = UNSET,

) -> AgentExecutionResponse | ApiErrorEnvelope | None:
    """ Get agent execution

     Returns one agent execution by id.

    Args:
        execution_id (str): Execution id
        include (str | Unset): Comma-separated optional sections, e.g. files

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentExecutionResponse | ApiErrorEnvelope
     """


    return sync_detailed(
        execution_id=execution_id,
client=client,
include=include,

    ).parsed

async def asyncio_detailed(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    include: str | Unset = UNSET,

) -> Response[AgentExecutionResponse | ApiErrorEnvelope]:
    """ Get agent execution

     Returns one agent execution by id.

    Args:
        execution_id (str): Execution id
        include (str | Unset): Comma-separated optional sections, e.g. files

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentExecutionResponse | ApiErrorEnvelope]
     """


    kwargs = _get_kwargs(
        execution_id=execution_id,
include=include,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    include: str | Unset = UNSET,

) -> AgentExecutionResponse | ApiErrorEnvelope | None:
    """ Get agent execution

     Returns one agent execution by id.

    Args:
        execution_id (str): Execution id
        include (str | Unset): Comma-separated optional sections, e.g. files

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentExecutionResponse | ApiErrorEnvelope
     """


    return (await asyncio_detailed(
        execution_id=execution_id,
client=client,
include=include,

    )).parsed

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.list_agent_executions_response import ListAgentExecutionsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    agent_id: str,
    *,
    status: str | Unset = UNSET,
    batch_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["status"] = status

    params["batchId"] = batch_id

    params["limit"] = limit

    params["offset"] = offset


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/agents/{agent_id}/executions".format(agent_id=quote(str(agent_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | ListAgentExecutionsResponse | None:
    if response.status_code == 200:
        response_200 = ListAgentExecutionsResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | ListAgentExecutionsResponse]:
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
    status: str | Unset = UNSET,
    batch_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> Response[ApiErrorEnvelope | ListAgentExecutionsResponse]:
    """ List agent executions

     Returns executions for an agent, optionally filtered by status or experiment batch.

    Args:
        agent_id (str): Agent id or slug
        status (str | Unset): Execution status filter
        batch_id (str | Unset): Experiment batch id filter
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | ListAgentExecutionsResponse]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
status=status,
batch_id=batch_id,
limit=limit,
offset=offset,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    batch_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> ApiErrorEnvelope | ListAgentExecutionsResponse | None:
    """ List agent executions

     Returns executions for an agent, optionally filtered by status or experiment batch.

    Args:
        agent_id (str): Agent id or slug
        status (str | Unset): Execution status filter
        batch_id (str | Unset): Experiment batch id filter
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | ListAgentExecutionsResponse
     """


    return sync_detailed(
        agent_id=agent_id,
client=client,
status=status,
batch_id=batch_id,
limit=limit,
offset=offset,

    ).parsed

async def asyncio_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    batch_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> Response[ApiErrorEnvelope | ListAgentExecutionsResponse]:
    """ List agent executions

     Returns executions for an agent, optionally filtered by status or experiment batch.

    Args:
        agent_id (str): Agent id or slug
        status (str | Unset): Execution status filter
        batch_id (str | Unset): Experiment batch id filter
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | ListAgentExecutionsResponse]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
status=status,
batch_id=batch_id,
limit=limit,
offset=offset,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    batch_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> ApiErrorEnvelope | ListAgentExecutionsResponse | None:
    """ List agent executions

     Returns executions for an agent, optionally filtered by status or experiment batch.

    Args:
        agent_id (str): Agent id or slug
        status (str | Unset): Execution status filter
        batch_id (str | Unset): Experiment batch id filter
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | ListAgentExecutionsResponse
     """


    return (await asyncio_detailed(
        agent_id=agent_id,
client=client,
status=status,
batch_id=batch_id,
limit=limit,
offset=offset,

    )).parsed

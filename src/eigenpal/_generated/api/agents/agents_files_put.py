from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agents_files_put_body import AgentsFilesPutBody
from ...models.agents_files_put_response_409 import AgentsFilesPutResponse409
from ...models.api_error_envelope import ApiErrorEnvelope
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    agent_id: str,
    *,
    body: AgentsFilesPutBody,
    path: str | Unset = UNSET,
    prefix: str | Unset = UNSET,
    ref: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["path"] = path

    params["prefix"] = prefix

    params["ref"] = ref


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/agents/{agent_id}/files".format(agent_id=quote(str(agent_id), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentsFilesPutResponse409 | ApiErrorEnvelope | None:
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

    if response.status_code == 409:
        response_409 = AgentsFilesPutResponse409.from_dict(response.json())



        return response_409

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AgentsFilesPutResponse409 | ApiErrorEnvelope]:
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
    body: AgentsFilesPutBody,
    path: str | Unset = UNSET,
    prefix: str | Unset = UNSET,
    ref: str | Unset = UNSET,

) -> Response[AgentsFilesPutResponse409 | ApiErrorEnvelope]:
    """ Upload one agent file (deprecated)

     Agent source is Git-backed. Use Git push or the builder instead.

    Args:
        agent_id (str): Agent id or slug
        path (str | Unset):
        prefix (str | Unset):
        ref (str | Unset): Git ref (default main)
        body (AgentsFilesPutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentsFilesPutResponse409 | ApiErrorEnvelope]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
body=body,
path=path,
prefix=prefix,
ref=ref,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgentsFilesPutBody,
    path: str | Unset = UNSET,
    prefix: str | Unset = UNSET,
    ref: str | Unset = UNSET,

) -> AgentsFilesPutResponse409 | ApiErrorEnvelope | None:
    """ Upload one agent file (deprecated)

     Agent source is Git-backed. Use Git push or the builder instead.

    Args:
        agent_id (str): Agent id or slug
        path (str | Unset):
        prefix (str | Unset):
        ref (str | Unset): Git ref (default main)
        body (AgentsFilesPutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentsFilesPutResponse409 | ApiErrorEnvelope
     """


    return sync_detailed(
        agent_id=agent_id,
client=client,
body=body,
path=path,
prefix=prefix,
ref=ref,

    ).parsed

async def asyncio_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgentsFilesPutBody,
    path: str | Unset = UNSET,
    prefix: str | Unset = UNSET,
    ref: str | Unset = UNSET,

) -> Response[AgentsFilesPutResponse409 | ApiErrorEnvelope]:
    """ Upload one agent file (deprecated)

     Agent source is Git-backed. Use Git push or the builder instead.

    Args:
        agent_id (str): Agent id or slug
        path (str | Unset):
        prefix (str | Unset):
        ref (str | Unset): Git ref (default main)
        body (AgentsFilesPutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentsFilesPutResponse409 | ApiErrorEnvelope]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
body=body,
path=path,
prefix=prefix,
ref=ref,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgentsFilesPutBody,
    path: str | Unset = UNSET,
    prefix: str | Unset = UNSET,
    ref: str | Unset = UNSET,

) -> AgentsFilesPutResponse409 | ApiErrorEnvelope | None:
    """ Upload one agent file (deprecated)

     Agent source is Git-backed. Use Git push or the builder instead.

    Args:
        agent_id (str): Agent id or slug
        path (str | Unset):
        prefix (str | Unset):
        ref (str | Unset): Git ref (default main)
        body (AgentsFilesPutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentsFilesPutResponse409 | ApiErrorEnvelope
     """


    return (await asyncio_detailed(
        agent_id=agent_id,
client=client,
body=body,
path=path,
prefix=prefix,
ref=ref,

    )).parsed

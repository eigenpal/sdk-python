from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agents_files_upload_batch_body import AgentsFilesUploadBatchBody
from ...models.agents_files_upload_batch_response_409 import AgentsFilesUploadBatchResponse409
from ...models.api_error_envelope import ApiErrorEnvelope
from typing import cast



def _get_kwargs(
    agent_id: str,
    *,
    body: AgentsFilesUploadBatchBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/agents/{agent_id}/files".format(agent_id=quote(str(agent_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentsFilesUploadBatchResponse409 | ApiErrorEnvelope | None:
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
        response_409 = AgentsFilesUploadBatchResponse409.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AgentsFilesUploadBatchResponse409 | ApiErrorEnvelope]:
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
    body: AgentsFilesUploadBatchBody,

) -> Response[AgentsFilesUploadBatchResponse409 | ApiErrorEnvelope]:
    """ Upload agent files (deprecated)

     Agent source is Git-backed. Use Git push or the builder instead.

    Args:
        agent_id (str): Agent id or slug
        body (AgentsFilesUploadBatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentsFilesUploadBatchResponse409 | ApiErrorEnvelope]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgentsFilesUploadBatchBody,

) -> AgentsFilesUploadBatchResponse409 | ApiErrorEnvelope | None:
    """ Upload agent files (deprecated)

     Agent source is Git-backed. Use Git push or the builder instead.

    Args:
        agent_id (str): Agent id or slug
        body (AgentsFilesUploadBatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentsFilesUploadBatchResponse409 | ApiErrorEnvelope
     """


    return sync_detailed(
        agent_id=agent_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgentsFilesUploadBatchBody,

) -> Response[AgentsFilesUploadBatchResponse409 | ApiErrorEnvelope]:
    """ Upload agent files (deprecated)

     Agent source is Git-backed. Use Git push or the builder instead.

    Args:
        agent_id (str): Agent id or slug
        body (AgentsFilesUploadBatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentsFilesUploadBatchResponse409 | ApiErrorEnvelope]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgentsFilesUploadBatchBody,

) -> AgentsFilesUploadBatchResponse409 | ApiErrorEnvelope | None:
    """ Upload agent files (deprecated)

     Agent source is Git-backed. Use Git push or the builder instead.

    Args:
        agent_id (str): Agent id or slug
        body (AgentsFilesUploadBatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentsFilesUploadBatchResponse409 | ApiErrorEnvelope
     """


    return (await asyncio_detailed(
        agent_id=agent_id,
client=client,
body=body,

    )).parsed

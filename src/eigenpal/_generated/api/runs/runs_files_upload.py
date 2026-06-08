from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.runs_files_upload_body import RunsFilesUploadBody
from ...models.runs_files_upload_response_201 import RunsFilesUploadResponse201
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: RunsFilesUploadBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/runs/{id}/files".format(id=quote(str(id), safe=""),),
    }

    _kwargs["files"] = body.to_multipart()



    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | RunsFilesUploadResponse201 | None:
    if response.status_code == 201:
        response_201 = RunsFilesUploadResponse201.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | RunsFilesUploadResponse201]:
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
    body: RunsFilesUploadBody,

) -> Response[ApiErrorEnvelope | RunsFilesUploadResponse201]:
    """ Upload run input file

     Upload a DB-backed workflow run input file. This endpoint is for workflow runs before execution
    starts; agent run downloads use artifacts.

    Args:
        id (str):
        body (RunsFilesUploadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | RunsFilesUploadResponse201]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RunsFilesUploadBody,

) -> ApiErrorEnvelope | RunsFilesUploadResponse201 | None:
    """ Upload run input file

     Upload a DB-backed workflow run input file. This endpoint is for workflow runs before execution
    starts; agent run downloads use artifacts.

    Args:
        id (str):
        body (RunsFilesUploadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | RunsFilesUploadResponse201
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RunsFilesUploadBody,

) -> Response[ApiErrorEnvelope | RunsFilesUploadResponse201]:
    """ Upload run input file

     Upload a DB-backed workflow run input file. This endpoint is for workflow runs before execution
    starts; agent run downloads use artifacts.

    Args:
        id (str):
        body (RunsFilesUploadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | RunsFilesUploadResponse201]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RunsFilesUploadBody,

) -> ApiErrorEnvelope | RunsFilesUploadResponse201 | None:
    """ Upload run input file

     Upload a DB-backed workflow run input file. This endpoint is for workflow runs before execution
    starts; agent run downloads use artifacts.

    Args:
        id (str):
        body (RunsFilesUploadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | RunsFilesUploadResponse201
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed

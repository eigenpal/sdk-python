from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.created_template import CreatedTemplate
from ...models.template_file_reference_request import TemplateFileReferenceRequest
from typing import cast



def _get_kwargs(
    *,
    body: TemplateFileReferenceRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}






    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/templates",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | CreatedTemplate | None:
    if response.status_code == 201:
        response_201 = CreatedTemplate.from_dict(response.json())



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

    if response.status_code == 413:
        response_413 = ApiErrorEnvelope.from_dict(response.json())



        return response_413

    if response.status_code == 422:
        response_422 = ApiErrorEnvelope.from_dict(response.json())



        return response_422

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | CreatedTemplate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TemplateFileReferenceRequest,

) -> Response[ApiErrorEnvelope | CreatedTemplate]:
    """ Upload template

     Create a stable `tmpl_…` resource and its first immutable content revision from a reusable `fileId`.
    Public SDK helpers `create(file)` and `createFromFileId(fileId)` upload through the Files API when
    needed, then send this JSON body. Generated clients send `{ fileId }` JSON only. The HTTP route
    still accepts a multipart `file` for CLI/internal use; that path is not generated into the public
    SDKs.

    Args:
        body (TemplateFileReferenceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | CreatedTemplate]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: TemplateFileReferenceRequest,

) -> ApiErrorEnvelope | CreatedTemplate | None:
    """ Upload template

     Create a stable `tmpl_…` resource and its first immutable content revision from a reusable `fileId`.
    Public SDK helpers `create(file)` and `createFromFileId(fileId)` upload through the Files API when
    needed, then send this JSON body. Generated clients send `{ fileId }` JSON only. The HTTP route
    still accepts a multipart `file` for CLI/internal use; that path is not generated into the public
    SDKs.

    Args:
        body (TemplateFileReferenceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | CreatedTemplate
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TemplateFileReferenceRequest,

) -> Response[ApiErrorEnvelope | CreatedTemplate]:
    """ Upload template

     Create a stable `tmpl_…` resource and its first immutable content revision from a reusable `fileId`.
    Public SDK helpers `create(file)` and `createFromFileId(fileId)` upload through the Files API when
    needed, then send this JSON body. Generated clients send `{ fileId }` JSON only. The HTTP route
    still accepts a multipart `file` for CLI/internal use; that path is not generated into the public
    SDKs.

    Args:
        body (TemplateFileReferenceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | CreatedTemplate]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TemplateFileReferenceRequest,

) -> ApiErrorEnvelope | CreatedTemplate | None:
    """ Upload template

     Create a stable `tmpl_…` resource and its first immutable content revision from a reusable `fileId`.
    Public SDK helpers `create(file)` and `createFromFileId(fileId)` upload through the Files API when
    needed, then send this JSON body. Generated clients send `{ fileId }` JSON only. The HTTP route
    still accepts a multipart `file` for CLI/internal use; that path is not generated into the public
    SDKs.

    Args:
        body (TemplateFileReferenceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | CreatedTemplate
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed

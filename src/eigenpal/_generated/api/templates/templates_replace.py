from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.template import Template
from ...models.template_replace_request import TemplateReplaceRequest
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: TemplateReplaceRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}






    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/templates/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | Template | None:
    if response.status_code == 200:
        response_200 = Template.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | Template]:
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
    body: TemplateReplaceRequest,

) -> Response[ApiErrorEnvelope | Template]:
    """ Create template revision

     Append an immutable revision and advance the logical template pointer from a reusable `fileId`.
    Public SDK helpers `replace(file)` and `replaceFromFileId(fileId)` upload through the Files API when
    needed, then send this JSON body. Generated clients send `{ fileId }` JSON only. The HTTP route
    still accepts a multipart `file` for CLI/internal use; that path is not generated into the public
    SDKs.

    Args:
        id (str): Logical template id (tmpl_…).
        body (TemplateReplaceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | Template]
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
    body: TemplateReplaceRequest,

) -> ApiErrorEnvelope | Template | None:
    """ Create template revision

     Append an immutable revision and advance the logical template pointer from a reusable `fileId`.
    Public SDK helpers `replace(file)` and `replaceFromFileId(fileId)` upload through the Files API when
    needed, then send this JSON body. Generated clients send `{ fileId }` JSON only. The HTTP route
    still accepts a multipart `file` for CLI/internal use; that path is not generated into the public
    SDKs.

    Args:
        id (str): Logical template id (tmpl_…).
        body (TemplateReplaceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | Template
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
    body: TemplateReplaceRequest,

) -> Response[ApiErrorEnvelope | Template]:
    """ Create template revision

     Append an immutable revision and advance the logical template pointer from a reusable `fileId`.
    Public SDK helpers `replace(file)` and `replaceFromFileId(fileId)` upload through the Files API when
    needed, then send this JSON body. Generated clients send `{ fileId }` JSON only. The HTTP route
    still accepts a multipart `file` for CLI/internal use; that path is not generated into the public
    SDKs.

    Args:
        id (str): Logical template id (tmpl_…).
        body (TemplateReplaceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | Template]
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
    body: TemplateReplaceRequest,

) -> ApiErrorEnvelope | Template | None:
    """ Create template revision

     Append an immutable revision and advance the logical template pointer from a reusable `fileId`.
    Public SDK helpers `replace(file)` and `replaceFromFileId(fileId)` upload through the Files API when
    needed, then send this JSON body. Generated clients send `{ fileId }` JSON only. The HTTP route
    still accepts a multipart `file` for CLI/internal use; that path is not generated into the public
    SDKs.

    Args:
        id (str): Logical template id (tmpl_…).
        body (TemplateReplaceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | Template
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed

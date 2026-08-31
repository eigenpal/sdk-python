from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.template_staging_request import TemplateStagingRequest
from ...models.template_staging_response import TemplateStagingResponse
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: TemplateStagingRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}






    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/templates/{id}/staging".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | TemplateStagingResponse | None:
    if response.status_code == 200:
        response_200 = TemplateStagingResponse.from_dict(response.json())



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

    if response.status_code == 409:
        response_409 = ApiErrorEnvelope.from_dict(response.json())



        return response_409

    if response.status_code == 413:
        response_413 = ApiErrorEnvelope.from_dict(response.json())



        return response_413

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | TemplateStagingResponse]:
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
    body: TemplateStagingRequest,

) -> Response[ApiErrorEnvelope | TemplateStagingResponse]:
    """ Finalize or hard-clean a staged template

     Consume the one-time cleanupProof issued on a staged create. `finalize` makes the template live so
    later deletion keeps pinned revisions. `cleanup` hard-removes only unpublished resources from that
    staging attempt. Normal DELETE is unchanged and never takes this path.

    Args:
        id (str): Logical template id (tmpl_…).
        body (TemplateStagingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | TemplateStagingResponse]
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
    body: TemplateStagingRequest,

) -> ApiErrorEnvelope | TemplateStagingResponse | None:
    """ Finalize or hard-clean a staged template

     Consume the one-time cleanupProof issued on a staged create. `finalize` makes the template live so
    later deletion keeps pinned revisions. `cleanup` hard-removes only unpublished resources from that
    staging attempt. Normal DELETE is unchanged and never takes this path.

    Args:
        id (str): Logical template id (tmpl_…).
        body (TemplateStagingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | TemplateStagingResponse
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
    body: TemplateStagingRequest,

) -> Response[ApiErrorEnvelope | TemplateStagingResponse]:
    """ Finalize or hard-clean a staged template

     Consume the one-time cleanupProof issued on a staged create. `finalize` makes the template live so
    later deletion keeps pinned revisions. `cleanup` hard-removes only unpublished resources from that
    staging attempt. Normal DELETE is unchanged and never takes this path.

    Args:
        id (str): Logical template id (tmpl_…).
        body (TemplateStagingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | TemplateStagingResponse]
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
    body: TemplateStagingRequest,

) -> ApiErrorEnvelope | TemplateStagingResponse | None:
    """ Finalize or hard-clean a staged template

     Consume the one-time cleanupProof issued on a staged create. `finalize` makes the template live so
    later deletion keeps pinned revisions. `cleanup` hard-removes only unpublished resources from that
    staging attempt. Normal DELETE is unchanged and never takes this path.

    Args:
        id (str): Logical template id (tmpl_…).
        body (TemplateStagingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | TemplateStagingResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed

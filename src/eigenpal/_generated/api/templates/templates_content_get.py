from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    revision_id: str | Unset = UNSET,

) -> dict[str, Any]:




    params: dict[str, Any] = {}

    params["revisionId"] = revision_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/templates/{id}/content".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ApiErrorEnvelope | bytes | None:
    if response.status_code == 200:
        response_200 = response.content
        return response_200

    if response.status_code == 302:
        response_302 = cast(Any, None)
        return response_302

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ApiErrorEnvelope | bytes]:
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
    revision_id: str | Unset = UNSET,

) -> Response[Any | ApiErrorEnvelope | bytes]:
    """ Download template content

     Download current bytes while the logical template exists, or a specific immutable revision using
    `revisionId`. Pinned revision downloads remain available after logical template deletion. Large
    objects may 302 to a short-lived signed storage URL.

    Args:
        id (str): Logical template id (tmpl_…).
        revision_id (str | Unset): Immutable revision id (tmpr_…). Omit for the current content.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiErrorEnvelope | bytes]
     """


    kwargs = _get_kwargs(
        id=id,
revision_id=revision_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    revision_id: str | Unset = UNSET,

) -> Any | ApiErrorEnvelope | bytes | None:
    """ Download template content

     Download current bytes while the logical template exists, or a specific immutable revision using
    `revisionId`. Pinned revision downloads remain available after logical template deletion. Large
    objects may 302 to a short-lived signed storage URL.

    Args:
        id (str): Logical template id (tmpl_…).
        revision_id (str | Unset): Immutable revision id (tmpr_…). Omit for the current content.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiErrorEnvelope | bytes
     """


    return sync_detailed(
        id=id,
client=client,
revision_id=revision_id,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    revision_id: str | Unset = UNSET,

) -> Response[Any | ApiErrorEnvelope | bytes]:
    """ Download template content

     Download current bytes while the logical template exists, or a specific immutable revision using
    `revisionId`. Pinned revision downloads remain available after logical template deletion. Large
    objects may 302 to a short-lived signed storage URL.

    Args:
        id (str): Logical template id (tmpl_…).
        revision_id (str | Unset): Immutable revision id (tmpr_…). Omit for the current content.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiErrorEnvelope | bytes]
     """


    kwargs = _get_kwargs(
        id=id,
revision_id=revision_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    revision_id: str | Unset = UNSET,

) -> Any | ApiErrorEnvelope | bytes | None:
    """ Download template content

     Download current bytes while the logical template exists, or a specific immutable revision using
    `revisionId`. Pinned revision downloads remain available after logical template deletion. Large
    objects may 302 to a short-lived signed storage URL.

    Args:
        id (str): Logical template id (tmpl_…).
        revision_id (str | Unset): Immutable revision id (tmpr_…). Omit for the current content.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiErrorEnvelope | bytes
     """


    return (await asyncio_detailed(
        id=id,
client=client,
revision_id=revision_id,

    )).parsed

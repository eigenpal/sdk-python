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
    example_ids: str | Unset = UNSET,

) -> dict[str, Any]:




    params: dict[str, Any] = {}

    params["exampleIds"] = example_ids


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/automations/{id}/dataset/export".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | bytes | None:
    if response.status_code == 200:
        response_200 = response.content
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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | bytes]:
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
    example_ids: str | Unset = UNSET,

) -> Response[ApiErrorEnvelope | bytes]:
    """ Export automation dataset

     Download the automation dataset as a ZIP archive. The archive uses the examples/<name>/input and
    examples/<name>/expected folder convention, so it can be re-imported into another automation or
    environment.

    Args:
        id (str): Automation id or typed alias.
        example_ids (str | Unset): Optional comma-separated dataset example ids to export. Omit to
            export the full dataset.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | bytes]
     """


    kwargs = _get_kwargs(
        id=id,
example_ids=example_ids,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    example_ids: str | Unset = UNSET,

) -> ApiErrorEnvelope | bytes | None:
    """ Export automation dataset

     Download the automation dataset as a ZIP archive. The archive uses the examples/<name>/input and
    examples/<name>/expected folder convention, so it can be re-imported into another automation or
    environment.

    Args:
        id (str): Automation id or typed alias.
        example_ids (str | Unset): Optional comma-separated dataset example ids to export. Omit to
            export the full dataset.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | bytes
     """


    return sync_detailed(
        id=id,
client=client,
example_ids=example_ids,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    example_ids: str | Unset = UNSET,

) -> Response[ApiErrorEnvelope | bytes]:
    """ Export automation dataset

     Download the automation dataset as a ZIP archive. The archive uses the examples/<name>/input and
    examples/<name>/expected folder convention, so it can be re-imported into another automation or
    environment.

    Args:
        id (str): Automation id or typed alias.
        example_ids (str | Unset): Optional comma-separated dataset example ids to export. Omit to
            export the full dataset.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | bytes]
     """


    kwargs = _get_kwargs(
        id=id,
example_ids=example_ids,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    example_ids: str | Unset = UNSET,

) -> ApiErrorEnvelope | bytes | None:
    """ Export automation dataset

     Download the automation dataset as a ZIP archive. The archive uses the examples/<name>/input and
    examples/<name>/expected folder convention, so it can be re-imported into another automation or
    environment.

    Args:
        id (str): Automation id or typed alias.
        example_ids (str | Unset): Optional comma-separated dataset example ids to export. Omit to
            export the full dataset.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | bytes
     """


    return (await asyncio_detailed(
        id=id,
client=client,
example_ids=example_ids,

    )).parsed

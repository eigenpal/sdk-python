from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.dataset_example import DatasetExample
from typing import cast



def _get_kwargs(
    id: str,
    example_id: str,

) -> dict[str, Any]:






    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/automations/{id}/examples/{example_id}".format(id=quote(str(id), safe=""),example_id=quote(str(example_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | DatasetExample | None:
    if response.status_code == 200:
        response_200 = DatasetExample.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | DatasetExample]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    example_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ApiErrorEnvelope | DatasetExample]:
    """ Delete dataset example

     Delete one dataset example from the automation dataset. This removes the example from future
    experiments.

    Args:
        id (str): Automation id or typed alias.
        example_id (str): Dataset example id. Agent examples may use deterministic name-derived
            ids returned by list/create responses.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | DatasetExample]
     """


    kwargs = _get_kwargs(
        id=id,
example_id=example_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    example_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> ApiErrorEnvelope | DatasetExample | None:
    """ Delete dataset example

     Delete one dataset example from the automation dataset. This removes the example from future
    experiments.

    Args:
        id (str): Automation id or typed alias.
        example_id (str): Dataset example id. Agent examples may use deterministic name-derived
            ids returned by list/create responses.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | DatasetExample
     """


    return sync_detailed(
        id=id,
example_id=example_id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    example_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ApiErrorEnvelope | DatasetExample]:
    """ Delete dataset example

     Delete one dataset example from the automation dataset. This removes the example from future
    experiments.

    Args:
        id (str): Automation id or typed alias.
        example_id (str): Dataset example id. Agent examples may use deterministic name-derived
            ids returned by list/create responses.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | DatasetExample]
     """


    kwargs = _get_kwargs(
        id=id,
example_id=example_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    example_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> ApiErrorEnvelope | DatasetExample | None:
    """ Delete dataset example

     Delete one dataset example from the automation dataset. This removes the example from future
    experiments.

    Args:
        id (str): Automation id or typed alias.
        example_id (str): Dataset example id. Agent examples may use deterministic name-derived
            ids returned by list/create responses.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | DatasetExample
     """


    return (await asyncio_detailed(
        id=id,
example_id=example_id,
client=client,

    )).parsed

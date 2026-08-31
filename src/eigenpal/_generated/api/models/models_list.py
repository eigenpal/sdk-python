from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.list_models_response import ListModelsResponse
from ...models.models_list_capability import ModelsListCapability
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    capability: ModelsListCapability | Unset = UNSET,

) -> dict[str, Any]:




    params: dict[str, Any] = {}

    json_capability: str | Unset = UNSET
    if not isinstance(capability, Unset):
        json_capability = capability.value

    params["capability"] = json_capability


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/models",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | ListModelsResponse | None:
    if response.status_code == 200:
        response_200 = ListModelsResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | ListModelsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    capability: ModelsListCapability | Unset = UNSET,

) -> Response[ApiErrorEnvelope | ListModelsResponse]:
    """ List configured models

     List text, vision, and OCR models configured for this tenant's environment from the workspace model
    catalog. This is a cheap read-only inventory: it does not call providers. `health` is `configured`
    or `unconfigured` from local credentials, never a live probe. Secrets and provider endpoints are
    never returned.

    Args:
        capability (ModelsListCapability | Unset): Return only models that support this capability
            (`text`, `vision`, or `ocr`).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | ListModelsResponse]
     """


    kwargs = _get_kwargs(
        capability=capability,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    capability: ModelsListCapability | Unset = UNSET,

) -> ApiErrorEnvelope | ListModelsResponse | None:
    """ List configured models

     List text, vision, and OCR models configured for this tenant's environment from the workspace model
    catalog. This is a cheap read-only inventory: it does not call providers. `health` is `configured`
    or `unconfigured` from local credentials, never a live probe. Secrets and provider endpoints are
    never returned.

    Args:
        capability (ModelsListCapability | Unset): Return only models that support this capability
            (`text`, `vision`, or `ocr`).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | ListModelsResponse
     """


    return sync_detailed(
        client=client,
capability=capability,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    capability: ModelsListCapability | Unset = UNSET,

) -> Response[ApiErrorEnvelope | ListModelsResponse]:
    """ List configured models

     List text, vision, and OCR models configured for this tenant's environment from the workspace model
    catalog. This is a cheap read-only inventory: it does not call providers. `health` is `configured`
    or `unconfigured` from local credentials, never a live probe. Secrets and provider endpoints are
    never returned.

    Args:
        capability (ModelsListCapability | Unset): Return only models that support this capability
            (`text`, `vision`, or `ocr`).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | ListModelsResponse]
     """


    kwargs = _get_kwargs(
        capability=capability,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    capability: ModelsListCapability | Unset = UNSET,

) -> ApiErrorEnvelope | ListModelsResponse | None:
    """ List configured models

     List text, vision, and OCR models configured for this tenant's environment from the workspace model
    catalog. This is a cheap read-only inventory: it does not call providers. `health` is `configured`
    or `unconfigured` from local credentials, never a live probe. Secrets and provider endpoints are
    never returned.

    Args:
        capability (ModelsListCapability | Unset): Return only models that support this capability
            (`text`, `vision`, or `ocr`).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | ListModelsResponse
     """


    return (await asyncio_detailed(
        client=client,
capability=capability,

    )).parsed

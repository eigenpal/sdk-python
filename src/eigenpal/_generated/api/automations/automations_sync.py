from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.automations_sync_response_200 import AutomationsSyncResponse200
from typing import cast



def _get_kwargs(
    id: str,

) -> dict[str, Any]:






    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/automations/{id}/sync".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | AutomationsSyncResponse200 | None:
    if response.status_code == 200:
        response_200 = AutomationsSyncResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | AutomationsSyncResponse200]:
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

) -> Response[ApiErrorEnvelope | AutomationsSyncResponse200]:
    """ Sync automation from latest Git release

     Reconciles automation registry metadata and trigger projections from the latest Git source release.
    This operation is idempotent for unchanged source state: repeated calls against the same latest
    release leave the same automation registry state and may repeat the same warnings. Requires a Bearer
    API token for the organization and a user-backed API key. It does not publish source; it reads the
    already-published latest release manifest. Versioned targets are rejected with 400, missing
    organization/source/release/manifest state returns 404, invalid manifests return 400, and provider
    or persistence failures return 5xx.

    Args:
        id (str): Automation target to sync, such as agents.invoice-agent or workflows.extract. Do
            not include a version; sync always uses the latest Git release.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | AutomationsSyncResponse200]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> ApiErrorEnvelope | AutomationsSyncResponse200 | None:
    """ Sync automation from latest Git release

     Reconciles automation registry metadata and trigger projections from the latest Git source release.
    This operation is idempotent for unchanged source state: repeated calls against the same latest
    release leave the same automation registry state and may repeat the same warnings. Requires a Bearer
    API token for the organization and a user-backed API key. It does not publish source; it reads the
    already-published latest release manifest. Versioned targets are rejected with 400, missing
    organization/source/release/manifest state returns 404, invalid manifests return 400, and provider
    or persistence failures return 5xx.

    Args:
        id (str): Automation target to sync, such as agents.invoice-agent or workflows.extract. Do
            not include a version; sync always uses the latest Git release.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | AutomationsSyncResponse200
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ApiErrorEnvelope | AutomationsSyncResponse200]:
    """ Sync automation from latest Git release

     Reconciles automation registry metadata and trigger projections from the latest Git source release.
    This operation is idempotent for unchanged source state: repeated calls against the same latest
    release leave the same automation registry state and may repeat the same warnings. Requires a Bearer
    API token for the organization and a user-backed API key. It does not publish source; it reads the
    already-published latest release manifest. Versioned targets are rejected with 400, missing
    organization/source/release/manifest state returns 404, invalid manifests return 400, and provider
    or persistence failures return 5xx.

    Args:
        id (str): Automation target to sync, such as agents.invoice-agent or workflows.extract. Do
            not include a version; sync always uses the latest Git release.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | AutomationsSyncResponse200]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> ApiErrorEnvelope | AutomationsSyncResponse200 | None:
    """ Sync automation from latest Git release

     Reconciles automation registry metadata and trigger projections from the latest Git source release.
    This operation is idempotent for unchanged source state: repeated calls against the same latest
    release leave the same automation registry state and may repeat the same warnings. Requires a Bearer
    API token for the organization and a user-backed API key. It does not publish source; it reads the
    already-published latest release manifest. Versioned targets are rejected with 400, missing
    organization/source/release/manifest state returns 404, invalid manifests return 400, and provider
    or persistence failures return 5xx.

    Args:
        id (str): Automation target to sync, such as agents.invoice-agent or workflows.extract. Do
            not include a version; sync always uses the latest Git release.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | AutomationsSyncResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed

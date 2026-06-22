from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.automations_experiments_list_response_200 import AutomationsExperimentsListResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,

) -> dict[str, Any]:




    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["fromDate"] = from_date

    params["toDate"] = to_date


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/automations/{id}/experiments".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | AutomationsExperimentsListResponse200 | None:
    if response.status_code == 200:
        response_200 = AutomationsExperimentsListResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | AutomationsExperimentsListResponse200]:
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
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,

) -> Response[ApiErrorEnvelope | AutomationsExperimentsListResponse200]:
    """ List experiments

     List experiment batches for one automation. Each experiment runs selected dataset examples and
    records automated evaluator scores.

    Args:
        id (str): Automation id or typed alias.
        limit (int | Unset): Maximum number of experiment batches to return.
        offset (int | Unset): Zero-based offset for paging through experiment batches.
        from_date (str | Unset): Filter to experiment batches created at or after this date or
            relative date.
        to_date (str | Unset): Filter to experiment batches created at or before this date or
            relative date.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | AutomationsExperimentsListResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
limit=limit,
offset=offset,
from_date=from_date,
to_date=to_date,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,

) -> ApiErrorEnvelope | AutomationsExperimentsListResponse200 | None:
    """ List experiments

     List experiment batches for one automation. Each experiment runs selected dataset examples and
    records automated evaluator scores.

    Args:
        id (str): Automation id or typed alias.
        limit (int | Unset): Maximum number of experiment batches to return.
        offset (int | Unset): Zero-based offset for paging through experiment batches.
        from_date (str | Unset): Filter to experiment batches created at or after this date or
            relative date.
        to_date (str | Unset): Filter to experiment batches created at or before this date or
            relative date.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | AutomationsExperimentsListResponse200
     """


    return sync_detailed(
        id=id,
client=client,
limit=limit,
offset=offset,
from_date=from_date,
to_date=to_date,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,

) -> Response[ApiErrorEnvelope | AutomationsExperimentsListResponse200]:
    """ List experiments

     List experiment batches for one automation. Each experiment runs selected dataset examples and
    records automated evaluator scores.

    Args:
        id (str): Automation id or typed alias.
        limit (int | Unset): Maximum number of experiment batches to return.
        offset (int | Unset): Zero-based offset for paging through experiment batches.
        from_date (str | Unset): Filter to experiment batches created at or after this date or
            relative date.
        to_date (str | Unset): Filter to experiment batches created at or before this date or
            relative date.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | AutomationsExperimentsListResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
limit=limit,
offset=offset,
from_date=from_date,
to_date=to_date,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,

) -> ApiErrorEnvelope | AutomationsExperimentsListResponse200 | None:
    """ List experiments

     List experiment batches for one automation. Each experiment runs selected dataset examples and
    records automated evaluator scores.

    Args:
        id (str): Automation id or typed alias.
        limit (int | Unset): Maximum number of experiment batches to return.
        offset (int | Unset): Zero-based offset for paging through experiment batches.
        from_date (str | Unset): Filter to experiment batches created at or after this date or
            relative date.
        to_date (str | Unset): Filter to experiment batches created at or before this date or
            relative date.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | AutomationsExperimentsListResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
limit=limit,
offset=offset,
from_date=from_date,
to_date=to_date,

    )).parsed

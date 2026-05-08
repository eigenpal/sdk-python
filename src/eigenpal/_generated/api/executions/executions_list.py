from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.list_executions_response import ListExecutionsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    workflow_id: str | Unset = UNSET,
    status: str | Unset = UNSET,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    example_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["workflowId"] = workflow_id

    params["status"] = status

    params["fromDate"] = from_date

    params["toDate"] = to_date

    params["exampleId"] = example_id

    params["limit"] = limit

    params["offset"] = offset


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/executions",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | ListExecutionsResponse | None:
    if response.status_code == 200:
        response_200 = ListExecutionsResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | ListExecutionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    workflow_id: str | Unset = UNSET,
    status: str | Unset = UNSET,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    example_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> Response[ApiErrorEnvelope | ListExecutionsResponse]:
    """ List executions

     Returns executions across the tenant, optionally filtered by workflow, status, date range, or eval
    example. Paginated.

    Args:
        workflow_id (str | Unset): Comma-separated list of workflow ids to filter by
        status (str | Unset): Comma-separated list of execution statuses to filter by
        from_date (str | Unset): ISO-8601 timestamp or relative expression (e.g. "now()-7d") for
            the lower bound on `createdAt`
        to_date (str | Unset): Upper bound on `createdAt`
        example_id (str | Unset): Filter to executions launched from a specific eval example
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | ListExecutionsResponse]
     """


    kwargs = _get_kwargs(
        workflow_id=workflow_id,
status=status,
from_date=from_date,
to_date=to_date,
example_id=example_id,
limit=limit,
offset=offset,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    workflow_id: str | Unset = UNSET,
    status: str | Unset = UNSET,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    example_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> ApiErrorEnvelope | ListExecutionsResponse | None:
    """ List executions

     Returns executions across the tenant, optionally filtered by workflow, status, date range, or eval
    example. Paginated.

    Args:
        workflow_id (str | Unset): Comma-separated list of workflow ids to filter by
        status (str | Unset): Comma-separated list of execution statuses to filter by
        from_date (str | Unset): ISO-8601 timestamp or relative expression (e.g. "now()-7d") for
            the lower bound on `createdAt`
        to_date (str | Unset): Upper bound on `createdAt`
        example_id (str | Unset): Filter to executions launched from a specific eval example
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | ListExecutionsResponse
     """


    return sync_detailed(
        client=client,
workflow_id=workflow_id,
status=status,
from_date=from_date,
to_date=to_date,
example_id=example_id,
limit=limit,
offset=offset,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    workflow_id: str | Unset = UNSET,
    status: str | Unset = UNSET,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    example_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> Response[ApiErrorEnvelope | ListExecutionsResponse]:
    """ List executions

     Returns executions across the tenant, optionally filtered by workflow, status, date range, or eval
    example. Paginated.

    Args:
        workflow_id (str | Unset): Comma-separated list of workflow ids to filter by
        status (str | Unset): Comma-separated list of execution statuses to filter by
        from_date (str | Unset): ISO-8601 timestamp or relative expression (e.g. "now()-7d") for
            the lower bound on `createdAt`
        to_date (str | Unset): Upper bound on `createdAt`
        example_id (str | Unset): Filter to executions launched from a specific eval example
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | ListExecutionsResponse]
     """


    kwargs = _get_kwargs(
        workflow_id=workflow_id,
status=status,
from_date=from_date,
to_date=to_date,
example_id=example_id,
limit=limit,
offset=offset,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    workflow_id: str | Unset = UNSET,
    status: str | Unset = UNSET,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    example_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> ApiErrorEnvelope | ListExecutionsResponse | None:
    """ List executions

     Returns executions across the tenant, optionally filtered by workflow, status, date range, or eval
    example. Paginated.

    Args:
        workflow_id (str | Unset): Comma-separated list of workflow ids to filter by
        status (str | Unset): Comma-separated list of execution statuses to filter by
        from_date (str | Unset): ISO-8601 timestamp or relative expression (e.g. "now()-7d") for
            the lower bound on `createdAt`
        to_date (str | Unset): Upper bound on `createdAt`
        example_id (str | Unset): Filter to executions launched from a specific eval example
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | ListExecutionsResponse
     """


    return (await asyncio_detailed(
        client=client,
workflow_id=workflow_id,
status=status,
from_date=from_date,
to_date=to_date,
example_id=example_id,
limit=limit,
offset=offset,

    )).parsed

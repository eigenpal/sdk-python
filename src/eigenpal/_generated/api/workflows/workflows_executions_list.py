from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.list_workflow_executions_response import ListWorkflowExecutionsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    status: str | Unset = UNSET,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    example_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["status"] = status

    params["fromDate"] = from_date

    params["toDate"] = to_date

    params["exampleId"] = example_id

    params["limit"] = limit

    params["offset"] = offset


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/workflows/{id}/executions".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | ListWorkflowExecutionsResponse | None:
    if response.status_code == 200:
        response_200 = ListWorkflowExecutionsResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | ListWorkflowExecutionsResponse]:
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
    status: str | Unset = UNSET,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    example_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> Response[ApiErrorEnvelope | ListWorkflowExecutionsResponse]:
    """ List workflow executions

     Returns executions for a workflow, optionally filtered by status, date range, or eval example.
    Paginated.

    Args:
        id (str): Workflow id (e.g. wf_abc123)
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
        Response[ApiErrorEnvelope | ListWorkflowExecutionsResponse]
     """


    kwargs = _get_kwargs(
        id=id,
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
    id: str,
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    example_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> ApiErrorEnvelope | ListWorkflowExecutionsResponse | None:
    """ List workflow executions

     Returns executions for a workflow, optionally filtered by status, date range, or eval example.
    Paginated.

    Args:
        id (str): Workflow id (e.g. wf_abc123)
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
        ApiErrorEnvelope | ListWorkflowExecutionsResponse
     """


    return sync_detailed(
        id=id,
client=client,
status=status,
from_date=from_date,
to_date=to_date,
example_id=example_id,
limit=limit,
offset=offset,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    example_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> Response[ApiErrorEnvelope | ListWorkflowExecutionsResponse]:
    """ List workflow executions

     Returns executions for a workflow, optionally filtered by status, date range, or eval example.
    Paginated.

    Args:
        id (str): Workflow id (e.g. wf_abc123)
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
        Response[ApiErrorEnvelope | ListWorkflowExecutionsResponse]
     """


    kwargs = _get_kwargs(
        id=id,
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
    id: str,
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    example_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> ApiErrorEnvelope | ListWorkflowExecutionsResponse | None:
    """ List workflow executions

     Returns executions for a workflow, optionally filtered by status, date range, or eval example.
    Paginated.

    Args:
        id (str): Workflow id (e.g. wf_abc123)
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
        ApiErrorEnvelope | ListWorkflowExecutionsResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
status=status,
from_date=from_date,
to_date=to_date,
example_id=example_id,
limit=limit,
offset=offset,

    )).parsed

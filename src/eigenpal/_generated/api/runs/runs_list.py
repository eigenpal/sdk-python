from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.runs_list_response import RunsListResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    type_: str | Unset = UNSET,
    source: str | Unset = UNSET,
    status: str | Unset = UNSET,
    trigger: str | Unset = UNSET,
    triggered_by: str | Unset = UNSET,
    source_ref: str | Unset = UNSET,
    batch_id: str | Unset = UNSET,
    example_id: str | Unset = UNSET,
    example_id_contains: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    created_after: str | Unset = UNSET,
    created_before: str | Unset = UNSET,
    completed_after: str | Unset = UNSET,
    completed_before: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    ids: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["type"] = type_

    params["source"] = source

    params["status"] = status

    params["trigger"] = trigger

    params["triggeredBy"] = triggered_by

    params["sourceRef"] = source_ref

    params["batchId"] = batch_id

    params["exampleId"] = example_id

    params["exampleIdContains"] = example_id_contains

    params["from"] = from_

    params["to"] = to

    params["createdAfter"] = created_after

    params["createdBefore"] = created_before

    params["completedAfter"] = completed_after

    params["completedBefore"] = completed_before

    params["cursor"] = cursor

    params["offset"] = offset

    params["limit"] = limit

    params["ids"] = ids


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/runs",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | RunsListResponse | None:
    if response.status_code == 200:
        response_200 = RunsListResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | RunsListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: str | Unset = UNSET,
    source: str | Unset = UNSET,
    status: str | Unset = UNSET,
    trigger: str | Unset = UNSET,
    triggered_by: str | Unset = UNSET,
    source_ref: str | Unset = UNSET,
    batch_id: str | Unset = UNSET,
    example_id: str | Unset = UNSET,
    example_id_contains: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    created_after: str | Unset = UNSET,
    created_before: str | Unset = UNSET,
    completed_after: str | Unset = UNSET,
    completed_before: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    ids: str | Unset = UNSET,

) -> Response[ApiErrorEnvelope | RunsListResponse]:
    """ List runs

     Tenant-scoped, cursor-paginated feed of workflow and agent runs. Use type and source filters to
    scope to one runtime or resource.

    Args:
        type_ (str | Unset):
        source (str | Unset):
        status (str | Unset):
        trigger (str | Unset):
        triggered_by (str | Unset):
        source_ref (str | Unset):
        batch_id (str | Unset):
        example_id (str | Unset):
        example_id_contains (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        created_after (str | Unset):
        created_before (str | Unset):
        completed_after (str | Unset):
        completed_before (str | Unset):
        cursor (str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | RunsListResponse]
     """


    kwargs = _get_kwargs(
        type_=type_,
source=source,
status=status,
trigger=trigger,
triggered_by=triggered_by,
source_ref=source_ref,
batch_id=batch_id,
example_id=example_id,
example_id_contains=example_id_contains,
from_=from_,
to=to,
created_after=created_after,
created_before=created_before,
completed_after=completed_after,
completed_before=completed_before,
cursor=cursor,
offset=offset,
limit=limit,
ids=ids,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    type_: str | Unset = UNSET,
    source: str | Unset = UNSET,
    status: str | Unset = UNSET,
    trigger: str | Unset = UNSET,
    triggered_by: str | Unset = UNSET,
    source_ref: str | Unset = UNSET,
    batch_id: str | Unset = UNSET,
    example_id: str | Unset = UNSET,
    example_id_contains: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    created_after: str | Unset = UNSET,
    created_before: str | Unset = UNSET,
    completed_after: str | Unset = UNSET,
    completed_before: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    ids: str | Unset = UNSET,

) -> ApiErrorEnvelope | RunsListResponse | None:
    """ List runs

     Tenant-scoped, cursor-paginated feed of workflow and agent runs. Use type and source filters to
    scope to one runtime or resource.

    Args:
        type_ (str | Unset):
        source (str | Unset):
        status (str | Unset):
        trigger (str | Unset):
        triggered_by (str | Unset):
        source_ref (str | Unset):
        batch_id (str | Unset):
        example_id (str | Unset):
        example_id_contains (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        created_after (str | Unset):
        created_before (str | Unset):
        completed_after (str | Unset):
        completed_before (str | Unset):
        cursor (str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | RunsListResponse
     """


    return sync_detailed(
        client=client,
type_=type_,
source=source,
status=status,
trigger=trigger,
triggered_by=triggered_by,
source_ref=source_ref,
batch_id=batch_id,
example_id=example_id,
example_id_contains=example_id_contains,
from_=from_,
to=to,
created_after=created_after,
created_before=created_before,
completed_after=completed_after,
completed_before=completed_before,
cursor=cursor,
offset=offset,
limit=limit,
ids=ids,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: str | Unset = UNSET,
    source: str | Unset = UNSET,
    status: str | Unset = UNSET,
    trigger: str | Unset = UNSET,
    triggered_by: str | Unset = UNSET,
    source_ref: str | Unset = UNSET,
    batch_id: str | Unset = UNSET,
    example_id: str | Unset = UNSET,
    example_id_contains: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    created_after: str | Unset = UNSET,
    created_before: str | Unset = UNSET,
    completed_after: str | Unset = UNSET,
    completed_before: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    ids: str | Unset = UNSET,

) -> Response[ApiErrorEnvelope | RunsListResponse]:
    """ List runs

     Tenant-scoped, cursor-paginated feed of workflow and agent runs. Use type and source filters to
    scope to one runtime or resource.

    Args:
        type_ (str | Unset):
        source (str | Unset):
        status (str | Unset):
        trigger (str | Unset):
        triggered_by (str | Unset):
        source_ref (str | Unset):
        batch_id (str | Unset):
        example_id (str | Unset):
        example_id_contains (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        created_after (str | Unset):
        created_before (str | Unset):
        completed_after (str | Unset):
        completed_before (str | Unset):
        cursor (str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | RunsListResponse]
     """


    kwargs = _get_kwargs(
        type_=type_,
source=source,
status=status,
trigger=trigger,
triggered_by=triggered_by,
source_ref=source_ref,
batch_id=batch_id,
example_id=example_id,
example_id_contains=example_id_contains,
from_=from_,
to=to,
created_after=created_after,
created_before=created_before,
completed_after=completed_after,
completed_before=completed_before,
cursor=cursor,
offset=offset,
limit=limit,
ids=ids,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    type_: str | Unset = UNSET,
    source: str | Unset = UNSET,
    status: str | Unset = UNSET,
    trigger: str | Unset = UNSET,
    triggered_by: str | Unset = UNSET,
    source_ref: str | Unset = UNSET,
    batch_id: str | Unset = UNSET,
    example_id: str | Unset = UNSET,
    example_id_contains: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    created_after: str | Unset = UNSET,
    created_before: str | Unset = UNSET,
    completed_after: str | Unset = UNSET,
    completed_before: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    ids: str | Unset = UNSET,

) -> ApiErrorEnvelope | RunsListResponse | None:
    """ List runs

     Tenant-scoped, cursor-paginated feed of workflow and agent runs. Use type and source filters to
    scope to one runtime or resource.

    Args:
        type_ (str | Unset):
        source (str | Unset):
        status (str | Unset):
        trigger (str | Unset):
        triggered_by (str | Unset):
        source_ref (str | Unset):
        batch_id (str | Unset):
        example_id (str | Unset):
        example_id_contains (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        created_after (str | Unset):
        created_before (str | Unset):
        completed_after (str | Unset):
        completed_before (str | Unset):
        cursor (str | Unset):
        offset (int | Unset):
        limit (int | Unset):
        ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | RunsListResponse
     """


    return (await asyncio_detailed(
        client=client,
type_=type_,
source=source,
status=status,
trigger=trigger,
triggered_by=triggered_by,
source_ref=source_ref,
batch_id=batch_id,
example_id=example_id,
example_id_contains=example_id_contains,
from_=from_,
to=to,
created_after=created_after,
created_before=created_before,
completed_after=completed_after,
completed_before=completed_before,
cursor=cursor,
offset=offset,
limit=limit,
ids=ids,

    )).parsed

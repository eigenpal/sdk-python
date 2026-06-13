from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.list_workflows_response import ListWorkflowsResponse
from ...models.workflows_list_kind import WorkflowsListKind
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    search: str | Unset = UNSET,
    name: str | Unset = UNSET,
    kind: WorkflowsListKind | Unset = UNSET,
    folder_id: None | str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> dict[str, Any]:




    params: dict[str, Any] = {}

    params["search"] = search

    params["name"] = name

    json_kind: str | Unset = UNSET
    if not isinstance(kind, Unset):
        json_kind = kind.value

    params["kind"] = json_kind

    json_folder_id: None | str | Unset
    if isinstance(folder_id, Unset):
        json_folder_id = UNSET
    else:
        json_folder_id = folder_id
    params["folderId"] = json_folder_id

    params["limit"] = limit

    params["offset"] = offset


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/workflows",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | ListWorkflowsResponse | None:
    if response.status_code == 200:
        response_200 = ListWorkflowsResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | ListWorkflowsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    search: str | Unset = UNSET,
    name: str | Unset = UNSET,
    kind: WorkflowsListKind | Unset = UNSET,
    folder_id: None | str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> Response[ApiErrorEnvelope | ListWorkflowsResponse]:
    """ List workflows

     List workflows with pagination.

    Args:
        search (str | Unset): Substring match against workflow name
        name (str | Unset): Exact-match lookup by workflow name (slug)
        kind (WorkflowsListKind | Unset): Filter by workflow kind
        folder_id (None | str | Unset): Filter by folder: omit for all workflows, 'null' for
            root/unfiled only, or a folder id
        limit (int | Unset): Page size (max 100, default 50)
        offset (int | Unset): Page offset

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | ListWorkflowsResponse]
     """


    kwargs = _get_kwargs(
        search=search,
name=name,
kind=kind,
folder_id=folder_id,
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
    search: str | Unset = UNSET,
    name: str | Unset = UNSET,
    kind: WorkflowsListKind | Unset = UNSET,
    folder_id: None | str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> ApiErrorEnvelope | ListWorkflowsResponse | None:
    """ List workflows

     List workflows with pagination.

    Args:
        search (str | Unset): Substring match against workflow name
        name (str | Unset): Exact-match lookup by workflow name (slug)
        kind (WorkflowsListKind | Unset): Filter by workflow kind
        folder_id (None | str | Unset): Filter by folder: omit for all workflows, 'null' for
            root/unfiled only, or a folder id
        limit (int | Unset): Page size (max 100, default 50)
        offset (int | Unset): Page offset

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | ListWorkflowsResponse
     """


    return sync_detailed(
        client=client,
search=search,
name=name,
kind=kind,
folder_id=folder_id,
limit=limit,
offset=offset,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    search: str | Unset = UNSET,
    name: str | Unset = UNSET,
    kind: WorkflowsListKind | Unset = UNSET,
    folder_id: None | str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> Response[ApiErrorEnvelope | ListWorkflowsResponse]:
    """ List workflows

     List workflows with pagination.

    Args:
        search (str | Unset): Substring match against workflow name
        name (str | Unset): Exact-match lookup by workflow name (slug)
        kind (WorkflowsListKind | Unset): Filter by workflow kind
        folder_id (None | str | Unset): Filter by folder: omit for all workflows, 'null' for
            root/unfiled only, or a folder id
        limit (int | Unset): Page size (max 100, default 50)
        offset (int | Unset): Page offset

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | ListWorkflowsResponse]
     """


    kwargs = _get_kwargs(
        search=search,
name=name,
kind=kind,
folder_id=folder_id,
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
    search: str | Unset = UNSET,
    name: str | Unset = UNSET,
    kind: WorkflowsListKind | Unset = UNSET,
    folder_id: None | str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> ApiErrorEnvelope | ListWorkflowsResponse | None:
    """ List workflows

     List workflows with pagination.

    Args:
        search (str | Unset): Substring match against workflow name
        name (str | Unset): Exact-match lookup by workflow name (slug)
        kind (WorkflowsListKind | Unset): Filter by workflow kind
        folder_id (None | str | Unset): Filter by folder: omit for all workflows, 'null' for
            root/unfiled only, or a folder id
        limit (int | Unset): Page size (max 100, default 50)
        offset (int | Unset): Page offset

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | ListWorkflowsResponse
     """


    return (await asyncio_detailed(
        client=client,
search=search,
name=name,
kind=kind,
folder_id=folder_id,
limit=limit,
offset=offset,

    )).parsed

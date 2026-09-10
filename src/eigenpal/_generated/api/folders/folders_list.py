from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.folder import Folder
from ...models.folder_type import FolderType
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    type_: FolderType,
    parent_id: str | Unset = UNSET,
    tree: str | Unset = UNSET,

) -> dict[str, Any]:




    params: dict[str, Any] = {}

    json_type_ = type_.value
    params["type"] = json_type_

    params["parentId"] = parent_id

    params["tree"] = tree


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/folders",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | list[Folder] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_list_folders_response_item_data in (_response_200):
            componentsschemas_list_folders_response_item = Folder.from_dict(componentsschemas_list_folders_response_item_data)



            response_200.append(componentsschemas_list_folders_response_item)

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | list[Folder]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: FolderType,
    parent_id: str | Unset = UNSET,
    tree: str | Unset = UNSET,

) -> Response[ApiErrorEnvelope | list[Folder]]:
    """ List folders

     List folders in one tree. `type` is required (`workflow` or `template`). Pass `tree=true` for the
    full nested tree with counts; otherwise list direct children of `parentId` (`null` for root).
    Deleting a folder later unfiles contained workflows or templates and does not delete them.

    Args:
        type_ (FolderType):
        parent_id (str | Unset): Limit to direct children of this folder. Pass `null` for root
            folders only. Ignored when `tree=true`.
        tree (str | Unset): When `true`, return the full tree for `type` with child counts (and
            workflow previews for workflow trees).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | list[Folder]]
     """


    kwargs = _get_kwargs(
        type_=type_,
parent_id=parent_id,
tree=tree,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    type_: FolderType,
    parent_id: str | Unset = UNSET,
    tree: str | Unset = UNSET,

) -> ApiErrorEnvelope | list[Folder] | None:
    """ List folders

     List folders in one tree. `type` is required (`workflow` or `template`). Pass `tree=true` for the
    full nested tree with counts; otherwise list direct children of `parentId` (`null` for root).
    Deleting a folder later unfiles contained workflows or templates and does not delete them.

    Args:
        type_ (FolderType):
        parent_id (str | Unset): Limit to direct children of this folder. Pass `null` for root
            folders only. Ignored when `tree=true`.
        tree (str | Unset): When `true`, return the full tree for `type` with child counts (and
            workflow previews for workflow trees).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | list[Folder]
     """


    return sync_detailed(
        client=client,
type_=type_,
parent_id=parent_id,
tree=tree,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: FolderType,
    parent_id: str | Unset = UNSET,
    tree: str | Unset = UNSET,

) -> Response[ApiErrorEnvelope | list[Folder]]:
    """ List folders

     List folders in one tree. `type` is required (`workflow` or `template`). Pass `tree=true` for the
    full nested tree with counts; otherwise list direct children of `parentId` (`null` for root).
    Deleting a folder later unfiles contained workflows or templates and does not delete them.

    Args:
        type_ (FolderType):
        parent_id (str | Unset): Limit to direct children of this folder. Pass `null` for root
            folders only. Ignored when `tree=true`.
        tree (str | Unset): When `true`, return the full tree for `type` with child counts (and
            workflow previews for workflow trees).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | list[Folder]]
     """


    kwargs = _get_kwargs(
        type_=type_,
parent_id=parent_id,
tree=tree,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    type_: FolderType,
    parent_id: str | Unset = UNSET,
    tree: str | Unset = UNSET,

) -> ApiErrorEnvelope | list[Folder] | None:
    """ List folders

     List folders in one tree. `type` is required (`workflow` or `template`). Pass `tree=true` for the
    full nested tree with counts; otherwise list direct children of `parentId` (`null` for root).
    Deleting a folder later unfiles contained workflows or templates and does not delete them.

    Args:
        type_ (FolderType):
        parent_id (str | Unset): Limit to direct children of this folder. Pass `null` for root
            folders only. Ignored when `tree=true`.
        tree (str | Unset): When `true`, return the full tree for `type` with child counts (and
            workflow previews for workflow trees).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | list[Folder]
     """


    return (await asyncio_detailed(
        client=client,
type_=type_,
parent_id=parent_id,
tree=tree,

    )).parsed

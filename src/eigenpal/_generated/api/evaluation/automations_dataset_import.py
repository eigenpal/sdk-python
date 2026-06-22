from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.automation_dataset_import_multipart_request import AutomationDatasetImportMultipartRequest
from ...models.dataset_import_response_type_0 import DatasetImportResponseType0
from ...models.dataset_import_response_type_1 import DatasetImportResponseType1
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: AutomationDatasetImportMultipartRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}






    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/automations/{id}/dataset/import".format(id=quote(str(id), safe=""),),
    }

    _kwargs["files"] = body.to_multipart()



    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | DatasetImportResponseType0 | DatasetImportResponseType1 | None:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> DatasetImportResponseType0 | DatasetImportResponseType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_dataset_import_response_type_0 = DatasetImportResponseType0.from_dict(data)



                return componentsschemas_dataset_import_response_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_dataset_import_response_type_1 = DatasetImportResponseType1.from_dict(data)



            return componentsschemas_dataset_import_response_type_1

        response_200 = _parse_response_200(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | DatasetImportResponseType0 | DatasetImportResponseType1]:
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
    body: AutomationDatasetImportMultipartRequest,

) -> Response[ApiErrorEnvelope | DatasetImportResponseType0 | DatasetImportResponseType1]:
    """ Import automation dataset

     Import a dataset ZIP archive using the examples/<name>/input and examples/<name>/expected folder
    convention. Use `mode=append` for additive imports or `mode=replace` to replace the dataset.

    Args:
        id (str): Automation id or typed alias.
        body (AutomationDatasetImportMultipartRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | DatasetImportResponseType0 | DatasetImportResponseType1]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AutomationDatasetImportMultipartRequest,

) -> ApiErrorEnvelope | DatasetImportResponseType0 | DatasetImportResponseType1 | None:
    """ Import automation dataset

     Import a dataset ZIP archive using the examples/<name>/input and examples/<name>/expected folder
    convention. Use `mode=append` for additive imports or `mode=replace` to replace the dataset.

    Args:
        id (str): Automation id or typed alias.
        body (AutomationDatasetImportMultipartRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | DatasetImportResponseType0 | DatasetImportResponseType1
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AutomationDatasetImportMultipartRequest,

) -> Response[ApiErrorEnvelope | DatasetImportResponseType0 | DatasetImportResponseType1]:
    """ Import automation dataset

     Import a dataset ZIP archive using the examples/<name>/input and examples/<name>/expected folder
    convention. Use `mode=append` for additive imports or `mode=replace` to replace the dataset.

    Args:
        id (str): Automation id or typed alias.
        body (AutomationDatasetImportMultipartRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | DatasetImportResponseType0 | DatasetImportResponseType1]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AutomationDatasetImportMultipartRequest,

) -> ApiErrorEnvelope | DatasetImportResponseType0 | DatasetImportResponseType1 | None:
    """ Import automation dataset

     Import a dataset ZIP archive using the examples/<name>/input and examples/<name>/expected folder
    convention. Use `mode=append` for additive imports or `mode=replace` to replace the dataset.

    Args:
        id (str): Automation id or typed alias.
        body (AutomationDatasetImportMultipartRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | DatasetImportResponseType0 | DatasetImportResponseType1
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed

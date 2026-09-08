from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.human_review_approve_response import HumanReviewApproveResponse
from ...models.human_reviews_approve_body import HumanReviewsApproveBody
from typing import cast



def _get_kwargs(
    task_id: str,
    *,
    body: HumanReviewsApproveBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}






    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/human-reviews/{task_id}/approve".format(task_id=quote(str(task_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | HumanReviewApproveResponse | None:
    if response.status_code == 200:
        response_200 = HumanReviewApproveResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | HumanReviewApproveResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    task_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: HumanReviewsApproveBody,

) -> Response[ApiErrorEnvelope | HumanReviewApproveResponse]:
    """ Approve human review task

     Approve a complete review task and resume the paused run. Requires every required field to be
    confirmed.

    Args:
        task_id (str): Human review task id
        body (HumanReviewsApproveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | HumanReviewApproveResponse]
     """


    kwargs = _get_kwargs(
        task_id=task_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    task_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: HumanReviewsApproveBody,

) -> ApiErrorEnvelope | HumanReviewApproveResponse | None:
    """ Approve human review task

     Approve a complete review task and resume the paused run. Requires every required field to be
    confirmed.

    Args:
        task_id (str): Human review task id
        body (HumanReviewsApproveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | HumanReviewApproveResponse
     """


    return sync_detailed(
        task_id=task_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    task_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: HumanReviewsApproveBody,

) -> Response[ApiErrorEnvelope | HumanReviewApproveResponse]:
    """ Approve human review task

     Approve a complete review task and resume the paused run. Requires every required field to be
    confirmed.

    Args:
        task_id (str): Human review task id
        body (HumanReviewsApproveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | HumanReviewApproveResponse]
     """


    kwargs = _get_kwargs(
        task_id=task_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    task_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: HumanReviewsApproveBody,

) -> ApiErrorEnvelope | HumanReviewApproveResponse | None:
    """ Approve human review task

     Approve a complete review task and resume the paused run. Requires every required field to be
    confirmed.

    Args:
        task_id (str): Human review task id
        body (HumanReviewsApproveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | HumanReviewApproveResponse
     """


    return (await asyncio_detailed(
        task_id=task_id,
client=client,
body=body,

    )).parsed

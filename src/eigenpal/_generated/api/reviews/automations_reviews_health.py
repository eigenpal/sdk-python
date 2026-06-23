from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.automations_reviews_health_bucket import AutomationsReviewsHealthBucket
from ...models.run_review_health_response import RunReviewHealthResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    trigger: str | Unset = UNSET,
    triggered_by: str | Unset = UNSET,
    source_ref: str | Unset = UNSET,
    batch_id: str | Unset = UNSET,
    example_id: str | Unset = UNSET,
    example_id_contains: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    completed_after: str | Unset = UNSET,
    completed_before: str | Unset = UNSET,
    experiments: str | Unset = UNSET,
    bucket: AutomationsReviewsHealthBucket | Unset = UNSET,
    rolling_window: int | Unset = UNSET,
    min_rolling_reviews: int | Unset = UNSET,

) -> dict[str, Any]:




    params: dict[str, Any] = {}

    params["type"] = type_

    params["status"] = status

    params["trigger"] = trigger

    params["triggeredBy"] = triggered_by

    params["sourceRef"] = source_ref

    params["batchId"] = batch_id

    params["exampleId"] = example_id

    params["exampleIdContains"] = example_id_contains

    params["from"] = from_

    params["to"] = to

    params["completedAfter"] = completed_after

    params["completedBefore"] = completed_before

    params["experiments"] = experiments

    json_bucket: str | Unset = UNSET
    if not isinstance(bucket, Unset):
        json_bucket = bucket.value

    params["bucket"] = json_bucket

    params["rollingWindow"] = rolling_window

    params["minRollingReviews"] = min_rolling_reviews


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/automations/{id}/reviews/health".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | RunReviewHealthResponse | None:
    if response.status_code == 200:
        response_200 = RunReviewHealthResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | RunReviewHealthResponse]:
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
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    trigger: str | Unset = UNSET,
    triggered_by: str | Unset = UNSET,
    source_ref: str | Unset = UNSET,
    batch_id: str | Unset = UNSET,
    example_id: str | Unset = UNSET,
    example_id_contains: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    completed_after: str | Unset = UNSET,
    completed_before: str | Unset = UNSET,
    experiments: str | Unset = UNSET,
    bucket: AutomationsReviewsHealthBucket | Unset = UNSET,
    rolling_window: int | Unset = UNSET,
    min_rolling_reviews: int | Unset = UNSET,

) -> Response[ApiErrorEnvelope | RunReviewHealthResponse]:
    """ Get automation review health

     Aggregates reviewed correctness, review coverage, bucketed counts, and rolling-window confidence for
    one automation. Prefer this endpoint for single-automation monitoring dashboards.

    Args:
        id (str): Workflow id, agent id, or typed alias like workflows.slug / agents.slug.
        type_ (str | Unset): Comma-separated: workflow,agent.
        status (str | Unset): Comma-separated execution statuses.
        trigger (str | Unset): Comma-separated trigger types.
        triggered_by (str | Unset): Comma-separated user ids, or __system__ for system-triggered
            runs.
        source_ref (str | Unset):
        batch_id (str | Unset):
        example_id (str | Unset):
        example_id_contains (str | Unset):
        from_ (str | Unset): Start of the run-created time range. Defaults to now-30d.
        to (str | Unset): End of the run-created time range.
        completed_after (str | Unset):
        completed_before (str | Unset):
        experiments (str | Unset): Set to false to exclude experiment batch runs.
        bucket (AutomationsReviewsHealthBucket | Unset): Calendar bucket size for the bar chart
            series. Defaults to day.
        rolling_window (int | Unset): Number of reviewed runs per rolling correctness point.
            Defaults to 100.
        min_rolling_reviews (int | Unset): Minimum reviewed runs required before emitting rolling
            points. Defaults to 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | RunReviewHealthResponse]
     """


    kwargs = _get_kwargs(
        id=id,
type_=type_,
status=status,
trigger=trigger,
triggered_by=triggered_by,
source_ref=source_ref,
batch_id=batch_id,
example_id=example_id,
example_id_contains=example_id_contains,
from_=from_,
to=to,
completed_after=completed_after,
completed_before=completed_before,
experiments=experiments,
bucket=bucket,
rolling_window=rolling_window,
min_rolling_reviews=min_rolling_reviews,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    trigger: str | Unset = UNSET,
    triggered_by: str | Unset = UNSET,
    source_ref: str | Unset = UNSET,
    batch_id: str | Unset = UNSET,
    example_id: str | Unset = UNSET,
    example_id_contains: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    completed_after: str | Unset = UNSET,
    completed_before: str | Unset = UNSET,
    experiments: str | Unset = UNSET,
    bucket: AutomationsReviewsHealthBucket | Unset = UNSET,
    rolling_window: int | Unset = UNSET,
    min_rolling_reviews: int | Unset = UNSET,

) -> ApiErrorEnvelope | RunReviewHealthResponse | None:
    """ Get automation review health

     Aggregates reviewed correctness, review coverage, bucketed counts, and rolling-window confidence for
    one automation. Prefer this endpoint for single-automation monitoring dashboards.

    Args:
        id (str): Workflow id, agent id, or typed alias like workflows.slug / agents.slug.
        type_ (str | Unset): Comma-separated: workflow,agent.
        status (str | Unset): Comma-separated execution statuses.
        trigger (str | Unset): Comma-separated trigger types.
        triggered_by (str | Unset): Comma-separated user ids, or __system__ for system-triggered
            runs.
        source_ref (str | Unset):
        batch_id (str | Unset):
        example_id (str | Unset):
        example_id_contains (str | Unset):
        from_ (str | Unset): Start of the run-created time range. Defaults to now-30d.
        to (str | Unset): End of the run-created time range.
        completed_after (str | Unset):
        completed_before (str | Unset):
        experiments (str | Unset): Set to false to exclude experiment batch runs.
        bucket (AutomationsReviewsHealthBucket | Unset): Calendar bucket size for the bar chart
            series. Defaults to day.
        rolling_window (int | Unset): Number of reviewed runs per rolling correctness point.
            Defaults to 100.
        min_rolling_reviews (int | Unset): Minimum reviewed runs required before emitting rolling
            points. Defaults to 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | RunReviewHealthResponse
     """


    return sync_detailed(
        id=id,
client=client,
type_=type_,
status=status,
trigger=trigger,
triggered_by=triggered_by,
source_ref=source_ref,
batch_id=batch_id,
example_id=example_id,
example_id_contains=example_id_contains,
from_=from_,
to=to,
completed_after=completed_after,
completed_before=completed_before,
experiments=experiments,
bucket=bucket,
rolling_window=rolling_window,
min_rolling_reviews=min_rolling_reviews,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    trigger: str | Unset = UNSET,
    triggered_by: str | Unset = UNSET,
    source_ref: str | Unset = UNSET,
    batch_id: str | Unset = UNSET,
    example_id: str | Unset = UNSET,
    example_id_contains: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    completed_after: str | Unset = UNSET,
    completed_before: str | Unset = UNSET,
    experiments: str | Unset = UNSET,
    bucket: AutomationsReviewsHealthBucket | Unset = UNSET,
    rolling_window: int | Unset = UNSET,
    min_rolling_reviews: int | Unset = UNSET,

) -> Response[ApiErrorEnvelope | RunReviewHealthResponse]:
    """ Get automation review health

     Aggregates reviewed correctness, review coverage, bucketed counts, and rolling-window confidence for
    one automation. Prefer this endpoint for single-automation monitoring dashboards.

    Args:
        id (str): Workflow id, agent id, or typed alias like workflows.slug / agents.slug.
        type_ (str | Unset): Comma-separated: workflow,agent.
        status (str | Unset): Comma-separated execution statuses.
        trigger (str | Unset): Comma-separated trigger types.
        triggered_by (str | Unset): Comma-separated user ids, or __system__ for system-triggered
            runs.
        source_ref (str | Unset):
        batch_id (str | Unset):
        example_id (str | Unset):
        example_id_contains (str | Unset):
        from_ (str | Unset): Start of the run-created time range. Defaults to now-30d.
        to (str | Unset): End of the run-created time range.
        completed_after (str | Unset):
        completed_before (str | Unset):
        experiments (str | Unset): Set to false to exclude experiment batch runs.
        bucket (AutomationsReviewsHealthBucket | Unset): Calendar bucket size for the bar chart
            series. Defaults to day.
        rolling_window (int | Unset): Number of reviewed runs per rolling correctness point.
            Defaults to 100.
        min_rolling_reviews (int | Unset): Minimum reviewed runs required before emitting rolling
            points. Defaults to 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | RunReviewHealthResponse]
     """


    kwargs = _get_kwargs(
        id=id,
type_=type_,
status=status,
trigger=trigger,
triggered_by=triggered_by,
source_ref=source_ref,
batch_id=batch_id,
example_id=example_id,
example_id_contains=example_id_contains,
from_=from_,
to=to,
completed_after=completed_after,
completed_before=completed_before,
experiments=experiments,
bucket=bucket,
rolling_window=rolling_window,
min_rolling_reviews=min_rolling_reviews,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    trigger: str | Unset = UNSET,
    triggered_by: str | Unset = UNSET,
    source_ref: str | Unset = UNSET,
    batch_id: str | Unset = UNSET,
    example_id: str | Unset = UNSET,
    example_id_contains: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    completed_after: str | Unset = UNSET,
    completed_before: str | Unset = UNSET,
    experiments: str | Unset = UNSET,
    bucket: AutomationsReviewsHealthBucket | Unset = UNSET,
    rolling_window: int | Unset = UNSET,
    min_rolling_reviews: int | Unset = UNSET,

) -> ApiErrorEnvelope | RunReviewHealthResponse | None:
    """ Get automation review health

     Aggregates reviewed correctness, review coverage, bucketed counts, and rolling-window confidence for
    one automation. Prefer this endpoint for single-automation monitoring dashboards.

    Args:
        id (str): Workflow id, agent id, or typed alias like workflows.slug / agents.slug.
        type_ (str | Unset): Comma-separated: workflow,agent.
        status (str | Unset): Comma-separated execution statuses.
        trigger (str | Unset): Comma-separated trigger types.
        triggered_by (str | Unset): Comma-separated user ids, or __system__ for system-triggered
            runs.
        source_ref (str | Unset):
        batch_id (str | Unset):
        example_id (str | Unset):
        example_id_contains (str | Unset):
        from_ (str | Unset): Start of the run-created time range. Defaults to now-30d.
        to (str | Unset): End of the run-created time range.
        completed_after (str | Unset):
        completed_before (str | Unset):
        experiments (str | Unset): Set to false to exclude experiment batch runs.
        bucket (AutomationsReviewsHealthBucket | Unset): Calendar bucket size for the bar chart
            series. Defaults to day.
        rolling_window (int | Unset): Number of reviewed runs per rolling correctness point.
            Defaults to 100.
        min_rolling_reviews (int | Unset): Minimum reviewed runs required before emitting rolling
            points. Defaults to 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | RunReviewHealthResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
type_=type_,
status=status,
trigger=trigger,
triggered_by=triggered_by,
source_ref=source_ref,
batch_id=batch_id,
example_id=example_id,
example_id_contains=example_id_contains,
from_=from_,
to=to,
completed_after=completed_after,
completed_before=completed_before,
experiments=experiments,
bucket=bucket,
rolling_window=rolling_window,
min_rolling_reviews=min_rolling_reviews,

    )).parsed

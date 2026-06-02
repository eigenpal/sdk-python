from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agents_runs_list_feedback_rating import AgentsRunsListFeedbackRating
from ...models.agents_runs_list_feedback_status import AgentsRunsListFeedbackStatus
from ...models.agents_runs_list_order import AgentsRunsListOrder
from ...models.agents_runs_list_sort import AgentsRunsListSort
from ...models.api_error_envelope import ApiErrorEnvelope
from ...models.list_agent_runs_response import ListAgentRunsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    agent_id: str,
    *,
    status: str | Unset = UNSET,
    batch_id: str | Unset = UNSET,
    example_id: str | Unset = UNSET,
    example_id_contains: str | Unset = UNSET,
    created_after: str | Unset = UNSET,
    created_before: str | Unset = UNSET,
    completed_after: str | Unset = UNSET,
    completed_before: str | Unset = UNSET,
    source_ref: str | Unset = UNSET,
    feedback_status: AgentsRunsListFeedbackStatus | Unset = UNSET,
    feedback_rating: AgentsRunsListFeedbackRating | Unset = UNSET,
    has_feedback: bool | Unset = UNSET,
    no_feedback: bool | Unset = UNSET,
    has_expected: bool | Unset = UNSET,
    has_expected_json: bool | Unset = UNSET,
    has_expected_files: bool | Unset = UNSET,
    feedback_body_contains: str | Unset = UNSET,
    feedback_created_after: str | Unset = UNSET,
    feedback_created_before: str | Unset = UNSET,
    feedback_updated_after: str | Unset = UNSET,
    feedback_updated_before: str | Unset = UNSET,
    feedback_resolved_after: str | Unset = UNSET,
    feedback_resolved_before: str | Unset = UNSET,
    promoted_to_example: bool | Unset = UNSET,
    promoted_example_name: str | Unset = UNSET,
    since_last_resolved: bool | Unset = UNSET,
    include: str | Unset = UNSET,
    sort: AgentsRunsListSort | Unset = UNSET,
    order: AgentsRunsListOrder | Unset = UNSET,
    scan_limit: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["status"] = status

    params["batchId"] = batch_id

    params["exampleId"] = example_id

    params["exampleIdContains"] = example_id_contains

    params["createdAfter"] = created_after

    params["createdBefore"] = created_before

    params["completedAfter"] = completed_after

    params["completedBefore"] = completed_before

    params["sourceRef"] = source_ref

    json_feedback_status: str | Unset = UNSET
    if not isinstance(feedback_status, Unset):
        json_feedback_status = feedback_status.value

    params["feedbackStatus"] = json_feedback_status

    json_feedback_rating: str | Unset = UNSET
    if not isinstance(feedback_rating, Unset):
        json_feedback_rating = feedback_rating.value

    params["feedbackRating"] = json_feedback_rating

    params["hasFeedback"] = has_feedback

    params["noFeedback"] = no_feedback

    params["hasExpected"] = has_expected

    params["hasExpectedJson"] = has_expected_json

    params["hasExpectedFiles"] = has_expected_files

    params["feedbackBodyContains"] = feedback_body_contains

    params["feedbackCreatedAfter"] = feedback_created_after

    params["feedbackCreatedBefore"] = feedback_created_before

    params["feedbackUpdatedAfter"] = feedback_updated_after

    params["feedbackUpdatedBefore"] = feedback_updated_before

    params["feedbackResolvedAfter"] = feedback_resolved_after

    params["feedbackResolvedBefore"] = feedback_resolved_before

    params["promotedToExample"] = promoted_to_example

    params["promotedExampleName"] = promoted_example_name

    params["sinceLastResolved"] = since_last_resolved

    params["include"] = include

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    json_order: str | Unset = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["scanLimit"] = scan_limit

    params["limit"] = limit

    params["offset"] = offset


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/agents/{agent_id}/runs".format(agent_id=quote(str(agent_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiErrorEnvelope | ListAgentRunsResponse | None:
    if response.status_code == 200:
        response_200 = ListAgentRunsResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiErrorEnvelope | ListAgentRunsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    batch_id: str | Unset = UNSET,
    example_id: str | Unset = UNSET,
    example_id_contains: str | Unset = UNSET,
    created_after: str | Unset = UNSET,
    created_before: str | Unset = UNSET,
    completed_after: str | Unset = UNSET,
    completed_before: str | Unset = UNSET,
    source_ref: str | Unset = UNSET,
    feedback_status: AgentsRunsListFeedbackStatus | Unset = UNSET,
    feedback_rating: AgentsRunsListFeedbackRating | Unset = UNSET,
    has_feedback: bool | Unset = UNSET,
    no_feedback: bool | Unset = UNSET,
    has_expected: bool | Unset = UNSET,
    has_expected_json: bool | Unset = UNSET,
    has_expected_files: bool | Unset = UNSET,
    feedback_body_contains: str | Unset = UNSET,
    feedback_created_after: str | Unset = UNSET,
    feedback_created_before: str | Unset = UNSET,
    feedback_updated_after: str | Unset = UNSET,
    feedback_updated_before: str | Unset = UNSET,
    feedback_resolved_after: str | Unset = UNSET,
    feedback_resolved_before: str | Unset = UNSET,
    promoted_to_example: bool | Unset = UNSET,
    promoted_example_name: str | Unset = UNSET,
    since_last_resolved: bool | Unset = UNSET,
    include: str | Unset = UNSET,
    sort: AgentsRunsListSort | Unset = UNSET,
    order: AgentsRunsListOrder | Unset = UNSET,
    scan_limit: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> Response[ApiErrorEnvelope | ListAgentRunsResponse]:
    """ List agent runs

     Returns runs for an agent, optionally filtered by status or experiment batch.

    Args:
        agent_id (str): Agent id or slug
        status (str | Unset): Run status filter
        batch_id (str | Unset): Experiment batch id filter
        example_id (str | Unset): Exact dataset example id (folder name) filter
        example_id_contains (str | Unset): Substring match on dataset example id
        created_after (str | Unset): Only runs created at/after this ISO timestamp
        created_before (str | Unset): Only runs created at/before this ISO timestamp
        completed_after (str | Unset): Only runs completed at/after this ISO timestamp
        completed_before (str | Unset): Only runs completed at/before this ISO timestamp
        source_ref (str | Unset): Filter by the source ref requested when the run was created
        feedback_status (AgentsRunsListFeedbackStatus | Unset):
        feedback_rating (AgentsRunsListFeedbackRating | Unset):
        has_feedback (bool | Unset):
        no_feedback (bool | Unset):
        has_expected (bool | Unset):
        has_expected_json (bool | Unset):
        has_expected_files (bool | Unset):
        feedback_body_contains (str | Unset):
        feedback_created_after (str | Unset):
        feedback_created_before (str | Unset):
        feedback_updated_after (str | Unset):
        feedback_updated_before (str | Unset):
        feedback_resolved_after (str | Unset):
        feedback_resolved_before (str | Unset):
        promoted_to_example (bool | Unset):
        promoted_example_name (str | Unset):
        since_last_resolved (bool | Unset):
        include (str | Unset): Comma-separated extra parts: feedback, expected, files
        sort (AgentsRunsListSort | Unset):
        order (AgentsRunsListOrder | Unset):
        scan_limit (int | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | ListAgentRunsResponse]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
status=status,
batch_id=batch_id,
example_id=example_id,
example_id_contains=example_id_contains,
created_after=created_after,
created_before=created_before,
completed_after=completed_after,
completed_before=completed_before,
source_ref=source_ref,
feedback_status=feedback_status,
feedback_rating=feedback_rating,
has_feedback=has_feedback,
no_feedback=no_feedback,
has_expected=has_expected,
has_expected_json=has_expected_json,
has_expected_files=has_expected_files,
feedback_body_contains=feedback_body_contains,
feedback_created_after=feedback_created_after,
feedback_created_before=feedback_created_before,
feedback_updated_after=feedback_updated_after,
feedback_updated_before=feedback_updated_before,
feedback_resolved_after=feedback_resolved_after,
feedback_resolved_before=feedback_resolved_before,
promoted_to_example=promoted_to_example,
promoted_example_name=promoted_example_name,
since_last_resolved=since_last_resolved,
include=include,
sort=sort,
order=order,
scan_limit=scan_limit,
limit=limit,
offset=offset,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    batch_id: str | Unset = UNSET,
    example_id: str | Unset = UNSET,
    example_id_contains: str | Unset = UNSET,
    created_after: str | Unset = UNSET,
    created_before: str | Unset = UNSET,
    completed_after: str | Unset = UNSET,
    completed_before: str | Unset = UNSET,
    source_ref: str | Unset = UNSET,
    feedback_status: AgentsRunsListFeedbackStatus | Unset = UNSET,
    feedback_rating: AgentsRunsListFeedbackRating | Unset = UNSET,
    has_feedback: bool | Unset = UNSET,
    no_feedback: bool | Unset = UNSET,
    has_expected: bool | Unset = UNSET,
    has_expected_json: bool | Unset = UNSET,
    has_expected_files: bool | Unset = UNSET,
    feedback_body_contains: str | Unset = UNSET,
    feedback_created_after: str | Unset = UNSET,
    feedback_created_before: str | Unset = UNSET,
    feedback_updated_after: str | Unset = UNSET,
    feedback_updated_before: str | Unset = UNSET,
    feedback_resolved_after: str | Unset = UNSET,
    feedback_resolved_before: str | Unset = UNSET,
    promoted_to_example: bool | Unset = UNSET,
    promoted_example_name: str | Unset = UNSET,
    since_last_resolved: bool | Unset = UNSET,
    include: str | Unset = UNSET,
    sort: AgentsRunsListSort | Unset = UNSET,
    order: AgentsRunsListOrder | Unset = UNSET,
    scan_limit: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> ApiErrorEnvelope | ListAgentRunsResponse | None:
    """ List agent runs

     Returns runs for an agent, optionally filtered by status or experiment batch.

    Args:
        agent_id (str): Agent id or slug
        status (str | Unset): Run status filter
        batch_id (str | Unset): Experiment batch id filter
        example_id (str | Unset): Exact dataset example id (folder name) filter
        example_id_contains (str | Unset): Substring match on dataset example id
        created_after (str | Unset): Only runs created at/after this ISO timestamp
        created_before (str | Unset): Only runs created at/before this ISO timestamp
        completed_after (str | Unset): Only runs completed at/after this ISO timestamp
        completed_before (str | Unset): Only runs completed at/before this ISO timestamp
        source_ref (str | Unset): Filter by the source ref requested when the run was created
        feedback_status (AgentsRunsListFeedbackStatus | Unset):
        feedback_rating (AgentsRunsListFeedbackRating | Unset):
        has_feedback (bool | Unset):
        no_feedback (bool | Unset):
        has_expected (bool | Unset):
        has_expected_json (bool | Unset):
        has_expected_files (bool | Unset):
        feedback_body_contains (str | Unset):
        feedback_created_after (str | Unset):
        feedback_created_before (str | Unset):
        feedback_updated_after (str | Unset):
        feedback_updated_before (str | Unset):
        feedback_resolved_after (str | Unset):
        feedback_resolved_before (str | Unset):
        promoted_to_example (bool | Unset):
        promoted_example_name (str | Unset):
        since_last_resolved (bool | Unset):
        include (str | Unset): Comma-separated extra parts: feedback, expected, files
        sort (AgentsRunsListSort | Unset):
        order (AgentsRunsListOrder | Unset):
        scan_limit (int | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | ListAgentRunsResponse
     """


    return sync_detailed(
        agent_id=agent_id,
client=client,
status=status,
batch_id=batch_id,
example_id=example_id,
example_id_contains=example_id_contains,
created_after=created_after,
created_before=created_before,
completed_after=completed_after,
completed_before=completed_before,
source_ref=source_ref,
feedback_status=feedback_status,
feedback_rating=feedback_rating,
has_feedback=has_feedback,
no_feedback=no_feedback,
has_expected=has_expected,
has_expected_json=has_expected_json,
has_expected_files=has_expected_files,
feedback_body_contains=feedback_body_contains,
feedback_created_after=feedback_created_after,
feedback_created_before=feedback_created_before,
feedback_updated_after=feedback_updated_after,
feedback_updated_before=feedback_updated_before,
feedback_resolved_after=feedback_resolved_after,
feedback_resolved_before=feedback_resolved_before,
promoted_to_example=promoted_to_example,
promoted_example_name=promoted_example_name,
since_last_resolved=since_last_resolved,
include=include,
sort=sort,
order=order,
scan_limit=scan_limit,
limit=limit,
offset=offset,

    ).parsed

async def asyncio_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    batch_id: str | Unset = UNSET,
    example_id: str | Unset = UNSET,
    example_id_contains: str | Unset = UNSET,
    created_after: str | Unset = UNSET,
    created_before: str | Unset = UNSET,
    completed_after: str | Unset = UNSET,
    completed_before: str | Unset = UNSET,
    source_ref: str | Unset = UNSET,
    feedback_status: AgentsRunsListFeedbackStatus | Unset = UNSET,
    feedback_rating: AgentsRunsListFeedbackRating | Unset = UNSET,
    has_feedback: bool | Unset = UNSET,
    no_feedback: bool | Unset = UNSET,
    has_expected: bool | Unset = UNSET,
    has_expected_json: bool | Unset = UNSET,
    has_expected_files: bool | Unset = UNSET,
    feedback_body_contains: str | Unset = UNSET,
    feedback_created_after: str | Unset = UNSET,
    feedback_created_before: str | Unset = UNSET,
    feedback_updated_after: str | Unset = UNSET,
    feedback_updated_before: str | Unset = UNSET,
    feedback_resolved_after: str | Unset = UNSET,
    feedback_resolved_before: str | Unset = UNSET,
    promoted_to_example: bool | Unset = UNSET,
    promoted_example_name: str | Unset = UNSET,
    since_last_resolved: bool | Unset = UNSET,
    include: str | Unset = UNSET,
    sort: AgentsRunsListSort | Unset = UNSET,
    order: AgentsRunsListOrder | Unset = UNSET,
    scan_limit: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> Response[ApiErrorEnvelope | ListAgentRunsResponse]:
    """ List agent runs

     Returns runs for an agent, optionally filtered by status or experiment batch.

    Args:
        agent_id (str): Agent id or slug
        status (str | Unset): Run status filter
        batch_id (str | Unset): Experiment batch id filter
        example_id (str | Unset): Exact dataset example id (folder name) filter
        example_id_contains (str | Unset): Substring match on dataset example id
        created_after (str | Unset): Only runs created at/after this ISO timestamp
        created_before (str | Unset): Only runs created at/before this ISO timestamp
        completed_after (str | Unset): Only runs completed at/after this ISO timestamp
        completed_before (str | Unset): Only runs completed at/before this ISO timestamp
        source_ref (str | Unset): Filter by the source ref requested when the run was created
        feedback_status (AgentsRunsListFeedbackStatus | Unset):
        feedback_rating (AgentsRunsListFeedbackRating | Unset):
        has_feedback (bool | Unset):
        no_feedback (bool | Unset):
        has_expected (bool | Unset):
        has_expected_json (bool | Unset):
        has_expected_files (bool | Unset):
        feedback_body_contains (str | Unset):
        feedback_created_after (str | Unset):
        feedback_created_before (str | Unset):
        feedback_updated_after (str | Unset):
        feedback_updated_before (str | Unset):
        feedback_resolved_after (str | Unset):
        feedback_resolved_before (str | Unset):
        promoted_to_example (bool | Unset):
        promoted_example_name (str | Unset):
        since_last_resolved (bool | Unset):
        include (str | Unset): Comma-separated extra parts: feedback, expected, files
        sort (AgentsRunsListSort | Unset):
        order (AgentsRunsListOrder | Unset):
        scan_limit (int | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorEnvelope | ListAgentRunsResponse]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
status=status,
batch_id=batch_id,
example_id=example_id,
example_id_contains=example_id_contains,
created_after=created_after,
created_before=created_before,
completed_after=completed_after,
completed_before=completed_before,
source_ref=source_ref,
feedback_status=feedback_status,
feedback_rating=feedback_rating,
has_feedback=has_feedback,
no_feedback=no_feedback,
has_expected=has_expected,
has_expected_json=has_expected_json,
has_expected_files=has_expected_files,
feedback_body_contains=feedback_body_contains,
feedback_created_after=feedback_created_after,
feedback_created_before=feedback_created_before,
feedback_updated_after=feedback_updated_after,
feedback_updated_before=feedback_updated_before,
feedback_resolved_after=feedback_resolved_after,
feedback_resolved_before=feedback_resolved_before,
promoted_to_example=promoted_to_example,
promoted_example_name=promoted_example_name,
since_last_resolved=since_last_resolved,
include=include,
sort=sort,
order=order,
scan_limit=scan_limit,
limit=limit,
offset=offset,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    batch_id: str | Unset = UNSET,
    example_id: str | Unset = UNSET,
    example_id_contains: str | Unset = UNSET,
    created_after: str | Unset = UNSET,
    created_before: str | Unset = UNSET,
    completed_after: str | Unset = UNSET,
    completed_before: str | Unset = UNSET,
    source_ref: str | Unset = UNSET,
    feedback_status: AgentsRunsListFeedbackStatus | Unset = UNSET,
    feedback_rating: AgentsRunsListFeedbackRating | Unset = UNSET,
    has_feedback: bool | Unset = UNSET,
    no_feedback: bool | Unset = UNSET,
    has_expected: bool | Unset = UNSET,
    has_expected_json: bool | Unset = UNSET,
    has_expected_files: bool | Unset = UNSET,
    feedback_body_contains: str | Unset = UNSET,
    feedback_created_after: str | Unset = UNSET,
    feedback_created_before: str | Unset = UNSET,
    feedback_updated_after: str | Unset = UNSET,
    feedback_updated_before: str | Unset = UNSET,
    feedback_resolved_after: str | Unset = UNSET,
    feedback_resolved_before: str | Unset = UNSET,
    promoted_to_example: bool | Unset = UNSET,
    promoted_example_name: str | Unset = UNSET,
    since_last_resolved: bool | Unset = UNSET,
    include: str | Unset = UNSET,
    sort: AgentsRunsListSort | Unset = UNSET,
    order: AgentsRunsListOrder | Unset = UNSET,
    scan_limit: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,

) -> ApiErrorEnvelope | ListAgentRunsResponse | None:
    """ List agent runs

     Returns runs for an agent, optionally filtered by status or experiment batch.

    Args:
        agent_id (str): Agent id or slug
        status (str | Unset): Run status filter
        batch_id (str | Unset): Experiment batch id filter
        example_id (str | Unset): Exact dataset example id (folder name) filter
        example_id_contains (str | Unset): Substring match on dataset example id
        created_after (str | Unset): Only runs created at/after this ISO timestamp
        created_before (str | Unset): Only runs created at/before this ISO timestamp
        completed_after (str | Unset): Only runs completed at/after this ISO timestamp
        completed_before (str | Unset): Only runs completed at/before this ISO timestamp
        source_ref (str | Unset): Filter by the source ref requested when the run was created
        feedback_status (AgentsRunsListFeedbackStatus | Unset):
        feedback_rating (AgentsRunsListFeedbackRating | Unset):
        has_feedback (bool | Unset):
        no_feedback (bool | Unset):
        has_expected (bool | Unset):
        has_expected_json (bool | Unset):
        has_expected_files (bool | Unset):
        feedback_body_contains (str | Unset):
        feedback_created_after (str | Unset):
        feedback_created_before (str | Unset):
        feedback_updated_after (str | Unset):
        feedback_updated_before (str | Unset):
        feedback_resolved_after (str | Unset):
        feedback_resolved_before (str | Unset):
        promoted_to_example (bool | Unset):
        promoted_example_name (str | Unset):
        since_last_resolved (bool | Unset):
        include (str | Unset): Comma-separated extra parts: feedback, expected, files
        sort (AgentsRunsListSort | Unset):
        order (AgentsRunsListOrder | Unset):
        scan_limit (int | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorEnvelope | ListAgentRunsResponse
     """


    return (await asyncio_detailed(
        agent_id=agent_id,
client=client,
status=status,
batch_id=batch_id,
example_id=example_id,
example_id_contains=example_id_contains,
created_after=created_after,
created_before=created_before,
completed_after=completed_after,
completed_before=completed_before,
source_ref=source_ref,
feedback_status=feedback_status,
feedback_rating=feedback_rating,
has_feedback=has_feedback,
no_feedback=no_feedback,
has_expected=has_expected,
has_expected_json=has_expected_json,
has_expected_files=has_expected_files,
feedback_body_contains=feedback_body_contains,
feedback_created_after=feedback_created_after,
feedback_created_before=feedback_created_before,
feedback_updated_after=feedback_updated_after,
feedback_updated_before=feedback_updated_before,
feedback_resolved_after=feedback_resolved_after,
feedback_resolved_before=feedback_resolved_before,
promoted_to_example=promoted_to_example,
promoted_example_name=promoted_example_name,
since_last_resolved=since_last_resolved,
include=include,
sort=sort,
order=order,
scan_limit=scan_limit,
limit=limit,
offset=offset,

    )).parsed

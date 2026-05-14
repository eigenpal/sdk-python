from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.agent_execution_summary_feedback_type_0_rating_type_0 import AgentExecutionSummaryFeedbackType0RatingType0
from ..models.agent_execution_summary_feedback_type_0_status_type_0 import AgentExecutionSummaryFeedbackType0StatusType0
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AgentExecutionSummaryFeedbackType0")



@_attrs_define
class AgentExecutionSummaryFeedbackType0:
    """ 
        Attributes:
            body (str):
            rating (AgentExecutionSummaryFeedbackType0RatingType0 | None | Unset):
            status (AgentExecutionSummaryFeedbackType0StatusType0 | None | Unset):
            created_at (None | str | Unset):
            created_by (None | str | Unset):
            created_by_email (None | str | Unset):
            updated_at (None | str | Unset):
            resolved_at (None | str | Unset):
            resolved_by (None | str | Unset):
            resolved_by_email (None | str | Unset):
            resolved_by_session_id (None | str | Unset):
            promoted_example_name (None | str | Unset):
     """

    body: str
    rating: AgentExecutionSummaryFeedbackType0RatingType0 | None | Unset = UNSET
    status: AgentExecutionSummaryFeedbackType0StatusType0 | None | Unset = UNSET
    created_at: None | str | Unset = UNSET
    created_by: None | str | Unset = UNSET
    created_by_email: None | str | Unset = UNSET
    updated_at: None | str | Unset = UNSET
    resolved_at: None | str | Unset = UNSET
    resolved_by: None | str | Unset = UNSET
    resolved_by_email: None | str | Unset = UNSET
    resolved_by_session_id: None | str | Unset = UNSET
    promoted_example_name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        body = self.body

        rating: None | str | Unset
        if isinstance(self.rating, Unset):
            rating = UNSET
        elif isinstance(self.rating, AgentExecutionSummaryFeedbackType0RatingType0):
            rating = self.rating.value
        else:
            rating = self.rating

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, AgentExecutionSummaryFeedbackType0StatusType0):
            status = self.status.value
        else:
            status = self.status

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        created_by_email: None | str | Unset
        if isinstance(self.created_by_email, Unset):
            created_by_email = UNSET
        else:
            created_by_email = self.created_by_email

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = self.updated_at

        resolved_at: None | str | Unset
        if isinstance(self.resolved_at, Unset):
            resolved_at = UNSET
        else:
            resolved_at = self.resolved_at

        resolved_by: None | str | Unset
        if isinstance(self.resolved_by, Unset):
            resolved_by = UNSET
        else:
            resolved_by = self.resolved_by

        resolved_by_email: None | str | Unset
        if isinstance(self.resolved_by_email, Unset):
            resolved_by_email = UNSET
        else:
            resolved_by_email = self.resolved_by_email

        resolved_by_session_id: None | str | Unset
        if isinstance(self.resolved_by_session_id, Unset):
            resolved_by_session_id = UNSET
        else:
            resolved_by_session_id = self.resolved_by_session_id

        promoted_example_name: None | str | Unset
        if isinstance(self.promoted_example_name, Unset):
            promoted_example_name = UNSET
        else:
            promoted_example_name = self.promoted_example_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "body": body,
        })
        if rating is not UNSET:
            field_dict["rating"] = rating
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_by_email is not UNSET:
            field_dict["createdByEmail"] = created_by_email
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if resolved_at is not UNSET:
            field_dict["resolvedAt"] = resolved_at
        if resolved_by is not UNSET:
            field_dict["resolvedBy"] = resolved_by
        if resolved_by_email is not UNSET:
            field_dict["resolvedByEmail"] = resolved_by_email
        if resolved_by_session_id is not UNSET:
            field_dict["resolvedBySessionId"] = resolved_by_session_id
        if promoted_example_name is not UNSET:
            field_dict["promotedExampleName"] = promoted_example_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        body = d.pop("body")

        def _parse_rating(data: object) -> AgentExecutionSummaryFeedbackType0RatingType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rating_type_0 = AgentExecutionSummaryFeedbackType0RatingType0(data)



                return rating_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentExecutionSummaryFeedbackType0RatingType0 | None | Unset, data)

        rating = _parse_rating(d.pop("rating", UNSET))


        def _parse_status(data: object) -> AgentExecutionSummaryFeedbackType0StatusType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = AgentExecutionSummaryFeedbackType0StatusType0(data)



                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentExecutionSummaryFeedbackType0StatusType0 | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_created_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))


        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("createdBy", UNSET))


        def _parse_created_by_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by_email = _parse_created_by_email(d.pop("createdByEmail", UNSET))


        def _parse_updated_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))


        def _parse_resolved_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resolved_at = _parse_resolved_at(d.pop("resolvedAt", UNSET))


        def _parse_resolved_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resolved_by = _parse_resolved_by(d.pop("resolvedBy", UNSET))


        def _parse_resolved_by_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resolved_by_email = _parse_resolved_by_email(d.pop("resolvedByEmail", UNSET))


        def _parse_resolved_by_session_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resolved_by_session_id = _parse_resolved_by_session_id(d.pop("resolvedBySessionId", UNSET))


        def _parse_promoted_example_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        promoted_example_name = _parse_promoted_example_name(d.pop("promotedExampleName", UNSET))


        agent_execution_summary_feedback_type_0 = cls(
            body=body,
            rating=rating,
            status=status,
            created_at=created_at,
            created_by=created_by,
            created_by_email=created_by_email,
            updated_at=updated_at,
            resolved_at=resolved_at,
            resolved_by=resolved_by,
            resolved_by_email=resolved_by_email,
            resolved_by_session_id=resolved_by_session_id,
            promoted_example_name=promoted_example_name,
        )

        return agent_execution_summary_feedback_type_0


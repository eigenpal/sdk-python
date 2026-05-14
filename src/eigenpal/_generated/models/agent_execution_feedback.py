from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.agent_execution_feedback_rating_type_0 import AgentExecutionFeedbackRatingType0
from ..models.agent_execution_feedback_status_type_0 import AgentExecutionFeedbackStatusType0
from typing import cast






T = TypeVar("T", bound="AgentExecutionFeedback")



@_attrs_define
class AgentExecutionFeedback:
    """ 
        Attributes:
            rating (AgentExecutionFeedbackRatingType0 | None):
            status (AgentExecutionFeedbackStatusType0 | None):
            created_at (None | str):
            created_by (None | str):
            created_by_email (None | str):
            updated_at (None | str):
            resolved_at (None | str):
            resolved_by (None | str):
            resolved_by_email (None | str):
            resolved_by_session_id (None | str):
            promoted_example_name (None | str):
            body (str):
     """

    rating: AgentExecutionFeedbackRatingType0 | None
    status: AgentExecutionFeedbackStatusType0 | None
    created_at: None | str
    created_by: None | str
    created_by_email: None | str
    updated_at: None | str
    resolved_at: None | str
    resolved_by: None | str
    resolved_by_email: None | str
    resolved_by_session_id: None | str
    promoted_example_name: None | str
    body: str





    def to_dict(self) -> dict[str, Any]:
        rating: None | str
        if isinstance(self.rating, AgentExecutionFeedbackRatingType0):
            rating = self.rating.value
        else:
            rating = self.rating

        status: None | str
        if isinstance(self.status, AgentExecutionFeedbackStatusType0):
            status = self.status.value
        else:
            status = self.status

        created_at: None | str
        created_at = self.created_at

        created_by: None | str
        created_by = self.created_by

        created_by_email: None | str
        created_by_email = self.created_by_email

        updated_at: None | str
        updated_at = self.updated_at

        resolved_at: None | str
        resolved_at = self.resolved_at

        resolved_by: None | str
        resolved_by = self.resolved_by

        resolved_by_email: None | str
        resolved_by_email = self.resolved_by_email

        resolved_by_session_id: None | str
        resolved_by_session_id = self.resolved_by_session_id

        promoted_example_name: None | str
        promoted_example_name = self.promoted_example_name

        body = self.body


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "rating": rating,
            "status": status,
            "createdAt": created_at,
            "createdBy": created_by,
            "createdByEmail": created_by_email,
            "updatedAt": updated_at,
            "resolvedAt": resolved_at,
            "resolvedBy": resolved_by,
            "resolvedByEmail": resolved_by_email,
            "resolvedBySessionId": resolved_by_session_id,
            "promotedExampleName": promoted_example_name,
            "body": body,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_rating(data: object) -> AgentExecutionFeedbackRatingType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rating_type_0 = AgentExecutionFeedbackRatingType0(data)



                return rating_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentExecutionFeedbackRatingType0 | None, data)

        rating = _parse_rating(d.pop("rating"))


        def _parse_status(data: object) -> AgentExecutionFeedbackStatusType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = AgentExecutionFeedbackStatusType0(data)



                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentExecutionFeedbackStatusType0 | None, data)

        status = _parse_status(d.pop("status"))


        def _parse_created_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_at = _parse_created_at(d.pop("createdAt"))


        def _parse_created_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_by = _parse_created_by(d.pop("createdBy"))


        def _parse_created_by_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_by_email = _parse_created_by_email(d.pop("createdByEmail"))


        def _parse_updated_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_at = _parse_updated_at(d.pop("updatedAt"))


        def _parse_resolved_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolved_at = _parse_resolved_at(d.pop("resolvedAt"))


        def _parse_resolved_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolved_by = _parse_resolved_by(d.pop("resolvedBy"))


        def _parse_resolved_by_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolved_by_email = _parse_resolved_by_email(d.pop("resolvedByEmail"))


        def _parse_resolved_by_session_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolved_by_session_id = _parse_resolved_by_session_id(d.pop("resolvedBySessionId"))


        def _parse_promoted_example_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        promoted_example_name = _parse_promoted_example_name(d.pop("promotedExampleName"))


        body = d.pop("body")

        agent_execution_feedback = cls(
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
            body=body,
        )

        return agent_execution_feedback


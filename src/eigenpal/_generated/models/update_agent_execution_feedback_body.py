from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_agent_execution_feedback_body_feedback_rating_type_0 import UpdateAgentExecutionFeedbackBodyFeedbackRatingType0
from ..models.update_agent_execution_feedback_body_feedback_status_type_0 import UpdateAgentExecutionFeedbackBodyFeedbackStatusType0
from ..models.update_agent_execution_feedback_body_rating_type_0 import UpdateAgentExecutionFeedbackBodyRatingType0
from ..models.update_agent_execution_feedback_body_status_type_0 import UpdateAgentExecutionFeedbackBodyStatusType0
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateAgentExecutionFeedbackBody")



@_attrs_define
class UpdateAgentExecutionFeedbackBody:
    """ 
        Attributes:
            body (None | str | Unset):
            feedback (None | str | Unset):
            rating (None | Unset | UpdateAgentExecutionFeedbackBodyRatingType0):
            feedback_rating (None | Unset | UpdateAgentExecutionFeedbackBodyFeedbackRatingType0):
            status (None | Unset | UpdateAgentExecutionFeedbackBodyStatusType0):
            feedback_status (None | Unset | UpdateAgentExecutionFeedbackBodyFeedbackStatusType0):
            expected (Any | None | Unset):
     """

    body: None | str | Unset = UNSET
    feedback: None | str | Unset = UNSET
    rating: None | Unset | UpdateAgentExecutionFeedbackBodyRatingType0 = UNSET
    feedback_rating: None | Unset | UpdateAgentExecutionFeedbackBodyFeedbackRatingType0 = UNSET
    status: None | Unset | UpdateAgentExecutionFeedbackBodyStatusType0 = UNSET
    feedback_status: None | Unset | UpdateAgentExecutionFeedbackBodyFeedbackStatusType0 = UNSET
    expected: Any | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        body: None | str | Unset
        if isinstance(self.body, Unset):
            body = UNSET
        else:
            body = self.body

        feedback: None | str | Unset
        if isinstance(self.feedback, Unset):
            feedback = UNSET
        else:
            feedback = self.feedback

        rating: None | str | Unset
        if isinstance(self.rating, Unset):
            rating = UNSET
        elif isinstance(self.rating, UpdateAgentExecutionFeedbackBodyRatingType0):
            rating = self.rating.value
        else:
            rating = self.rating

        feedback_rating: None | str | Unset
        if isinstance(self.feedback_rating, Unset):
            feedback_rating = UNSET
        elif isinstance(self.feedback_rating, UpdateAgentExecutionFeedbackBodyFeedbackRatingType0):
            feedback_rating = self.feedback_rating.value
        else:
            feedback_rating = self.feedback_rating

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, UpdateAgentExecutionFeedbackBodyStatusType0):
            status = self.status.value
        else:
            status = self.status

        feedback_status: None | str | Unset
        if isinstance(self.feedback_status, Unset):
            feedback_status = UNSET
        elif isinstance(self.feedback_status, UpdateAgentExecutionFeedbackBodyFeedbackStatusType0):
            feedback_status = self.feedback_status.value
        else:
            feedback_status = self.feedback_status

        expected: Any | None | Unset
        if isinstance(self.expected, Unset):
            expected = UNSET
        else:
            expected = self.expected


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if body is not UNSET:
            field_dict["body"] = body
        if feedback is not UNSET:
            field_dict["feedback"] = feedback
        if rating is not UNSET:
            field_dict["rating"] = rating
        if feedback_rating is not UNSET:
            field_dict["feedbackRating"] = feedback_rating
        if status is not UNSET:
            field_dict["status"] = status
        if feedback_status is not UNSET:
            field_dict["feedbackStatus"] = feedback_status
        if expected is not UNSET:
            field_dict["expected"] = expected

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body = _parse_body(d.pop("body", UNSET))


        def _parse_feedback(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        feedback = _parse_feedback(d.pop("feedback", UNSET))


        def _parse_rating(data: object) -> None | Unset | UpdateAgentExecutionFeedbackBodyRatingType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rating_type_0 = UpdateAgentExecutionFeedbackBodyRatingType0(data)



                return rating_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateAgentExecutionFeedbackBodyRatingType0, data)

        rating = _parse_rating(d.pop("rating", UNSET))


        def _parse_feedback_rating(data: object) -> None | Unset | UpdateAgentExecutionFeedbackBodyFeedbackRatingType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                feedback_rating_type_0 = UpdateAgentExecutionFeedbackBodyFeedbackRatingType0(data)



                return feedback_rating_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateAgentExecutionFeedbackBodyFeedbackRatingType0, data)

        feedback_rating = _parse_feedback_rating(d.pop("feedbackRating", UNSET))


        def _parse_status(data: object) -> None | Unset | UpdateAgentExecutionFeedbackBodyStatusType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = UpdateAgentExecutionFeedbackBodyStatusType0(data)



                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateAgentExecutionFeedbackBodyStatusType0, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_feedback_status(data: object) -> None | Unset | UpdateAgentExecutionFeedbackBodyFeedbackStatusType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                feedback_status_type_0 = UpdateAgentExecutionFeedbackBodyFeedbackStatusType0(data)



                return feedback_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateAgentExecutionFeedbackBodyFeedbackStatusType0, data)

        feedback_status = _parse_feedback_status(d.pop("feedbackStatus", UNSET))


        def _parse_expected(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        expected = _parse_expected(d.pop("expected", UNSET))


        update_agent_execution_feedback_body = cls(
            body=body,
            feedback=feedback,
            rating=rating,
            feedback_rating=feedback_rating,
            status=status,
            feedback_status=feedback_status,
            expected=expected,
        )


        update_agent_execution_feedback_body.additional_properties = d
        return update_agent_execution_feedback_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

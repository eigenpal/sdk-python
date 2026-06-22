from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.run_feedback_request_rating_type_0 import RunFeedbackRequestRatingType0
from ..models.run_feedback_request_status_type_0 import RunFeedbackRequestStatusType0
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RunFeedbackRequest")



@_attrs_define
class RunFeedbackRequest:
    """ Partial update for run feedback. Omitted fields are preserved; pass null to clear a field.

        Attributes:
            body (None | str | Unset): Human feedback text. Pass null to clear the text.
            rating (None | RunFeedbackRequestRatingType0 | Unset): Human verdict for this run: `pass`, `fail`, or `partial`.
                Pass null to clear it.
            status (None | RunFeedbackRequestStatusType0 | Unset): Review lifecycle status: `open`, `resolved`, or
                `ignored`. Pass null to clear it.
            expected (Any | None | Unset): Expected JSON output for this run. Pass null to clear it.
     """

    body: None | str | Unset = UNSET
    rating: None | RunFeedbackRequestRatingType0 | Unset = UNSET
    status: None | RunFeedbackRequestStatusType0 | Unset = UNSET
    expected: Any | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        body: None | str | Unset
        if isinstance(self.body, Unset):
            body = UNSET
        else:
            body = self.body

        rating: None | str | Unset
        if isinstance(self.rating, Unset):
            rating = UNSET
        elif isinstance(self.rating, RunFeedbackRequestRatingType0):
            rating = self.rating.value
        else:
            rating = self.rating

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, RunFeedbackRequestStatusType0):
            status = self.status.value
        else:
            status = self.status

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
        if rating is not UNSET:
            field_dict["rating"] = rating
        if status is not UNSET:
            field_dict["status"] = status
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


        def _parse_rating(data: object) -> None | RunFeedbackRequestRatingType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rating_type_0 = RunFeedbackRequestRatingType0(data)



                return rating_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RunFeedbackRequestRatingType0 | Unset, data)

        rating = _parse_rating(d.pop("rating", UNSET))


        def _parse_status(data: object) -> None | RunFeedbackRequestStatusType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = RunFeedbackRequestStatusType0(data)



                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RunFeedbackRequestStatusType0 | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_expected(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        expected = _parse_expected(d.pop("expected", UNSET))


        run_feedback_request = cls(
            body=body,
            rating=rating,
            status=status,
            expected=expected,
        )


        run_feedback_request.additional_properties = d
        return run_feedback_request

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

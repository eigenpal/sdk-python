from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="DatasetReviewFocusFieldOutput")



@_attrs_define
class DatasetReviewFocusFieldOutput:
    """
        Attributes:
            path (str): Dotted expected-output path the reviewer should inspect, e.g. vendor.iban.
            reason (None | str | Unset): Optional reason this field needs attention.
     """

    path: str
    reason: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        path = self.path

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "path": path,
        })
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))


        dataset_review_focus_field_output = cls(
            path=path,
            reason=reason,
        )

        return dataset_review_focus_field_output

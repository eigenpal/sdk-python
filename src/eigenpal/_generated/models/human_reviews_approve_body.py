from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="HumanReviewsApproveBody")



@_attrs_define
class HumanReviewsApproveBody:
    """
        Attributes:
            expected_version (int):
     """

    expected_version: int





    def to_dict(self) -> dict[str, Any]:
        expected_version = self.expected_version


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "expectedVersion": expected_version,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expected_version = d.pop("expectedVersion")

        human_reviews_approve_body = cls(
            expected_version=expected_version,
        )

        return human_reviews_approve_body

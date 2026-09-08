from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="HumanReviewsRejectBody")



@_attrs_define
class HumanReviewsRejectBody:
    """
        Attributes:
            expected_version (int):
            idempotency_key (str):
            reason (str):
     """

    expected_version: int
    idempotency_key: str
    reason: str





    def to_dict(self) -> dict[str, Any]:
        expected_version = self.expected_version

        idempotency_key = self.idempotency_key

        reason = self.reason


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "expectedVersion": expected_version,
            "idempotencyKey": idempotency_key,
            "reason": reason,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expected_version = d.pop("expectedVersion")

        idempotency_key = d.pop("idempotencyKey")

        reason = d.pop("reason")

        human_reviews_reject_body = cls(
            expected_version=expected_version,
            idempotency_key=idempotency_key,
            reason=reason,
        )

        return human_reviews_reject_body

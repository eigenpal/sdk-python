from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="HumanReviewsConfirmFieldBody")



@_attrs_define
class HumanReviewsConfirmFieldBody:
    """
        Attributes:
            expected_version (int):
            idempotency_key (str):
            path (str):
            value (bool | float | None | str):
            confirmed (bool | Unset):  Default: True.
     """

    expected_version: int
    idempotency_key: str
    path: str
    value: bool | float | None | str
    confirmed: bool | Unset = True





    def to_dict(self) -> dict[str, Any]:
        expected_version = self.expected_version

        idempotency_key = self.idempotency_key

        path = self.path

        value: bool | float | None | str
        value = self.value

        confirmed = self.confirmed


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "expectedVersion": expected_version,
            "idempotencyKey": idempotency_key,
            "path": path,
            "value": value,
        })
        if confirmed is not UNSET:
            field_dict["confirmed"] = confirmed

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expected_version = d.pop("expectedVersion")

        idempotency_key = d.pop("idempotencyKey")

        path = d.pop("path")

        def _parse_value(data: object) -> bool | float | None | str:
            if data is None:
                return data
            return cast(bool | float | None | str, data)

        value = _parse_value(d.pop("value"))


        confirmed = d.pop("confirmed", UNSET)

        human_reviews_confirm_field_body = cls(
            expected_version=expected_version,
            idempotency_key=idempotency_key,
            path=path,
            value=value,
            confirmed=confirmed,
        )

        return human_reviews_confirm_field_body

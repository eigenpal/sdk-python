from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.human_review_task_detail_decisions_item_reason import HumanReviewTaskDetailDecisionsItemReason
from typing import cast






T = TypeVar("T", bound="HumanReviewTaskDetailDecisionsItem")



@_attrs_define
class HumanReviewTaskDetailDecisionsItem:
    """
        Attributes:
            id (str):
            path (str):
            original_value (bool | float | None | str):
            current_value (bool | float | None | str):
            required (bool):
            reason (HumanReviewTaskDetailDecisionsItemReason):
            confirmed_by (None | str):
            confirmed_at (None | str):
            version (int):
     """

    id: str
    path: str
    original_value: bool | float | None | str
    current_value: bool | float | None | str
    required: bool
    reason: HumanReviewTaskDetailDecisionsItemReason
    confirmed_by: None | str
    confirmed_at: None | str
    version: int





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        path = self.path

        original_value: bool | float | None | str
        original_value = self.original_value

        current_value: bool | float | None | str
        current_value = self.current_value

        required = self.required

        reason = self.reason.value

        confirmed_by: None | str
        confirmed_by = self.confirmed_by

        confirmed_at: None | str
        confirmed_at = self.confirmed_at

        version = self.version


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "path": path,
            "originalValue": original_value,
            "currentValue": current_value,
            "required": required,
            "reason": reason,
            "confirmedBy": confirmed_by,
            "confirmedAt": confirmed_at,
            "version": version,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        path = d.pop("path")

        def _parse_original_value(data: object) -> bool | float | None | str:
            if data is None:
                return data
            return cast(bool | float | None | str, data)

        original_value = _parse_original_value(d.pop("originalValue"))


        def _parse_current_value(data: object) -> bool | float | None | str:
            if data is None:
                return data
            return cast(bool | float | None | str, data)

        current_value = _parse_current_value(d.pop("currentValue"))


        required = d.pop("required")

        reason = HumanReviewTaskDetailDecisionsItemReason(d.pop("reason"))




        def _parse_confirmed_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        confirmed_by = _parse_confirmed_by(d.pop("confirmedBy"))


        def _parse_confirmed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        confirmed_at = _parse_confirmed_at(d.pop("confirmedAt"))


        version = d.pop("version")

        human_review_task_detail_decisions_item = cls(
            id=id,
            path=path,
            original_value=original_value,
            current_value=current_value,
            required=required,
            reason=reason,
            confirmed_by=confirmed_by,
            confirmed_at=confirmed_at,
            version=version,
        )

        return human_review_task_detail_decisions_item

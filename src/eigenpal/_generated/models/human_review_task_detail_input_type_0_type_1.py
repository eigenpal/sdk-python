from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Literal, cast






T = TypeVar("T", bound="HumanReviewTaskDetailInputType0Type1")



@_attrs_define
class HumanReviewTaskDetailInputType0Type1:
    """
        Attributes:
            status (Literal['omitted_too_large']):
     """

    status: Literal['omitted_too_large']





    def to_dict(self) -> dict[str, Any]:
        status = self.status


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = cast(Literal['omitted_too_large'] , d.pop("status"))
        if status != 'omitted_too_large':
            raise ValueError(f"status must match const 'omitted_too_large', got '{status}'")

        human_review_task_detail_input_type_0_type_1 = cls(
            status=status,
        )

        return human_review_task_detail_input_type_0_type_1

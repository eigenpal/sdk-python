from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.human_review_task_detail_input_type_0_type_0_data_type_0 import HumanReviewTaskDetailInputType0Type0DataType0





T = TypeVar("T", bound="HumanReviewTaskDetailInputType0Type0")



@_attrs_define
class HumanReviewTaskDetailInputType0Type0:
    """
        Attributes:
            status (Literal['available']):
            data (HumanReviewTaskDetailInputType0Type0DataType0 | list[Any]):
     """

    status: Literal['available']
    data: HumanReviewTaskDetailInputType0Type0DataType0 | list[Any]





    def to_dict(self) -> dict[str, Any]:
        from ..models.human_review_task_detail_input_type_0_type_0_data_type_0 import HumanReviewTaskDetailInputType0Type0DataType0
        status = self.status

        data: dict[str, Any] | list[Any]
        if isinstance(self.data, HumanReviewTaskDetailInputType0Type0DataType0):
            data = self.data.to_dict()
        else:
            data = self.data





        field_dict: dict[str, Any] = {}

        field_dict.update({
            "status": status,
            "data": data,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.human_review_task_detail_input_type_0_type_0_data_type_0 import HumanReviewTaskDetailInputType0Type0DataType0
        d = dict(src_dict)
        status = cast(Literal['available'] , d.pop("status"))
        if status != 'available':
            raise ValueError(f"status must match const 'available', got '{status}'")

        def _parse_data(data: object) -> HumanReviewTaskDetailInputType0Type0DataType0 | list[Any]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = HumanReviewTaskDetailInputType0Type0DataType0.from_dict(data)



                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            data_type_1 = cast(list[Any], data)

            return data_type_1

        data = _parse_data(d.pop("data"))


        human_review_task_detail_input_type_0_type_0 = cls(
            status=status,
            data=data,
        )

        return human_review_task_detail_input_type_0_type_0

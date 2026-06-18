from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.dataset_example import DatasetExample





T = TypeVar("T", bound="DatasetExampleList")



@_attrs_define
class DatasetExampleList:
    """
        Attributes:
            data (list[DatasetExample]):
            total (int):
            limit (int):
            offset (int):
     """

    data: list[DatasetExample]
    total: int
    limit: int
    offset: int





    def to_dict(self) -> dict[str, Any]:
        from ..models.dataset_example import DatasetExample
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)



        total = self.total

        limit = self.limit

        offset = self.offset


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "data": data,
            "total": total,
            "limit": limit,
            "offset": offset,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_example import DatasetExample
        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            data_item = DatasetExample.from_dict(data_item_data)



            data.append(data_item)


        total = d.pop("total")

        limit = d.pop("limit")

        offset = d.pop("offset")

        dataset_example_list = cls(
            data=data,
            total=total,
            limit=limit,
            offset=offset,
        )

        return dataset_example_list

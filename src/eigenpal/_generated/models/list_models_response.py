from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.public_model import PublicModel





T = TypeVar("T", bound="ListModelsResponse")



@_attrs_define
class ListModelsResponse:
    """
        Attributes:
            data (list[PublicModel]):
            total (int):
     """

    data: list[PublicModel]
    total: int





    def to_dict(self) -> dict[str, Any]:
        from ..models.public_model import PublicModel
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)



        total = self.total


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "data": data,
            "total": total,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_model import PublicModel
        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            data_item = PublicModel.from_dict(data_item_data)



            data.append(data_item)


        total = d.pop("total")

        list_models_response = cls(
            data=data,
            total=total,
        )

        return list_models_response

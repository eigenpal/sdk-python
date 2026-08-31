from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.template import Template





T = TypeVar("T", bound="ListTemplatesResponse")



@_attrs_define
class ListTemplatesResponse:
    """
        Attributes:
            items (list[Template]):
            total (int):
     """

    items: list[Template]
    total: int





    def to_dict(self) -> dict[str, Any]:
        from ..models.template import Template
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)



        total = self.total


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "items": items,
            "total": total,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template import Template
        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in (_items):
            items_item = Template.from_dict(items_item_data)



            items.append(items_item)


        total = d.pop("total")

        list_templates_response = cls(
            items=items,
            total=total,
        )

        return list_templates_response

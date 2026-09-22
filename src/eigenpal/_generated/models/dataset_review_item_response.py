from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.dataset_review_item import DatasetReviewItem





T = TypeVar("T", bound="DatasetReviewItemResponse")



@_attrs_define
class DatasetReviewItemResponse:
    """
        Attributes:
            item (DatasetReviewItem):
     """

    item: DatasetReviewItem





    def to_dict(self) -> dict[str, Any]:
        from ..models.dataset_review_item import DatasetReviewItem
        item = self.item.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "item": item,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_review_item import DatasetReviewItem
        d = dict(src_dict)
        item = DatasetReviewItem.from_dict(d.pop("item"))




        dataset_review_item_response = cls(
            item=item,
        )

        return dataset_review_item_response

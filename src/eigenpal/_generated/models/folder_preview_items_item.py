from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.folder_preview_items_item_kind import FolderPreviewItemsItemKind






T = TypeVar("T", bound="FolderPreviewItemsItem")



@_attrs_define
class FolderPreviewItemsItem:
    """
        Attributes:
            name (str):
            kind (FolderPreviewItemsItemKind):
     """

    name: str
    kind: FolderPreviewItemsItemKind





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        kind = self.kind.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
            "kind": kind,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        kind = FolderPreviewItemsItemKind(d.pop("kind"))




        folder_preview_items_item = cls(
            name=name,
            kind=kind,
        )

        return folder_preview_items_item

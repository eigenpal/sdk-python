from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.folder_type import FolderType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.folder_preview_items_item import FolderPreviewItemsItem





T = TypeVar("T", bound="Folder")



@_attrs_define
class Folder:
    """
        Attributes:
            id (str):
            parent_id (None | str):
            type_ (FolderType):
            name (str):
            created_at (str):
            child_count (int | Unset): Direct subfolder count. Present on tree listings.
            workflow_count (int | Unset): Workflows filed directly in this folder. Present on workflow-tree listings.
            preview_items (list[FolderPreviewItemsItem] | Unset): Up to a handful of item names — subfolders first, then
                workflows — for a peek at folder contents. Present on workflow-tree listings.
     """

    id: str
    parent_id: None | str
    type_: FolderType
    name: str
    created_at: str
    child_count: int | Unset = UNSET
    workflow_count: int | Unset = UNSET
    preview_items: list[FolderPreviewItemsItem] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.folder_preview_items_item import FolderPreviewItemsItem
        id = self.id

        parent_id: None | str
        parent_id = self.parent_id

        type_ = self.type_.value

        name = self.name

        created_at: str
        created_at = self.created_at

        child_count = self.child_count

        workflow_count = self.workflow_count

        preview_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.preview_items, Unset):
            preview_items = []
            for preview_items_item_data in self.preview_items:
                preview_items_item = preview_items_item_data.to_dict()
                preview_items.append(preview_items_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "parentId": parent_id,
            "type": type_,
            "name": name,
            "createdAt": created_at,
        })
        if child_count is not UNSET:
            field_dict["childCount"] = child_count
        if workflow_count is not UNSET:
            field_dict["workflowCount"] = workflow_count
        if preview_items is not UNSET:
            field_dict["previewItems"] = preview_items

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.folder_preview_items_item import FolderPreviewItemsItem
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_parent_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        parent_id = _parse_parent_id(d.pop("parentId"))


        type_ = FolderType(d.pop("type"))




        name = d.pop("name")

        def _parse_created_at(data: object) -> str:
            return cast(str, data)

        created_at = _parse_created_at(d.pop("createdAt"))


        child_count = d.pop("childCount", UNSET)

        workflow_count = d.pop("workflowCount", UNSET)

        _preview_items = d.pop("previewItems", UNSET)
        preview_items: list[FolderPreviewItemsItem] | Unset = UNSET
        if _preview_items is not UNSET:
            preview_items = []
            for preview_items_item_data in _preview_items:
                preview_items_item = FolderPreviewItemsItem.from_dict(preview_items_item_data)



                preview_items.append(preview_items_item)


        folder = cls(
            id=id,
            parent_id=parent_id,
            type_=type_,
            name=name,
            created_at=created_at,
            child_count=child_count,
            workflow_count=workflow_count,
            preview_items=preview_items,
        )

        return folder

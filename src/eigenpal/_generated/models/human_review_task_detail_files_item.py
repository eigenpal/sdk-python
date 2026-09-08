from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.human_review_task_detail_files_item_role import HumanReviewTaskDetailFilesItemRole
from ..types import UNSET, Unset






T = TypeVar("T", bound="HumanReviewTaskDetailFilesItem")



@_attrs_define
class HumanReviewTaskDetailFilesItem:
    """
        Attributes:
            file_id (str):
            filename (str):
            artifact_path (str):
            mime_type (str | Unset):
            size (int | Unset):
            field_name (str | Unset):
            role (HumanReviewTaskDetailFilesItemRole | Unset): run_input for authorized run input files; attachment for
                extra current-run files. Omitted on historical tasks and inferred at read time.
     """

    file_id: str
    filename: str
    artifact_path: str
    mime_type: str | Unset = UNSET
    size: int | Unset = UNSET
    field_name: str | Unset = UNSET
    role: HumanReviewTaskDetailFilesItemRole | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        file_id = self.file_id

        filename = self.filename

        artifact_path = self.artifact_path

        mime_type = self.mime_type

        size = self.size

        field_name = self.field_name

        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
            "fileId": file_id,
            "filename": filename,
            "artifactPath": artifact_path,
        })
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if size is not UNSET:
            field_dict["size"] = size
        if field_name is not UNSET:
            field_dict["fieldName"] = field_name
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_id = d.pop("fileId")

        filename = d.pop("filename")

        artifact_path = d.pop("artifactPath")

        mime_type = d.pop("mimeType", UNSET)

        size = d.pop("size", UNSET)

        field_name = d.pop("fieldName", UNSET)

        _role = d.pop("role", UNSET)
        role: HumanReviewTaskDetailFilesItemRole | Unset
        if isinstance(_role,  Unset):
            role = UNSET
        else:
            role = HumanReviewTaskDetailFilesItemRole(_role)




        human_review_task_detail_files_item = cls(
            file_id=file_id,
            filename=filename,
            artifact_path=artifact_path,
            mime_type=mime_type,
            size=size,
            field_name=field_name,
            role=role,
        )

        return human_review_task_detail_files_item

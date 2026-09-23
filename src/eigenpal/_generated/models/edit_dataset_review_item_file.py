from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from ..types import File, FileTypes
from ..types import UNSET, Unset
from io import BytesIO
from typing import cast
from typing import Literal, cast






T = TypeVar("T", bound="EditDatasetReviewItemFile")



@_attrs_define
class EditDatasetReviewItemFile:
    """
        Attributes:
            expected_updated_at (str):
            action (Literal['edit-file'] | Unset): Must be edit-file for the multipart item PATCH form.
            file (File | Unset): Corrected expected-file bytes (50MB cap).
            file_path (str | Unset):
            new_path (str | Unset):
            comment (None | str | Unset):
     """

    expected_updated_at: str
    action: Literal['edit-file'] | Unset = UNSET
    file: File | Unset = UNSET
    file_path: str | Unset = UNSET
    new_path: str | Unset = UNSET
    comment: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        expected_updated_at = self.expected_updated_at

        action = self.action

        file: FileTypes | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()


        file_path = self.file_path

        new_path = self.new_path

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "expectedUpdatedAt": expected_updated_at,
        })
        if action is not UNSET:
            field_dict["action"] = action
        if file is not UNSET:
            field_dict["file"] = file
        if file_path is not UNSET:
            field_dict["filePath"] = file_path
        if new_path is not UNSET:
            field_dict["newPath"] = new_path
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("expectedUpdatedAt", (None, str(self.expected_updated_at).encode(), "text/plain")))



        if not isinstance(self.action, Unset):
            files.append(("action", (None, self.action, "text/plain")))



        if not isinstance(self.file, Unset):
            files.append(("file", self.file.to_tuple()))



        if not isinstance(self.file_path, Unset):
            files.append(("filePath", (None, str(self.file_path).encode(), "text/plain")))



        if not isinstance(self.new_path, Unset):
            files.append(("newPath", (None, str(self.new_path).encode(), "text/plain")))



        if not isinstance(self.comment, Unset):
            if isinstance(self.comment, str):

                files.append(("comment", (None, str(self.comment).encode(), "text/plain")))
            else:
                files.append(("comment", (None, str(self.comment).encode(), "text/plain")))



        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expected_updated_at = d.pop("expectedUpdatedAt")

        action = cast(Literal['edit-file'] | Unset , d.pop("action", UNSET))
        if action != 'edit-file'and not isinstance(action, Unset):
            raise ValueError(f"action must match const 'edit-file', got '{action}'")

        _file = d.pop("file", UNSET)
        file: File | Unset
        if isinstance(_file,  Unset):
            file = UNSET
        else:
            file = File(
             payload = BytesIO(_file)
        )




        file_path = d.pop("filePath", UNSET)

        new_path = d.pop("newPath", UNSET)

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))


        edit_dataset_review_item_file = cls(
            expected_updated_at=expected_updated_at,
            action=action,
            file=file,
            file_path=file_path,
            new_path=new_path,
            comment=comment,
        )


        edit_dataset_review_item_file.additional_properties = d
        return edit_dataset_review_item_file

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

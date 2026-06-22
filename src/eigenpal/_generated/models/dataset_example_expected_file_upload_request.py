from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from ..types import File, FileTypes
from io import BytesIO
from typing import cast






T = TypeVar("T", bound="DatasetExampleExpectedFileUploadRequest")



@_attrs_define
class DatasetExampleExpectedFileUploadRequest:
    """
        Attributes:
            file (list[File]): One or more expected files to upload.
     """

    file: list[File]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        file = []
        for file_item_data in self.file:
            file_item = file_item_data.to_tuple()

            file.append(file_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "file": file,
        })

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        for file_item_element in self.file:
            files.append(("file", file_item_element.to_tuple()))





        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = []
        _file = d.pop("file")
        for file_item_data in (_file):
            file_item = File(
                 payload = BytesIO(file_item_data)
            )



            file.append(file_item)


        dataset_example_expected_file_upload_request = cls(
            file=file,
        )


        dataset_example_expected_file_upload_request.additional_properties = d
        return dataset_example_expected_file_upload_request

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from ..models.automation_dataset_import_multipart_request_mode import AutomationDatasetImportMultipartRequestMode
from ..types import File, FileTypes
from ..types import UNSET, Unset
from io import BytesIO






T = TypeVar("T", bound="AutomationDatasetImportMultipartRequest")



@_attrs_define
class AutomationDatasetImportMultipartRequest:
    """
        Attributes:
            file (File): Dataset ZIP file
            mode (AutomationDatasetImportMultipartRequestMode | Unset):
     """

    file: File
    mode: AutomationDatasetImportMultipartRequestMode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()


        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "file": file,
        })
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))



        if not isinstance(self.mode, Unset):
            files.append(("mode",  (None, str(self.mode.value).encode(), "text/plain")))




        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = File(
             payload = BytesIO(d.pop("file"))
        )




        _mode = d.pop("mode", UNSET)
        mode: AutomationDatasetImportMultipartRequestMode | Unset
        if isinstance(_mode,  Unset):
            mode = UNSET
        else:
            mode = AutomationDatasetImportMultipartRequestMode(_mode)




        automation_dataset_import_multipart_request = cls(
            file=file,
            mode=mode,
        )


        automation_dataset_import_multipart_request.additional_properties = d
        return automation_dataset_import_multipart_request

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="DatasetExampleInputFileRenameResponse")



@_attrs_define
class DatasetExampleInputFileRenameResponse:
    """
        Attributes:
            ok (bool):
            filename (str):
            path (str): Updated input file path.
     """

    ok: bool
    filename: str
    path: str





    def to_dict(self) -> dict[str, Any]:
        ok = self.ok

        filename = self.filename

        path = self.path


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ok": ok,
            "filename": filename,
            "path": path,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ok = d.pop("ok")

        filename = d.pop("filename")

        path = d.pop("path")

        dataset_example_input_file_rename_response = cls(
            ok=ok,
            filename=filename,
            path=path,
        )

        return dataset_example_input_file_rename_response

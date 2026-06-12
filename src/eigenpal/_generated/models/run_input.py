from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.run_file import RunFile





T = TypeVar("T", bound="RunInput")



@_attrs_define
class RunInput:
    """
        Attributes:
            args (Any): Input arguments the run was started with.
            files (list[RunFile] | Unset): Uploaded input files (agent runs only).
            metadata (Any | Unset): Caller-supplied run metadata, if any.
     """

    args: Any
    files: list[RunFile] | Unset = UNSET
    metadata: Any | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_file import RunFile
        args = self.args

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)



        metadata = self.metadata


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "args": args,
        })
        if files is not UNSET:
            field_dict["files"] = files
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_file import RunFile
        d = dict(src_dict)
        args = d.pop("args")

        _files = d.pop("files", UNSET)
        files: list[RunFile] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = RunFile.from_dict(files_item_data)



                files.append(files_item)


        metadata = d.pop("metadata", UNSET)

        run_input = cls(
            args=args,
            files=files,
            metadata=metadata,
        )

        return run_input

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





T = TypeVar("T", bound="AgentRunExecutionExpected")



@_attrs_define
class AgentRunExecutionExpected:
    """ Ground-truth expected output and files.

        Attributes:
            output (Any | Unset):
            files (list[RunFile] | Unset):
     """

    output: Any | Unset = UNSET
    files: list[RunFile] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_file import RunFile
        output = self.output

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if output is not UNSET:
            field_dict["output"] = output
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_file import RunFile
        d = dict(src_dict)
        output = d.pop("output", UNSET)

        _files = d.pop("files", UNSET)
        files: list[RunFile] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = RunFile.from_dict(files_item_data)



                files.append(files_item)


        agent_run_execution_expected = cls(
            output=output,
            files=files,
        )

        return agent_run_execution_expected

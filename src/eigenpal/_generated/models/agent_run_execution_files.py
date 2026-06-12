from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.run_file import RunFile





T = TypeVar("T", bound="AgentRunExecutionFiles")



@_attrs_define
class AgentRunExecutionFiles:
    """
        Attributes:
            output (list[RunFile]): Output artifacts the agent produced.
     """

    output: list[RunFile]





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_file import RunFile
        output = []
        for output_item_data in self.output:
            output_item = output_item_data.to_dict()
            output.append(output_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "output": output,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_file import RunFile
        d = dict(src_dict)
        output = []
        _output = d.pop("output")
        for output_item_data in (_output):
            output_item = RunFile.from_dict(output_item_data)



            output.append(output_item)


        agent_run_execution_files = cls(
            output=output,
        )

        return agent_run_execution_files

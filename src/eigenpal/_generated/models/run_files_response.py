from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.run_files_response_inputs_item import RunFilesResponseInputsItem
  from ..models.run_files_response_outputs_by_step import RunFilesResponseOutputsByStep





T = TypeVar("T", bound="RunFilesResponse")



@_attrs_define
class RunFilesResponse:
    """
        Attributes:
            inputs (list[RunFilesResponseInputsItem]):
            outputs_by_step (RunFilesResponseOutputsByStep):
     """

    inputs: list[RunFilesResponseInputsItem]
    outputs_by_step: RunFilesResponseOutputsByStep





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_files_response_inputs_item import RunFilesResponseInputsItem
        from ..models.run_files_response_outputs_by_step import RunFilesResponseOutputsByStep
        inputs = []
        for inputs_item_data in self.inputs:
            inputs_item = inputs_item_data.to_dict()
            inputs.append(inputs_item)



        outputs_by_step = self.outputs_by_step.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "inputs": inputs,
            "outputsByStep": outputs_by_step,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_files_response_inputs_item import RunFilesResponseInputsItem
        from ..models.run_files_response_outputs_by_step import RunFilesResponseOutputsByStep
        d = dict(src_dict)
        inputs = []
        _inputs = d.pop("inputs")
        for inputs_item_data in (_inputs):
            inputs_item = RunFilesResponseInputsItem.from_dict(inputs_item_data)



            inputs.append(inputs_item)


        outputs_by_step = RunFilesResponseOutputsByStep.from_dict(d.pop("outputsByStep"))




        run_files_response = cls(
            inputs=inputs,
            outputs_by_step=outputs_by_step,
        )

        return run_files_response

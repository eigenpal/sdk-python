from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.run_cancel_response_type import RunCancelResponseType
from typing import cast

if TYPE_CHECKING:
  from ..models.run_cancel_response_cancellation import RunCancelResponseCancellation
  from ..models.run_cancel_response_execution import RunCancelResponseExecution





T = TypeVar("T", bound="RunCancelResponse")



@_attrs_define
class RunCancelResponse:
    """
        Attributes:
            id (str):
            type_ (RunCancelResponseType):
            finished (bool): True when the run has reached a terminal status.
            execution (RunCancelResponseExecution):
            cancellation (RunCancelResponseCancellation):
     """

    id: str
    type_: RunCancelResponseType
    finished: bool
    execution: RunCancelResponseExecution
    cancellation: RunCancelResponseCancellation





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_cancel_response_cancellation import RunCancelResponseCancellation
        from ..models.run_cancel_response_execution import RunCancelResponseExecution
        id = self.id

        type_ = self.type_.value

        finished = self.finished

        execution = self.execution.to_dict()

        cancellation = self.cancellation.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "type": type_,
            "finished": finished,
            "execution": execution,
            "cancellation": cancellation,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_cancel_response_cancellation import RunCancelResponseCancellation
        from ..models.run_cancel_response_execution import RunCancelResponseExecution
        d = dict(src_dict)
        id = d.pop("id")

        type_ = RunCancelResponseType(d.pop("type"))




        finished = d.pop("finished")

        execution = RunCancelResponseExecution.from_dict(d.pop("execution"))




        cancellation = RunCancelResponseCancellation.from_dict(d.pop("cancellation"))




        run_cancel_response = cls(
            id=id,
            type_=type_,
            finished=finished,
            execution=execution,
            cancellation=cancellation,
        )

        return run_cancel_response

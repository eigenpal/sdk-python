from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.run_execution_retry_next_run_type_0 import RunExecutionRetryNextRunType0





T = TypeVar("T", bound="RunExecutionRetry")



@_attrs_define
class RunExecutionRetry:
    """
        Attributes:
            number (float): Retry attempt index (0 = original run).
            previous_run_id (None | str): Run id of the prior attempt in the retry chain.
            next_run (None | RunExecutionRetryNextRunType0): Retry run spawned from this run, if any.
     """

    number: float
    previous_run_id: None | str
    next_run: None | RunExecutionRetryNextRunType0





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_execution_retry_next_run_type_0 import RunExecutionRetryNextRunType0
        number = self.number

        previous_run_id: None | str
        previous_run_id = self.previous_run_id

        next_run: dict[str, Any] | None
        if isinstance(self.next_run, RunExecutionRetryNextRunType0):
            next_run = self.next_run.to_dict()
        else:
            next_run = self.next_run


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "number": number,
            "previousRunId": previous_run_id,
            "nextRun": next_run,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_execution_retry_next_run_type_0 import RunExecutionRetryNextRunType0
        d = dict(src_dict)
        number = d.pop("number")

        def _parse_previous_run_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        previous_run_id = _parse_previous_run_id(d.pop("previousRunId"))


        def _parse_next_run(data: object) -> None | RunExecutionRetryNextRunType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                next_run_type_0 = RunExecutionRetryNextRunType0.from_dict(data)



                return next_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RunExecutionRetryNextRunType0, data)

        next_run = _parse_next_run(d.pop("nextRun"))


        run_execution_retry = cls(
            number=number,
            previous_run_id=previous_run_id,
            next_run=next_run,
        )

        return run_execution_retry

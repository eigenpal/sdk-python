from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.execution_status import ExecutionStatus
from typing import cast

if TYPE_CHECKING:
  from ..models.run_execution_retry import RunExecutionRetry





T = TypeVar("T", bound="RunExecutionMeta")



@_attrs_define
class RunExecutionMeta:
    """
        Attributes:
            status (ExecutionStatus):
            schema_valid (bool | None): Whether the completed output matched the workflow or agent output schema.
            batch_id (None | str): Experiment batch id when the run is part of a batch.
            retry (RunExecutionRetry):
     """

    status: ExecutionStatus
    schema_valid: bool | None
    batch_id: None | str
    retry: RunExecutionRetry





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_execution_retry import RunExecutionRetry
        status = self.status.value

        schema_valid: bool | None
        schema_valid = self.schema_valid

        batch_id: None | str
        batch_id = self.batch_id

        retry = self.retry.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "status": status,
            "schemaValid": schema_valid,
            "batchId": batch_id,
            "retry": retry,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_execution_retry import RunExecutionRetry
        d = dict(src_dict)
        status = ExecutionStatus(d.pop("status"))




        def _parse_schema_valid(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        schema_valid = _parse_schema_valid(d.pop("schemaValid"))


        def _parse_batch_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        batch_id = _parse_batch_id(d.pop("batchId"))


        retry = RunExecutionRetry.from_dict(d.pop("retry"))




        run_execution_meta = cls(
            status=status,
            schema_valid=schema_valid,
            batch_id=batch_id,
            retry=retry,
        )

        return run_execution_meta

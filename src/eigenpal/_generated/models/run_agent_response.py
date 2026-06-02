from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.execution_status import ExecutionStatus
from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.run_agent_response_cost import RunAgentResponseCost





T = TypeVar("T", bound="RunAgentResponse")



@_attrs_define
class RunAgentResponse:
    """ 
        Attributes:
            run_id (str):
            status (ExecutionStatus | Literal['timeout'] | Unset):
            output (Any | Unset):
            schema_valid (bool | None | Unset):
            error (None | str | Unset):
            cost (RunAgentResponseCost | Unset):
     """

    run_id: str
    status: ExecutionStatus | Literal['timeout'] | Unset = UNSET
    output: Any | Unset = UNSET
    schema_valid: bool | None | Unset = UNSET
    error: None | str | Unset = UNSET
    cost: RunAgentResponseCost | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_agent_response_cost import RunAgentResponseCost
        run_id = self.run_id

        status: Literal['timeout'] | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, ExecutionStatus):
            status = self.status.value
        else:
            status = self.status

        output = self.output

        schema_valid: bool | None | Unset
        if isinstance(self.schema_valid, Unset):
            schema_valid = UNSET
        else:
            schema_valid = self.schema_valid

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        cost: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cost, Unset):
            cost = self.cost.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "runId": run_id,
        })
        if status is not UNSET:
            field_dict["status"] = status
        if output is not UNSET:
            field_dict["output"] = output
        if schema_valid is not UNSET:
            field_dict["schemaValid"] = schema_valid
        if error is not UNSET:
            field_dict["error"] = error
        if cost is not UNSET:
            field_dict["cost"] = cost

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_agent_response_cost import RunAgentResponseCost
        d = dict(src_dict)
        run_id = d.pop("runId")

        def _parse_status(data: object) -> ExecutionStatus | Literal['timeout'] | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = ExecutionStatus(data)



                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            status_type_1 = cast(Literal['timeout'] , data)
            if status_type_1 != 'timeout':
                raise ValueError(f"status_type_1 must match const 'timeout', got '{status_type_1}'")
            return status_type_1

        status = _parse_status(d.pop("status", UNSET))


        output = d.pop("output", UNSET)

        def _parse_schema_valid(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        schema_valid = _parse_schema_valid(d.pop("schemaValid", UNSET))


        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))


        _cost = d.pop("cost", UNSET)
        cost: RunAgentResponseCost | Unset
        if isinstance(_cost,  Unset):
            cost = UNSET
        else:
            cost = RunAgentResponseCost.from_dict(_cost)




        run_agent_response = cls(
            run_id=run_id,
            status=status,
            output=output,
            schema_valid=schema_valid,
            error=error,
            cost=cost,
        )

        return run_agent_response


from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AgentSummaryStats")



@_attrs_define
class AgentSummaryStats:
    """ 
        Attributes:
            example_count (int | Unset):
            total_executions (int | Unset):
            last_execution_at (None | str | Unset):
            avg_duration_ms (float | None | Unset):
            avg_credits (float | None | Unset):
     """

    example_count: int | Unset = UNSET
    total_executions: int | Unset = UNSET
    last_execution_at: None | str | Unset = UNSET
    avg_duration_ms: float | None | Unset = UNSET
    avg_credits: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        example_count = self.example_count

        total_executions = self.total_executions

        last_execution_at: None | str | Unset
        if isinstance(self.last_execution_at, Unset):
            last_execution_at = UNSET
        else:
            last_execution_at = self.last_execution_at

        avg_duration_ms: float | None | Unset
        if isinstance(self.avg_duration_ms, Unset):
            avg_duration_ms = UNSET
        else:
            avg_duration_ms = self.avg_duration_ms

        avg_credits: float | None | Unset
        if isinstance(self.avg_credits, Unset):
            avg_credits = UNSET
        else:
            avg_credits = self.avg_credits


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if example_count is not UNSET:
            field_dict["exampleCount"] = example_count
        if total_executions is not UNSET:
            field_dict["totalExecutions"] = total_executions
        if last_execution_at is not UNSET:
            field_dict["lastExecutionAt"] = last_execution_at
        if avg_duration_ms is not UNSET:
            field_dict["avgDurationMs"] = avg_duration_ms
        if avg_credits is not UNSET:
            field_dict["avgCredits"] = avg_credits

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        example_count = d.pop("exampleCount", UNSET)

        total_executions = d.pop("totalExecutions", UNSET)

        def _parse_last_execution_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_execution_at = _parse_last_execution_at(d.pop("lastExecutionAt", UNSET))


        def _parse_avg_duration_ms(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        avg_duration_ms = _parse_avg_duration_ms(d.pop("avgDurationMs", UNSET))


        def _parse_avg_credits(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        avg_credits = _parse_avg_credits(d.pop("avgCredits", UNSET))


        agent_summary_stats = cls(
            example_count=example_count,
            total_executions=total_executions,
            last_execution_at=last_execution_at,
            avg_duration_ms=avg_duration_ms,
            avg_credits=avg_credits,
        )


        agent_summary_stats.additional_properties = d
        return agent_summary_stats

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

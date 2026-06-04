from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.execution_observability_failure_category import ExecutionObservabilityFailureCategory
from ..models.execution_observability_failure_phase import ExecutionObservabilityFailurePhase
from ..types import UNSET, Unset






T = TypeVar("T", bound="ExecutionObservabilityFailure")



@_attrs_define
class ExecutionObservabilityFailure:
    """ 
        Attributes:
            phase (ExecutionObservabilityFailurePhase):
            code (str):
            category (ExecutionObservabilityFailureCategory):
            retryable (bool):
            user_message (str):
            occurred_at (str):
            provider (str | Unset):
     """

    phase: ExecutionObservabilityFailurePhase
    code: str
    category: ExecutionObservabilityFailureCategory
    retryable: bool
    user_message: str
    occurred_at: str
    provider: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        phase = self.phase.value

        code = self.code

        category = self.category.value

        retryable = self.retryable

        user_message = self.user_message

        occurred_at = self.occurred_at

        provider = self.provider


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "phase": phase,
            "code": code,
            "category": category,
            "retryable": retryable,
            "userMessage": user_message,
            "occurredAt": occurred_at,
        })
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        phase = ExecutionObservabilityFailurePhase(d.pop("phase"))




        code = d.pop("code")

        category = ExecutionObservabilityFailureCategory(d.pop("category"))




        retryable = d.pop("retryable")

        user_message = d.pop("userMessage")

        occurred_at = d.pop("occurredAt")

        provider = d.pop("provider", UNSET)

        execution_observability_failure = cls(
            phase=phase,
            code=code,
            category=category,
            retryable=retryable,
            user_message=user_message,
            occurred_at=occurred_at,
            provider=provider,
        )

        return execution_observability_failure


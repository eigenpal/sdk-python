from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="EvalResult")



@_attrs_define
class EvalResult:
    """
        Attributes:
            id (str):
            run_id (str):
            automation_id (None | str):
            evaluator_name (str):
            evaluator_type (str):
            score (float | None):
            passed (bool | None):
            label (None | str):
            weight (float | None):
            pass_threshold (float | None):
            description (None | str):
            details (Any | None):
            error (None | str):
            created_at (str):
     """

    id: str
    run_id: str
    automation_id: None | str
    evaluator_name: str
    evaluator_type: str
    score: float | None
    passed: bool | None
    label: None | str
    weight: float | None
    pass_threshold: float | None
    description: None | str
    details: Any | None
    error: None | str
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        run_id = self.run_id

        automation_id: None | str
        automation_id = self.automation_id

        evaluator_name = self.evaluator_name

        evaluator_type = self.evaluator_type

        score: float | None
        score = self.score

        passed: bool | None
        passed = self.passed

        label: None | str
        label = self.label

        weight: float | None
        weight = self.weight

        pass_threshold: float | None
        pass_threshold = self.pass_threshold

        description: None | str
        description = self.description

        details: Any | None
        details = self.details

        error: None | str
        error = self.error

        created_at: str
        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "runId": run_id,
            "automationId": automation_id,
            "evaluatorName": evaluator_name,
            "evaluatorType": evaluator_type,
            "score": score,
            "passed": passed,
            "label": label,
            "weight": weight,
            "passThreshold": pass_threshold,
            "description": description,
            "details": details,
            "error": error,
            "createdAt": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        run_id = d.pop("runId")

        def _parse_automation_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        automation_id = _parse_automation_id(d.pop("automationId"))


        evaluator_name = d.pop("evaluatorName")

        evaluator_type = d.pop("evaluatorType")

        def _parse_score(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        score = _parse_score(d.pop("score"))


        def _parse_passed(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        passed = _parse_passed(d.pop("passed"))


        def _parse_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        label = _parse_label(d.pop("label"))


        def _parse_weight(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        weight = _parse_weight(d.pop("weight"))


        def _parse_pass_threshold(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        pass_threshold = _parse_pass_threshold(d.pop("passThreshold"))


        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))


        def _parse_details(data: object) -> Any | None:
            if data is None:
                return data
            return cast(Any | None, data)

        details = _parse_details(d.pop("details"))


        def _parse_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error = _parse_error(d.pop("error"))


        def _parse_created_at(data: object) -> str:
            return cast(str, data)

        created_at = _parse_created_at(d.pop("createdAt"))


        eval_result = cls(
            id=id,
            run_id=run_id,
            automation_id=automation_id,
            evaluator_name=evaluator_name,
            evaluator_type=evaluator_type,
            score=score,
            passed=passed,
            label=label,
            weight=weight,
            pass_threshold=pass_threshold,
            description=description,
            details=details,
            error=error,
            created_at=created_at,
        )

        return eval_result

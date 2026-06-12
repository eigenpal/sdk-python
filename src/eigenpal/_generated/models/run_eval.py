from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RunEval")



@_attrs_define
class RunEval:
    """
        Attributes:
            example (None | str): Eval example label (agent example name or workflow example id).
            score (float | None):
            passed (bool | None):
            example_id (None | str | Unset): Workflow eval example folder id (workflow runs only).
     """

    example: None | str
    score: float | None
    passed: bool | None
    example_id: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        example: None | str
        example = self.example

        score: float | None
        score = self.score

        passed: bool | None
        passed = self.passed

        example_id: None | str | Unset
        if isinstance(self.example_id, Unset):
            example_id = UNSET
        else:
            example_id = self.example_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "example": example,
            "score": score,
            "passed": passed,
        })
        if example_id is not UNSET:
            field_dict["exampleId"] = example_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_example(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        example = _parse_example(d.pop("example"))


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


        def _parse_example_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        example_id = _parse_example_id(d.pop("exampleId", UNSET))


        run_eval = cls(
            example=example,
            score=score,
            passed=passed,
            example_id=example_id,
        )

        return run_eval

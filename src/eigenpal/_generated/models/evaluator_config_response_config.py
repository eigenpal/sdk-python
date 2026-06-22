from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="EvaluatorConfigResponseConfig")



@_attrs_define
class EvaluatorConfigResponseConfig:
    """
        Attributes:
            evaluators (list[Any]): Parsed evaluator definitions from the YAML.
            pass_threshold (float): Overall score threshold required for the experiment to pass.
     """

    evaluators: list[Any]
    pass_threshold: float





    def to_dict(self) -> dict[str, Any]:
        evaluators = self.evaluators



        pass_threshold = self.pass_threshold


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "evaluators": evaluators,
            "passThreshold": pass_threshold,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        evaluators = cast(list[Any], d.pop("evaluators"))


        pass_threshold = d.pop("passThreshold")

        evaluator_config_response_config = cls(
            evaluators=evaluators,
            pass_threshold=pass_threshold,
        )

        return evaluator_config_response_config

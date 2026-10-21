from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.agent_evaluation_pass_type_1_weights import AgentEvaluationPassType1Weights





T = TypeVar("T", bound="AgentEvaluationPassType1")



@_attrs_define
class AgentEvaluationPassType1:
    """
        Attributes:
            kind (Literal['weighted']):
            weights (AgentEvaluationPassType1Weights):
            threshold (float):
     """

    kind: Literal['weighted']
    weights: AgentEvaluationPassType1Weights
    threshold: float





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_evaluation_pass_type_1_weights import AgentEvaluationPassType1Weights # noqa: PLC0415
        kind = self.kind

        weights = self.weights.to_dict()

        threshold = self.threshold


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "kind": kind,
            "weights": weights,
            "threshold": threshold,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_evaluation_pass_type_1_weights import AgentEvaluationPassType1Weights # noqa: PLC0415
        d = dict(src_dict)
        kind = cast(Literal['weighted'] , d.pop("kind"))
        if kind != 'weighted':
            raise ValueError(f"kind must match const 'weighted', got '{kind}'")

        weights = AgentEvaluationPassType1Weights.from_dict(d.pop("weights"))




        threshold = d.pop("threshold")

        agent_evaluation_pass_type_1 = cls(
            kind=kind,
            weights=weights,
            threshold=threshold,
        )

        return agent_evaluation_pass_type_1

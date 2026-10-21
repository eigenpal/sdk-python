from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.agent_evaluation import AgentEvaluation
  from ..models.agent_evaluator_config_response_source import AgentEvaluatorConfigResponseSource





T = TypeVar("T", bound="AgentEvaluatorConfigResponse")



@_attrs_define
class AgentEvaluatorConfigResponse:
    """
        Attributes:
            automation_id (str):
            automation_type (Literal['agent']):
            source (AgentEvaluatorConfigResponseSource):
            evaluation (AgentEvaluation | None):
     """

    automation_id: str
    automation_type: Literal['agent']
    source: AgentEvaluatorConfigResponseSource
    evaluation: AgentEvaluation | None





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_evaluation import AgentEvaluation # noqa: PLC0415
        from ..models.agent_evaluator_config_response_source import AgentEvaluatorConfigResponseSource # noqa: PLC0415
        automation_id = self.automation_id

        automation_type = self.automation_type

        source = self.source.to_dict()

        evaluation: dict[str, Any] | None
        if isinstance(self.evaluation, AgentEvaluation):
            evaluation = self.evaluation.to_dict()
        else:
            evaluation = self.evaluation


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "automationId": automation_id,
            "automationType": automation_type,
            "source": source,
            "evaluation": evaluation,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_evaluation import AgentEvaluation # noqa: PLC0415
        from ..models.agent_evaluator_config_response_source import AgentEvaluatorConfigResponseSource # noqa: PLC0415
        d = dict(src_dict)
        automation_id = d.pop("automationId")

        automation_type = cast(Literal['agent'] , d.pop("automationType"))
        if automation_type != 'agent':
            raise ValueError(f"automationType must match const 'agent', got '{automation_type}'")

        source = AgentEvaluatorConfigResponseSource.from_dict(d.pop("source"))




        def _parse_evaluation(data: object) -> AgentEvaluation | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                evaluation_type_0 = AgentEvaluation.from_dict(data)



                return evaluation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentEvaluation | None, data)

        evaluation = _parse_evaluation(d.pop("evaluation"))


        agent_evaluator_config_response = cls(
            automation_id=automation_id,
            automation_type=automation_type,
            source=source,
            evaluation=evaluation,
        )

        return agent_evaluator_config_response

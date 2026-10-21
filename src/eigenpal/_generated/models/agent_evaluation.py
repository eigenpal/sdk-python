from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.agent_evaluation_evaluators import AgentEvaluationEvaluators
  from ..models.agent_evaluation_pass_type_0 import AgentEvaluationPassType0
  from ..models.agent_evaluation_pass_type_1 import AgentEvaluationPassType1





T = TypeVar("T", bound="AgentEvaluation")



@_attrs_define
class AgentEvaluation:
    """
        Attributes:
            evaluators (AgentEvaluationEvaluators):
            pass_ (AgentEvaluationPassType0 | AgentEvaluationPassType1):
     """

    evaluators: AgentEvaluationEvaluators
    pass_: AgentEvaluationPassType0 | AgentEvaluationPassType1





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_evaluation_evaluators import AgentEvaluationEvaluators # noqa: PLC0415
        from ..models.agent_evaluation_pass_type_0 import AgentEvaluationPassType0 # noqa: PLC0415
        from ..models.agent_evaluation_pass_type_1 import AgentEvaluationPassType1 # noqa: PLC0415
        evaluators = self.evaluators.to_dict()

        pass_: dict[str, Any]
        if isinstance(self.pass_, AgentEvaluationPassType0):
            pass_ = self.pass_.to_dict()
        else:
            pass_ = self.pass_.to_dict()



        field_dict: dict[str, Any] = {}

        field_dict.update({
            "evaluators": evaluators,
            "pass": pass_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_evaluation_evaluators import AgentEvaluationEvaluators # noqa: PLC0415
        from ..models.agent_evaluation_pass_type_0 import AgentEvaluationPassType0 # noqa: PLC0415
        from ..models.agent_evaluation_pass_type_1 import AgentEvaluationPassType1 # noqa: PLC0415
        d = dict(src_dict)
        evaluators = AgentEvaluationEvaluators.from_dict(d.pop("evaluators"))




        def _parse_pass_(data: object) -> AgentEvaluationPassType0 | AgentEvaluationPassType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pass_type_0 = AgentEvaluationPassType0.from_dict(data)



                return pass_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            pass_type_1 = AgentEvaluationPassType1.from_dict(data)



            return pass_type_1

        pass_ = _parse_pass_(d.pop("pass"))


        agent_evaluation = cls(
            evaluators=evaluators,
            pass_=pass_,
        )

        return agent_evaluation

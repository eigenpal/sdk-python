from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.workflow_evaluator_config import WorkflowEvaluatorConfig





T = TypeVar("T", bound="WorkflowEvaluatorConfigResponse")



@_attrs_define
class WorkflowEvaluatorConfigResponse:
    """
        Attributes:
            automation_id (str):
            automation_type (Literal['workflow']):
            yaml (str): Workflow evaluator configuration YAML.
            config (WorkflowEvaluatorConfig):
     """

    automation_id: str
    automation_type: Literal['workflow']
    yaml: str
    config: WorkflowEvaluatorConfig





    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_evaluator_config import WorkflowEvaluatorConfig # noqa: PLC0415
        automation_id = self.automation_id

        automation_type = self.automation_type

        yaml = self.yaml

        config = self.config.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "automationId": automation_id,
            "automationType": automation_type,
            "yaml": yaml,
            "config": config,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_evaluator_config import WorkflowEvaluatorConfig # noqa: PLC0415
        d = dict(src_dict)
        automation_id = d.pop("automationId")

        automation_type = cast(Literal['workflow'] , d.pop("automationType"))
        if automation_type != 'workflow':
            raise ValueError(f"automationType must match const 'workflow', got '{automation_type}'")

        yaml = d.pop("yaml")

        config = WorkflowEvaluatorConfig.from_dict(d.pop("config"))




        workflow_evaluator_config_response = cls(
            automation_id=automation_id,
            automation_type=automation_type,
            yaml=yaml,
            config=config,
        )

        return workflow_evaluator_config_response

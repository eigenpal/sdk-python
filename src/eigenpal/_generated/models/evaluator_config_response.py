from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.automation_type import AutomationType
from typing import cast

if TYPE_CHECKING:
  from ..models.evaluator_config_response_config import EvaluatorConfigResponseConfig





T = TypeVar("T", bound="EvaluatorConfigResponse")



@_attrs_define
class EvaluatorConfigResponse:
    """ Evaluator YAML and parsed evaluator configuration for an automation.

        Attributes:
            automation_id (str): Automation that owns this evaluator config.
            automation_type (AutomationType):
            yaml (str): Evaluator configuration YAML.
            config (EvaluatorConfigResponseConfig):
     """

    automation_id: str
    automation_type: AutomationType
    yaml: str
    config: EvaluatorConfigResponseConfig





    def to_dict(self) -> dict[str, Any]:
        from ..models.evaluator_config_response_config import EvaluatorConfigResponseConfig
        automation_id = self.automation_id

        automation_type = self.automation_type.value

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
        from ..models.evaluator_config_response_config import EvaluatorConfigResponseConfig
        d = dict(src_dict)
        automation_id = d.pop("automationId")

        automation_type = AutomationType(d.pop("automationType"))




        yaml = d.pop("yaml")

        config = EvaluatorConfigResponseConfig.from_dict(d.pop("config"))




        evaluator_config_response = cls(
            automation_id=automation_id,
            automation_type=automation_type,
            yaml=yaml,
            config=config,
        )

        return evaluator_config_response

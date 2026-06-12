from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.run_artifact import RunArtifact





T = TypeVar("T", bound="RunArtifactsResponse")



@_attrs_define
class RunArtifactsResponse:
    """
        Attributes:
            artifacts (list[RunArtifact]):
     """

    artifacts: list[RunArtifact]





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_artifact import RunArtifact
        artifacts = []
        for artifacts_item_data in self.artifacts:
            artifacts_item = artifacts_item_data.to_dict()
            artifacts.append(artifacts_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "artifacts": artifacts,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_artifact import RunArtifact
        d = dict(src_dict)
        artifacts = []
        _artifacts = d.pop("artifacts")
        for artifacts_item_data in (_artifacts):
            artifacts_item = RunArtifact.from_dict(artifacts_item_data)



            artifacts.append(artifacts_item)


        run_artifacts_response = cls(
            artifacts=artifacts,
        )

        return run_artifacts_response

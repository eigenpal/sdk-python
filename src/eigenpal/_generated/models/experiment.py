from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.automation_type import AutomationType
from ..models.experiment_status import ExperimentStatus
from typing import cast






T = TypeVar("T", bound="Experiment")



@_attrs_define
class Experiment:
    """ Experiment batch summary for an automation dataset run.

        Attributes:
            id (str): Experiment batch id. Some CLI commands historically call this a batch id.
            automation_id (str): Automation this experiment belongs to.
            automation_type (AutomationType):
            status (ExperimentStatus): Experiment batch status.
            run_count (int): Total runs in the experiment.
            completed_count (int): Runs that have completed.
            passed_count (int): Runs whose evaluator scores passed.
            failed_count (int): Runs whose evaluator scores failed.
            avg_score (float | None): Average automated evaluator score.
            created_at (str):
            completed_at (None | str):
            version (None | str):
     """

    id: str
    automation_id: str
    automation_type: AutomationType
    status: ExperimentStatus
    run_count: int
    completed_count: int
    passed_count: int
    failed_count: int
    avg_score: float | None
    created_at: str
    completed_at: None | str
    version: None | str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        automation_id = self.automation_id

        automation_type = self.automation_type.value

        status = self.status.value

        run_count = self.run_count

        completed_count = self.completed_count

        passed_count = self.passed_count

        failed_count = self.failed_count

        avg_score: float | None
        avg_score = self.avg_score

        created_at: str
        created_at = self.created_at

        completed_at: None | str
        completed_at = self.completed_at

        version: None | str
        version = self.version


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "automationId": automation_id,
            "automationType": automation_type,
            "status": status,
            "runCount": run_count,
            "completedCount": completed_count,
            "passedCount": passed_count,
            "failedCount": failed_count,
            "avgScore": avg_score,
            "createdAt": created_at,
            "completedAt": completed_at,
            "version": version,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        automation_id = d.pop("automationId")

        automation_type = AutomationType(d.pop("automationType"))




        status = ExperimentStatus(d.pop("status"))




        run_count = d.pop("runCount")

        completed_count = d.pop("completedCount")

        passed_count = d.pop("passedCount")

        failed_count = d.pop("failedCount")

        def _parse_avg_score(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        avg_score = _parse_avg_score(d.pop("avgScore"))


        def _parse_created_at(data: object) -> str:
            return cast(str, data)

        created_at = _parse_created_at(d.pop("createdAt"))


        def _parse_completed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        completed_at = _parse_completed_at(d.pop("completedAt"))


        def _parse_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        version = _parse_version(d.pop("version"))


        experiment = cls(
            id=id,
            automation_id=automation_id,
            automation_type=automation_type,
            status=status,
            run_count=run_count,
            completed_count=completed_count,
            passed_count=passed_count,
            failed_count=failed_count,
            avg_score=avg_score,
            created_at=created_at,
            completed_at=completed_at,
            version=version,
        )

        return experiment

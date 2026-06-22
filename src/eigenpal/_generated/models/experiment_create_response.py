from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.experiment_create_response_runs_item import ExperimentCreateResponseRunsItem





T = TypeVar("T", bound="ExperimentCreateResponse")



@_attrs_define
class ExperimentCreateResponse:
    """ Accepted experiment batch and the runs it enqueued.

        Attributes:
            id (str): Experiment batch id.
            runs (list[ExperimentCreateResponseRunsItem]): Runs enqueued for this experiment.
            total (int): Number of runs enqueued.
     """

    id: str
    runs: list[ExperimentCreateResponseRunsItem]
    total: int





    def to_dict(self) -> dict[str, Any]:
        from ..models.experiment_create_response_runs_item import ExperimentCreateResponseRunsItem
        id = self.id

        runs = []
        for runs_item_data in self.runs:
            runs_item = runs_item_data.to_dict()
            runs.append(runs_item)



        total = self.total


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "runs": runs,
            "total": total,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.experiment_create_response_runs_item import ExperimentCreateResponseRunsItem
        d = dict(src_dict)
        id = d.pop("id")

        runs = []
        _runs = d.pop("runs")
        for runs_item_data in (_runs):
            runs_item = ExperimentCreateResponseRunsItem.from_dict(runs_item_data)



            runs.append(runs_item)


        total = d.pop("total")

        experiment_create_response = cls(
            id=id,
            runs=runs,
            total=total,
        )

        return experiment_create_response

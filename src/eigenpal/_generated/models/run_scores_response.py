from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.eval_result import EvalResult





T = TypeVar("T", bound="RunScoresResponse")



@_attrs_define
class RunScoresResponse:
    """ Automated evaluator results attached to a run.

        Attributes:
            scores (list[EvalResult]): Automated evaluator scores for the run. These are separate from human feedback
                `rating` values.
     """

    scores: list[EvalResult]





    def to_dict(self) -> dict[str, Any]:
        from ..models.eval_result import EvalResult
        scores = []
        for scores_item_data in self.scores:
            scores_item = scores_item_data.to_dict()
            scores.append(scores_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "scores": scores,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eval_result import EvalResult
        d = dict(src_dict)
        scores = []
        _scores = d.pop("scores")
        for scores_item_data in (_scores):
            scores_item = EvalResult.from_dict(scores_item_data)



            scores.append(scores_item)


        run_scores_response = cls(
            scores=scores,
        )

        return run_scores_response

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.eval_result import EvalResult





T = TypeVar("T", bound="EvalResultsResponse")



@_attrs_define
class EvalResultsResponse:
    """
        Attributes:
            results (list[EvalResult]):
     """

    results: list[EvalResult]





    def to_dict(self) -> dict[str, Any]:
        from ..models.eval_result import EvalResult
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "results": results,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eval_result import EvalResult
        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in (_results):
            results_item = EvalResult.from_dict(results_item_data)



            results.append(results_item)


        eval_results_response = cls(
            results=results,
        )

        return eval_results_response

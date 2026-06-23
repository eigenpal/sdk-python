from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Literal, cast






T = TypeVar("T", bound="RunReviewHealthConfidence")



@_attrs_define
class RunReviewHealthConfidence:
    """ Wilson score confidence interval for reviewed correctness. Null bounds mean there are no reviewed runs in the
    sample.

        Attributes:
            lower (float | None):
            upper (float | None):
            method (Literal['wilson']):
     """

    lower: float | None
    upper: float | None
    method: Literal['wilson']





    def to_dict(self) -> dict[str, Any]:
        lower: float | None
        lower = self.lower

        upper: float | None
        upper = self.upper

        method = self.method


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "lower": lower,
            "upper": upper,
            "method": method,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_lower(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        lower = _parse_lower(d.pop("lower"))


        def _parse_upper(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        upper = _parse_upper(d.pop("upper"))


        method = cast(Literal['wilson'] , d.pop("method"))
        if method != 'wilson':
            raise ValueError(f"method must match const 'wilson', got '{method}'")

        run_review_health_confidence = cls(
            lower=lower,
            upper=upper,
            method=method,
        )

        return run_review_health_confidence

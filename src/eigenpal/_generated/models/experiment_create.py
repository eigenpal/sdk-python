from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ExperimentCreate")



@_attrs_define
class ExperimentCreate:
    """
        Attributes:
            examples (list[str] | Unset):
            batch_concurrency (int | None | Unset):
            source_ref (str | Unset):
     """

    examples: list[str] | Unset = UNSET
    batch_concurrency: int | None | Unset = UNSET
    source_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        examples: list[str] | Unset = UNSET
        if not isinstance(self.examples, Unset):
            examples = self.examples



        batch_concurrency: int | None | Unset
        if isinstance(self.batch_concurrency, Unset):
            batch_concurrency = UNSET
        else:
            batch_concurrency = self.batch_concurrency

        source_ref = self.source_ref


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if examples is not UNSET:
            field_dict["examples"] = examples
        if batch_concurrency is not UNSET:
            field_dict["batchConcurrency"] = batch_concurrency
        if source_ref is not UNSET:
            field_dict["sourceRef"] = source_ref

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        examples = cast(list[str], d.pop("examples", UNSET))


        def _parse_batch_concurrency(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        batch_concurrency = _parse_batch_concurrency(d.pop("batchConcurrency", UNSET))


        source_ref = d.pop("sourceRef", UNSET)

        experiment_create = cls(
            examples=examples,
            batch_concurrency=batch_concurrency,
            source_ref=source_ref,
        )


        experiment_create.additional_properties = d
        return experiment_create

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

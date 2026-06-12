from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.run_accepted_type import RunAcceptedType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.run_source import RunSource





T = TypeVar("T", bound="RunAccepted")



@_attrs_define
class RunAccepted:
    """
        Attributes:
            id (str):
            type_ (RunAcceptedType):
            finished (bool):
            source (RunSource | Unset):
     """

    id: str
    type_: RunAcceptedType
    finished: bool
    source: RunSource | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_source import RunSource
        id = self.id

        type_ = self.type_.value

        finished = self.finished

        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "type": type_,
            "finished": finished,
        })
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_source import RunSource
        d = dict(src_dict)
        id = d.pop("id")

        type_ = RunAcceptedType(d.pop("type"))




        finished = d.pop("finished")

        _source = d.pop("source", UNSET)
        source: RunSource | Unset
        if isinstance(_source,  Unset):
            source = UNSET
        else:
            source = RunSource.from_dict(_source)




        run_accepted = cls(
            id=id,
            type_=type_,
            finished=finished,
            source=source,
        )

        return run_accepted

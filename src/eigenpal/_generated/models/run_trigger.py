from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.run_trigger_by_type_0 import RunTriggerByType0





T = TypeVar("T", bound="RunTrigger")



@_attrs_define
class RunTrigger:
    """
        Attributes:
            type_ (None | str):
            by (None | RunTriggerByType0):
            email (Any | Unset): Inbound email trigger details (agent runs, `expand=input` not required).
     """

    type_: None | str
    by: None | RunTriggerByType0
    email: Any | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_trigger_by_type_0 import RunTriggerByType0
        type_: None | str
        type_ = self.type_

        by: dict[str, Any] | None
        if isinstance(self.by, RunTriggerByType0):
            by = self.by.to_dict()
        else:
            by = self.by

        email = self.email


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
            "by": by,
        })
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_trigger_by_type_0 import RunTriggerByType0
        d = dict(src_dict)
        def _parse_type_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        type_ = _parse_type_(d.pop("type"))


        def _parse_by(data: object) -> None | RunTriggerByType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                by_type_0 = RunTriggerByType0.from_dict(data)



                return by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RunTriggerByType0, data)

        by = _parse_by(d.pop("by"))


        email = d.pop("email", UNSET)

        run_trigger = cls(
            type_=type_,
            by=by,
            email=email,
        )

        return run_trigger

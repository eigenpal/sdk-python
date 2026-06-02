from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AgentExecutionSummaryTriggeredByType0")



@_attrs_define
class AgentExecutionSummaryTriggeredByType0:
    """ 
        Attributes:
            id (str):
            email (str):
            name (None | str | Unset):
     """

    id: str
    email: str
    name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "email": email,
        })
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        agent_execution_summary_triggered_by_type_0 = cls(
            id=id,
            email=email,
            name=name,
        )

        return agent_execution_summary_triggered_by_type_0


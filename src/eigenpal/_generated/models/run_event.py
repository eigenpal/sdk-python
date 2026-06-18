from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.run_event_metadata import RunEventMetadata





T = TypeVar("T", bound="RunEvent")



@_attrs_define
class RunEvent:
    """
        Attributes:
            type_ (str):
            timestamp (str):
            status (None | str | Unset):
            message (None | str | Unset):
            metadata (RunEventMetadata | Unset):
     """

    type_: str
    timestamp: str
    status: None | str | Unset = UNSET
    message: None | str | Unset = UNSET
    metadata: RunEventMetadata | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_event_metadata import RunEventMetadata
        type_ = self.type_

        timestamp = self.timestamp

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
            "timestamp": timestamp,
        })
        if status is not UNSET:
            field_dict["status"] = status
        if message is not UNSET:
            field_dict["message"] = message
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_event_metadata import RunEventMetadata
        d = dict(src_dict)
        type_ = d.pop("type")

        timestamp = d.pop("timestamp")

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))


        _metadata = d.pop("metadata", UNSET)
        metadata: RunEventMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = RunEventMetadata.from_dict(_metadata)




        run_event = cls(
            type_=type_,
            timestamp=timestamp,
            status=status,
            message=message,
            metadata=metadata,
        )

        return run_event

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.run_start_body_files import RunStartBodyFiles
  from ..models.run_start_body_input import RunStartBodyInput
  from ..models.run_start_body_metadata import RunStartBodyMetadata
  from ..models.run_start_body_overrides import RunStartBodyOverrides





T = TypeVar("T", bound="RunStartBody")



@_attrs_define
class RunStartBody:
    """ Run envelope. Declare provenance with the `X-Eigenpal-Trigger` header (`api` or `cli`). Legacy 0.5.12 body shapes
    remain accepted.

        Attributes:
            target (str): Automation target without a version suffix, e.g. workflows.invoice or agents.support.
            input_ (RunStartBodyInput | Unset): Scalar and structured automation arguments.
            files (RunStartBodyFiles | Unset): File inputs as references (`{ fileId, filename?, mimeType? }`). Upload bytes
                via multipart `files.<fieldName>` parts instead.
            overrides (RunStartBodyOverrides | Unset): Per-step output overrides. Workflow runs only.
            metadata (RunStartBodyMetadata | Unset): Caller-supplied run metadata.
     """

    target: str
    input_: RunStartBodyInput | Unset = UNSET
    files: RunStartBodyFiles | Unset = UNSET
    overrides: RunStartBodyOverrides | Unset = UNSET
    metadata: RunStartBodyMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_start_body_files import RunStartBodyFiles
        from ..models.run_start_body_input import RunStartBodyInput
        from ..models.run_start_body_metadata import RunStartBodyMetadata
        from ..models.run_start_body_overrides import RunStartBodyOverrides
        target = self.target

        input_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_, Unset):
            input_ = self.input_.to_dict()

        files: dict[str, Any] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = self.files.to_dict()

        overrides: dict[str, Any] | Unset = UNSET
        if not isinstance(self.overrides, Unset):
            overrides = self.overrides.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "target": target,
        })
        if input_ is not UNSET:
            field_dict["input"] = input_
        if files is not UNSET:
            field_dict["files"] = files
        if overrides is not UNSET:
            field_dict["overrides"] = overrides
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_start_body_files import RunStartBodyFiles
        from ..models.run_start_body_input import RunStartBodyInput
        from ..models.run_start_body_metadata import RunStartBodyMetadata
        from ..models.run_start_body_overrides import RunStartBodyOverrides
        d = dict(src_dict)
        target = d.pop("target")

        _input_ = d.pop("input", UNSET)
        input_: RunStartBodyInput | Unset
        if isinstance(_input_,  Unset):
            input_ = UNSET
        else:
            input_ = RunStartBodyInput.from_dict(_input_)




        _files = d.pop("files", UNSET)
        files: RunStartBodyFiles | Unset
        if isinstance(_files,  Unset):
            files = UNSET
        else:
            files = RunStartBodyFiles.from_dict(_files)




        _overrides = d.pop("overrides", UNSET)
        overrides: RunStartBodyOverrides | Unset
        if isinstance(_overrides,  Unset):
            overrides = UNSET
        else:
            overrides = RunStartBodyOverrides.from_dict(_overrides)




        _metadata = d.pop("metadata", UNSET)
        metadata: RunStartBodyMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = RunStartBodyMetadata.from_dict(_metadata)




        run_start_body = cls(
            target=target,
            input_=input_,
            files=files,
            overrides=overrides,
            metadata=metadata,
        )


        run_start_body.additional_properties = d
        return run_start_body

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

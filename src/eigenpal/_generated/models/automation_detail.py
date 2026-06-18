from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.automation_type import AutomationType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.automation_detail_input_schema_type_0 import AutomationDetailInputSchemaType0
  from ..models.automation_detail_output_schema_type_0 import AutomationDetailOutputSchemaType0
  from ..models.automation_trigger_state import AutomationTriggerState





T = TypeVar("T", bound="AutomationDetail")



@_attrs_define
class AutomationDetail:
    """
        Attributes:
            id (str): Implementation id for the automation. Workflow automations use workflow ids; agent automations use
                agent workflow ids.
            type_ (AutomationType):
            slug (str):
            name (None | str):
            created_at (str):
            description (None | str | Unset):
            status (str | Unset):
            version (None | str | Unset):
            triggers (AutomationTriggerState | Unset):
            implementation_available (bool | Unset): False when the automations registry row exists but the workflow/agent
                implementation row is missing.
            updated_at (str | Unset):
            input_schema (AutomationDetailInputSchemaType0 | None | Unset):
            output_schema (AutomationDetailOutputSchemaType0 | None | Unset):
     """

    id: str
    type_: AutomationType
    slug: str
    name: None | str
    created_at: str
    description: None | str | Unset = UNSET
    status: str | Unset = UNSET
    version: None | str | Unset = UNSET
    triggers: AutomationTriggerState | Unset = UNSET
    implementation_available: bool | Unset = UNSET
    updated_at: str | Unset = UNSET
    input_schema: AutomationDetailInputSchemaType0 | None | Unset = UNSET
    output_schema: AutomationDetailOutputSchemaType0 | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.automation_detail_input_schema_type_0 import AutomationDetailInputSchemaType0
        from ..models.automation_detail_output_schema_type_0 import AutomationDetailOutputSchemaType0
        from ..models.automation_trigger_state import AutomationTriggerState
        id = self.id

        type_ = self.type_.value

        slug = self.slug

        name: None | str
        name = self.name

        created_at: str
        created_at = self.created_at

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        status = self.status

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        triggers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.triggers, Unset):
            triggers = self.triggers.to_dict()

        implementation_available = self.implementation_available

        updated_at: str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = self.updated_at

        input_schema: dict[str, Any] | None | Unset
        if isinstance(self.input_schema, Unset):
            input_schema = UNSET
        elif isinstance(self.input_schema, AutomationDetailInputSchemaType0):
            input_schema = self.input_schema.to_dict()
        else:
            input_schema = self.input_schema

        output_schema: dict[str, Any] | None | Unset
        if isinstance(self.output_schema, Unset):
            output_schema = UNSET
        elif isinstance(self.output_schema, AutomationDetailOutputSchemaType0):
            output_schema = self.output_schema.to_dict()
        else:
            output_schema = self.output_schema


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "type": type_,
            "slug": slug,
            "name": name,
            "createdAt": created_at,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
        if version is not UNSET:
            field_dict["version"] = version
        if triggers is not UNSET:
            field_dict["triggers"] = triggers
        if implementation_available is not UNSET:
            field_dict["implementationAvailable"] = implementation_available
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if input_schema is not UNSET:
            field_dict["inputSchema"] = input_schema
        if output_schema is not UNSET:
            field_dict["outputSchema"] = output_schema

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automation_detail_input_schema_type_0 import AutomationDetailInputSchemaType0
        from ..models.automation_detail_output_schema_type_0 import AutomationDetailOutputSchemaType0
        from ..models.automation_trigger_state import AutomationTriggerState
        d = dict(src_dict)
        id = d.pop("id")

        type_ = AutomationType(d.pop("type"))




        slug = d.pop("slug")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))


        def _parse_created_at(data: object) -> str:
            return cast(str, data)

        created_at = _parse_created_at(d.pop("createdAt"))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        status = d.pop("status", UNSET)

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))


        _triggers = d.pop("triggers", UNSET)
        triggers: AutomationTriggerState | Unset
        if isinstance(_triggers,  Unset):
            triggers = UNSET
        else:
            triggers = AutomationTriggerState.from_dict(_triggers)




        implementation_available = d.pop("implementationAvailable", UNSET)

        def _parse_updated_at(data: object) -> str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(str | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))


        def _parse_input_schema(data: object) -> AutomationDetailInputSchemaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                input_schema_type_0 = AutomationDetailInputSchemaType0.from_dict(data)



                return input_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AutomationDetailInputSchemaType0 | None | Unset, data)

        input_schema = _parse_input_schema(d.pop("inputSchema", UNSET))


        def _parse_output_schema(data: object) -> AutomationDetailOutputSchemaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                output_schema_type_0 = AutomationDetailOutputSchemaType0.from_dict(data)



                return output_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AutomationDetailOutputSchemaType0 | None | Unset, data)

        output_schema = _parse_output_schema(d.pop("outputSchema", UNSET))


        automation_detail = cls(
            id=id,
            type_=type_,
            slug=slug,
            name=name,
            created_at=created_at,
            description=description,
            status=status,
            version=version,
            triggers=triggers,
            implementation_available=implementation_available,
            updated_at=updated_at,
            input_schema=input_schema,
            output_schema=output_schema,
        )

        return automation_detail

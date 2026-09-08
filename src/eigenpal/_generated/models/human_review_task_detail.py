from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.human_review_task_detail_source_kind import HumanReviewTaskDetailSourceKind
from ..models.human_review_task_detail_status import HumanReviewTaskDetailStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.human_review_task_detail_decisions_item import HumanReviewTaskDetailDecisionsItem
  from ..models.human_review_task_detail_draft_data_type_0 import HumanReviewTaskDetailDraftDataType0
  from ..models.human_review_task_detail_field_metadata import HumanReviewTaskDetailFieldMetadata
  from ..models.human_review_task_detail_files_item import HumanReviewTaskDetailFilesItem
  from ..models.human_review_task_detail_input_type_0_type_0 import HumanReviewTaskDetailInputType0Type0
  from ..models.human_review_task_detail_input_type_0_type_1 import HumanReviewTaskDetailInputType0Type1
  from ..models.human_review_task_detail_lineage import HumanReviewTaskDetailLineage
  from ..models.human_review_task_detail_machine_data_type_0 import HumanReviewTaskDetailMachineDataType0
  from ..models.human_review_task_detail_parsed_document import HumanReviewTaskDetailParsedDocument
  from ..models.human_review_task_detail_schema_type_0 import HumanReviewTaskDetailSchemaType0
  from ..models.human_review_task_detail_selection_reasons import HumanReviewTaskDetailSelectionReasons





T = TypeVar("T", bound="HumanReviewTaskDetail")



@_attrs_define
class HumanReviewTaskDetail:
    """
        Attributes:
            id (str):
            execution_id (str):
            automation_id (str):
            automation_name (str):
            source_kind (HumanReviewTaskDetailSourceKind):
            source_label (str):
            status (HumanReviewTaskDetailStatus):
            required_count (int):
            confirmed_count (int):
            version (int):
            created_at (str):
            updated_at (str):
            files (list[HumanReviewTaskDetailFilesItem]):
            input_ (HumanReviewTaskDetailInputType0Type0 | HumanReviewTaskDetailInputType0Type1 | None): Non-file trigger
                input derived at read time. Null when every field is a file or external source id. omitted_too_large when the
                projection exceeds the review data byte limit.
            machine_data (HumanReviewTaskDetailMachineDataType0 | list[Any]):
            draft_data (HumanReviewTaskDetailDraftDataType0 | list[Any]):
            schema (HumanReviewTaskDetailSchemaType0 | None):
            field_metadata (HumanReviewTaskDetailFieldMetadata):
            required_paths (list[str]):
            selection_reasons (HumanReviewTaskDetailSelectionReasons):
            decisions (list[HumanReviewTaskDetailDecisionsItem]):
            instructions (None | str):
            completed_by (None | str):
            completed_at (None | str):
            outcome_reason (None | str):
            lineage (HumanReviewTaskDetailLineage | Unset): Optional lineage@1 document resolved from the extract sidecar.
                Omitted when missing or unreadable. Validate with @openparser/lineage.
            parsed_document (HumanReviewTaskDetailParsedDocument | Unset): Optional ParsedDocument resolved from the extract
                sidecar. Omitted when missing or unreadable. Validate with @openparser/schema.
     """

    id: str
    execution_id: str
    automation_id: str
    automation_name: str
    source_kind: HumanReviewTaskDetailSourceKind
    source_label: str
    status: HumanReviewTaskDetailStatus
    required_count: int
    confirmed_count: int
    version: int
    created_at: str
    updated_at: str
    files: list[HumanReviewTaskDetailFilesItem]
    input_: HumanReviewTaskDetailInputType0Type0 | HumanReviewTaskDetailInputType0Type1 | None
    machine_data: HumanReviewTaskDetailMachineDataType0 | list[Any]
    draft_data: HumanReviewTaskDetailDraftDataType0 | list[Any]
    schema: HumanReviewTaskDetailSchemaType0 | None
    field_metadata: HumanReviewTaskDetailFieldMetadata
    required_paths: list[str]
    selection_reasons: HumanReviewTaskDetailSelectionReasons
    decisions: list[HumanReviewTaskDetailDecisionsItem]
    instructions: None | str
    completed_by: None | str
    completed_at: None | str
    outcome_reason: None | str
    lineage: HumanReviewTaskDetailLineage | Unset = UNSET
    parsed_document: HumanReviewTaskDetailParsedDocument | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.human_review_task_detail_decisions_item import HumanReviewTaskDetailDecisionsItem
        from ..models.human_review_task_detail_draft_data_type_0 import HumanReviewTaskDetailDraftDataType0
        from ..models.human_review_task_detail_field_metadata import HumanReviewTaskDetailFieldMetadata
        from ..models.human_review_task_detail_files_item import HumanReviewTaskDetailFilesItem
        from ..models.human_review_task_detail_input_type_0_type_0 import HumanReviewTaskDetailInputType0Type0
        from ..models.human_review_task_detail_input_type_0_type_1 import HumanReviewTaskDetailInputType0Type1
        from ..models.human_review_task_detail_lineage import HumanReviewTaskDetailLineage
        from ..models.human_review_task_detail_machine_data_type_0 import HumanReviewTaskDetailMachineDataType0
        from ..models.human_review_task_detail_parsed_document import HumanReviewTaskDetailParsedDocument
        from ..models.human_review_task_detail_schema_type_0 import HumanReviewTaskDetailSchemaType0
        from ..models.human_review_task_detail_selection_reasons import HumanReviewTaskDetailSelectionReasons
        id = self.id

        execution_id = self.execution_id

        automation_id = self.automation_id

        automation_name = self.automation_name

        source_kind = self.source_kind.value

        source_label = self.source_label

        status = self.status.value

        required_count = self.required_count

        confirmed_count = self.confirmed_count

        version = self.version

        created_at = self.created_at

        updated_at = self.updated_at

        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)



        input_: dict[str, Any] | None
        if isinstance(self.input_, HumanReviewTaskDetailInputType0Type0):
            input_ = self.input_.to_dict()
        elif isinstance(self.input_, HumanReviewTaskDetailInputType0Type1):
            input_ = self.input_.to_dict()
        else:
            input_ = self.input_

        machine_data: dict[str, Any] | list[Any]
        if isinstance(self.machine_data, HumanReviewTaskDetailMachineDataType0):
            machine_data = self.machine_data.to_dict()
        else:
            machine_data = self.machine_data




        draft_data: dict[str, Any] | list[Any]
        if isinstance(self.draft_data, HumanReviewTaskDetailDraftDataType0):
            draft_data = self.draft_data.to_dict()
        else:
            draft_data = self.draft_data




        schema: dict[str, Any] | None
        if isinstance(self.schema, HumanReviewTaskDetailSchemaType0):
            schema = self.schema.to_dict()
        else:
            schema = self.schema

        field_metadata = self.field_metadata.to_dict()

        required_paths = self.required_paths



        selection_reasons = self.selection_reasons.to_dict()

        decisions = []
        for decisions_item_data in self.decisions:
            decisions_item = decisions_item_data.to_dict()
            decisions.append(decisions_item)



        instructions: None | str
        instructions = self.instructions

        completed_by: None | str
        completed_by = self.completed_by

        completed_at: None | str
        completed_at = self.completed_at

        outcome_reason: None | str
        outcome_reason = self.outcome_reason

        lineage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lineage, Unset):
            lineage = self.lineage.to_dict()

        parsed_document: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parsed_document, Unset):
            parsed_document = self.parsed_document.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "executionId": execution_id,
            "automationId": automation_id,
            "automationName": automation_name,
            "sourceKind": source_kind,
            "sourceLabel": source_label,
            "status": status,
            "requiredCount": required_count,
            "confirmedCount": confirmed_count,
            "version": version,
            "createdAt": created_at,
            "updatedAt": updated_at,
            "files": files,
            "input": input_,
            "machineData": machine_data,
            "draftData": draft_data,
            "schema": schema,
            "fieldMetadata": field_metadata,
            "requiredPaths": required_paths,
            "selectionReasons": selection_reasons,
            "decisions": decisions,
            "instructions": instructions,
            "completedBy": completed_by,
            "completedAt": completed_at,
            "outcomeReason": outcome_reason,
        })
        if lineage is not UNSET:
            field_dict["lineage"] = lineage
        if parsed_document is not UNSET:
            field_dict["parsedDocument"] = parsed_document

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.human_review_task_detail_decisions_item import HumanReviewTaskDetailDecisionsItem
        from ..models.human_review_task_detail_draft_data_type_0 import HumanReviewTaskDetailDraftDataType0
        from ..models.human_review_task_detail_field_metadata import HumanReviewTaskDetailFieldMetadata
        from ..models.human_review_task_detail_files_item import HumanReviewTaskDetailFilesItem
        from ..models.human_review_task_detail_input_type_0_type_0 import HumanReviewTaskDetailInputType0Type0
        from ..models.human_review_task_detail_input_type_0_type_1 import HumanReviewTaskDetailInputType0Type1
        from ..models.human_review_task_detail_lineage import HumanReviewTaskDetailLineage
        from ..models.human_review_task_detail_machine_data_type_0 import HumanReviewTaskDetailMachineDataType0
        from ..models.human_review_task_detail_parsed_document import HumanReviewTaskDetailParsedDocument
        from ..models.human_review_task_detail_schema_type_0 import HumanReviewTaskDetailSchemaType0
        from ..models.human_review_task_detail_selection_reasons import HumanReviewTaskDetailSelectionReasons
        d = dict(src_dict)
        id = d.pop("id")

        execution_id = d.pop("executionId")

        automation_id = d.pop("automationId")

        automation_name = d.pop("automationName")

        source_kind = HumanReviewTaskDetailSourceKind(d.pop("sourceKind"))




        source_label = d.pop("sourceLabel")

        status = HumanReviewTaskDetailStatus(d.pop("status"))




        required_count = d.pop("requiredCount")

        confirmed_count = d.pop("confirmedCount")

        version = d.pop("version")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        files = []
        _files = d.pop("files")
        for files_item_data in (_files):
            files_item = HumanReviewTaskDetailFilesItem.from_dict(files_item_data)



            files.append(files_item)


        def _parse_input_(data: object) -> HumanReviewTaskDetailInputType0Type0 | HumanReviewTaskDetailInputType0Type1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                input_type_0_type_0 = HumanReviewTaskDetailInputType0Type0.from_dict(data)



                return input_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                input_type_0_type_1 = HumanReviewTaskDetailInputType0Type1.from_dict(data)



                return input_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HumanReviewTaskDetailInputType0Type0 | HumanReviewTaskDetailInputType0Type1 | None, data)

        input_ = _parse_input_(d.pop("input"))


        def _parse_machine_data(data: object) -> HumanReviewTaskDetailMachineDataType0 | list[Any]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                machine_data_type_0 = HumanReviewTaskDetailMachineDataType0.from_dict(data)



                return machine_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            machine_data_type_1 = cast(list[Any], data)

            return machine_data_type_1

        machine_data = _parse_machine_data(d.pop("machineData"))


        def _parse_draft_data(data: object) -> HumanReviewTaskDetailDraftDataType0 | list[Any]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                draft_data_type_0 = HumanReviewTaskDetailDraftDataType0.from_dict(data)



                return draft_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            draft_data_type_1 = cast(list[Any], data)

            return draft_data_type_1

        draft_data = _parse_draft_data(d.pop("draftData"))


        def _parse_schema(data: object) -> HumanReviewTaskDetailSchemaType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schema_type_0 = HumanReviewTaskDetailSchemaType0.from_dict(data)



                return schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HumanReviewTaskDetailSchemaType0 | None, data)

        schema = _parse_schema(d.pop("schema"))


        field_metadata = HumanReviewTaskDetailFieldMetadata.from_dict(d.pop("fieldMetadata"))




        required_paths = cast(list[str], d.pop("requiredPaths"))


        selection_reasons = HumanReviewTaskDetailSelectionReasons.from_dict(d.pop("selectionReasons"))




        decisions = []
        _decisions = d.pop("decisions")
        for decisions_item_data in (_decisions):
            decisions_item = HumanReviewTaskDetailDecisionsItem.from_dict(decisions_item_data)



            decisions.append(decisions_item)


        def _parse_instructions(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        instructions = _parse_instructions(d.pop("instructions"))


        def _parse_completed_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        completed_by = _parse_completed_by(d.pop("completedBy"))


        def _parse_completed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        completed_at = _parse_completed_at(d.pop("completedAt"))


        def _parse_outcome_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        outcome_reason = _parse_outcome_reason(d.pop("outcomeReason"))


        _lineage = d.pop("lineage", UNSET)
        lineage: HumanReviewTaskDetailLineage | Unset
        if isinstance(_lineage,  Unset):
            lineage = UNSET
        else:
            lineage = HumanReviewTaskDetailLineage.from_dict(_lineage)




        _parsed_document = d.pop("parsedDocument", UNSET)
        parsed_document: HumanReviewTaskDetailParsedDocument | Unset
        if isinstance(_parsed_document,  Unset):
            parsed_document = UNSET
        else:
            parsed_document = HumanReviewTaskDetailParsedDocument.from_dict(_parsed_document)




        human_review_task_detail = cls(
            id=id,
            execution_id=execution_id,
            automation_id=automation_id,
            automation_name=automation_name,
            source_kind=source_kind,
            source_label=source_label,
            status=status,
            required_count=required_count,
            confirmed_count=confirmed_count,
            version=version,
            created_at=created_at,
            updated_at=updated_at,
            files=files,
            input_=input_,
            machine_data=machine_data,
            draft_data=draft_data,
            schema=schema,
            field_metadata=field_metadata,
            required_paths=required_paths,
            selection_reasons=selection_reasons,
            decisions=decisions,
            instructions=instructions,
            completed_by=completed_by,
            completed_at=completed_at,
            outcome_reason=outcome_reason,
            lineage=lineage,
            parsed_document=parsed_document,
        )

        return human_review_task_detail

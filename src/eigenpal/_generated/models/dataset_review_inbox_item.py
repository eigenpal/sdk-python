from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.dataset_review_inbox_item_status import DatasetReviewInboxItemStatus
from typing import cast

if TYPE_CHECKING:
  from ..models.dataset_review_focus_field_output import DatasetReviewFocusFieldOutput
  from ..models.dataset_review_progress import DatasetReviewProgress





T = TypeVar("T", bound="DatasetReviewInboxItem")



@_attrs_define
class DatasetReviewInboxItem:
    """
        Attributes:
            id (str):
            automation_id (str):
            title (str):
            instructions (None | str):
            focus_fields (list[DatasetReviewFocusFieldOutput]):
            ignored_fields (list[str]):
            status (DatasetReviewInboxItemStatus):
            example_names (list[str]):
            progress (DatasetReviewProgress):
            created_by (None | str):
            created_at (str):
            closed_at (None | str):
            automation_name (str): Display name for the automation that owns this review request.
     """

    id: str
    automation_id: str
    title: str
    instructions: None | str
    focus_fields: list[DatasetReviewFocusFieldOutput]
    ignored_fields: list[str]
    status: DatasetReviewInboxItemStatus
    example_names: list[str]
    progress: DatasetReviewProgress
    created_by: None | str
    created_at: str
    closed_at: None | str
    automation_name: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.dataset_review_focus_field_output import DatasetReviewFocusFieldOutput
        from ..models.dataset_review_progress import DatasetReviewProgress
        id = self.id

        automation_id = self.automation_id

        title = self.title

        instructions: None | str
        instructions = self.instructions

        focus_fields = []
        for focus_fields_item_data in self.focus_fields:
            focus_fields_item = focus_fields_item_data.to_dict()
            focus_fields.append(focus_fields_item)



        ignored_fields = self.ignored_fields



        status = self.status.value

        example_names = self.example_names



        progress = self.progress.to_dict()

        created_by: None | str
        created_by = self.created_by

        created_at = self.created_at

        closed_at: None | str
        closed_at = self.closed_at

        automation_name = self.automation_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "automationId": automation_id,
            "title": title,
            "instructions": instructions,
            "focusFields": focus_fields,
            "ignoredFields": ignored_fields,
            "status": status,
            "exampleNames": example_names,
            "progress": progress,
            "createdBy": created_by,
            "createdAt": created_at,
            "closedAt": closed_at,
            "automationName": automation_name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_review_focus_field_output import DatasetReviewFocusFieldOutput
        from ..models.dataset_review_progress import DatasetReviewProgress
        d = dict(src_dict)
        id = d.pop("id")

        automation_id = d.pop("automationId")

        title = d.pop("title")

        def _parse_instructions(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        instructions = _parse_instructions(d.pop("instructions"))


        focus_fields = []
        _focus_fields = d.pop("focusFields")
        for focus_fields_item_data in (_focus_fields):
            focus_fields_item = DatasetReviewFocusFieldOutput.from_dict(focus_fields_item_data)



            focus_fields.append(focus_fields_item)


        ignored_fields = cast(list[str], d.pop("ignoredFields"))


        status = DatasetReviewInboxItemStatus(d.pop("status"))




        example_names = cast(list[str], d.pop("exampleNames"))


        progress = DatasetReviewProgress.from_dict(d.pop("progress"))




        def _parse_created_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_by = _parse_created_by(d.pop("createdBy"))


        created_at = d.pop("createdAt")

        def _parse_closed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        closed_at = _parse_closed_at(d.pop("closedAt"))


        automation_name = d.pop("automationName")

        dataset_review_inbox_item = cls(
            id=id,
            automation_id=automation_id,
            title=title,
            instructions=instructions,
            focus_fields=focus_fields,
            ignored_fields=ignored_fields,
            status=status,
            example_names=example_names,
            progress=progress,
            created_by=created_by,
            created_at=created_at,
            closed_at=closed_at,
            automation_name=automation_name,
        )

        return dataset_review_inbox_item

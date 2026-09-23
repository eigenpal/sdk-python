from enum import Enum

class UpdateDatasetReviewItemAction(str, Enum):
    APPROVE = "approve"
    COMMENT = "comment"
    EDIT = "edit"
    EDIT_FILE = "edit-file"
    FIELD_DECISION = "field-decision"
    FILE_DECISION = "file-decision"
    REMOVE = "remove"
    REOPEN = "reopen"

    def __str__(self) -> str:
        return str(self.value)

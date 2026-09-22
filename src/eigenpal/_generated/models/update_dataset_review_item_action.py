from enum import Enum

class UpdateDatasetReviewItemAction(str, Enum):
    APPROVE = "approve"
    COMMENT = "comment"
    EDIT = "edit"
    FIELD_DECISION = "field-decision"
    REJECT = "reject"
    REOPEN = "reopen"

    def __str__(self) -> str:
        return str(self.value)

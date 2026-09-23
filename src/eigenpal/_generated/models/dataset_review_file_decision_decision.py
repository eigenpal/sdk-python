from enum import Enum

class DatasetReviewFileDecisionDecision(str, Enum):
    APPROVED = "approved"
    REMOVED = "removed"

    def __str__(self) -> str:
        return str(self.value)

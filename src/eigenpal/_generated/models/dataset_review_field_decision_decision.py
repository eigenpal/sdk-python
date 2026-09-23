from enum import Enum

class DatasetReviewFieldDecisionDecision(str, Enum):
    APPROVED = "approved"
    REMOVED = "removed"

    def __str__(self) -> str:
        return str(self.value)

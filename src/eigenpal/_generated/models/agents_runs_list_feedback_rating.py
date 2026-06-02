from enum import Enum

class AgentsRunsListFeedbackRating(str, Enum):
    FAIL = "fail"
    NONE = "none"
    PARTIAL = "partial"
    PASS = "pass"

    def __str__(self) -> str:
        return str(self.value)

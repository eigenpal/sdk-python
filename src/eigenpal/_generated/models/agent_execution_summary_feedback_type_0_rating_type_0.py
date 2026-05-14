from enum import Enum

class AgentExecutionSummaryFeedbackType0RatingType0(str, Enum):
    FAIL = "fail"
    PARTIAL = "partial"
    PASS = "pass"

    def __str__(self) -> str:
        return str(self.value)

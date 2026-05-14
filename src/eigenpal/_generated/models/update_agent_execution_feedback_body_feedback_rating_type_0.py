from enum import Enum

class UpdateAgentExecutionFeedbackBodyFeedbackRatingType0(str, Enum):
    FAIL = "fail"
    PARTIAL = "partial"
    PASS = "pass"

    def __str__(self) -> str:
        return str(self.value)

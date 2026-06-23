from enum import Enum

class RunReviewSummaryVerdictType0(str, Enum):
    CORRECT = "correct"
    INCORRECT = "incorrect"

    def __str__(self) -> str:
        return str(self.value)

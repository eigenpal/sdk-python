from enum import Enum

class RunReviewRequestVerdictType0(str, Enum):
    CORRECT = "correct"
    INCORRECT = "incorrect"

    def __str__(self) -> str:
        return str(self.value)

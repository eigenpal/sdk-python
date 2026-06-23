from enum import Enum

class RunReviewCorrectionFileVerdictType0(str, Enum):
    CORRECT = "correct"
    REPLACED = "replaced"
    WRONG = "wrong"

    def __str__(self) -> str:
        return str(self.value)

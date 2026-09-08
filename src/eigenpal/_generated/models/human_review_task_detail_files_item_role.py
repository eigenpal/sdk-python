from enum import Enum

class HumanReviewTaskDetailFilesItemRole(str, Enum):
    ATTACHMENT = "attachment"
    RUN_INPUT = "run_input"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum

class UpdateAgentExecutionFeedbackBodyStatusType0(str, Enum):
    IGNORED = "ignored"
    OPEN = "open"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)

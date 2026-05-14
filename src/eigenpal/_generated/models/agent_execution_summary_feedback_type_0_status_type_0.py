from enum import Enum

class AgentExecutionSummaryFeedbackType0StatusType0(str, Enum):
    IGNORED = "ignored"
    OPEN = "open"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)

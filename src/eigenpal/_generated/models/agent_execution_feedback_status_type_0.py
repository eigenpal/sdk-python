from enum import Enum

class AgentExecutionFeedbackStatusType0(str, Enum):
    IGNORED = "ignored"
    OPEN = "open"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)

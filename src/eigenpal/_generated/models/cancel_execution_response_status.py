from enum import Enum

class CancelExecutionResponseStatus(str, Enum):
    ALREADY_TERMINAL = "already-terminal"
    CANCELLATION_REQUESTED = "cancellation-requested"
    CANCELLED = "cancelled"

    def __str__(self) -> str:
        return str(self.value)

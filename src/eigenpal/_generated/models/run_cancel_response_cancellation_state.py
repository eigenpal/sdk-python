from enum import Enum

class RunCancelResponseCancellationState(str, Enum):
    ALREADY_TERMINAL = "already_terminal"
    CANCELLED = "cancelled"
    REQUESTED = "requested"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum

class ExecutionObservabilityPhasesItemStatus(str, Enum):
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    FAILED = "failed"
    PENDING = "pending"
    RUNNING = "running"
    SKIPPED = "skipped"

    def __str__(self) -> str:
        return str(self.value)

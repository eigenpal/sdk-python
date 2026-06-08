from enum import Enum

class RunSummaryStatus(str, Enum):
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    CREATED = "created"
    FAILED = "failed"
    FINALIZING = "finalizing"
    PENDING = "pending"
    REJECTED = "rejected"
    RUNNING = "running"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum

class ExperimentDetailStatus(str, Enum):
    COMPLETED = "completed"
    QUEUED = "queued"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)

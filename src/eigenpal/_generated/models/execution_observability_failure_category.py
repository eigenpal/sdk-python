from enum import Enum

class ExecutionObservabilityFailureCategory(str, Enum):
    ENVIRONMENT = "environment"
    FINALIZATION = "finalization"
    INPUT = "input"
    OUTPUT = "output"
    RUNTIME = "runtime"
    SOURCE = "source"
    SYSTEM = "system"

    def __str__(self) -> str:
        return str(self.value)

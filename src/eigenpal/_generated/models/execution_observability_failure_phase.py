from enum import Enum

class ExecutionObservabilityFailurePhase(str, Enum):
    COLLECTING_OUTPUTS = "collecting_outputs"
    FINALIZING = "finalizing"
    INSTALLING_DEPENDENCIES = "installing_dependencies"
    PREPARING_ENVIRONMENT = "preparing_environment"
    PREPARING_INPUTS = "preparing_inputs"
    QUEUED = "queued"
    RUNNING = "running"
    STARTING = "starting"

    def __str__(self) -> str:
        return str(self.value)

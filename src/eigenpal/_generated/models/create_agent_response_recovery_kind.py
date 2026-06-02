from enum import Enum

class CreateAgentResponseRecoveryKind(str, Enum):
    EXISTING = "existing"
    LEGACY_HYDRATE = "legacy_hydrate"
    MINIMAL_SCAFFOLD = "minimal_scaffold"

    def __str__(self) -> str:
        return str(self.value)

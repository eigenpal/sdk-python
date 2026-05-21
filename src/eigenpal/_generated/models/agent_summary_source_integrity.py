from enum import Enum

class AgentSummarySourceIntegrity(str, Enum):
    HEALTHY = "healthy"
    SOURCE_MISSING = "source_missing"
    UNREGISTERED = "unregistered"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum

class PublicModelHealth(str, Enum):
    CONFIGURED = "configured"
    UNCONFIGURED = "unconfigured"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)

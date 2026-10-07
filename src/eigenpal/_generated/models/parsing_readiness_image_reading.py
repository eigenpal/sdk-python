from enum import Enum

class ParsingReadinessImageReading(str, Enum):
    CONFIGURED = "configured"
    UNCONFIGURED = "unconfigured"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum

class AutomationsExperimentsExportIncludeTrace(str, Enum):
    FALSE = "false"
    TRUE = "true"
    VALUE_0 = "0"
    VALUE_1 = "1"

    def __str__(self) -> str:
        return str(self.value)

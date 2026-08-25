from enum import Enum

class AutomationsExamplesListInclude(str, Enum):
    FULL = "full"
    METADATA = "metadata"

    def __str__(self) -> str:
        return str(self.value)

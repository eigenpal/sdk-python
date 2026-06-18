from enum import Enum

class AutomationDatasetImportMultipartRequestMode(str, Enum):
    APPEND = "append"
    REPLACE = "replace"

    def __str__(self) -> str:
        return str(self.value)

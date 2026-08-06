from enum import Enum

class CreateFileMultipartRequestPurpose(str, Enum):
    BUILDER_ATTACHMENT = "builder-attachment"
    RUN_INPUT = "run-input"

    def __str__(self) -> str:
        return str(self.value)

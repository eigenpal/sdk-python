from enum import Enum

class PublicModelCapabilitiesItem(str, Enum):
    OCR = "ocr"
    TEXT = "text"
    VISION = "vision"

    def __str__(self) -> str:
        return str(self.value)

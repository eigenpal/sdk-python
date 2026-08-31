from enum import Enum

class PublicModelKind(str, Enum):
    LLM = "llm"
    OCR = "ocr"

    def __str__(self) -> str:
        return str(self.value)

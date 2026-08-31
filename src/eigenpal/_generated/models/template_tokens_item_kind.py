from enum import Enum

class TemplateTokensItemKind(str, Enum):
    LOOP = "loop"
    VARIABLE = "variable"

    def __str__(self) -> str:
        return str(self.value)

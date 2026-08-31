from enum import Enum

class CreatedTemplateTokensItemKind(str, Enum):
    LOOP = "loop"
    VARIABLE = "variable"

    def __str__(self) -> str:
        return str(self.value)

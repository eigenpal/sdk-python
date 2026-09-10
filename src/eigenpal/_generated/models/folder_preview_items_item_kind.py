from enum import Enum

class FolderPreviewItemsItemKind(str, Enum):
    FOLDER = "folder"
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)

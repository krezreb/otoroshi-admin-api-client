from enum import Enum


class PatchDocumentOp(str, Enum):
    ADD = "add"
    REMOVE = "remove"
    REPLACE = "replace"
    MOVE = "move"
    COPY = "copy"
    TEST = "test"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class OtoroshisslClientAuth(str, Enum):
    NEED = "Need"
    NONE = "None"
    WANT = "Want"

    def __str__(self) -> str:
        return str(self.value)

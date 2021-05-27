from enum import Enum


class OtoroshimodelsAlwaysMatchType(str, Enum):
    ALWAYS = "Always"

    def __str__(self) -> str:
        return str(self.value)

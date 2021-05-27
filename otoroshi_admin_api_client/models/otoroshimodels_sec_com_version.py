from enum import Enum


class OtoroshimodelsSecComVersion(str, Enum):
    V1 = "V1"
    V2 = "v2"

    def __str__(self) -> str:
        return str(self.value)

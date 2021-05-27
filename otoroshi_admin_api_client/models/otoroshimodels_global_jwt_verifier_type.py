from enum import Enum


class OtoroshimodelsGlobalJwtVerifierType(str, Enum):
    GLOBAL_ = "global"
    LOCAL = "local"
    REF = "ref"

    def __str__(self) -> str:
        return str(self.value)

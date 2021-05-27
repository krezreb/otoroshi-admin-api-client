from enum import Enum


class OtoroshimodelsOtoroshiAdminType(str, Enum):
    SIMPLE = "SIMPLE"
    WEBAUTHN = "WEBAUTHN"

    def __str__(self) -> str:
        return str(self.value)

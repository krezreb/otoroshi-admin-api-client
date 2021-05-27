from enum import Enum


class OtoroshimodelsSimpleOtoroshiAdminType(str, Enum):
    SIMPLE = "simple"
    WEBAUTHN = "webauthn"

    def __str__(self) -> str:
        return str(self.value)

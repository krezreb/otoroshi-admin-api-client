from enum import Enum


class OtoroshimodelsWebAuthnOtoroshiAdminType(str, Enum):
    SIMPLE = "simple"
    WEBAUTHN = "webauthn"

    def __str__(self) -> str:
        return str(self.value)

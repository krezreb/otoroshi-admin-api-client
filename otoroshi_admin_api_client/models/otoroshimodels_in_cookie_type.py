from enum import Enum


class OtoroshimodelsInCookieType(str, Enum):
    INQUERYPARAM = "InQueryParam"
    INHEADER = "InHeader"
    INCOOKIE = "InCookie"

    def __str__(self) -> str:
        return str(self.value)

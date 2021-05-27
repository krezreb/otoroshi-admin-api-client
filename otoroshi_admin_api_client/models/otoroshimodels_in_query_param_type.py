from enum import Enum


class OtoroshimodelsInQueryParamType(str, Enum):
    INQUERYPARAM = "InQueryParam"
    INHEADER = "InHeader"
    INCOOKIE = "InCookie"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class OtoroshimodelsMaxmindGeolocationSettingsType(str, Enum):
    NONE = "none"
    MAXMIND = "maxmind"
    IPSTACK = "ipstack"

    def __str__(self) -> str:
        return str(self.value)

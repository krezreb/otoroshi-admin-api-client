from enum import Enum


class OtoroshimodelsZoneMatchType(str, Enum):
    ALWAYSMATCH = "AlwaysMatch"
    NETWORKLOCATIONMATCH = "NetworkLocationMatch"
    GEOLOCATIONMATCH = "GeolocationMatch"

    def __str__(self) -> str:
        return str(self.value)

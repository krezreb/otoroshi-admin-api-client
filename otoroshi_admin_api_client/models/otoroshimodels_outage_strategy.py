from enum import Enum


class OtoroshimodelsOutageStrategy(str, Enum):
    ALLSERVICESPERGROUP = "AllServicesPerGroup"
    ONESERVICEPERGROUP = "OneServicePerGroup"

    def __str__(self) -> str:
        return str(self.value)

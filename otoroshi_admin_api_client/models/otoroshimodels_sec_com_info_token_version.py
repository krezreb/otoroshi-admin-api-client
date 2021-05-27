from enum import Enum


class OtoroshimodelsSecComInfoTokenVersion(str, Enum):
    LEGACY = "Legacy"
    LATEST = "Latest"

    def __str__(self) -> str:
        return str(self.value)

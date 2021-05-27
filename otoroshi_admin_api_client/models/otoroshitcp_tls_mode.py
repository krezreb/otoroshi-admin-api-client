from enum import Enum


class OtoroshitcpTlsMode(str, Enum):
    DISABLED = "Disabled"
    ENABLED = "Enabled"
    PASSTHROUGH = "PassThrough"

    def __str__(self) -> str:
        return str(self.value)

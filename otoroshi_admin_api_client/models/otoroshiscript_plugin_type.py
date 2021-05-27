from enum import Enum


class OtoroshiscriptPluginType(str, Enum):
    APP = "app"
    TRANSFORMER = "transformer"
    VALIDATOR = "validator"
    PREROUTE = "preroute"
    SINK = "sink"
    LISTENER = "listener"
    JOB = "job"
    EXPORTER = "exporter"

    def __str__(self) -> str:
        return str(self.value)

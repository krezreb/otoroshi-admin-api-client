from enum import Enum


class OtoroshimodelsDataExporterConfigType(str, Enum):
    KAFKA = "kafka"
    PULSAR = "pulsar"
    ELASTIC = "elastic"
    WEBHOOK = "webhook"
    FILE = "file"
    MAILER = "mailer"
    CUSTOM = "custom"
    NONE = "none"
    CONSOLE = "console"
    METRICS = "metrics"

    def __str__(self) -> str:
        return str(self.value)

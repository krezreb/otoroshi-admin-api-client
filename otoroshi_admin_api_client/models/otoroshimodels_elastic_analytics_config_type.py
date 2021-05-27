from enum import Enum


class OtoroshimodelsElasticAnalyticsConfigType(str, Enum):
    ELASTIC = "elastic"
    WEBHOOK = "webhook"
    KAFKA = "kafka"
    PULSAR = "pulsar"
    FILE = "file"
    MAILER = "mailer"
    CUSTOM = "custom"
    CONSOLE = "console"
    METRICS = "metrics"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class OtoroshiutilsmailerGenericMailerSettingsType(str, Enum):
    NONE = "none"
    CONSOLE = "console"
    GENERIC = "generic"
    MAILGUN = "mailgun"
    MAILJET = "mailjet"
    SENDGRID = "sendgrid"

    def __str__(self) -> str:
        return str(self.value)

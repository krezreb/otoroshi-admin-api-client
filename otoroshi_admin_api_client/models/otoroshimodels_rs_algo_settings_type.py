from enum import Enum


class OtoroshimodelsRSAlgoSettingsType(str, Enum):
    HSALGOSETTINGS = "HSAlgoSettings"
    RSALGOSETTINGS = "RSAlgoSettings"
    ESALGOSETTINGS = "ESAlgoSettings"
    JWKSALGOSETTINGS = "JWKSAlgoSettings"
    RSAKPALGOSETTINGS = "RSAKPAlgoSettings"
    ESKPALGOSETTINGS = "ESKPAlgoSettings"
    KIDALGOSETTINGS = "KidAlgoSettings"

    def __str__(self) -> str:
        return str(self.value)

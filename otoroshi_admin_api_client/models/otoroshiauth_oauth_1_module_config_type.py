from enum import Enum


class OtoroshiauthOauth1ModuleConfigType(str, Enum):
    SAML = "saml"
    OAUTH1 = "oauth1"
    OAUTH2 = "oauth2"
    LDAP = "ldap"
    BASIC = "basic"

    def __str__(self) -> str:
        return str(self.value)
from enum import Enum


class OtoroshimodelsTransformType(str, Enum):
    PASSTHROUGH = "PassThrough"
    SIGN = "Sign"
    TRANSFORM = "Transform"
    DEFAULTTOKEN = "DefaultToken"

    def __str__(self) -> str:
        return str(self.value)

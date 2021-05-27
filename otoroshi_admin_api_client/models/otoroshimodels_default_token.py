from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_default_token_token import OtoroshimodelsDefaultTokenToken
from ..models.otoroshimodels_default_token_type import OtoroshimodelsDefaultTokenType
from ..models.otoroshimodels_verification_settings import OtoroshimodelsVerificationSettings
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsDefaultToken")


@attr.s(auto_attribs=True)
class OtoroshimodelsDefaultToken:
    """Default jwt token when no other token validated"""

    verification_settings: Union[Unset, OtoroshimodelsVerificationSettings] = UNSET
    type: Union[Unset, OtoroshimodelsDefaultTokenType] = UNSET
    strict: Union[Unset, bool] = UNSET
    token: Union[Unset, OtoroshimodelsDefaultTokenToken] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        verification_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.verification_settings, Unset):
            verification_settings = self.verification_settings.to_dict()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        strict = self.strict
        token: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.token, Unset):
            token = self.token.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if verification_settings is not UNSET:
            field_dict["verificationSettings"] = verification_settings
        if type is not UNSET:
            field_dict["type"] = type
        if strict is not UNSET:
            field_dict["strict"] = strict
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _verification_settings = d.pop("verificationSettings", UNSET)
        verification_settings: Union[Unset, OtoroshimodelsVerificationSettings]
        if isinstance(_verification_settings, Unset):
            verification_settings = UNSET
        else:
            verification_settings = OtoroshimodelsVerificationSettings.from_dict(_verification_settings)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshimodelsDefaultTokenType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshimodelsDefaultTokenType(_type)

        strict = d.pop("strict", UNSET)

        _token = d.pop("token", UNSET)
        token: Union[Unset, OtoroshimodelsDefaultTokenToken]
        if isinstance(_token, Unset):
            token = UNSET
        else:
            token = OtoroshimodelsDefaultTokenToken.from_dict(_token)

        otoroshimodels_default_token = cls(
            verification_settings=verification_settings,
            type=type,
            strict=strict,
            token=token,
        )

        otoroshimodels_default_token.additional_properties = d
        return otoroshimodels_default_token

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

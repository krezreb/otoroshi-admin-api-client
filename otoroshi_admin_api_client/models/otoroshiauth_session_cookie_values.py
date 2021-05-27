from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshiauthSessionCookieValues")


@attr.s(auto_attribs=True)
class OtoroshiauthSessionCookieValues:
    """The configuration for session cookie"""

    http_only: Union[Unset, bool] = UNSET
    secure: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        http_only = self.http_only
        secure = self.secure

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if http_only is not UNSET:
            field_dict["httpOnly"] = http_only
        if secure is not UNSET:
            field_dict["secure"] = secure

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        http_only = d.pop("httpOnly", UNSET)

        secure = d.pop("secure", UNSET)

        otoroshiauth_session_cookie_values = cls(
            http_only=http_only,
            secure=secure,
        )

        otoroshiauth_session_cookie_values.additional_properties = d
        return otoroshiauth_session_cookie_values

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

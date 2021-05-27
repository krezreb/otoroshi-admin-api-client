from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsCleverCloudSettings")


@attr.s(auto_attribs=True)
class OtoroshimodelsCleverCloudSettings:
    """Settings for connection to the clever-cloud api"""

    consumer_secret: Union[Unset, str] = UNSET
    consumer_key: Union[Unset, str] = UNSET
    secret: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    orga_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        consumer_secret = self.consumer_secret
        consumer_key = self.consumer_key
        secret = self.secret
        token = self.token
        orga_id = self.orga_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if consumer_secret is not UNSET:
            field_dict["consumerSecret"] = consumer_secret
        if consumer_key is not UNSET:
            field_dict["consumerKey"] = consumer_key
        if secret is not UNSET:
            field_dict["secret"] = secret
        if token is not UNSET:
            field_dict["token"] = token
        if orga_id is not UNSET:
            field_dict["orgaId"] = orga_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        consumer_secret = d.pop("consumerSecret", UNSET)

        consumer_key = d.pop("consumerKey", UNSET)

        secret = d.pop("secret", UNSET)

        token = d.pop("token", UNSET)

        orga_id = d.pop("orgaId", UNSET)

        otoroshimodels_clever_cloud_settings = cls(
            consumer_secret=consumer_secret,
            consumer_key=consumer_key,
            secret=secret,
            token=token,
            orga_id=orga_id,
        )

        otoroshimodels_clever_cloud_settings.additional_properties = d
        return otoroshimodels_clever_cloud_settings

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

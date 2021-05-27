from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_webhook_headers import OtoroshimodelsWebhookHeaders
from ..models.otoroshimodels_webhook_type import OtoroshimodelsWebhookType
from ..models.otoroshiutilshttp_mtls_config import OtoroshiutilshttpMtlsConfig
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsWebhook")


@attr.s(auto_attribs=True)
class OtoroshimodelsWebhook:
    """Settings for webhook call"""

    headers: Union[Unset, OtoroshimodelsWebhookHeaders] = UNSET
    mtls_config: Union[Unset, OtoroshiutilshttpMtlsConfig] = UNSET
    type: Union[Unset, OtoroshimodelsWebhookType] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        headers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        mtls_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mtls_config, Unset):
            mtls_config = self.mtls_config.to_dict()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if headers is not UNSET:
            field_dict["headers"] = headers
        if mtls_config is not UNSET:
            field_dict["mtlsConfig"] = mtls_config
        if type is not UNSET:
            field_dict["type"] = type
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, OtoroshimodelsWebhookHeaders]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = OtoroshimodelsWebhookHeaders.from_dict(_headers)

        _mtls_config = d.pop("mtlsConfig", UNSET)
        mtls_config: Union[Unset, OtoroshiutilshttpMtlsConfig]
        if isinstance(_mtls_config, Unset):
            mtls_config = UNSET
        else:
            mtls_config = OtoroshiutilshttpMtlsConfig.from_dict(_mtls_config)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshimodelsWebhookType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshimodelsWebhookType(_type)

        url = d.pop("url", UNSET)

        otoroshimodels_webhook = cls(
            headers=headers,
            mtls_config=mtls_config,
            type=type,
            url=url,
        )

        otoroshimodels_webhook.additional_properties = d
        return otoroshimodels_webhook

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

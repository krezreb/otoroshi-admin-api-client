from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshiutilshttpMtlsConfig")


@attr.s(auto_attribs=True)
class OtoroshiutilshttpMtlsConfig:
    """TLS settings for the http client"""

    mtls: Union[Unset, bool] = UNSET
    loose: Union[Unset, bool] = UNSET
    trust_all: Union[Unset, bool] = UNSET
    trusted_certs: Union[Unset, List[str]] = UNSET
    certs: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mtls = self.mtls
        loose = self.loose
        trust_all = self.trust_all
        trusted_certs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.trusted_certs, Unset):
            trusted_certs = self.trusted_certs

        certs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.certs, Unset):
            certs = self.certs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mtls is not UNSET:
            field_dict["mtls"] = mtls
        if loose is not UNSET:
            field_dict["loose"] = loose
        if trust_all is not UNSET:
            field_dict["trustAll"] = trust_all
        if trusted_certs is not UNSET:
            field_dict["trustedCerts"] = trusted_certs
        if certs is not UNSET:
            field_dict["certs"] = certs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mtls = d.pop("mtls", UNSET)

        loose = d.pop("loose", UNSET)

        trust_all = d.pop("trustAll", UNSET)

        trusted_certs = cast(List[str], d.pop("trustedCerts", UNSET))

        certs = cast(List[str], d.pop("certs", UNSET))

        otoroshiutilshttp_mtls_config = cls(
            mtls=mtls,
            loose=loose,
            trust_all=trust_all,
            trusted_certs=trusted_certs,
            certs=certs,
        )

        otoroshiutilshttp_mtls_config.additional_properties = d
        return otoroshiutilshttp_mtls_config

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

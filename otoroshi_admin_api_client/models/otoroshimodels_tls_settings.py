from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.null import Null
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsTlsSettings")


@attr.s(auto_attribs=True)
class OtoroshimodelsTlsSettings:
    """Global TLS settings. The default domain that will be picked if no certificate matches the current request"""

    default_domain: Union[Null, Unset, str] = UNSET
    random_if_not_found: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        default_domain: Union[Dict[str, Any], Unset, str]
        if isinstance(self.default_domain, Unset):
            default_domain = UNSET
        elif isinstance(self.default_domain, Null):
            default_domain = UNSET
            if not isinstance(self.default_domain, Unset):
                default_domain = self.default_domain.to_dict()

        else:
            default_domain = self.default_domain

        random_if_not_found = self.random_if_not_found

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_domain is not UNSET:
            field_dict["defaultDomain"] = default_domain
        if random_if_not_found is not UNSET:
            field_dict["randomIfNotFound"] = random_if_not_found

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_default_domain(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _default_domain_type_0 = data
                default_domain_type_0: Union[Unset, Null]
                if isinstance(_default_domain_type_0, Unset):
                    default_domain_type_0 = UNSET
                else:
                    default_domain_type_0 = Null.from_dict(_default_domain_type_0)

                return default_domain_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        default_domain = _parse_default_domain(d.pop("defaultDomain", UNSET))

        random_if_not_found = d.pop("randomIfNotFound", UNSET)

        otoroshimodels_tls_settings = cls(
            default_domain=default_domain,
            random_if_not_found=random_if_not_found,
        )

        otoroshimodels_tls_settings.additional_properties = d
        return otoroshimodels_tls_settings

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

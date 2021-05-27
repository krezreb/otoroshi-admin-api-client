from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.null import Null
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsCustomHeadersAuthConstraints")


@attr.s(auto_attribs=True)
class OtoroshimodelsCustomHeadersAuthConstraints:
    """Settings to extract apikey from a custom headers"""

    enabled: Union[Unset, bool] = UNSET
    client_id_header_name: Union[Null, Unset, str] = UNSET
    client_secret_header_name: Union[Null, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        client_id_header_name: Union[Dict[str, Any], Unset, str]
        if isinstance(self.client_id_header_name, Unset):
            client_id_header_name = UNSET
        elif isinstance(self.client_id_header_name, Null):
            client_id_header_name = UNSET
            if not isinstance(self.client_id_header_name, Unset):
                client_id_header_name = self.client_id_header_name.to_dict()

        else:
            client_id_header_name = self.client_id_header_name

        client_secret_header_name: Union[Dict[str, Any], Unset, str]
        if isinstance(self.client_secret_header_name, Unset):
            client_secret_header_name = UNSET
        elif isinstance(self.client_secret_header_name, Null):
            client_secret_header_name = UNSET
            if not isinstance(self.client_secret_header_name, Unset):
                client_secret_header_name = self.client_secret_header_name.to_dict()

        else:
            client_secret_header_name = self.client_secret_header_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if client_id_header_name is not UNSET:
            field_dict["clientIdHeaderName"] = client_id_header_name
        if client_secret_header_name is not UNSET:
            field_dict["clientSecretHeaderName"] = client_secret_header_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        def _parse_client_id_header_name(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _client_id_header_name_type_0 = data
                client_id_header_name_type_0: Union[Unset, Null]
                if isinstance(_client_id_header_name_type_0, Unset):
                    client_id_header_name_type_0 = UNSET
                else:
                    client_id_header_name_type_0 = Null.from_dict(_client_id_header_name_type_0)

                return client_id_header_name_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        client_id_header_name = _parse_client_id_header_name(d.pop("clientIdHeaderName", UNSET))

        def _parse_client_secret_header_name(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _client_secret_header_name_type_0 = data
                client_secret_header_name_type_0: Union[Unset, Null]
                if isinstance(_client_secret_header_name_type_0, Unset):
                    client_secret_header_name_type_0 = UNSET
                else:
                    client_secret_header_name_type_0 = Null.from_dict(_client_secret_header_name_type_0)

                return client_secret_header_name_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        client_secret_header_name = _parse_client_secret_header_name(d.pop("clientSecretHeaderName", UNSET))

        otoroshimodels_custom_headers_auth_constraints = cls(
            enabled=enabled,
            client_id_header_name=client_id_header_name,
            client_secret_header_name=client_secret_header_name,
        )

        otoroshimodels_custom_headers_auth_constraints.additional_properties = d
        return otoroshimodels_custom_headers_auth_constraints

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

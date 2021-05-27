from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_api_key_route_matcher import OtoroshimodelsApiKeyRouteMatcher
from ..models.otoroshimodels_basic_auth_constraints import OtoroshimodelsBasicAuthConstraints
from ..models.otoroshimodels_client_id_auth_constraints import OtoroshimodelsClientIdAuthConstraints
from ..models.otoroshimodels_custom_headers_auth_constraints import OtoroshimodelsCustomHeadersAuthConstraints
from ..models.otoroshimodels_jwt_auth_constraints import OtoroshimodelsJwtAuthConstraints
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsApiKeyConstraints")


@attr.s(auto_attribs=True)
class OtoroshimodelsApiKeyConstraints:
    """Settings used to extract apikeys from http requests and routing traffic"""

    custom_headers_auth: Union[Unset, OtoroshimodelsCustomHeadersAuthConstraints] = UNSET
    routing: Union[Unset, OtoroshimodelsApiKeyRouteMatcher] = UNSET
    client_id_auth: Union[Unset, OtoroshimodelsClientIdAuthConstraints] = UNSET
    jwt_auth: Union[Unset, OtoroshimodelsJwtAuthConstraints] = UNSET
    basic_auth: Union[Unset, OtoroshimodelsBasicAuthConstraints] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        custom_headers_auth: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_headers_auth, Unset):
            custom_headers_auth = self.custom_headers_auth.to_dict()

        routing: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.routing, Unset):
            routing = self.routing.to_dict()

        client_id_auth: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.client_id_auth, Unset):
            client_id_auth = self.client_id_auth.to_dict()

        jwt_auth: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.jwt_auth, Unset):
            jwt_auth = self.jwt_auth.to_dict()

        basic_auth: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.basic_auth, Unset):
            basic_auth = self.basic_auth.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom_headers_auth is not UNSET:
            field_dict["customHeadersAuth"] = custom_headers_auth
        if routing is not UNSET:
            field_dict["routing"] = routing
        if client_id_auth is not UNSET:
            field_dict["clientIdAuth"] = client_id_auth
        if jwt_auth is not UNSET:
            field_dict["jwtAuth"] = jwt_auth
        if basic_auth is not UNSET:
            field_dict["basicAuth"] = basic_auth

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _custom_headers_auth = d.pop("customHeadersAuth", UNSET)
        custom_headers_auth: Union[Unset, OtoroshimodelsCustomHeadersAuthConstraints]
        if isinstance(_custom_headers_auth, Unset):
            custom_headers_auth = UNSET
        else:
            custom_headers_auth = OtoroshimodelsCustomHeadersAuthConstraints.from_dict(_custom_headers_auth)

        _routing = d.pop("routing", UNSET)
        routing: Union[Unset, OtoroshimodelsApiKeyRouteMatcher]
        if isinstance(_routing, Unset):
            routing = UNSET
        else:
            routing = OtoroshimodelsApiKeyRouteMatcher.from_dict(_routing)

        _client_id_auth = d.pop("clientIdAuth", UNSET)
        client_id_auth: Union[Unset, OtoroshimodelsClientIdAuthConstraints]
        if isinstance(_client_id_auth, Unset):
            client_id_auth = UNSET
        else:
            client_id_auth = OtoroshimodelsClientIdAuthConstraints.from_dict(_client_id_auth)

        _jwt_auth = d.pop("jwtAuth", UNSET)
        jwt_auth: Union[Unset, OtoroshimodelsJwtAuthConstraints]
        if isinstance(_jwt_auth, Unset):
            jwt_auth = UNSET
        else:
            jwt_auth = OtoroshimodelsJwtAuthConstraints.from_dict(_jwt_auth)

        _basic_auth = d.pop("basicAuth", UNSET)
        basic_auth: Union[Unset, OtoroshimodelsBasicAuthConstraints]
        if isinstance(_basic_auth, Unset):
            basic_auth = UNSET
        else:
            basic_auth = OtoroshimodelsBasicAuthConstraints.from_dict(_basic_auth)

        otoroshimodels_api_key_constraints = cls(
            custom_headers_auth=custom_headers_auth,
            routing=routing,
            client_id_auth=client_id_auth,
            jwt_auth=jwt_auth,
            basic_auth=basic_auth,
        )

        otoroshimodels_api_key_constraints.additional_properties = d
        return otoroshimodels_api_key_constraints

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

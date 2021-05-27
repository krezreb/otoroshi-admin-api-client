from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.null import Null
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsJwtAuthConstraints")


@attr.s(auto_attribs=True)
class OtoroshimodelsJwtAuthConstraints:
    """Settings to extract apikey from a jwt token"""

    key_pair_signed: Union[Unset, bool] = UNSET
    cookie_name: Union[Null, Unset, str] = UNSET
    query_name: Union[Null, Unset, str] = UNSET
    header_name: Union[Null, Unset, str] = UNSET
    secret_signed: Union[Unset, bool] = UNSET
    max_jwt_lifespan_secs: Union[Null, Unset, int] = UNSET
    enabled: Union[Unset, bool] = UNSET
    include_request_attributes: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key_pair_signed = self.key_pair_signed
        cookie_name: Union[Dict[str, Any], Unset, str]
        if isinstance(self.cookie_name, Unset):
            cookie_name = UNSET
        elif isinstance(self.cookie_name, Null):
            cookie_name = UNSET
            if not isinstance(self.cookie_name, Unset):
                cookie_name = self.cookie_name.to_dict()

        else:
            cookie_name = self.cookie_name

        query_name: Union[Dict[str, Any], Unset, str]
        if isinstance(self.query_name, Unset):
            query_name = UNSET
        elif isinstance(self.query_name, Null):
            query_name = UNSET
            if not isinstance(self.query_name, Unset):
                query_name = self.query_name.to_dict()

        else:
            query_name = self.query_name

        header_name: Union[Dict[str, Any], Unset, str]
        if isinstance(self.header_name, Unset):
            header_name = UNSET
        elif isinstance(self.header_name, Null):
            header_name = UNSET
            if not isinstance(self.header_name, Unset):
                header_name = self.header_name.to_dict()

        else:
            header_name = self.header_name

        secret_signed = self.secret_signed
        max_jwt_lifespan_secs: Union[Dict[str, Any], Unset, int]
        if isinstance(self.max_jwt_lifespan_secs, Unset):
            max_jwt_lifespan_secs = UNSET
        elif isinstance(self.max_jwt_lifespan_secs, Null):
            max_jwt_lifespan_secs = UNSET
            if not isinstance(self.max_jwt_lifespan_secs, Unset):
                max_jwt_lifespan_secs = self.max_jwt_lifespan_secs.to_dict()

        else:
            max_jwt_lifespan_secs = self.max_jwt_lifespan_secs

        enabled = self.enabled
        include_request_attributes = self.include_request_attributes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key_pair_signed is not UNSET:
            field_dict["keyPairSigned"] = key_pair_signed
        if cookie_name is not UNSET:
            field_dict["cookieName"] = cookie_name
        if query_name is not UNSET:
            field_dict["queryName"] = query_name
        if header_name is not UNSET:
            field_dict["headerName"] = header_name
        if secret_signed is not UNSET:
            field_dict["secretSigned"] = secret_signed
        if max_jwt_lifespan_secs is not UNSET:
            field_dict["maxJwtLifespanSecs"] = max_jwt_lifespan_secs
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if include_request_attributes is not UNSET:
            field_dict["includeRequestAttributes"] = include_request_attributes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key_pair_signed = d.pop("keyPairSigned", UNSET)

        def _parse_cookie_name(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _cookie_name_type_0 = data
                cookie_name_type_0: Union[Unset, Null]
                if isinstance(_cookie_name_type_0, Unset):
                    cookie_name_type_0 = UNSET
                else:
                    cookie_name_type_0 = Null.from_dict(_cookie_name_type_0)

                return cookie_name_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        cookie_name = _parse_cookie_name(d.pop("cookieName", UNSET))

        def _parse_query_name(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _query_name_type_0 = data
                query_name_type_0: Union[Unset, Null]
                if isinstance(_query_name_type_0, Unset):
                    query_name_type_0 = UNSET
                else:
                    query_name_type_0 = Null.from_dict(_query_name_type_0)

                return query_name_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        query_name = _parse_query_name(d.pop("queryName", UNSET))

        def _parse_header_name(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _header_name_type_0 = data
                header_name_type_0: Union[Unset, Null]
                if isinstance(_header_name_type_0, Unset):
                    header_name_type_0 = UNSET
                else:
                    header_name_type_0 = Null.from_dict(_header_name_type_0)

                return header_name_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        header_name = _parse_header_name(d.pop("headerName", UNSET))

        secret_signed = d.pop("secretSigned", UNSET)

        def _parse_max_jwt_lifespan_secs(data: object) -> Union[Null, Unset, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _max_jwt_lifespan_secs_type_0 = data
                max_jwt_lifespan_secs_type_0: Union[Unset, Null]
                if isinstance(_max_jwt_lifespan_secs_type_0, Unset):
                    max_jwt_lifespan_secs_type_0 = UNSET
                else:
                    max_jwt_lifespan_secs_type_0 = Null.from_dict(_max_jwt_lifespan_secs_type_0)

                return max_jwt_lifespan_secs_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, int], data)

        max_jwt_lifespan_secs = _parse_max_jwt_lifespan_secs(d.pop("maxJwtLifespanSecs", UNSET))

        enabled = d.pop("enabled", UNSET)

        include_request_attributes = d.pop("includeRequestAttributes", UNSET)

        otoroshimodels_jwt_auth_constraints = cls(
            key_pair_signed=key_pair_signed,
            cookie_name=cookie_name,
            query_name=query_name,
            header_name=header_name,
            secret_signed=secret_signed,
            max_jwt_lifespan_secs=max_jwt_lifespan_secs,
            enabled=enabled,
            include_request_attributes=include_request_attributes,
        )

        otoroshimodels_jwt_auth_constraints.additional_properties = d
        return otoroshimodels_jwt_auth_constraints

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

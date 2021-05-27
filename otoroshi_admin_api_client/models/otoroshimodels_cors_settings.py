from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.null import Null
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsCorsSettings")


@attr.s(auto_attribs=True)
class OtoroshimodelsCorsSettings:
    """Settings for CORS support"""

    enabled: Union[Unset, bool] = UNSET
    allow_credentials: Union[Unset, bool] = UNSET
    max_age: Union[Null, Unset, float] = UNSET
    allow_methods: Union[Unset, List[str]] = UNSET
    allow_headers: Union[Unset, List[str]] = UNSET
    excluded_patterns: Union[Unset, List[str]] = UNSET
    expose_headers: Union[Unset, List[str]] = UNSET
    allow_origin: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        allow_credentials = self.allow_credentials
        max_age: Union[Dict[str, Any], Unset, float]
        if isinstance(self.max_age, Unset):
            max_age = UNSET
        elif isinstance(self.max_age, Null):
            max_age = UNSET
            if not isinstance(self.max_age, Unset):
                max_age = self.max_age.to_dict()

        else:
            max_age = self.max_age

        allow_methods: Union[Unset, List[str]] = UNSET
        if not isinstance(self.allow_methods, Unset):
            allow_methods = self.allow_methods

        allow_headers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.allow_headers, Unset):
            allow_headers = self.allow_headers

        excluded_patterns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.excluded_patterns, Unset):
            excluded_patterns = self.excluded_patterns

        expose_headers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.expose_headers, Unset):
            expose_headers = self.expose_headers

        allow_origin = self.allow_origin

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if allow_credentials is not UNSET:
            field_dict["allowCredentials"] = allow_credentials
        if max_age is not UNSET:
            field_dict["maxAge"] = max_age
        if allow_methods is not UNSET:
            field_dict["allowMethods"] = allow_methods
        if allow_headers is not UNSET:
            field_dict["allowHeaders"] = allow_headers
        if excluded_patterns is not UNSET:
            field_dict["excludedPatterns"] = excluded_patterns
        if expose_headers is not UNSET:
            field_dict["exposeHeaders"] = expose_headers
        if allow_origin is not UNSET:
            field_dict["allowOrigin"] = allow_origin

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        allow_credentials = d.pop("allowCredentials", UNSET)

        def _parse_max_age(data: object) -> Union[Null, Unset, float]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _max_age_type_0 = data
                max_age_type_0: Union[Unset, Null]
                if isinstance(_max_age_type_0, Unset):
                    max_age_type_0 = UNSET
                else:
                    max_age_type_0 = Null.from_dict(_max_age_type_0)

                return max_age_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, float], data)

        max_age = _parse_max_age(d.pop("maxAge", UNSET))

        allow_methods = cast(List[str], d.pop("allowMethods", UNSET))

        allow_headers = cast(List[str], d.pop("allowHeaders", UNSET))

        excluded_patterns = cast(List[str], d.pop("excludedPatterns", UNSET))

        expose_headers = cast(List[str], d.pop("exposeHeaders", UNSET))

        allow_origin = d.pop("allowOrigin", UNSET)

        otoroshimodels_cors_settings = cls(
            enabled=enabled,
            allow_credentials=allow_credentials,
            max_age=max_age,
            allow_methods=allow_methods,
            allow_headers=allow_headers,
            excluded_patterns=excluded_patterns,
            expose_headers=expose_headers,
            allow_origin=allow_origin,
        )

        otoroshimodels_cors_settings.additional_properties = d
        return otoroshimodels_cors_settings

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

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_in_cookie import OtoroshimodelsInCookie
from ..models.otoroshimodels_in_header import OtoroshimodelsInHeader
from ..models.otoroshimodels_in_query_param import OtoroshimodelsInQueryParam
from ..models.otoroshimodels_mapping_settings import OtoroshimodelsMappingSettings
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsTransformSettings")


@attr.s(auto_attribs=True)
class OtoroshimodelsTransformSettings:
    """jwt token transformation settings"""

    location: Union[OtoroshimodelsInCookie, OtoroshimodelsInHeader, OtoroshimodelsInQueryParam, Unset] = UNSET
    mapping_settings: Union[Unset, OtoroshimodelsMappingSettings] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        location: Union[Dict[str, Any], Unset]
        if isinstance(self.location, Unset):
            location = UNSET
        elif isinstance(self.location, OtoroshimodelsInCookie):
            location = self.location.to_dict()

        elif isinstance(self.location, OtoroshimodelsInHeader):
            location = self.location.to_dict()

        else:
            location = self.location.to_dict()

        mapping_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mapping_settings, Unset):
            mapping_settings = self.mapping_settings.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if location is not UNSET:
            field_dict["location"] = location
        if mapping_settings is not UNSET:
            field_dict["mappingSettings"] = mapping_settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_location(
            data: object,
        ) -> Union[OtoroshimodelsInCookie, OtoroshimodelsInHeader, OtoroshimodelsInQueryParam, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_jwt_token_location_type_0 = OtoroshimodelsInCookie.from_dict(data)

                return componentsschemasotoroshimodels_jwt_token_location_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasotoroshimodels_jwt_token_location_type_1 = OtoroshimodelsInHeader.from_dict(data)

                return componentsschemasotoroshimodels_jwt_token_location_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemasotoroshimodels_jwt_token_location_type_2 = OtoroshimodelsInQueryParam.from_dict(data)

            return componentsschemasotoroshimodels_jwt_token_location_type_2

        location = _parse_location(d.pop("location", UNSET))

        _mapping_settings = d.pop("mappingSettings", UNSET)
        mapping_settings: Union[Unset, OtoroshimodelsMappingSettings]
        if isinstance(_mapping_settings, Unset):
            mapping_settings = UNSET
        else:
            mapping_settings = OtoroshimodelsMappingSettings.from_dict(_mapping_settings)

        otoroshimodels_transform_settings = cls(
            location=location,
            mapping_settings=mapping_settings,
        )

        otoroshimodels_transform_settings.additional_properties = d
        return otoroshimodels_transform_settings

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

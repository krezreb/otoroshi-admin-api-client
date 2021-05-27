from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsGeoPositionRadius")


@attr.s(auto_attribs=True)
class OtoroshimodelsGeoPositionRadius:
    """Geolocation radius"""

    latitude: Union[Unset, float] = UNSET
    longitude: Union[Unset, float] = UNSET
    radius: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        latitude = self.latitude
        longitude = self.longitude
        radius = self.radius

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if radius is not UNSET:
            field_dict["radius"] = radius

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        radius = d.pop("radius", UNSET)

        otoroshimodels_geo_position_radius = cls(
            latitude=latitude,
            longitude=longitude,
            radius=radius,
        )

        otoroshimodels_geo_position_radius.additional_properties = d
        return otoroshimodels_geo_position_radius

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

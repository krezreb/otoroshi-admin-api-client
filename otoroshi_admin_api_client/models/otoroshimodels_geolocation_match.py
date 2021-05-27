from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_geo_position_radius import OtoroshimodelsGeoPositionRadius
from ..models.otoroshimodels_geolocation_match_type import OtoroshimodelsGeolocationMatchType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsGeolocationMatch")


@attr.s(auto_attribs=True)
class OtoroshimodelsGeolocationMatch:
    """Match a target if in the same geo location radius"""

    positions: Union[Unset, List[OtoroshimodelsGeoPositionRadius]] = UNSET
    type: Union[Unset, OtoroshimodelsGeolocationMatchType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        positions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.positions, Unset):
            positions = []
            for positions_item_data in self.positions:
                positions_item = positions_item_data.to_dict()

                positions.append(positions_item)

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if positions is not UNSET:
            field_dict["positions"] = positions
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        positions = []
        _positions = d.pop("positions", UNSET)
        for positions_item_data in _positions or []:
            positions_item = OtoroshimodelsGeoPositionRadius.from_dict(positions_item_data)

            positions.append(positions_item)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshimodelsGeolocationMatchType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshimodelsGeolocationMatchType(_type)

        otoroshimodels_geolocation_match = cls(
            positions=positions,
            type=type,
        )

        otoroshimodels_geolocation_match.additional_properties = d
        return otoroshimodels_geolocation_match

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

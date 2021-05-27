from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_restriction_path import OtoroshimodelsRestrictionPath
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsRestrictions")


@attr.s(auto_attribs=True)
class OtoroshimodelsRestrictions:
    """Http requests restrictions for a service or an apikey"""

    forbidden: Union[Unset, List[OtoroshimodelsRestrictionPath]] = UNSET
    allowed: Union[Unset, List[OtoroshimodelsRestrictionPath]] = UNSET
    not_found: Union[Unset, List[OtoroshimodelsRestrictionPath]] = UNSET
    allow_last: Union[Unset, bool] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        forbidden: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.forbidden, Unset):
            forbidden = []
            for forbidden_item_data in self.forbidden:
                forbidden_item = forbidden_item_data.to_dict()

                forbidden.append(forbidden_item)

        allowed: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.allowed, Unset):
            allowed = []
            for allowed_item_data in self.allowed:
                allowed_item = allowed_item_data.to_dict()

                allowed.append(allowed_item)

        not_found: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.not_found, Unset):
            not_found = []
            for not_found_item_data in self.not_found:
                not_found_item = not_found_item_data.to_dict()

                not_found.append(not_found_item)

        allow_last = self.allow_last
        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if forbidden is not UNSET:
            field_dict["forbidden"] = forbidden
        if allowed is not UNSET:
            field_dict["allowed"] = allowed
        if not_found is not UNSET:
            field_dict["notFound"] = not_found
        if allow_last is not UNSET:
            field_dict["allowLast"] = allow_last
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        forbidden = []
        _forbidden = d.pop("forbidden", UNSET)
        for forbidden_item_data in _forbidden or []:
            forbidden_item = OtoroshimodelsRestrictionPath.from_dict(forbidden_item_data)

            forbidden.append(forbidden_item)

        allowed = []
        _allowed = d.pop("allowed", UNSET)
        for allowed_item_data in _allowed or []:
            allowed_item = OtoroshimodelsRestrictionPath.from_dict(allowed_item_data)

            allowed.append(allowed_item)

        not_found = []
        _not_found = d.pop("notFound", UNSET)
        for not_found_item_data in _not_found or []:
            not_found_item = OtoroshimodelsRestrictionPath.from_dict(not_found_item_data)

            not_found.append(not_found_item)

        allow_last = d.pop("allowLast", UNSET)

        enabled = d.pop("enabled", UNSET)

        otoroshimodels_restrictions = cls(
            forbidden=forbidden,
            allowed=allowed,
            not_found=not_found,
            allow_last=allow_last,
            enabled=enabled,
        )

        otoroshimodels_restrictions.additional_properties = d
        return otoroshimodels_restrictions

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

from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.otoroshimodels_ref_jwt_verifier_type import OtoroshimodelsRefJwtVerifierType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsRefJwtVerifier")


@attr.s(auto_attribs=True)
class OtoroshimodelsRefJwtVerifier:
    """Reference to a jwt verifier"""

    excluded_patterns: Union[Unset, List[str]] = UNSET
    ids: Union[Unset, List[str]] = UNSET
    type: Union[Unset, OtoroshimodelsRefJwtVerifierType] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        excluded_patterns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.excluded_patterns, Unset):
            excluded_patterns = self.excluded_patterns

        ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if excluded_patterns is not UNSET:
            field_dict["excludedPatterns"] = excluded_patterns
        if ids is not UNSET:
            field_dict["ids"] = ids
        if type is not UNSET:
            field_dict["type"] = type
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        excluded_patterns = cast(List[str], d.pop("excludedPatterns", UNSET))

        ids = cast(List[str], d.pop("ids", UNSET))

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshimodelsRefJwtVerifierType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshimodelsRefJwtVerifierType(_type)

        enabled = d.pop("enabled", UNSET)

        otoroshimodels_ref_jwt_verifier = cls(
            excluded_patterns=excluded_patterns,
            ids=ids,
            type=type,
            enabled=enabled,
        )

        otoroshimodels_ref_jwt_verifier.additional_properties = d
        return otoroshimodels_ref_jwt_verifier

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

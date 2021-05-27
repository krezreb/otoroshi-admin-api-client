from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.otoroshimodels_api_key_route_matcher_all_meta_in import OtoroshimodelsApiKeyRouteMatcherAllMetaIn
from ..models.otoroshimodels_api_key_route_matcher_none_meta_in import OtoroshimodelsApiKeyRouteMatcherNoneMetaIn
from ..models.otoroshimodels_api_key_route_matcher_one_meta_in import OtoroshimodelsApiKeyRouteMatcherOneMetaIn
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsApiKeyRouteMatcher")


@attr.s(auto_attribs=True)
class OtoroshimodelsApiKeyRouteMatcher:
    """Routing settings based on apikeys metadata and tags"""

    one_tag_in: Union[Unset, List[str]] = UNSET
    none_meta_keys_in: Union[Unset, List[str]] = UNSET
    one_meta_in: Union[Unset, OtoroshimodelsApiKeyRouteMatcherOneMetaIn] = UNSET
    one_meta_key_in: Union[Unset, List[str]] = UNSET
    all_meta_keys_in: Union[Unset, List[str]] = UNSET
    none_tag_in: Union[Unset, List[str]] = UNSET
    all_tags_in: Union[Unset, List[str]] = UNSET
    all_meta_in: Union[Unset, OtoroshimodelsApiKeyRouteMatcherAllMetaIn] = UNSET
    none_meta_in: Union[Unset, OtoroshimodelsApiKeyRouteMatcherNoneMetaIn] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        one_tag_in: Union[Unset, List[str]] = UNSET
        if not isinstance(self.one_tag_in, Unset):
            one_tag_in = self.one_tag_in

        none_meta_keys_in: Union[Unset, List[str]] = UNSET
        if not isinstance(self.none_meta_keys_in, Unset):
            none_meta_keys_in = self.none_meta_keys_in

        one_meta_in: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.one_meta_in, Unset):
            one_meta_in = self.one_meta_in.to_dict()

        one_meta_key_in: Union[Unset, List[str]] = UNSET
        if not isinstance(self.one_meta_key_in, Unset):
            one_meta_key_in = self.one_meta_key_in

        all_meta_keys_in: Union[Unset, List[str]] = UNSET
        if not isinstance(self.all_meta_keys_in, Unset):
            all_meta_keys_in = self.all_meta_keys_in

        none_tag_in: Union[Unset, List[str]] = UNSET
        if not isinstance(self.none_tag_in, Unset):
            none_tag_in = self.none_tag_in

        all_tags_in: Union[Unset, List[str]] = UNSET
        if not isinstance(self.all_tags_in, Unset):
            all_tags_in = self.all_tags_in

        all_meta_in: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.all_meta_in, Unset):
            all_meta_in = self.all_meta_in.to_dict()

        none_meta_in: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.none_meta_in, Unset):
            none_meta_in = self.none_meta_in.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if one_tag_in is not UNSET:
            field_dict["oneTagIn"] = one_tag_in
        if none_meta_keys_in is not UNSET:
            field_dict["noneMetaKeysIn"] = none_meta_keys_in
        if one_meta_in is not UNSET:
            field_dict["oneMetaIn"] = one_meta_in
        if one_meta_key_in is not UNSET:
            field_dict["oneMetaKeyIn"] = one_meta_key_in
        if all_meta_keys_in is not UNSET:
            field_dict["allMetaKeysIn"] = all_meta_keys_in
        if none_tag_in is not UNSET:
            field_dict["noneTagIn"] = none_tag_in
        if all_tags_in is not UNSET:
            field_dict["allTagsIn"] = all_tags_in
        if all_meta_in is not UNSET:
            field_dict["allMetaIn"] = all_meta_in
        if none_meta_in is not UNSET:
            field_dict["noneMetaIn"] = none_meta_in

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        one_tag_in = cast(List[str], d.pop("oneTagIn", UNSET))

        none_meta_keys_in = cast(List[str], d.pop("noneMetaKeysIn", UNSET))

        _one_meta_in = d.pop("oneMetaIn", UNSET)
        one_meta_in: Union[Unset, OtoroshimodelsApiKeyRouteMatcherOneMetaIn]
        if isinstance(_one_meta_in, Unset):
            one_meta_in = UNSET
        else:
            one_meta_in = OtoroshimodelsApiKeyRouteMatcherOneMetaIn.from_dict(_one_meta_in)

        one_meta_key_in = cast(List[str], d.pop("oneMetaKeyIn", UNSET))

        all_meta_keys_in = cast(List[str], d.pop("allMetaKeysIn", UNSET))

        none_tag_in = cast(List[str], d.pop("noneTagIn", UNSET))

        all_tags_in = cast(List[str], d.pop("allTagsIn", UNSET))

        _all_meta_in = d.pop("allMetaIn", UNSET)
        all_meta_in: Union[Unset, OtoroshimodelsApiKeyRouteMatcherAllMetaIn]
        if isinstance(_all_meta_in, Unset):
            all_meta_in = UNSET
        else:
            all_meta_in = OtoroshimodelsApiKeyRouteMatcherAllMetaIn.from_dict(_all_meta_in)

        _none_meta_in = d.pop("noneMetaIn", UNSET)
        none_meta_in: Union[Unset, OtoroshimodelsApiKeyRouteMatcherNoneMetaIn]
        if isinstance(_none_meta_in, Unset):
            none_meta_in = UNSET
        else:
            none_meta_in = OtoroshimodelsApiKeyRouteMatcherNoneMetaIn.from_dict(_none_meta_in)

        otoroshimodels_api_key_route_matcher = cls(
            one_tag_in=one_tag_in,
            none_meta_keys_in=none_meta_keys_in,
            one_meta_in=one_meta_in,
            one_meta_key_in=one_meta_key_in,
            all_meta_keys_in=all_meta_keys_in,
            none_tag_in=none_tag_in,
            all_tags_in=all_tags_in,
            all_meta_in=all_meta_in,
            none_meta_in=none_meta_in,
        )

        otoroshimodels_api_key_route_matcher.additional_properties = d
        return otoroshimodels_api_key_route_matcher

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

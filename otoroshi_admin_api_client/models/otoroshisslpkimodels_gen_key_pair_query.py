from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshisslpkimodelsGenKeyPairQuery")


@attr.s(auto_attribs=True)
class OtoroshisslpkimodelsGenKeyPairQuery:
    """Settings for generating a keypair"""

    algo: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        algo = self.algo
        size = self.size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if algo is not UNSET:
            field_dict["algo"] = algo
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        algo = d.pop("algo", UNSET)

        size = d.pop("size", UNSET)

        otoroshisslpkimodels_gen_key_pair_query = cls(
            algo=algo,
            size=size,
        )

        otoroshisslpkimodels_gen_key_pair_query.additional_properties = d
        return otoroshisslpkimodels_gen_key_pair_query

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

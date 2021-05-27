from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshisslpkimodelsGenKeyPairResponse")


@attr.s(auto_attribs=True)
class OtoroshisslpkimodelsGenKeyPairResponse:
    """Response for a keypair generation operation"""

    public_key: Union[Unset, str] = UNSET
    private_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        public_key = self.public_key
        private_key = self.private_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key
        if private_key is not UNSET:
            field_dict["privateKey"] = private_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        public_key = d.pop("publicKey", UNSET)

        private_key = d.pop("privateKey", UNSET)

        otoroshisslpkimodels_gen_key_pair_response = cls(
            public_key=public_key,
            private_key=private_key,
        )

        otoroshisslpkimodels_gen_key_pair_response.additional_properties = d
        return otoroshisslpkimodels_gen_key_pair_response

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

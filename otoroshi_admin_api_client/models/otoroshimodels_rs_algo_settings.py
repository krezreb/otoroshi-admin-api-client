from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.null import Null
from ..models.otoroshimodels_rs_algo_settings_type import OtoroshimodelsRSAlgoSettingsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsRSAlgoSettings")


@attr.s(auto_attribs=True)
class OtoroshimodelsRSAlgoSettings:
    """Settings to use RSA signing algorithm"""

    private_key: Union[Null, Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    public_key: Union[Unset, str] = UNSET
    type: Union[Unset, OtoroshimodelsRSAlgoSettingsType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        private_key: Union[Dict[str, Any], Unset, str]
        if isinstance(self.private_key, Unset):
            private_key = UNSET
        elif isinstance(self.private_key, Null):
            private_key = UNSET
            if not isinstance(self.private_key, Unset):
                private_key = self.private_key.to_dict()

        else:
            private_key = self.private_key

        size = self.size
        public_key = self.public_key
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if private_key is not UNSET:
            field_dict["privateKey"] = private_key
        if size is not UNSET:
            field_dict["size"] = size
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_private_key(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _private_key_type_0 = data
                private_key_type_0: Union[Unset, Null]
                if isinstance(_private_key_type_0, Unset):
                    private_key_type_0 = UNSET
                else:
                    private_key_type_0 = Null.from_dict(_private_key_type_0)

                return private_key_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        private_key = _parse_private_key(d.pop("privateKey", UNSET))

        size = d.pop("size", UNSET)

        public_key = d.pop("publicKey", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshimodelsRSAlgoSettingsType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshimodelsRSAlgoSettingsType(_type)

        otoroshimodels_rs_algo_settings = cls(
            private_key=private_key,
            size=size,
            public_key=public_key,
            type=type,
        )

        otoroshimodels_rs_algo_settings.additional_properties = d
        return otoroshimodels_rs_algo_settings

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

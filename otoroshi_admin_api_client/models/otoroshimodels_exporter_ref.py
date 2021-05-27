from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_exporter_ref_config import OtoroshimodelsExporterRefConfig
from ..models.otoroshimodels_exporter_ref_type import OtoroshimodelsExporterRefType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsExporterRef")


@attr.s(auto_attribs=True)
class OtoroshimodelsExporterRef:
    """Reference to a data exporter"""

    ref: Union[Unset, str] = UNSET
    type: Union[Unset, OtoroshimodelsExporterRefType] = UNSET
    config: Union[Unset, OtoroshimodelsExporterRefConfig] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ref is not UNSET:
            field_dict["ref"] = ref
        if type is not UNSET:
            field_dict["type"] = type
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ref = d.pop("ref", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, OtoroshimodelsExporterRefType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OtoroshimodelsExporterRefType(_type)

        _config = d.pop("config", UNSET)
        config: Union[Unset, OtoroshimodelsExporterRefConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = OtoroshimodelsExporterRefConfig.from_dict(_config)

        otoroshimodels_exporter_ref = cls(
            ref=ref,
            type=type,
            config=config,
        )

        otoroshimodels_exporter_ref.additional_properties = d
        return otoroshimodels_exporter_ref

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

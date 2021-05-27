from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_data_exporter_config_filtering_exclude_item import (
    OtoroshimodelsDataExporterConfigFilteringExcludeItem,
)
from ..models.otoroshimodels_data_exporter_config_filtering_include_item import (
    OtoroshimodelsDataExporterConfigFilteringIncludeItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsDataExporterConfigFiltering")


@attr.s(auto_attribs=True)
class OtoroshimodelsDataExporterConfigFiltering:
    """Settings to match otoroshi events"""

    include: Union[Unset, List[OtoroshimodelsDataExporterConfigFilteringIncludeItem]] = UNSET
    exclude: Union[Unset, List[OtoroshimodelsDataExporterConfigFilteringExcludeItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        include: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.include, Unset):
            include = []
            for include_item_data in self.include:
                include_item = include_item_data.to_dict()

                include.append(include_item)

        exclude: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.exclude, Unset):
            exclude = []
            for exclude_item_data in self.exclude:
                exclude_item = exclude_item_data.to_dict()

                exclude.append(exclude_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if include is not UNSET:
            field_dict["include"] = include
        if exclude is not UNSET:
            field_dict["exclude"] = exclude

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        include = []
        _include = d.pop("include", UNSET)
        for include_item_data in _include or []:
            include_item = OtoroshimodelsDataExporterConfigFilteringIncludeItem.from_dict(include_item_data)

            include.append(include_item)

        exclude = []
        _exclude = d.pop("exclude", UNSET)
        for exclude_item_data in _exclude or []:
            exclude_item = OtoroshimodelsDataExporterConfigFilteringExcludeItem.from_dict(exclude_item_data)

            exclude.append(exclude_item)

        otoroshimodels_data_exporter_config_filtering = cls(
            include=include,
            exclude=exclude,
        )

        otoroshimodels_data_exporter_config_filtering.additional_properties = d
        return otoroshimodels_data_exporter_config_filtering

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

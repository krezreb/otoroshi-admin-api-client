from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.null import Null
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsApiDescriptor")


@attr.s(auto_attribs=True)
class OtoroshimodelsApiDescriptor:
    """Represent if a service exposes an API with an optional url to an openapi descriptor"""

    expose_api: Union[Unset, bool] = UNSET
    open_api_descriptor_url: Union[Null, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        expose_api = self.expose_api
        open_api_descriptor_url: Union[Dict[str, Any], Unset, str]
        if isinstance(self.open_api_descriptor_url, Unset):
            open_api_descriptor_url = UNSET
        elif isinstance(self.open_api_descriptor_url, Null):
            open_api_descriptor_url = UNSET
            if not isinstance(self.open_api_descriptor_url, Unset):
                open_api_descriptor_url = self.open_api_descriptor_url.to_dict()

        else:
            open_api_descriptor_url = self.open_api_descriptor_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expose_api is not UNSET:
            field_dict["exposeApi"] = expose_api
        if open_api_descriptor_url is not UNSET:
            field_dict["openApiDescriptorUrl"] = open_api_descriptor_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        expose_api = d.pop("exposeApi", UNSET)

        def _parse_open_api_descriptor_url(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _open_api_descriptor_url_type_0 = data
                open_api_descriptor_url_type_0: Union[Unset, Null]
                if isinstance(_open_api_descriptor_url_type_0, Unset):
                    open_api_descriptor_url_type_0 = UNSET
                else:
                    open_api_descriptor_url_type_0 = Null.from_dict(_open_api_descriptor_url_type_0)

                return open_api_descriptor_url_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        open_api_descriptor_url = _parse_open_api_descriptor_url(d.pop("openApiDescriptorUrl", UNSET))

        otoroshimodels_api_descriptor = cls(
            expose_api=expose_api,
            open_api_descriptor_url=open_api_descriptor_url,
        )

        otoroshimodels_api_descriptor.additional_properties = d
        return otoroshimodels_api_descriptor

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

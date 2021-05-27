from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_error_template_messages import OtoroshimodelsErrorTemplateMessages
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsErrorTemplate")


@attr.s(auto_attribs=True)
class OtoroshimodelsErrorTemplate:
    """Service descriptor error template"""

    template_50_x: Union[Unset, str] = UNSET
    template_maintenance: Union[Unset, str] = UNSET
    template_build: Union[Unset, str] = UNSET
    service_id: Union[Unset, str] = UNSET
    messages: Union[Unset, OtoroshimodelsErrorTemplateMessages] = UNSET
    template_40_x: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        template_50_x = self.template_50_x
        template_maintenance = self.template_maintenance
        template_build = self.template_build
        service_id = self.service_id
        messages: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = self.messages.to_dict()

        template_40_x = self.template_40_x

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if template_50_x is not UNSET:
            field_dict["template50x"] = template_50_x
        if template_maintenance is not UNSET:
            field_dict["templateMaintenance"] = template_maintenance
        if template_build is not UNSET:
            field_dict["templateBuild"] = template_build
        if service_id is not UNSET:
            field_dict["serviceId"] = service_id
        if messages is not UNSET:
            field_dict["messages"] = messages
        if template_40_x is not UNSET:
            field_dict["template40x"] = template_40_x

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        template_50_x = d.pop("template50x", UNSET)

        template_maintenance = d.pop("templateMaintenance", UNSET)

        template_build = d.pop("templateBuild", UNSET)

        service_id = d.pop("serviceId", UNSET)

        _messages = d.pop("messages", UNSET)
        messages: Union[Unset, OtoroshimodelsErrorTemplateMessages]
        if isinstance(_messages, Unset):
            messages = UNSET
        else:
            messages = OtoroshimodelsErrorTemplateMessages.from_dict(_messages)

        template_40_x = d.pop("template40x", UNSET)

        otoroshimodels_error_template = cls(
            template_50_x=template_50_x,
            template_maintenance=template_maintenance,
            template_build=template_build,
            service_id=service_id,
            messages=messages,
            template_40_x=template_40_x,
        )

        otoroshimodels_error_template.additional_properties = d
        return otoroshimodels_error_template

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

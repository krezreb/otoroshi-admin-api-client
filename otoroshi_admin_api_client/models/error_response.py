from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorResponse")


@attr.s(auto_attribs=True)
class ErrorResponse:
    """Typical error returned by otoroshi"""

    error: Union[Unset, str] = UNSET
    error_description: Union[Unset, str] = UNSET
    otoroshi_error: Union[Unset, str] = UNSET
    otoroshi_error_msg: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error = self.error
        error_description = self.error_description
        otoroshi_error = self.otoroshi_error
        otoroshi_error_msg = self.otoroshi_error_msg

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if error_description is not UNSET:
            field_dict["error_description"] = error_description
        if otoroshi_error is not UNSET:
            field_dict["Otoroshi-Error"] = otoroshi_error
        if otoroshi_error_msg is not UNSET:
            field_dict["Otoroshi-Error-Msg"] = otoroshi_error_msg

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error = d.pop("error", UNSET)

        error_description = d.pop("error_description", UNSET)

        otoroshi_error = d.pop("Otoroshi-Error", UNSET)

        otoroshi_error_msg = d.pop("Otoroshi-Error-Msg", UNSET)

        error_response = cls(
            error=error,
            error_description=error_description,
            otoroshi_error=otoroshi_error,
            otoroshi_error_msg=otoroshi_error_msg,
        )

        error_response.additional_properties = d
        return error_response

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

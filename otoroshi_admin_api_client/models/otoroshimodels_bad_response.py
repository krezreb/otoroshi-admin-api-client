from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_bad_response_headers import OtoroshimodelsBadResponseHeaders
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsBadResponse")


@attr.s(auto_attribs=True)
class OtoroshimodelsBadResponse:
    """Settings for a bad response return (chaos engineering)"""

    status: Union[Unset, int] = UNSET
    body: Union[Unset, str] = UNSET
    headers: Union[Unset, OtoroshimodelsBadResponseHeaders] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status
        body = self.body
        headers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if body is not UNSET:
            field_dict["body"] = body
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = d.pop("status", UNSET)

        body = d.pop("body", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, OtoroshimodelsBadResponseHeaders]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = OtoroshimodelsBadResponseHeaders.from_dict(_headers)

        otoroshimodels_bad_response = cls(
            status=status,
            body=body,
            headers=headers,
        )

        otoroshimodels_bad_response.additional_properties = d
        return otoroshimodels_bad_response

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

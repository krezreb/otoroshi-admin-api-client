from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.otoroshimodels_bad_response import OtoroshimodelsBadResponse
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsBadResponsesFaultConfig")


@attr.s(auto_attribs=True)
class OtoroshimodelsBadResponsesFaultConfig:
    """List of bad response settings"""

    ratio: Union[Unset, float] = UNSET
    responses: Union[Unset, List[OtoroshimodelsBadResponse]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ratio = self.ratio
        responses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.responses, Unset):
            responses = []
            for responses_item_data in self.responses:
                responses_item = responses_item_data.to_dict()

                responses.append(responses_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ratio is not UNSET:
            field_dict["ratio"] = ratio
        if responses is not UNSET:
            field_dict["responses"] = responses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ratio = d.pop("ratio", UNSET)

        responses = []
        _responses = d.pop("responses", UNSET)
        for responses_item_data in _responses or []:
            responses_item = OtoroshimodelsBadResponse.from_dict(responses_item_data)

            responses.append(responses_item)

        otoroshimodels_bad_responses_fault_config = cls(
            ratio=ratio,
            responses=responses,
        )

        otoroshimodels_bad_responses_fault_config.additional_properties = d
        return otoroshimodels_bad_responses_fault_config

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

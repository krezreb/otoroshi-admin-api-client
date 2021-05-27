from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.null import Null
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsSecComHeaders")


@attr.s(auto_attribs=True)
class OtoroshimodelsSecComHeaders:
    """Header names for the otoroshi exchange protocol"""

    claim_request_name: Union[Null, Unset, str] = UNSET
    state_request_name: Union[Null, Unset, str] = UNSET
    state_response_name: Union[Null, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        claim_request_name: Union[Dict[str, Any], Unset, str]
        if isinstance(self.claim_request_name, Unset):
            claim_request_name = UNSET
        elif isinstance(self.claim_request_name, Null):
            claim_request_name = UNSET
            if not isinstance(self.claim_request_name, Unset):
                claim_request_name = self.claim_request_name.to_dict()

        else:
            claim_request_name = self.claim_request_name

        state_request_name: Union[Dict[str, Any], Unset, str]
        if isinstance(self.state_request_name, Unset):
            state_request_name = UNSET
        elif isinstance(self.state_request_name, Null):
            state_request_name = UNSET
            if not isinstance(self.state_request_name, Unset):
                state_request_name = self.state_request_name.to_dict()

        else:
            state_request_name = self.state_request_name

        state_response_name: Union[Dict[str, Any], Unset, str]
        if isinstance(self.state_response_name, Unset):
            state_response_name = UNSET
        elif isinstance(self.state_response_name, Null):
            state_response_name = UNSET
            if not isinstance(self.state_response_name, Unset):
                state_response_name = self.state_response_name.to_dict()

        else:
            state_response_name = self.state_response_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if claim_request_name is not UNSET:
            field_dict["claimRequestName"] = claim_request_name
        if state_request_name is not UNSET:
            field_dict["stateRequestName"] = state_request_name
        if state_response_name is not UNSET:
            field_dict["stateResponseName"] = state_response_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_claim_request_name(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _claim_request_name_type_0 = data
                claim_request_name_type_0: Union[Unset, Null]
                if isinstance(_claim_request_name_type_0, Unset):
                    claim_request_name_type_0 = UNSET
                else:
                    claim_request_name_type_0 = Null.from_dict(_claim_request_name_type_0)

                return claim_request_name_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        claim_request_name = _parse_claim_request_name(d.pop("claimRequestName", UNSET))

        def _parse_state_request_name(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _state_request_name_type_0 = data
                state_request_name_type_0: Union[Unset, Null]
                if isinstance(_state_request_name_type_0, Unset):
                    state_request_name_type_0 = UNSET
                else:
                    state_request_name_type_0 = Null.from_dict(_state_request_name_type_0)

                return state_request_name_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        state_request_name = _parse_state_request_name(d.pop("stateRequestName", UNSET))

        def _parse_state_response_name(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _state_response_name_type_0 = data
                state_response_name_type_0: Union[Unset, Null]
                if isinstance(_state_response_name_type_0, Unset):
                    state_response_name_type_0 = UNSET
                else:
                    state_response_name_type_0 = Null.from_dict(_state_response_name_type_0)

                return state_response_name_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        state_response_name = _parse_state_response_name(d.pop("stateResponseName", UNSET))

        otoroshimodels_sec_com_headers = cls(
            claim_request_name=claim_request_name,
            state_request_name=state_request_name,
            state_response_name=state_response_name,
        )

        otoroshimodels_sec_com_headers.additional_properties = d
        return otoroshimodels_sec_com_headers

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

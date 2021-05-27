from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.null import Null
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshimodelsClientIdAuthConstraints")


@attr.s(auto_attribs=True)
class OtoroshimodelsClientIdAuthConstraints:
    """Settings to extract apikey (using client_id only) from a header or query param"""

    enabled: Union[Unset, bool] = UNSET
    header_name: Union[Null, Unset, str] = UNSET
    query_name: Union[Null, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        header_name: Union[Dict[str, Any], Unset, str]
        if isinstance(self.header_name, Unset):
            header_name = UNSET
        elif isinstance(self.header_name, Null):
            header_name = UNSET
            if not isinstance(self.header_name, Unset):
                header_name = self.header_name.to_dict()

        else:
            header_name = self.header_name

        query_name: Union[Dict[str, Any], Unset, str]
        if isinstance(self.query_name, Unset):
            query_name = UNSET
        elif isinstance(self.query_name, Null):
            query_name = UNSET
            if not isinstance(self.query_name, Unset):
                query_name = self.query_name.to_dict()

        else:
            query_name = self.query_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if header_name is not UNSET:
            field_dict["headerName"] = header_name
        if query_name is not UNSET:
            field_dict["queryName"] = query_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        def _parse_header_name(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _header_name_type_0 = data
                header_name_type_0: Union[Unset, Null]
                if isinstance(_header_name_type_0, Unset):
                    header_name_type_0 = UNSET
                else:
                    header_name_type_0 = Null.from_dict(_header_name_type_0)

                return header_name_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        header_name = _parse_header_name(d.pop("headerName", UNSET))

        def _parse_query_name(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _query_name_type_0 = data
                query_name_type_0: Union[Unset, Null]
                if isinstance(_query_name_type_0, Unset):
                    query_name_type_0 = UNSET
                else:
                    query_name_type_0 = Null.from_dict(_query_name_type_0)

                return query_name_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        query_name = _parse_query_name(d.pop("queryName", UNSET))

        otoroshimodels_client_id_auth_constraints = cls(
            enabled=enabled,
            header_name=header_name,
            query_name=query_name,
        )

        otoroshimodels_client_id_auth_constraints.additional_properties = d
        return otoroshimodels_client_id_auth_constraints

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

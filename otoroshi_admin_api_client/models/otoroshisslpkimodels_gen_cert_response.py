from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.null import Null
from ..models.otoroshisslpkimodels_gen_csr_query import OtoroshisslpkimodelsGenCsrQuery
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshisslpkimodelsGenCertResponse")


@attr.s(auto_attribs=True)
class OtoroshisslpkimodelsGenCertResponse:
    """Response for a certificate generation operation"""

    ca: Union[Unset, str] = UNSET
    ca_chain: Union[Unset, List[str]] = UNSET
    csr_query: Union[Null, Union[Null, OtoroshisslpkimodelsGenCsrQuery], Unset] = UNSET
    cert: Union[Unset, str] = UNSET
    serial: Union[Unset, int] = UNSET
    key: Union[Unset, str] = UNSET
    csr: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ca = self.ca
        ca_chain: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ca_chain, Unset):
            ca_chain = self.ca_chain

        csr_query: Union[Dict[str, Any], Unset]
        if isinstance(self.csr_query, Unset):
            csr_query = UNSET
        elif isinstance(self.csr_query, Null):
            csr_query = UNSET
            if not isinstance(self.csr_query, Unset):
                csr_query = self.csr_query.to_dict()

        else:
            csr_query
            if isinstance(self.csr_query, Unset):
                csr_query = UNSET
            elif isinstance(self.csr_query, Null):
                csr_query = UNSET
                if not isinstance(self.csr_query, Unset):
                    csr_query = self.csr_query.to_dict()

            else:
                csr_query = UNSET
                if not isinstance(self.csr_query, Unset):
                    csr_query = self.csr_query.to_dict()

        cert = self.cert
        serial = self.serial
        key = self.key
        csr = self.csr

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ca is not UNSET:
            field_dict["ca"] = ca
        if ca_chain is not UNSET:
            field_dict["caChain"] = ca_chain
        if csr_query is not UNSET:
            field_dict["csrQuery"] = csr_query
        if cert is not UNSET:
            field_dict["cert"] = cert
        if serial is not UNSET:
            field_dict["serial"] = serial
        if key is not UNSET:
            field_dict["key"] = key
        if csr is not UNSET:
            field_dict["csr"] = csr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ca = d.pop("ca", UNSET)

        ca_chain = cast(List[str], d.pop("caChain", UNSET))

        def _parse_csr_query(data: object) -> Union[Null, Union[Null, OtoroshisslpkimodelsGenCsrQuery], Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _csr_query_type_0 = data
                csr_query_type_0: Union[Unset, Null]
                if isinstance(_csr_query_type_0, Unset):
                    csr_query_type_0 = UNSET
                else:
                    csr_query_type_0 = Null.from_dict(_csr_query_type_0)

                return csr_query_type_0
            except:  # noqa: E722
                pass
            if not True:
                raise TypeError()

            def _parse_csr_query_type_1(data: object) -> Union[Null, OtoroshisslpkimodelsGenCsrQuery, Unset]:
                if isinstance(data, Unset):
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _csr_query_type_1_type_0 = data
                    csr_query_type_1_type_0: Union[Unset, Null]
                    if isinstance(_csr_query_type_1_type_0, Unset):
                        csr_query_type_1_type_0 = UNSET
                    else:
                        csr_query_type_1_type_0 = Null.from_dict(_csr_query_type_1_type_0)

                    return csr_query_type_1_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                _csr_query_type_1_type_1 = data
                csr_query_type_1_type_1: Union[Unset, OtoroshisslpkimodelsGenCsrQuery]
                if isinstance(_csr_query_type_1_type_1, Unset):
                    csr_query_type_1_type_1 = UNSET
                else:
                    csr_query_type_1_type_1 = OtoroshisslpkimodelsGenCsrQuery.from_dict(_csr_query_type_1_type_1)

                return csr_query_type_1_type_1

            csr_query_type_1 = _parse_csr_query_type_1(data)

            return csr_query_type_1

        csr_query = _parse_csr_query(d.pop("csrQuery", UNSET))

        cert = d.pop("cert", UNSET)

        serial = d.pop("serial", UNSET)

        key = d.pop("key", UNSET)

        csr = d.pop("csr", UNSET)

        otoroshisslpkimodels_gen_cert_response = cls(
            ca=ca,
            ca_chain=ca_chain,
            csr_query=csr_query,
            cert=cert,
            serial=serial,
            key=key,
            csr=csr,
        )

        otoroshisslpkimodels_gen_cert_response.additional_properties = d
        return otoroshisslpkimodels_gen_cert_response

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

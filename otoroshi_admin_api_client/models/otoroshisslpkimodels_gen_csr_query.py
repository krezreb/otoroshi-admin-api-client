from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.null import Null
from ..models.otoroshisslpkimodels_gen_csr_query_name import OtoroshisslpkimodelsGenCsrQueryName
from ..models.otoroshisslpkimodels_gen_key_pair_query import OtoroshisslpkimodelsGenKeyPairQuery
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoroshisslpkimodelsGenCsrQuery")


@attr.s(auto_attribs=True)
class OtoroshisslpkimodelsGenCsrQuery:
    """Settings for generating a certificate"""

    client: Union[Unset, bool] = UNSET
    hosts: Union[Unset, List[str]] = UNSET
    key: Union[Unset, OtoroshisslpkimodelsGenKeyPairQuery] = UNSET
    include_aia: Union[Unset, bool] = UNSET
    signature_alg: Union[Unset, str] = UNSET
    existing_serial_number: Union[Null, Unset, int] = UNSET
    duration: Union[Unset, float] = UNSET
    digest_alg: Union[Unset, str] = UNSET
    ca: Union[Unset, bool] = UNSET
    name: Union[Unset, OtoroshisslpkimodelsGenCsrQueryName] = UNSET
    subject: Union[Null, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client = self.client
        hosts: Union[Unset, List[str]] = UNSET
        if not isinstance(self.hosts, Unset):
            hosts = self.hosts

        key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.to_dict()

        include_aia = self.include_aia
        signature_alg = self.signature_alg
        existing_serial_number: Union[Dict[str, Any], Unset, int]
        if isinstance(self.existing_serial_number, Unset):
            existing_serial_number = UNSET
        elif isinstance(self.existing_serial_number, Null):
            existing_serial_number = UNSET
            if not isinstance(self.existing_serial_number, Unset):
                existing_serial_number = self.existing_serial_number.to_dict()

        else:
            existing_serial_number = self.existing_serial_number

        duration = self.duration
        digest_alg = self.digest_alg
        ca = self.ca
        name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.to_dict()

        subject: Union[Dict[str, Any], Unset, str]
        if isinstance(self.subject, Unset):
            subject = UNSET
        elif isinstance(self.subject, Null):
            subject = UNSET
            if not isinstance(self.subject, Unset):
                subject = self.subject.to_dict()

        else:
            subject = self.subject

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client is not UNSET:
            field_dict["client"] = client
        if hosts is not UNSET:
            field_dict["hosts"] = hosts
        if key is not UNSET:
            field_dict["key"] = key
        if include_aia is not UNSET:
            field_dict["includeAIA"] = include_aia
        if signature_alg is not UNSET:
            field_dict["signatureAlg"] = signature_alg
        if existing_serial_number is not UNSET:
            field_dict["existingSerialNumber"] = existing_serial_number
        if duration is not UNSET:
            field_dict["duration"] = duration
        if digest_alg is not UNSET:
            field_dict["digestAlg"] = digest_alg
        if ca is not UNSET:
            field_dict["ca"] = ca
        if name is not UNSET:
            field_dict["name"] = name
        if subject is not UNSET:
            field_dict["subject"] = subject

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client = d.pop("client", UNSET)

        hosts = cast(List[str], d.pop("hosts", UNSET))

        _key = d.pop("key", UNSET)
        key: Union[Unset, OtoroshisslpkimodelsGenKeyPairQuery]
        if isinstance(_key, Unset):
            key = UNSET
        else:
            key = OtoroshisslpkimodelsGenKeyPairQuery.from_dict(_key)

        include_aia = d.pop("includeAIA", UNSET)

        signature_alg = d.pop("signatureAlg", UNSET)

        def _parse_existing_serial_number(data: object) -> Union[Null, Unset, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _existing_serial_number_type_0 = data
                existing_serial_number_type_0: Union[Unset, Null]
                if isinstance(_existing_serial_number_type_0, Unset):
                    existing_serial_number_type_0 = UNSET
                else:
                    existing_serial_number_type_0 = Null.from_dict(_existing_serial_number_type_0)

                return existing_serial_number_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, int], data)

        existing_serial_number = _parse_existing_serial_number(d.pop("existingSerialNumber", UNSET))

        duration = d.pop("duration", UNSET)

        digest_alg = d.pop("digestAlg", UNSET)

        ca = d.pop("ca", UNSET)

        _name = d.pop("name", UNSET)
        name: Union[Unset, OtoroshisslpkimodelsGenCsrQueryName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = OtoroshisslpkimodelsGenCsrQueryName.from_dict(_name)

        def _parse_subject(data: object) -> Union[Null, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _subject_type_0 = data
                subject_type_0: Union[Unset, Null]
                if isinstance(_subject_type_0, Unset):
                    subject_type_0 = UNSET
                else:
                    subject_type_0 = Null.from_dict(_subject_type_0)

                return subject_type_0
            except:  # noqa: E722
                pass
            return cast(Union[Null, Unset, str], data)

        subject = _parse_subject(d.pop("subject", UNSET))

        otoroshisslpkimodels_gen_csr_query = cls(
            client=client,
            hosts=hosts,
            key=key,
            include_aia=include_aia,
            signature_alg=signature_alg,
            existing_serial_number=existing_serial_number,
            duration=duration,
            digest_alg=digest_alg,
            ca=ca,
            name=name,
            subject=subject,
        )

        otoroshisslpkimodels_gen_csr_query.additional_properties = d
        return otoroshisslpkimodels_gen_csr_query

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

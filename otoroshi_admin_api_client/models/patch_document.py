from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.patch_document_op import PatchDocumentOp
from ..models.patch_document_value import PatchDocumentValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchDocument")


@attr.s(auto_attribs=True)
class PatchDocument:
    """A JSONPatch document as defined by RFC 6902"""

    op: PatchDocumentOp
    path: str
    value: Union[Unset, PatchDocumentValue] = UNSET
    from_: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        op = self.op.value

        path = self.path
        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        from_ = self.from_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "op": op,
                "path": path,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value
        if from_ is not UNSET:
            field_dict["from"] = from_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        op = PatchDocumentOp(d.pop("op"))

        path = d.pop("path")

        _value = d.pop("value", UNSET)
        value: Union[Unset, PatchDocumentValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = PatchDocumentValue.from_dict(_value)

        from_ = d.pop("from", UNSET)

        patch_document = cls(
            op=op,
            path=path,
            value=value,
            from_=from_,
        )

        patch_document.additional_properties = d
        return patch_document

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

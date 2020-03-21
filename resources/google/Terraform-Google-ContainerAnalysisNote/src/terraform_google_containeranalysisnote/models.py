# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]


@dataclass
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    AttestationAuthority: Optional[Sequence["_AttestationAuthority"]]
    Timeouts: Optional["_Timeouts"]
    Hint: Optional[Sequence["_Hint"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            AttestationAuthority=json_data.get("AttestationAuthority"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Hint=json_data.get("Hint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AttestationAuthority:
    Hint: Optional[Sequence["_Hint"]]

    @classmethod
    def _deserialize(
        cls: Type["_AttestationAuthority"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttestationAuthority"]:
        if not json_data:
            return None
        return cls(
            Hint=json_data.get("Hint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttestationAuthority = AttestationAuthority


@dataclass
class Hint:
    HumanReadableName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Hint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Hint"]:
        if not json_data:
            return None
        return cls(
            HumanReadableName=json_data.get("HumanReadableName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Hint = Hint


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts



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
    KeyRing: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
    Name: Optional[str]
    Purpose: Optional[str]
    RotationPeriod: Optional[str]
    SelfLink: Optional[str]
    Timeouts: Optional["_Timeouts"]
    VersionTemplate: Optional[Sequence["_VersionTemplate"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            KeyRing=json_data.get("KeyRing"),
            Labels=json_data.get("Labels"),
            Name=json_data.get("Name"),
            Purpose=json_data.get("Purpose"),
            RotationPeriod=json_data.get("RotationPeriod"),
            SelfLink=json_data.get("SelfLink"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            VersionTemplate=json_data.get("VersionTemplate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Labels:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


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


@dataclass
class VersionTemplate:
    Algorithm: Optional[str]
    ProtectionLevel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionTemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionTemplate"]:
        if not json_data:
            return None
        return cls(
            Algorithm=json_data.get("Algorithm"),
            ProtectionLevel=json_data.get("ProtectionLevel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionTemplate = VersionTemplate



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
    Attached: Optional[bool]
    AvailabilityZone: Optional[str]
    Encrypt: Optional[bool]
    Period: Optional[float]
    ProjectId: Optional[float]
    SnapshotId: Optional[str]
    StorageName: Optional[str]
    StorageSize: Optional[float]
    StorageStatus: Optional[str]
    StorageType: Optional[str]
    Tags: Optional[Sequence["_Tags"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Attached=json_data.get("Attached"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Encrypt=json_data.get("Encrypt"),
            Period=json_data.get("Period"),
            ProjectId=json_data.get("ProjectId"),
            SnapshotId=json_data.get("SnapshotId"),
            StorageName=json_data.get("StorageName"),
            StorageSize=json_data.get("StorageSize"),
            StorageStatus=json_data.get("StorageStatus"),
            StorageType=json_data.get("StorageType"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags



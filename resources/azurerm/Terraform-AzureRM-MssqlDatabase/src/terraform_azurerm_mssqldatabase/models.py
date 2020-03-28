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
    AutoPauseDelayInMinutes: Optional[float]
    Collation: Optional[str]
    CreateMode: Optional[str]
    CreationSourceDatabaseId: Optional[str]
    ElasticPoolId: Optional[str]
    Id: Optional[str]
    LicenseType: Optional[str]
    MaxSizeGb: Optional[float]
    MinCapacity: Optional[float]
    Name: Optional[str]
    ReadReplicaCount: Optional[float]
    ReadScale: Optional[bool]
    RestorePointInTime: Optional[str]
    SampleName: Optional[str]
    ServerId: Optional[str]
    SkuName: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    ZoneRedundant: Optional[bool]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AutoPauseDelayInMinutes=json_data.get("AutoPauseDelayInMinutes"),
            Collation=json_data.get("Collation"),
            CreateMode=json_data.get("CreateMode"),
            CreationSourceDatabaseId=json_data.get("CreationSourceDatabaseId"),
            ElasticPoolId=json_data.get("ElasticPoolId"),
            Id=json_data.get("Id"),
            LicenseType=json_data.get("LicenseType"),
            MaxSizeGb=json_data.get("MaxSizeGb"),
            MinCapacity=json_data.get("MinCapacity"),
            Name=json_data.get("Name"),
            ReadReplicaCount=json_data.get("ReadReplicaCount"),
            ReadScale=json_data.get("ReadScale"),
            RestorePointInTime=json_data.get("RestorePointInTime"),
            SampleName=json_data.get("SampleName"),
            ServerId=json_data.get("ServerId"),
            SkuName=json_data.get("SkuName"),
            Tags=json_data.get("Tags"),
            ZoneRedundant=json_data.get("ZoneRedundant"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts



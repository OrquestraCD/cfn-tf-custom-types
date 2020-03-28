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
    Arn: Optional[str]
    Description: Optional[str]
    EncryptionKeyId: Optional[str]
    ForceDeleteWithoutRecovery: Optional[bool]
    Id: Optional[str]
    PlannedDeleteTime: Optional[str]
    RecoveryWindowInDays: Optional[float]
    SecretData: Optional[str]
    SecretDataType: Optional[str]
    SecretName: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    VersionId: Optional[str]
    VersionStages: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            Description=json_data.get("Description"),
            EncryptionKeyId=json_data.get("EncryptionKeyId"),
            ForceDeleteWithoutRecovery=json_data.get("ForceDeleteWithoutRecovery"),
            Id=json_data.get("Id"),
            PlannedDeleteTime=json_data.get("PlannedDeleteTime"),
            RecoveryWindowInDays=json_data.get("RecoveryWindowInDays"),
            SecretData=json_data.get("SecretData"),
            SecretDataType=json_data.get("SecretDataType"),
            SecretName=json_data.get("SecretName"),
            Tags=json_data.get("Tags"),
            VersionId=json_data.get("VersionId"),
            VersionStages=json_data.get("VersionStages"),
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



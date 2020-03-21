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
    S3BucketArn: Optional[str]
    Subdirectory: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Uri: Optional[str]
    S3Config: Optional[Sequence["_S3Config"]]

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
            S3BucketArn=json_data.get("S3BucketArn"),
            Subdirectory=json_data.get("Subdirectory"),
            Tags=json_data.get("Tags"),
            Uri=json_data.get("Uri"),
            S3Config=json_data.get("S3Config"),
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


@dataclass
class S3Config:
    BucketAccessRoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Config"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Config"]:
        if not json_data:
            return None
        return cls(
            BucketAccessRoleArn=json_data.get("BucketAccessRoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Config = S3Config



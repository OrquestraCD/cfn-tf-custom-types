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
    AwsServiceName: Optional[str]
    CreateDate: Optional[str]
    CustomSuffix: Optional[str]
    Description: Optional[str]
    Name: Optional[str]
    Path: Optional[str]
    UniqueId: Optional[str]

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
            AwsServiceName=json_data.get("AwsServiceName"),
            CreateDate=json_data.get("CreateDate"),
            CustomSuffix=json_data.get("CustomSuffix"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            UniqueId=json_data.get("UniqueId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel



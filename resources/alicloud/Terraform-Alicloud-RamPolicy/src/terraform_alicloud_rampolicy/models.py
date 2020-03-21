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
    AttachmentCount: Optional[float]
    Description: Optional[str]
    Document: Optional[str]
    Force: Optional[bool]
    Name: Optional[str]
    Type: Optional[str]
    Version: Optional[str]
    Statement: Optional[Sequence["_Statement"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AttachmentCount=json_data.get("AttachmentCount"),
            Description=json_data.get("Description"),
            Document=json_data.get("Document"),
            Force=json_data.get("Force"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            Version=json_data.get("Version"),
            Statement=json_data.get("Statement"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Statement:
    Action: Optional[Sequence[str]]
    Effect: Optional[str]
    Resource: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Statement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Statement"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Effect=json_data.get("Effect"),
            Resource=json_data.get("Resource"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Statement = Statement



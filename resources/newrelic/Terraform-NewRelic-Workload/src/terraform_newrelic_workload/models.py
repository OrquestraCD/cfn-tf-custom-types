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
    AccountId: Optional[float]
    CompositeEntitySearchQuery: Optional[str]
    EntityGuids: Optional[Sequence[str]]
    Guid: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Permalink: Optional[str]
    ScopeAccountIds: Optional[Sequence[float]]
    WorkloadId: Optional[float]
    EntitySearchQuery: Optional[Sequence["_EntitySearchQuery"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AccountId=json_data.get("AccountId"),
            CompositeEntitySearchQuery=json_data.get("CompositeEntitySearchQuery"),
            EntityGuids=json_data.get("EntityGuids"),
            Guid=json_data.get("Guid"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Permalink=json_data.get("Permalink"),
            ScopeAccountIds=json_data.get("ScopeAccountIds"),
            WorkloadId=json_data.get("WorkloadId"),
            EntitySearchQuery=json_data.get("EntitySearchQuery"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EntitySearchQuery:
    Query: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EntitySearchQuery"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EntitySearchQuery"]:
        if not json_data:
            return None
        return cls(
            Query=json_data.get("Query"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EntitySearchQuery = EntitySearchQuery



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
    AlertMessage: Optional[str]
    AlertPriority: Optional[str]
    AlertTags: Optional[Sequence[str]]
    Description: Optional[str]
    Enabled: Optional[bool]
    Interval: Optional[float]
    IntervalUnit: Optional[str]
    Name: Optional[str]
    OwnerTeamId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AlertMessage=json_data.get("AlertMessage"),
            AlertPriority=json_data.get("AlertPriority"),
            AlertTags=json_data.get("AlertTags"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            Interval=json_data.get("Interval"),
            IntervalUnit=json_data.get("IntervalUnit"),
            Name=json_data.get("Name"),
            OwnerTeamId=json_data.get("OwnerTeamId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel



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
    BotName: Optional[str]
    Location: Optional[str]
    ResourceGroupName: Optional[str]
    Site: Optional[Sequence["_Site"]]
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
            BotName=json_data.get("BotName"),
            Location=json_data.get("Location"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Site=json_data.get("Site"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Site:
    Enabled: Optional[bool]
    EnhancedAuthenticationEnabled: Optional[bool]
    Name: Optional[str]
    TrustedOrigins: Optional[Sequence[str]]
    V1Allowed: Optional[bool]
    V3Allowed: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Site"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Site"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            EnhancedAuthenticationEnabled=json_data.get("EnhancedAuthenticationEnabled"),
            Name=json_data.get("Name"),
            TrustedOrigins=json_data.get("TrustedOrigins"),
            V1Allowed=json_data.get("V1Allowed"),
            V3Allowed=json_data.get("V3Allowed"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Site = Site


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



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
    Address: Optional[str]
    AddressType: Optional[str]
    CreationTimestamp: Optional[str]
    Description: Optional[str]
    IpVersion: Optional[str]
    Name: Optional[str]
    Network: Optional[str]
    PrefixLength: Optional[float]
    Project: Optional[str]
    Purpose: Optional[str]
    SelfLink: Optional[str]
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
            Address=json_data.get("Address"),
            AddressType=json_data.get("AddressType"),
            CreationTimestamp=json_data.get("CreationTimestamp"),
            Description=json_data.get("Description"),
            IpVersion=json_data.get("IpVersion"),
            Name=json_data.get("Name"),
            Network=json_data.get("Network"),
            PrefixLength=json_data.get("PrefixLength"),
            Project=json_data.get("Project"),
            Purpose=json_data.get("Purpose"),
            SelfLink=json_data.get("SelfLink"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts



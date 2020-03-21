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
    AdminState: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    IpPoolId: Optional[str]
    MacPoolId: Optional[str]
    Revision: Optional[float]
    TransportZoneId: Optional[str]
    Vlan: Optional[float]
    AddressBinding: Optional[Sequence["_AddressBinding"]]
    SwitchingProfileId: Optional[Sequence["_SwitchingProfileId"]]
    Tag: Optional[Sequence["_Tag"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AdminState=json_data.get("AdminState"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            IpPoolId=json_data.get("IpPoolId"),
            MacPoolId=json_data.get("MacPoolId"),
            Revision=json_data.get("Revision"),
            TransportZoneId=json_data.get("TransportZoneId"),
            Vlan=json_data.get("Vlan"),
            AddressBinding=json_data.get("AddressBinding"),
            SwitchingProfileId=json_data.get("SwitchingProfileId"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AddressBinding:
    IpAddress: Optional[str]
    MacAddress: Optional[str]
    Vlan: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AddressBinding"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddressBinding"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
            MacAddress=json_data.get("MacAddress"),
            Vlan=json_data.get("Vlan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddressBinding = AddressBinding


@dataclass
class SwitchingProfileId:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SwitchingProfileId"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SwitchingProfileId"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SwitchingProfileId = SwitchingProfileId


@dataclass
class Tag:
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag



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
    AdvertiseConfigRevision: Optional[float]
    AdvertiseConnectedRoutes: Optional[bool]
    AdvertiseLbSnatIpRoutes: Optional[bool]
    AdvertiseLbVipRoutes: Optional[bool]
    AdvertiseNatRoutes: Optional[bool]
    AdvertiseStaticRoutes: Optional[bool]
    Description: Optional[str]
    DisplayName: Optional[str]
    EdgeClusterId: Optional[str]
    EnableRouterAdvertisement: Optional[bool]
    FailoverMode: Optional[str]
    Revision: Optional[float]
    FirewallSections: Optional[Sequence["_FirewallSections"]]
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
            AdvertiseConfigRevision=json_data.get("AdvertiseConfigRevision"),
            AdvertiseConnectedRoutes=json_data.get("AdvertiseConnectedRoutes"),
            AdvertiseLbSnatIpRoutes=json_data.get("AdvertiseLbSnatIpRoutes"),
            AdvertiseLbVipRoutes=json_data.get("AdvertiseLbVipRoutes"),
            AdvertiseNatRoutes=json_data.get("AdvertiseNatRoutes"),
            AdvertiseStaticRoutes=json_data.get("AdvertiseStaticRoutes"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            EdgeClusterId=json_data.get("EdgeClusterId"),
            EnableRouterAdvertisement=json_data.get("EnableRouterAdvertisement"),
            FailoverMode=json_data.get("FailoverMode"),
            Revision=json_data.get("Revision"),
            FirewallSections=json_data.get("FirewallSections"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FirewallSections:
    TargetId: Optional[str]
    TargetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FirewallSections"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FirewallSections"]:
        if not json_data:
            return None
        return cls(
            TargetId=json_data.get("TargetId"),
            TargetType=json_data.get("TargetType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FirewallSections = FirewallSections


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



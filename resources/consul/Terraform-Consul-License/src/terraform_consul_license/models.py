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
    CustomerId: Optional[str]
    Datacenter: Optional[str]
    ExpirationTime: Optional[str]
    Features: Optional[Sequence[str]]
    Flags: Optional[Sequence["_Flags"]]
    Id: Optional[str]
    InstallationId: Optional[str]
    IssueTime: Optional[str]
    License: Optional[str]
    LicenseId: Optional[str]
    Product: Optional[str]
    StartTime: Optional[str]
    Valid: Optional[bool]
    Warnings: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CustomerId=json_data.get("CustomerId"),
            Datacenter=json_data.get("Datacenter"),
            ExpirationTime=json_data.get("ExpirationTime"),
            Features=json_data.get("Features"),
            Flags=json_data.get("Flags"),
            Id=json_data.get("Id"),
            InstallationId=json_data.get("InstallationId"),
            IssueTime=json_data.get("IssueTime"),
            License=json_data.get("License"),
            LicenseId=json_data.get("LicenseId"),
            Product=json_data.get("Product"),
            StartTime=json_data.get("StartTime"),
            Valid=json_data.get("Valid"),
            Warnings=json_data.get("Warnings"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Flags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Flags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Flags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Flags = Flags



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
    Id: Optional[str]
    RServicesEnabled: Optional[bool]
    SqlConnectivityPort: Optional[float]
    SqlConnectivityType: Optional[str]
    SqlConnectivityUpdatePassword: Optional[str]
    SqlConnectivityUpdateUsername: Optional[str]
    SqlLicenseType: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    VirtualMachineId: Optional[str]
    AutoPatching: Optional[Sequence["_AutoPatching"]]
    KeyVaultCredential: Optional[Sequence["_KeyVaultCredential"]]
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
            Id=json_data.get("Id"),
            RServicesEnabled=json_data.get("RServicesEnabled"),
            SqlConnectivityPort=json_data.get("SqlConnectivityPort"),
            SqlConnectivityType=json_data.get("SqlConnectivityType"),
            SqlConnectivityUpdatePassword=json_data.get("SqlConnectivityUpdatePassword"),
            SqlConnectivityUpdateUsername=json_data.get("SqlConnectivityUpdateUsername"),
            SqlLicenseType=json_data.get("SqlLicenseType"),
            Tags=json_data.get("Tags"),
            VirtualMachineId=json_data.get("VirtualMachineId"),
            AutoPatching=json_data.get("AutoPatching"),
            KeyVaultCredential=json_data.get("KeyVaultCredential"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class AutoPatching:
    DayOfWeek: Optional[str]
    MaintenanceWindowDurationInMinutes: Optional[float]
    MaintenanceWindowStartingHour: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoPatching"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoPatching"]:
        if not json_data:
            return None
        return cls(
            DayOfWeek=json_data.get("DayOfWeek"),
            MaintenanceWindowDurationInMinutes=json_data.get("MaintenanceWindowDurationInMinutes"),
            MaintenanceWindowStartingHour=json_data.get("MaintenanceWindowStartingHour"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoPatching = AutoPatching


@dataclass
class KeyVaultCredential:
    KeyVaultUrl: Optional[str]
    Name: Optional[str]
    ServicePrincipalName: Optional[str]
    ServicePrincipalSecret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeyVaultCredential"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyVaultCredential"]:
        if not json_data:
            return None
        return cls(
            KeyVaultUrl=json_data.get("KeyVaultUrl"),
            Name=json_data.get("Name"),
            ServicePrincipalName=json_data.get("ServicePrincipalName"),
            ServicePrincipalSecret=json_data.get("ServicePrincipalSecret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyVaultCredential = KeyVaultCredential


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



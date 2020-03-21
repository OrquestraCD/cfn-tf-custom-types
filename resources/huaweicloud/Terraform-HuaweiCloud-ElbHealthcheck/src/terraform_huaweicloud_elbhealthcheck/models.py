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
    CreateTime: Optional[str]
    HealthcheckConnectPort: Optional[float]
    HealthcheckInterval: Optional[float]
    HealthcheckProtocol: Optional[str]
    HealthcheckTimeout: Optional[float]
    HealthcheckUri: Optional[str]
    HealthyThreshold: Optional[float]
    ListenerId: Optional[str]
    UnhealthyThreshold: Optional[float]
    UpdateTime: Optional[str]
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
            CreateTime=json_data.get("CreateTime"),
            HealthcheckConnectPort=json_data.get("HealthcheckConnectPort"),
            HealthcheckInterval=json_data.get("HealthcheckInterval"),
            HealthcheckProtocol=json_data.get("HealthcheckProtocol"),
            HealthcheckTimeout=json_data.get("HealthcheckTimeout"),
            HealthcheckUri=json_data.get("HealthcheckUri"),
            HealthyThreshold=json_data.get("HealthyThreshold"),
            ListenerId=json_data.get("ListenerId"),
            UnhealthyThreshold=json_data.get("UnhealthyThreshold"),
            UpdateTime=json_data.get("UpdateTime"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts



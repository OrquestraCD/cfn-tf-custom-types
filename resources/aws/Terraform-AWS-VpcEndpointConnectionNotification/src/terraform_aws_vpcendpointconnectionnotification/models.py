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
    ConnectionEvents: Optional[Sequence[str]]
    ConnectionNotificationArn: Optional[str]
    NotificationType: Optional[str]
    State: Optional[str]
    VpcEndpointId: Optional[str]
    VpcEndpointServiceId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ConnectionEvents=json_data.get("ConnectionEvents"),
            ConnectionNotificationArn=json_data.get("ConnectionNotificationArn"),
            NotificationType=json_data.get("NotificationType"),
            State=json_data.get("State"),
            VpcEndpointId=json_data.get("VpcEndpointId"),
            VpcEndpointServiceId=json_data.get("VpcEndpointServiceId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel



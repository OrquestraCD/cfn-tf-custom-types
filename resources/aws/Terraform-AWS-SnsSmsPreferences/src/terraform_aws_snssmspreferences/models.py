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
    DefaultSenderId: Optional[str]
    DefaultSmsType: Optional[str]
    DeliveryStatusIamRoleArn: Optional[str]
    DeliveryStatusSuccessSamplingRate: Optional[str]
    MonthlySpendLimit: Optional[str]
    UsageReportS3Bucket: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DefaultSenderId=json_data.get("DefaultSenderId"),
            DefaultSmsType=json_data.get("DefaultSmsType"),
            DeliveryStatusIamRoleArn=json_data.get("DeliveryStatusIamRoleArn"),
            DeliveryStatusSuccessSamplingRate=json_data.get("DeliveryStatusSuccessSamplingRate"),
            MonthlySpendLimit=json_data.get("MonthlySpendLimit"),
            UsageReportS3Bucket=json_data.get("UsageReportS3Bucket"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel



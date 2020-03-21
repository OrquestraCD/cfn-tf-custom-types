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
    Domain: Optional[str]
    DomainId: Optional[str]
    Hostname: Optional[str]
    Name: Optional[str]
    Priority: Optional[str]
    Ttl: Optional[str]
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Domain=json_data.get("Domain"),
            DomainId=json_data.get("DomainId"),
            Hostname=json_data.get("Hostname"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            Ttl=json_data.get("Ttl"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel



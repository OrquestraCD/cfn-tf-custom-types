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
    Name: Optional[str]
    GeoMatchConstraint: Optional[Sequence["_GeoMatchConstraint"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Name=json_data.get("Name"),
            GeoMatchConstraint=json_data.get("GeoMatchConstraint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class GeoMatchConstraint:
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GeoMatchConstraint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeoMatchConstraint"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeoMatchConstraint = GeoMatchConstraint



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
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    GithubConfiguration: Optional[Sequence["_GithubConfiguration"]]
    Identity: Optional[Sequence["_Identity"]]
    Timeouts: Optional["_Timeouts"]
    VstsConfiguration: Optional[Sequence["_VstsConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=json_data.get("Tags"),
            GithubConfiguration=json_data.get("GithubConfiguration"),
            Identity=json_data.get("Identity"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            VstsConfiguration=json_data.get("VstsConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class GithubConfiguration:
    AccountName: Optional[str]
    BranchName: Optional[str]
    GitUrl: Optional[str]
    RepositoryName: Optional[str]
    RootFolder: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GithubConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GithubConfiguration"]:
        if not json_data:
            return None
        return cls(
            AccountName=json_data.get("AccountName"),
            BranchName=json_data.get("BranchName"),
            GitUrl=json_data.get("GitUrl"),
            RepositoryName=json_data.get("RepositoryName"),
            RootFolder=json_data.get("RootFolder"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GithubConfiguration = GithubConfiguration


@dataclass
class Identity:
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Identity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Identity"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Identity = Identity


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


@dataclass
class VstsConfiguration:
    AccountName: Optional[str]
    BranchName: Optional[str]
    ProjectName: Optional[str]
    RepositoryName: Optional[str]
    RootFolder: Optional[str]
    TenantId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VstsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VstsConfiguration"]:
        if not json_data:
            return None
        return cls(
            AccountName=json_data.get("AccountName"),
            BranchName=json_data.get("BranchName"),
            ProjectName=json_data.get("ProjectName"),
            RepositoryName=json_data.get("RepositoryName"),
            RootFolder=json_data.get("RootFolder"),
            TenantId=json_data.get("TenantId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VstsConfiguration = VstsConfiguration



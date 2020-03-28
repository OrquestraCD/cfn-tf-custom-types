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
    ApplicationId: Optional[str]
    Decision: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Precedence: Optional[float]
    ZoneId: Optional[str]
    Exclude: Optional[Sequence["_Exclude"]]
    Include: Optional[Sequence["_Include"]]
    Require: Optional[Sequence["_Require"]]
    Azure: Optional[Sequence["_Azure"]]
    Github: Optional[Sequence["_Github"]]
    Gsuite: Optional[Sequence["_Gsuite"]]
    Okta: Optional[Sequence["_Okta"]]
    Saml: Optional[Sequence["_Saml"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ApplicationId=json_data.get("ApplicationId"),
            Decision=json_data.get("Decision"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Precedence=json_data.get("Precedence"),
            ZoneId=json_data.get("ZoneId"),
            Exclude=json_data.get("Exclude"),
            Include=json_data.get("Include"),
            Require=json_data.get("Require"),
            Azure=json_data.get("Azure"),
            Github=json_data.get("Github"),
            Gsuite=json_data.get("Gsuite"),
            Okta=json_data.get("Okta"),
            Saml=json_data.get("Saml"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Exclude:
    AnyValidServiceToken: Optional[bool]
    Certificate: Optional[bool]
    CommonName: Optional[str]
    Email: Optional[Sequence[str]]
    EmailDomain: Optional[Sequence[str]]
    Everyone: Optional[bool]
    Group: Optional[Sequence[str]]
    Ip: Optional[Sequence[str]]
    ServiceToken: Optional[Sequence[str]]
    Azure: Optional[Sequence["_Azure"]]
    Github: Optional[Sequence["_Github"]]
    Gsuite: Optional[Sequence["_Gsuite"]]
    Okta: Optional[Sequence["_Okta"]]
    Saml: Optional[Sequence["_Saml"]]

    @classmethod
    def _deserialize(
        cls: Type["_Exclude"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Exclude"]:
        if not json_data:
            return None
        return cls(
            AnyValidServiceToken=json_data.get("AnyValidServiceToken"),
            Certificate=json_data.get("Certificate"),
            CommonName=json_data.get("CommonName"),
            Email=json_data.get("Email"),
            EmailDomain=json_data.get("EmailDomain"),
            Everyone=json_data.get("Everyone"),
            Group=json_data.get("Group"),
            Ip=json_data.get("Ip"),
            ServiceToken=json_data.get("ServiceToken"),
            Azure=json_data.get("Azure"),
            Github=json_data.get("Github"),
            Gsuite=json_data.get("Gsuite"),
            Okta=json_data.get("Okta"),
            Saml=json_data.get("Saml"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Exclude = Exclude


@dataclass
class Azure:
    Id: Optional[str]
    IdentityProviderId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Azure"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Azure"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            IdentityProviderId=json_data.get("IdentityProviderId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Azure = Azure


@dataclass
class Github:
    IdentityProviderId: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Github"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Github"]:
        if not json_data:
            return None
        return cls(
            IdentityProviderId=json_data.get("IdentityProviderId"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Github = Github


@dataclass
class Gsuite:
    Email: Optional[str]
    IdentityProviderId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Gsuite"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Gsuite"]:
        if not json_data:
            return None
        return cls(
            Email=json_data.get("Email"),
            IdentityProviderId=json_data.get("IdentityProviderId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Gsuite = Gsuite


@dataclass
class Okta:
    IdentityProviderId: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Okta"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Okta"]:
        if not json_data:
            return None
        return cls(
            IdentityProviderId=json_data.get("IdentityProviderId"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Okta = Okta


@dataclass
class Saml:
    AttributeName: Optional[str]
    AttributeValue: Optional[str]
    IdentityProviderId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Saml"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Saml"]:
        if not json_data:
            return None
        return cls(
            AttributeName=json_data.get("AttributeName"),
            AttributeValue=json_data.get("AttributeValue"),
            IdentityProviderId=json_data.get("IdentityProviderId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Saml = Saml


@dataclass
class Include:
    AnyValidServiceToken: Optional[bool]
    Certificate: Optional[bool]
    CommonName: Optional[str]
    Email: Optional[Sequence[str]]
    EmailDomain: Optional[Sequence[str]]
    Everyone: Optional[bool]
    Group: Optional[Sequence[str]]
    Ip: Optional[Sequence[str]]
    ServiceToken: Optional[Sequence[str]]
    Azure: Optional[Sequence["_Azure"]]
    Github: Optional[Sequence["_Github"]]
    Gsuite: Optional[Sequence["_Gsuite"]]
    Okta: Optional[Sequence["_Okta"]]
    Saml: Optional[Sequence["_Saml"]]

    @classmethod
    def _deserialize(
        cls: Type["_Include"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Include"]:
        if not json_data:
            return None
        return cls(
            AnyValidServiceToken=json_data.get("AnyValidServiceToken"),
            Certificate=json_data.get("Certificate"),
            CommonName=json_data.get("CommonName"),
            Email=json_data.get("Email"),
            EmailDomain=json_data.get("EmailDomain"),
            Everyone=json_data.get("Everyone"),
            Group=json_data.get("Group"),
            Ip=json_data.get("Ip"),
            ServiceToken=json_data.get("ServiceToken"),
            Azure=json_data.get("Azure"),
            Github=json_data.get("Github"),
            Gsuite=json_data.get("Gsuite"),
            Okta=json_data.get("Okta"),
            Saml=json_data.get("Saml"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Include = Include


@dataclass
class Require:
    AnyValidServiceToken: Optional[bool]
    Certificate: Optional[bool]
    CommonName: Optional[str]
    Email: Optional[Sequence[str]]
    EmailDomain: Optional[Sequence[str]]
    Everyone: Optional[bool]
    Group: Optional[Sequence[str]]
    Ip: Optional[Sequence[str]]
    ServiceToken: Optional[Sequence[str]]
    Azure: Optional[Sequence["_Azure"]]
    Github: Optional[Sequence["_Github"]]
    Gsuite: Optional[Sequence["_Gsuite"]]
    Okta: Optional[Sequence["_Okta"]]
    Saml: Optional[Sequence["_Saml"]]

    @classmethod
    def _deserialize(
        cls: Type["_Require"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Require"]:
        if not json_data:
            return None
        return cls(
            AnyValidServiceToken=json_data.get("AnyValidServiceToken"),
            Certificate=json_data.get("Certificate"),
            CommonName=json_data.get("CommonName"),
            Email=json_data.get("Email"),
            EmailDomain=json_data.get("EmailDomain"),
            Everyone=json_data.get("Everyone"),
            Group=json_data.get("Group"),
            Ip=json_data.get("Ip"),
            ServiceToken=json_data.get("ServiceToken"),
            Azure=json_data.get("Azure"),
            Github=json_data.get("Github"),
            Gsuite=json_data.get("Gsuite"),
            Okta=json_data.get("Okta"),
            Saml=json_data.get("Saml"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Require = Require



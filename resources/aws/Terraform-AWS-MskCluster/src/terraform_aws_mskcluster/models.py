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
    Arn: Optional[str]
    BootstrapBrokers: Optional[str]
    BootstrapBrokersTls: Optional[str]
    ClusterName: Optional[str]
    CurrentVersion: Optional[str]
    EnhancedMonitoring: Optional[str]
    Id: Optional[str]
    KafkaVersion: Optional[str]
    NumberOfBrokerNodes: Optional[float]
    Tags: Optional[Sequence["_Tags"]]
    ZookeeperConnectString: Optional[str]
    BrokerNodeGroupInfo: Optional[Sequence["_BrokerNodeGroupInfo"]]
    ClientAuthentication: Optional[Sequence["_ClientAuthentication"]]
    ConfigurationInfo: Optional[Sequence["_ConfigurationInfo"]]
    EncryptionInfo: Optional[Sequence["_EncryptionInfo"]]
    LoggingInfo: Optional[Sequence["_LoggingInfo"]]
    OpenMonitoring: Optional[Sequence["_OpenMonitoring"]]
    Tls: Optional[Sequence["_Tls"]]
    EncryptionInTransit: Optional[Sequence["_EncryptionInTransit"]]
    BrokerLogs: Optional[Sequence["_BrokerLogs"]]
    Prometheus: Optional[Sequence["_Prometheus"]]
    CloudwatchLogs: Optional[Sequence["_CloudwatchLogs"]]
    Firehose: Optional[Sequence["_Firehose"]]
    S3: Optional[Sequence["_S3"]]
    JmxExporter: Optional[Sequence["_JmxExporter"]]
    NodeExporter: Optional[Sequence["_NodeExporter"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            BootstrapBrokers=json_data.get("BootstrapBrokers"),
            BootstrapBrokersTls=json_data.get("BootstrapBrokersTls"),
            ClusterName=json_data.get("ClusterName"),
            CurrentVersion=json_data.get("CurrentVersion"),
            EnhancedMonitoring=json_data.get("EnhancedMonitoring"),
            Id=json_data.get("Id"),
            KafkaVersion=json_data.get("KafkaVersion"),
            NumberOfBrokerNodes=json_data.get("NumberOfBrokerNodes"),
            Tags=json_data.get("Tags"),
            ZookeeperConnectString=json_data.get("ZookeeperConnectString"),
            BrokerNodeGroupInfo=json_data.get("BrokerNodeGroupInfo"),
            ClientAuthentication=json_data.get("ClientAuthentication"),
            ConfigurationInfo=json_data.get("ConfigurationInfo"),
            EncryptionInfo=json_data.get("EncryptionInfo"),
            LoggingInfo=json_data.get("LoggingInfo"),
            OpenMonitoring=json_data.get("OpenMonitoring"),
            Tls=json_data.get("Tls"),
            EncryptionInTransit=json_data.get("EncryptionInTransit"),
            BrokerLogs=json_data.get("BrokerLogs"),
            Prometheus=json_data.get("Prometheus"),
            CloudwatchLogs=json_data.get("CloudwatchLogs"),
            Firehose=json_data.get("Firehose"),
            S3=json_data.get("S3"),
            JmxExporter=json_data.get("JmxExporter"),
            NodeExporter=json_data.get("NodeExporter"),
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
class BrokerNodeGroupInfo:
    AzDistribution: Optional[str]
    ClientSubnets: Optional[Sequence[str]]
    EbsVolumeSize: Optional[float]
    InstanceType: Optional[str]
    SecurityGroups: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_BrokerNodeGroupInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BrokerNodeGroupInfo"]:
        if not json_data:
            return None
        return cls(
            AzDistribution=json_data.get("AzDistribution"),
            ClientSubnets=json_data.get("ClientSubnets"),
            EbsVolumeSize=json_data.get("EbsVolumeSize"),
            InstanceType=json_data.get("InstanceType"),
            SecurityGroups=json_data.get("SecurityGroups"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BrokerNodeGroupInfo = BrokerNodeGroupInfo


@dataclass
class ClientAuthentication:
    Tls: Optional[Sequence["_Tls"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientAuthentication"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientAuthentication"]:
        if not json_data:
            return None
        return cls(
            Tls=json_data.get("Tls"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientAuthentication = ClientAuthentication


@dataclass
class Tls:
    CertificateAuthorityArns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Tls"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tls"]:
        if not json_data:
            return None
        return cls(
            CertificateAuthorityArns=json_data.get("CertificateAuthorityArns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tls = Tls


@dataclass
class ConfigurationInfo:
    Arn: Optional[str]
    Revision: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationInfo"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
            Revision=json_data.get("Revision"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigurationInfo = ConfigurationInfo


@dataclass
class EncryptionInfo:
    EncryptionAtRestKmsKeyArn: Optional[str]
    EncryptionInTransit: Optional[Sequence["_EncryptionInTransit"]]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionInfo"]:
        if not json_data:
            return None
        return cls(
            EncryptionAtRestKmsKeyArn=json_data.get("EncryptionAtRestKmsKeyArn"),
            EncryptionInTransit=json_data.get("EncryptionInTransit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionInfo = EncryptionInfo


@dataclass
class EncryptionInTransit:
    ClientBroker: Optional[str]
    InCluster: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionInTransit"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionInTransit"]:
        if not json_data:
            return None
        return cls(
            ClientBroker=json_data.get("ClientBroker"),
            InCluster=json_data.get("InCluster"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionInTransit = EncryptionInTransit


@dataclass
class LoggingInfo:
    BrokerLogs: Optional[Sequence["_BrokerLogs"]]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingInfo"]:
        if not json_data:
            return None
        return cls(
            BrokerLogs=json_data.get("BrokerLogs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingInfo = LoggingInfo


@dataclass
class BrokerLogs:
    CloudwatchLogs: Optional[Sequence["_CloudwatchLogs"]]
    Firehose: Optional[Sequence["_Firehose"]]
    S3: Optional[Sequence["_S3"]]

    @classmethod
    def _deserialize(
        cls: Type["_BrokerLogs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BrokerLogs"]:
        if not json_data:
            return None
        return cls(
            CloudwatchLogs=json_data.get("CloudwatchLogs"),
            Firehose=json_data.get("Firehose"),
            S3=json_data.get("S3"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BrokerLogs = BrokerLogs


@dataclass
class CloudwatchLogs:
    Enabled: Optional[bool]
    LogGroup: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudwatchLogs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudwatchLogs"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            LogGroup=json_data.get("LogGroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudwatchLogs = CloudwatchLogs


@dataclass
class Firehose:
    DeliveryStream: Optional[str]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Firehose"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Firehose"]:
        if not json_data:
            return None
        return cls(
            DeliveryStream=json_data.get("DeliveryStream"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Firehose = Firehose


@dataclass
class S3:
    Bucket: Optional[str]
    Enabled: Optional[bool]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            Enabled=json_data.get("Enabled"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3 = S3


@dataclass
class OpenMonitoring:
    Prometheus: Optional[Sequence["_Prometheus"]]

    @classmethod
    def _deserialize(
        cls: Type["_OpenMonitoring"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpenMonitoring"]:
        if not json_data:
            return None
        return cls(
            Prometheus=json_data.get("Prometheus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OpenMonitoring = OpenMonitoring


@dataclass
class Prometheus:
    JmxExporter: Optional[Sequence["_JmxExporter"]]
    NodeExporter: Optional[Sequence["_NodeExporter"]]

    @classmethod
    def _deserialize(
        cls: Type["_Prometheus"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Prometheus"]:
        if not json_data:
            return None
        return cls(
            JmxExporter=json_data.get("JmxExporter"),
            NodeExporter=json_data.get("NodeExporter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Prometheus = Prometheus


@dataclass
class JmxExporter:
    EnabledInBroker: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_JmxExporter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JmxExporter"]:
        if not json_data:
            return None
        return cls(
            EnabledInBroker=json_data.get("EnabledInBroker"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JmxExporter = JmxExporter


@dataclass
class NodeExporter:
    EnabledInBroker: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_NodeExporter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeExporter"]:
        if not json_data:
            return None
        return cls(
            EnabledInBroker=json_data.get("EnabledInBroker"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeExporter = NodeExporter



# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'KubernetesClusterInstalledApplication',
    'KubernetesClusterPools',
    'GetDiskImageDiskimageResult',
    'GetDiskImageFilterResult',
    'GetDiskImageSortResult',
    'GetInstancesFilterResult',
    'GetInstancesInstanceResult',
    'GetInstancesSizeFilterResult',
    'GetInstancesSizeSizeResult',
    'GetInstancesSizeSortResult',
    'GetInstancesSortResult',
    'GetKubernetesClusterInstalledApplicationResult',
    'GetKubernetesClusterPoolResult',
    'GetKubernetesVersionFilterResult',
    'GetKubernetesVersionSortResult',
    'GetKubernetesVersionVersionResult',
    'GetLoadBalancerBackendResult',
    'GetRegionFilterResult',
    'GetRegionRegionResult',
    'GetRegionSortResult',
    'GetSizeFilterResult',
    'GetSizeSizeResult',
    'GetSizeSortResult',
]

@pulumi.output_type
class KubernetesClusterInstalledApplication(dict):
    def __init__(__self__, *,
                 application: Optional[str] = None,
                 category: Optional[str] = None,
                 installed: Optional[bool] = None,
                 version: Optional[str] = None):
        if application is not None:
            pulumi.set(__self__, "application", application)
        if category is not None:
            pulumi.set(__self__, "category", category)
        if installed is not None:
            pulumi.set(__self__, "installed", installed)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def application(self) -> Optional[str]:
        return pulumi.get(self, "application")

    @property
    @pulumi.getter
    def category(self) -> Optional[str]:
        return pulumi.get(self, "category")

    @property
    @pulumi.getter
    def installed(self) -> Optional[bool]:
        return pulumi.get(self, "installed")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        return pulumi.get(self, "version")


@pulumi.output_type
class KubernetesClusterPools(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "nodeCount":
            suggest = "node_count"
        elif key == "instanceNames":
            suggest = "instance_names"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in KubernetesClusterPools. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        KubernetesClusterPools.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        KubernetesClusterPools.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 node_count: int,
                 size: str,
                 instance_names: Optional[Sequence[str]] = None,
                 label: Optional[str] = None):
        pulumi.set(__self__, "node_count", node_count)
        pulumi.set(__self__, "size", size)
        if instance_names is not None:
            pulumi.set(__self__, "instance_names", instance_names)
        if label is not None:
            pulumi.set(__self__, "label", label)

    @property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> int:
        return pulumi.get(self, "node_count")

    @property
    @pulumi.getter
    def size(self) -> str:
        return pulumi.get(self, "size")

    @property
    @pulumi.getter(name="instanceNames")
    def instance_names(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "instance_names")

    @property
    @pulumi.getter
    def label(self) -> Optional[str]:
        return pulumi.get(self, "label")


@pulumi.output_type
class GetDiskImageDiskimageResult(dict):
    def __init__(__self__, *,
                 id: str,
                 label: str,
                 name: str,
                 version: str):
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "label", label)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def label(self) -> str:
        return pulumi.get(self, "label")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def version(self) -> str:
        return pulumi.get(self, "version")


@pulumi.output_type
class GetDiskImageFilterResult(dict):
    def __init__(__self__, *,
                 key: str,
                 values: Sequence[str],
                 all: Optional[bool] = None,
                 match_by: Optional[str] = None):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "values", values)
        if all is not None:
            pulumi.set(__self__, "all", all)
        if match_by is not None:
            pulumi.set(__self__, "match_by", match_by)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @property
    @pulumi.getter
    def all(self) -> Optional[bool]:
        return pulumi.get(self, "all")

    @property
    @pulumi.getter(name="matchBy")
    def match_by(self) -> Optional[str]:
        return pulumi.get(self, "match_by")


@pulumi.output_type
class GetDiskImageSortResult(dict):
    def __init__(__self__, *,
                 key: str,
                 direction: Optional[str] = None):
        pulumi.set(__self__, "key", key)
        if direction is not None:
            pulumi.set(__self__, "direction", direction)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def direction(self) -> Optional[str]:
        return pulumi.get(self, "direction")


@pulumi.output_type
class GetInstancesFilterResult(dict):
    def __init__(__self__, *,
                 key: str,
                 values: Sequence[str],
                 all: Optional[bool] = None,
                 match_by: Optional[str] = None):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "values", values)
        if all is not None:
            pulumi.set(__self__, "all", all)
        if match_by is not None:
            pulumi.set(__self__, "match_by", match_by)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @property
    @pulumi.getter
    def all(self) -> Optional[bool]:
        return pulumi.get(self, "all")

    @property
    @pulumi.getter(name="matchBy")
    def match_by(self) -> Optional[str]:
        return pulumi.get(self, "match_by")


@pulumi.output_type
class GetInstancesInstanceResult(dict):
    def __init__(__self__, *,
                 cpu_cores: int,
                 created_at: str,
                 disk_gb: int,
                 firewall_id: str,
                 hostname: str,
                 id: str,
                 initial_password: str,
                 initial_user: str,
                 network_id: str,
                 notes: str,
                 private_ip: str,
                 pseudo_ip: str,
                 public_ip: str,
                 ram_mb: int,
                 region: str,
                 reverse_dns: str,
                 script: str,
                 size: str,
                 sshkey_id: str,
                 status: str,
                 tags: Sequence[str],
                 template: str):
        pulumi.set(__self__, "cpu_cores", cpu_cores)
        pulumi.set(__self__, "created_at", created_at)
        pulumi.set(__self__, "disk_gb", disk_gb)
        pulumi.set(__self__, "firewall_id", firewall_id)
        pulumi.set(__self__, "hostname", hostname)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "initial_password", initial_password)
        pulumi.set(__self__, "initial_user", initial_user)
        pulumi.set(__self__, "network_id", network_id)
        pulumi.set(__self__, "notes", notes)
        pulumi.set(__self__, "private_ip", private_ip)
        pulumi.set(__self__, "pseudo_ip", pseudo_ip)
        pulumi.set(__self__, "public_ip", public_ip)
        pulumi.set(__self__, "ram_mb", ram_mb)
        pulumi.set(__self__, "region", region)
        pulumi.set(__self__, "reverse_dns", reverse_dns)
        pulumi.set(__self__, "script", script)
        pulumi.set(__self__, "size", size)
        pulumi.set(__self__, "sshkey_id", sshkey_id)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "tags", tags)
        pulumi.set(__self__, "template", template)

    @property
    @pulumi.getter(name="cpuCores")
    def cpu_cores(self) -> int:
        return pulumi.get(self, "cpu_cores")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="diskGb")
    def disk_gb(self) -> int:
        return pulumi.get(self, "disk_gb")

    @property
    @pulumi.getter(name="firewallId")
    def firewall_id(self) -> str:
        return pulumi.get(self, "firewall_id")

    @property
    @pulumi.getter
    def hostname(self) -> str:
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="initialPassword")
    def initial_password(self) -> str:
        return pulumi.get(self, "initial_password")

    @property
    @pulumi.getter(name="initialUser")
    def initial_user(self) -> str:
        return pulumi.get(self, "initial_user")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> str:
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter
    def notes(self) -> str:
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> str:
        return pulumi.get(self, "private_ip")

    @property
    @pulumi.getter(name="pseudoIp")
    def pseudo_ip(self) -> str:
        return pulumi.get(self, "pseudo_ip")

    @property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> str:
        return pulumi.get(self, "public_ip")

    @property
    @pulumi.getter(name="ramMb")
    def ram_mb(self) -> int:
        return pulumi.get(self, "ram_mb")

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="reverseDns")
    def reverse_dns(self) -> str:
        return pulumi.get(self, "reverse_dns")

    @property
    @pulumi.getter
    def script(self) -> str:
        return pulumi.get(self, "script")

    @property
    @pulumi.getter
    def size(self) -> str:
        return pulumi.get(self, "size")

    @property
    @pulumi.getter(name="sshkeyId")
    def sshkey_id(self) -> str:
        return pulumi.get(self, "sshkey_id")

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Sequence[str]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def template(self) -> str:
        return pulumi.get(self, "template")


@pulumi.output_type
class GetInstancesSizeFilterResult(dict):
    def __init__(__self__, *,
                 key: str,
                 values: Sequence[str],
                 all: Optional[bool] = None,
                 match_by: Optional[str] = None):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "values", values)
        if all is not None:
            pulumi.set(__self__, "all", all)
        if match_by is not None:
            pulumi.set(__self__, "match_by", match_by)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @property
    @pulumi.getter
    def all(self) -> Optional[bool]:
        return pulumi.get(self, "all")

    @property
    @pulumi.getter(name="matchBy")
    def match_by(self) -> Optional[str]:
        return pulumi.get(self, "match_by")


@pulumi.output_type
class GetInstancesSizeSizeResult(dict):
    def __init__(__self__, *,
                 cpu: int,
                 description: str,
                 disk: int,
                 name: str,
                 ram: int,
                 selectable: bool,
                 type: str):
        pulumi.set(__self__, "cpu", cpu)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "disk", disk)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "ram", ram)
        pulumi.set(__self__, "selectable", selectable)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def cpu(self) -> int:
        return pulumi.get(self, "cpu")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def disk(self) -> int:
        return pulumi.get(self, "disk")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def ram(self) -> int:
        return pulumi.get(self, "ram")

    @property
    @pulumi.getter
    def selectable(self) -> bool:
        return pulumi.get(self, "selectable")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")


@pulumi.output_type
class GetInstancesSizeSortResult(dict):
    def __init__(__self__, *,
                 key: str,
                 direction: Optional[str] = None):
        pulumi.set(__self__, "key", key)
        if direction is not None:
            pulumi.set(__self__, "direction", direction)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def direction(self) -> Optional[str]:
        return pulumi.get(self, "direction")


@pulumi.output_type
class GetInstancesSortResult(dict):
    def __init__(__self__, *,
                 key: str,
                 direction: Optional[str] = None):
        pulumi.set(__self__, "key", key)
        if direction is not None:
            pulumi.set(__self__, "direction", direction)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def direction(self) -> Optional[str]:
        return pulumi.get(self, "direction")


@pulumi.output_type
class GetKubernetesClusterInstalledApplicationResult(dict):
    def __init__(__self__, *,
                 application: str,
                 category: str,
                 installed: bool,
                 version: str):
        pulumi.set(__self__, "application", application)
        pulumi.set(__self__, "category", category)
        pulumi.set(__self__, "installed", installed)
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def application(self) -> str:
        return pulumi.get(self, "application")

    @property
    @pulumi.getter
    def category(self) -> str:
        return pulumi.get(self, "category")

    @property
    @pulumi.getter
    def installed(self) -> bool:
        return pulumi.get(self, "installed")

    @property
    @pulumi.getter
    def version(self) -> str:
        return pulumi.get(self, "version")


@pulumi.output_type
class GetKubernetesClusterPoolResult(dict):
    def __init__(__self__, *,
                 instance_names: Sequence[str],
                 label: str,
                 node_count: int,
                 size: str):
        pulumi.set(__self__, "instance_names", instance_names)
        pulumi.set(__self__, "label", label)
        pulumi.set(__self__, "node_count", node_count)
        pulumi.set(__self__, "size", size)

    @property
    @pulumi.getter(name="instanceNames")
    def instance_names(self) -> Sequence[str]:
        return pulumi.get(self, "instance_names")

    @property
    @pulumi.getter
    def label(self) -> str:
        return pulumi.get(self, "label")

    @property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> int:
        return pulumi.get(self, "node_count")

    @property
    @pulumi.getter
    def size(self) -> str:
        return pulumi.get(self, "size")


@pulumi.output_type
class GetKubernetesVersionFilterResult(dict):
    def __init__(__self__, *,
                 key: str,
                 values: Sequence[str],
                 all: Optional[bool] = None,
                 match_by: Optional[str] = None):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "values", values)
        if all is not None:
            pulumi.set(__self__, "all", all)
        if match_by is not None:
            pulumi.set(__self__, "match_by", match_by)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @property
    @pulumi.getter
    def all(self) -> Optional[bool]:
        return pulumi.get(self, "all")

    @property
    @pulumi.getter(name="matchBy")
    def match_by(self) -> Optional[str]:
        return pulumi.get(self, "match_by")


@pulumi.output_type
class GetKubernetesVersionSortResult(dict):
    def __init__(__self__, *,
                 key: str,
                 direction: Optional[str] = None):
        pulumi.set(__self__, "key", key)
        if direction is not None:
            pulumi.set(__self__, "direction", direction)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def direction(self) -> Optional[str]:
        return pulumi.get(self, "direction")


@pulumi.output_type
class GetKubernetesVersionVersionResult(dict):
    def __init__(__self__, *,
                 default: bool,
                 label: str,
                 type: str,
                 version: str):
        pulumi.set(__self__, "default", default)
        pulumi.set(__self__, "label", label)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def default(self) -> bool:
        return pulumi.get(self, "default")

    @property
    @pulumi.getter
    def label(self) -> str:
        return pulumi.get(self, "label")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> str:
        return pulumi.get(self, "version")


@pulumi.output_type
class GetLoadBalancerBackendResult(dict):
    def __init__(__self__, *,
                 health_check_port: int,
                 ip: str,
                 protocol: str,
                 source_port: int,
                 target_port: int):
        pulumi.set(__self__, "health_check_port", health_check_port)
        pulumi.set(__self__, "ip", ip)
        pulumi.set(__self__, "protocol", protocol)
        pulumi.set(__self__, "source_port", source_port)
        pulumi.set(__self__, "target_port", target_port)

    @property
    @pulumi.getter(name="healthCheckPort")
    def health_check_port(self) -> int:
        return pulumi.get(self, "health_check_port")

    @property
    @pulumi.getter
    def ip(self) -> str:
        return pulumi.get(self, "ip")

    @property
    @pulumi.getter
    def protocol(self) -> str:
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="sourcePort")
    def source_port(self) -> int:
        return pulumi.get(self, "source_port")

    @property
    @pulumi.getter(name="targetPort")
    def target_port(self) -> int:
        return pulumi.get(self, "target_port")


@pulumi.output_type
class GetRegionFilterResult(dict):
    def __init__(__self__, *,
                 key: str,
                 values: Sequence[str],
                 all: Optional[bool] = None,
                 match_by: Optional[str] = None):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "values", values)
        if all is not None:
            pulumi.set(__self__, "all", all)
        if match_by is not None:
            pulumi.set(__self__, "match_by", match_by)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @property
    @pulumi.getter
    def all(self) -> Optional[bool]:
        return pulumi.get(self, "all")

    @property
    @pulumi.getter(name="matchBy")
    def match_by(self) -> Optional[str]:
        return pulumi.get(self, "match_by")


@pulumi.output_type
class GetRegionRegionResult(dict):
    def __init__(__self__, *,
                 code: str,
                 country: str,
                 default: bool,
                 name: str):
        pulumi.set(__self__, "code", code)
        pulumi.set(__self__, "country", country)
        pulumi.set(__self__, "default", default)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def code(self) -> str:
        return pulumi.get(self, "code")

    @property
    @pulumi.getter
    def country(self) -> str:
        return pulumi.get(self, "country")

    @property
    @pulumi.getter
    def default(self) -> bool:
        return pulumi.get(self, "default")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")


@pulumi.output_type
class GetRegionSortResult(dict):
    def __init__(__self__, *,
                 key: str,
                 direction: Optional[str] = None):
        pulumi.set(__self__, "key", key)
        if direction is not None:
            pulumi.set(__self__, "direction", direction)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def direction(self) -> Optional[str]:
        return pulumi.get(self, "direction")


@pulumi.output_type
class GetSizeFilterResult(dict):
    def __init__(__self__, *,
                 key: str,
                 values: Sequence[str],
                 all: Optional[bool] = None,
                 match_by: Optional[str] = None):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "values", values)
        if all is not None:
            pulumi.set(__self__, "all", all)
        if match_by is not None:
            pulumi.set(__self__, "match_by", match_by)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @property
    @pulumi.getter
    def all(self) -> Optional[bool]:
        return pulumi.get(self, "all")

    @property
    @pulumi.getter(name="matchBy")
    def match_by(self) -> Optional[str]:
        return pulumi.get(self, "match_by")


@pulumi.output_type
class GetSizeSizeResult(dict):
    def __init__(__self__, *,
                 cpu: int,
                 description: str,
                 disk: int,
                 name: str,
                 ram: int,
                 selectable: bool,
                 type: str):
        pulumi.set(__self__, "cpu", cpu)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "disk", disk)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "ram", ram)
        pulumi.set(__self__, "selectable", selectable)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def cpu(self) -> int:
        return pulumi.get(self, "cpu")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def disk(self) -> int:
        return pulumi.get(self, "disk")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def ram(self) -> int:
        return pulumi.get(self, "ram")

    @property
    @pulumi.getter
    def selectable(self) -> bool:
        return pulumi.get(self, "selectable")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")


@pulumi.output_type
class GetSizeSortResult(dict):
    def __init__(__self__, *,
                 key: str,
                 direction: Optional[str] = None):
        pulumi.set(__self__, "key", key)
        if direction is not None:
            pulumi.set(__self__, "direction", direction)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def direction(self) -> Optional[str]:
        return pulumi.get(self, "direction")



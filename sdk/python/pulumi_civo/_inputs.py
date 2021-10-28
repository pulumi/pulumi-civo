# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'KubernetesClusterInstalledApplicationArgs',
    'KubernetesClusterInstanceArgs',
    'KubernetesClusterPoolArgs',
    'KubernetesClusterPoolInstanceArgs',
    'GetDiskImageFilterArgs',
    'GetDiskImageSortArgs',
    'GetInstancesFilterArgs',
    'GetInstancesSizeFilterArgs',
    'GetInstancesSizeSortArgs',
    'GetInstancesSortArgs',
    'GetKubernetesVersionFilterArgs',
    'GetKubernetesVersionSortArgs',
    'GetRegionFilterArgs',
    'GetRegionSortArgs',
    'GetTemplateFilterArgs',
    'GetTemplateSortArgs',
]

@pulumi.input_type
class KubernetesClusterInstalledApplicationArgs:
    def __init__(__self__, *,
                 application: Optional[pulumi.Input[str]] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 installed: Optional[pulumi.Input[bool]] = None,
                 version: Optional[pulumi.Input[str]] = None):
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
    def application(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "application")

    @application.setter
    def application(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application", value)

    @property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "category", value)

    @property
    @pulumi.getter
    def installed(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "installed")

    @installed.setter
    def installed(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "installed", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


@pulumi.input_type
class KubernetesClusterInstanceArgs:
    def __init__(__self__, *,
                 cpu_cores: Optional[pulumi.Input[int]] = None,
                 disk_gb: Optional[pulumi.Input[int]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 ram_mb: Optional[pulumi.Input[int]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        if cpu_cores is not None:
            pulumi.set(__self__, "cpu_cores", cpu_cores)
        if disk_gb is not None:
            pulumi.set(__self__, "disk_gb", disk_gb)
        if hostname is not None:
            pulumi.set(__self__, "hostname", hostname)
        if ram_mb is not None:
            pulumi.set(__self__, "ram_mb", ram_mb)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="cpuCores")
    def cpu_cores(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "cpu_cores")

    @cpu_cores.setter
    def cpu_cores(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cpu_cores", value)

    @property
    @pulumi.getter(name="diskGb")
    def disk_gb(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "disk_gb")

    @disk_gb.setter
    def disk_gb(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "disk_gb", value)

    @property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter(name="ramMb")
    def ram_mb(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "ram_mb")

    @ram_mb.setter
    def ram_mb(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ram_mb", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class KubernetesClusterPoolArgs:
    def __init__(__self__, *,
                 count: Optional[pulumi.Input[int]] = None,
                 instance_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 instances: Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesClusterPoolInstanceArgs']]]] = None,
                 size: Optional[pulumi.Input[str]] = None):
        if count is not None:
            pulumi.set(__self__, "count", count)
        if instance_names is not None:
            pulumi.set(__self__, "instance_names", instance_names)
        if instances is not None:
            pulumi.set(__self__, "instances", instances)
        if size is not None:
            pulumi.set(__self__, "size", size)

    @property
    @pulumi.getter
    def count(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "count")

    @count.setter
    def count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "count", value)

    @property
    @pulumi.getter(name="instanceNames")
    def instance_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "instance_names")

    @instance_names.setter
    def instance_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "instance_names", value)

    @property
    @pulumi.getter
    def instances(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesClusterPoolInstanceArgs']]]]:
        return pulumi.get(self, "instances")

    @instances.setter
    def instances(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesClusterPoolInstanceArgs']]]]):
        pulumi.set(self, "instances", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "size", value)


@pulumi.input_type
class KubernetesClusterPoolInstanceArgs:
    def __init__(__self__, *,
                 cpu_cores: Optional[pulumi.Input[int]] = None,
                 disk_gb: Optional[pulumi.Input[int]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 ram_mb: Optional[pulumi.Input[int]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        if cpu_cores is not None:
            pulumi.set(__self__, "cpu_cores", cpu_cores)
        if disk_gb is not None:
            pulumi.set(__self__, "disk_gb", disk_gb)
        if hostname is not None:
            pulumi.set(__self__, "hostname", hostname)
        if ram_mb is not None:
            pulumi.set(__self__, "ram_mb", ram_mb)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="cpuCores")
    def cpu_cores(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "cpu_cores")

    @cpu_cores.setter
    def cpu_cores(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cpu_cores", value)

    @property
    @pulumi.getter(name="diskGb")
    def disk_gb(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "disk_gb")

    @disk_gb.setter
    def disk_gb(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "disk_gb", value)

    @property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter(name="ramMb")
    def ram_mb(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "ram_mb")

    @ram_mb.setter
    def ram_mb(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ram_mb", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class GetDiskImageFilterArgs:
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

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def all(self) -> Optional[bool]:
        return pulumi.get(self, "all")

    @all.setter
    def all(self, value: Optional[bool]):
        pulumi.set(self, "all", value)

    @property
    @pulumi.getter(name="matchBy")
    def match_by(self) -> Optional[str]:
        return pulumi.get(self, "match_by")

    @match_by.setter
    def match_by(self, value: Optional[str]):
        pulumi.set(self, "match_by", value)


@pulumi.input_type
class GetDiskImageSortArgs:
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

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def direction(self) -> Optional[str]:
        return pulumi.get(self, "direction")

    @direction.setter
    def direction(self, value: Optional[str]):
        pulumi.set(self, "direction", value)


@pulumi.input_type
class GetInstancesFilterArgs:
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

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def all(self) -> Optional[bool]:
        return pulumi.get(self, "all")

    @all.setter
    def all(self, value: Optional[bool]):
        pulumi.set(self, "all", value)

    @property
    @pulumi.getter(name="matchBy")
    def match_by(self) -> Optional[str]:
        return pulumi.get(self, "match_by")

    @match_by.setter
    def match_by(self, value: Optional[str]):
        pulumi.set(self, "match_by", value)


@pulumi.input_type
class GetInstancesSizeFilterArgs:
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

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def all(self) -> Optional[bool]:
        return pulumi.get(self, "all")

    @all.setter
    def all(self, value: Optional[bool]):
        pulumi.set(self, "all", value)

    @property
    @pulumi.getter(name="matchBy")
    def match_by(self) -> Optional[str]:
        return pulumi.get(self, "match_by")

    @match_by.setter
    def match_by(self, value: Optional[str]):
        pulumi.set(self, "match_by", value)


@pulumi.input_type
class GetInstancesSizeSortArgs:
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

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def direction(self) -> Optional[str]:
        return pulumi.get(self, "direction")

    @direction.setter
    def direction(self, value: Optional[str]):
        pulumi.set(self, "direction", value)


@pulumi.input_type
class GetInstancesSortArgs:
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

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def direction(self) -> Optional[str]:
        return pulumi.get(self, "direction")

    @direction.setter
    def direction(self, value: Optional[str]):
        pulumi.set(self, "direction", value)


@pulumi.input_type
class GetKubernetesVersionFilterArgs:
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

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def all(self) -> Optional[bool]:
        return pulumi.get(self, "all")

    @all.setter
    def all(self, value: Optional[bool]):
        pulumi.set(self, "all", value)

    @property
    @pulumi.getter(name="matchBy")
    def match_by(self) -> Optional[str]:
        return pulumi.get(self, "match_by")

    @match_by.setter
    def match_by(self, value: Optional[str]):
        pulumi.set(self, "match_by", value)


@pulumi.input_type
class GetKubernetesVersionSortArgs:
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

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def direction(self) -> Optional[str]:
        return pulumi.get(self, "direction")

    @direction.setter
    def direction(self, value: Optional[str]):
        pulumi.set(self, "direction", value)


@pulumi.input_type
class GetRegionFilterArgs:
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

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def all(self) -> Optional[bool]:
        return pulumi.get(self, "all")

    @all.setter
    def all(self, value: Optional[bool]):
        pulumi.set(self, "all", value)

    @property
    @pulumi.getter(name="matchBy")
    def match_by(self) -> Optional[str]:
        return pulumi.get(self, "match_by")

    @match_by.setter
    def match_by(self, value: Optional[str]):
        pulumi.set(self, "match_by", value)


@pulumi.input_type
class GetRegionSortArgs:
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

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def direction(self) -> Optional[str]:
        return pulumi.get(self, "direction")

    @direction.setter
    def direction(self, value: Optional[str]):
        pulumi.set(self, "direction", value)


@pulumi.input_type
class GetTemplateFilterArgs:
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

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def all(self) -> Optional[bool]:
        return pulumi.get(self, "all")

    @all.setter
    def all(self, value: Optional[bool]):
        pulumi.set(self, "all", value)

    @property
    @pulumi.getter(name="matchBy")
    def match_by(self) -> Optional[str]:
        return pulumi.get(self, "match_by")

    @match_by.setter
    def match_by(self, value: Optional[str]):
        pulumi.set(self, "match_by", value)


@pulumi.input_type
class GetTemplateSortArgs:
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

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def direction(self) -> Optional[str]:
        return pulumi.get(self, "direction")

    @direction.setter
    def direction(self, value: Optional[str]):
        pulumi.set(self, "direction", value)



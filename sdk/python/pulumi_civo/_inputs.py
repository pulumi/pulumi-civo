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
    'FirewallEgressRuleArgs',
    'FirewallIngressRuleArgs',
    'KubernetesClusterInstalledApplicationArgs',
    'KubernetesClusterPoolsArgs',
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
    'GetSizeFilterArgs',
    'GetSizeSortArgs',
]

@pulumi.input_type
class FirewallEgressRuleArgs:
    def __init__(__self__, *,
                 action: pulumi.Input[str],
                 cidrs: pulumi.Input[Sequence[pulumi.Input[str]]],
                 id: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 port_range: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] action: The action of the rule can be allow or deny. When we set the `action = 'allow'`, this is going to add a rule to allow traffic. Similarly, setting `action = 'deny'` will deny the traffic.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] cidrs: The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32 to open just for a specific IP address)
        :param pulumi.Input[str] id: The ID of this resource.
        :param pulumi.Input[str] label: A string that will be the displayed name/reference for this rule
        :param pulumi.Input[str] port_range: The port or port range to open, can be a single port or a range separated by a dash (`-`), e.g. `80` or `80-443`
        :param pulumi.Input[str] protocol: The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "cidrs", cidrs)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if port_range is not None:
            pulumi.set(__self__, "port_range", port_range)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Input[str]:
        """
        The action of the rule can be allow or deny. When we set the `action = 'allow'`, this is going to add a rule to allow traffic. Similarly, setting `action = 'deny'` will deny the traffic.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: pulumi.Input[str]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter
    def cidrs(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32 to open just for a specific IP address)
        """
        return pulumi.get(self, "cidrs")

    @cidrs.setter
    def cidrs(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "cidrs", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        """
        A string that will be the displayed name/reference for this rule
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter(name="portRange")
    def port_range(self) -> Optional[pulumi.Input[str]]:
        """
        The port or port range to open, can be a single port or a range separated by a dash (`-`), e.g. `80` or `80-443`
        """
        return pulumi.get(self, "port_range")

    @port_range.setter
    def port_range(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "port_range", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[str]]:
        """
        The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol", value)


@pulumi.input_type
class FirewallIngressRuleArgs:
    def __init__(__self__, *,
                 action: pulumi.Input[str],
                 cidrs: pulumi.Input[Sequence[pulumi.Input[str]]],
                 id: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 port_range: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] action: The action of the rule can be allow or deny. When we set the `action = 'allow'`, this is going to add a rule to allow traffic. Similarly, setting `action = 'deny'` will deny the traffic.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] cidrs: The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32 to open just for a specific IP address)
        :param pulumi.Input[str] id: The ID of this resource.
        :param pulumi.Input[str] label: A string that will be the displayed name/reference for this rule
        :param pulumi.Input[str] port_range: The port or port range to open, can be a single port or a range separated by a dash (`-`), e.g. `80` or `80-443`
        :param pulumi.Input[str] protocol: The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "cidrs", cidrs)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if port_range is not None:
            pulumi.set(__self__, "port_range", port_range)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Input[str]:
        """
        The action of the rule can be allow or deny. When we set the `action = 'allow'`, this is going to add a rule to allow traffic. Similarly, setting `action = 'deny'` will deny the traffic.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: pulumi.Input[str]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter
    def cidrs(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32 to open just for a specific IP address)
        """
        return pulumi.get(self, "cidrs")

    @cidrs.setter
    def cidrs(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "cidrs", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        """
        A string that will be the displayed name/reference for this rule
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter(name="portRange")
    def port_range(self) -> Optional[pulumi.Input[str]]:
        """
        The port or port range to open, can be a single port or a range separated by a dash (`-`), e.g. `80` or `80-443`
        """
        return pulumi.get(self, "port_range")

    @port_range.setter
    def port_range(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "port_range", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[str]]:
        """
        The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol", value)


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
class KubernetesClusterPoolsArgs:
    def __init__(__self__, *,
                 node_count: pulumi.Input[int],
                 size: pulumi.Input[str],
                 instance_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 label: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[int] node_count: Number of nodes in the nodepool
        :param pulumi.Input[str] size: Size of the nodes in the nodepool
        :param pulumi.Input[Sequence[pulumi.Input[str]]] instance_names: Instance names in the nodepool
        :param pulumi.Input[str] label: Node pool label, if you don't provide one, we will generate one for you
        """
        pulumi.set(__self__, "node_count", node_count)
        pulumi.set(__self__, "size", size)
        if instance_names is not None:
            pulumi.set(__self__, "instance_names", instance_names)
        if label is not None:
            pulumi.set(__self__, "label", label)

    @property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> pulumi.Input[int]:
        """
        Number of nodes in the nodepool
        """
        return pulumi.get(self, "node_count")

    @node_count.setter
    def node_count(self, value: pulumi.Input[int]):
        pulumi.set(self, "node_count", value)

    @property
    @pulumi.getter
    def size(self) -> pulumi.Input[str]:
        """
        Size of the nodes in the nodepool
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: pulumi.Input[str]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter(name="instanceNames")
    def instance_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Instance names in the nodepool
        """
        return pulumi.get(self, "instance_names")

    @instance_names.setter
    def instance_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "instance_names", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        """
        Node pool label, if you don't provide one, we will generate one for you
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)


@pulumi.input_type
class GetDiskImageFilterArgs:
    def __init__(__self__, *,
                 key: str,
                 values: Sequence[str],
                 all: Optional[bool] = None,
                 match_by: Optional[str] = None):
        """
        :param str key: Filter diskimages by this key. This may be one of `id`, `label`, `name`, `version`.
        :param Sequence[str] values: Only retrieves `diskimages` which keys has value that matches one of the values provided here
        :param bool all: Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
        :param str match_by: One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "values", values)
        if all is not None:
            pulumi.set(__self__, "all", all)
        if match_by is not None:
            pulumi.set(__self__, "match_by", match_by)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Filter diskimages by this key. This may be one of `id`, `label`, `name`, `version`.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        """
        Only retrieves `diskimages` which keys has value that matches one of the values provided here
        """
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def all(self) -> Optional[bool]:
        """
        Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
        """
        return pulumi.get(self, "all")

    @all.setter
    def all(self, value: Optional[bool]):
        pulumi.set(self, "all", value)

    @property
    @pulumi.getter(name="matchBy")
    def match_by(self) -> Optional[str]:
        """
        One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
        """
        return pulumi.get(self, "match_by")

    @match_by.setter
    def match_by(self, value: Optional[str]):
        pulumi.set(self, "match_by", value)


@pulumi.input_type
class GetDiskImageSortArgs:
    def __init__(__self__, *,
                 key: str,
                 direction: Optional[str] = None):
        """
        :param str key: Sort diskimages by this key. This may be one of `id`, `label`, `name`, `version`.
        :param str direction: The sort direction. This may be either `asc` or `desc`.
        """
        pulumi.set(__self__, "key", key)
        if direction is not None:
            pulumi.set(__self__, "direction", direction)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Sort diskimages by this key. This may be one of `id`, `label`, `name`, `version`.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def direction(self) -> Optional[str]:
        """
        The sort direction. This may be either `asc` or `desc`.
        """
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
        """
        :param str key: Filter instances by this key. This may be one of `cpu_cores`, `created_at`, `disk_gb`, `firewall_id`, `hostname`, `id`, `initial_password`, `initial_user`, `network_id`, `notes`, `private_ip`, `pseudo_ip`, `public_ip`, `ram_mb`, `region`, `reverse_dns`, `script`, `size`, `sshkey_id`, `status`, `tags`, `template`.
        :param Sequence[str] values: Only retrieves `instances` which keys has value that matches one of the values provided here
        :param bool all: Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
        :param str match_by: One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "values", values)
        if all is not None:
            pulumi.set(__self__, "all", all)
        if match_by is not None:
            pulumi.set(__self__, "match_by", match_by)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Filter instances by this key. This may be one of `cpu_cores`, `created_at`, `disk_gb`, `firewall_id`, `hostname`, `id`, `initial_password`, `initial_user`, `network_id`, `notes`, `private_ip`, `pseudo_ip`, `public_ip`, `ram_mb`, `region`, `reverse_dns`, `script`, `size`, `sshkey_id`, `status`, `tags`, `template`.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        """
        Only retrieves `instances` which keys has value that matches one of the values provided here
        """
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def all(self) -> Optional[bool]:
        """
        Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
        """
        return pulumi.get(self, "all")

    @all.setter
    def all(self, value: Optional[bool]):
        pulumi.set(self, "all", value)

    @property
    @pulumi.getter(name="matchBy")
    def match_by(self) -> Optional[str]:
        """
        One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
        """
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
        """
        :param str key: Filter sizes by this key. This may be one of `cpu`, `description`, `disk`, `name`, `ram`, `selectable`, `type`.
        :param Sequence[str] values: Only retrieves `sizes` which keys has value that matches one of the values provided here
        :param bool all: Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
        :param str match_by: One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "values", values)
        if all is not None:
            pulumi.set(__self__, "all", all)
        if match_by is not None:
            pulumi.set(__self__, "match_by", match_by)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Filter sizes by this key. This may be one of `cpu`, `description`, `disk`, `name`, `ram`, `selectable`, `type`.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        """
        Only retrieves `sizes` which keys has value that matches one of the values provided here
        """
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def all(self) -> Optional[bool]:
        """
        Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
        """
        return pulumi.get(self, "all")

    @all.setter
    def all(self, value: Optional[bool]):
        pulumi.set(self, "all", value)

    @property
    @pulumi.getter(name="matchBy")
    def match_by(self) -> Optional[str]:
        """
        One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
        """
        return pulumi.get(self, "match_by")

    @match_by.setter
    def match_by(self, value: Optional[str]):
        pulumi.set(self, "match_by", value)


@pulumi.input_type
class GetInstancesSizeSortArgs:
    def __init__(__self__, *,
                 key: str,
                 direction: Optional[str] = None):
        """
        :param str key: Sort sizes by this key. This may be one of `cpu`, `description`, `disk`, `name`, `ram`, `selectable`, `type`.
        :param str direction: The sort direction. This may be either `asc` or `desc`.
        """
        pulumi.set(__self__, "key", key)
        if direction is not None:
            pulumi.set(__self__, "direction", direction)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Sort sizes by this key. This may be one of `cpu`, `description`, `disk`, `name`, `ram`, `selectable`, `type`.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def direction(self) -> Optional[str]:
        """
        The sort direction. This may be either `asc` or `desc`.
        """
        return pulumi.get(self, "direction")

    @direction.setter
    def direction(self, value: Optional[str]):
        pulumi.set(self, "direction", value)


@pulumi.input_type
class GetInstancesSortArgs:
    def __init__(__self__, *,
                 key: str,
                 direction: Optional[str] = None):
        """
        :param str key: Sort instances by this key. This may be one of `cpu_cores`, `created_at`, `disk_gb`, `firewall_id`, `hostname`, `id`, `initial_password`, `initial_user`, `network_id`, `notes`, `private_ip`, `pseudo_ip`, `public_ip`, `ram_mb`, `region`, `reverse_dns`, `script`, `size`, `sshkey_id`, `status`, `template`.
        :param str direction: The sort direction. This may be either `asc` or `desc`.
        """
        pulumi.set(__self__, "key", key)
        if direction is not None:
            pulumi.set(__self__, "direction", direction)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Sort instances by this key. This may be one of `cpu_cores`, `created_at`, `disk_gb`, `firewall_id`, `hostname`, `id`, `initial_password`, `initial_user`, `network_id`, `notes`, `private_ip`, `pseudo_ip`, `public_ip`, `ram_mb`, `region`, `reverse_dns`, `script`, `size`, `sshkey_id`, `status`, `template`.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def direction(self) -> Optional[str]:
        """
        The sort direction. This may be either `asc` or `desc`.
        """
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
        """
        :param str key: Filter versions by this key. This may be one of `default`, `label`, `type`, `version`.
        :param Sequence[str] values: Only retrieves `versions` which keys has value that matches one of the values provided here
        :param bool all: Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
        :param str match_by: One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "values", values)
        if all is not None:
            pulumi.set(__self__, "all", all)
        if match_by is not None:
            pulumi.set(__self__, "match_by", match_by)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Filter versions by this key. This may be one of `default`, `label`, `type`, `version`.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        """
        Only retrieves `versions` which keys has value that matches one of the values provided here
        """
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def all(self) -> Optional[bool]:
        """
        Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
        """
        return pulumi.get(self, "all")

    @all.setter
    def all(self, value: Optional[bool]):
        pulumi.set(self, "all", value)

    @property
    @pulumi.getter(name="matchBy")
    def match_by(self) -> Optional[str]:
        """
        One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
        """
        return pulumi.get(self, "match_by")

    @match_by.setter
    def match_by(self, value: Optional[str]):
        pulumi.set(self, "match_by", value)


@pulumi.input_type
class GetKubernetesVersionSortArgs:
    def __init__(__self__, *,
                 key: str,
                 direction: Optional[str] = None):
        """
        :param str key: Sort versions by this key. This may be one of `default`, `label`, `type`, `version`.
        :param str direction: The sort direction. This may be either `asc` or `desc`.
        """
        pulumi.set(__self__, "key", key)
        if direction is not None:
            pulumi.set(__self__, "direction", direction)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Sort versions by this key. This may be one of `default`, `label`, `type`, `version`.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def direction(self) -> Optional[str]:
        """
        The sort direction. This may be either `asc` or `desc`.
        """
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
        """
        :param str key: Filter regions by this key. This may be one of `code`, `country`, `default`, `name`.
        :param Sequence[str] values: Only retrieves `regions` which keys has value that matches one of the values provided here
        :param bool all: Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
        :param str match_by: One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "values", values)
        if all is not None:
            pulumi.set(__self__, "all", all)
        if match_by is not None:
            pulumi.set(__self__, "match_by", match_by)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Filter regions by this key. This may be one of `code`, `country`, `default`, `name`.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        """
        Only retrieves `regions` which keys has value that matches one of the values provided here
        """
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def all(self) -> Optional[bool]:
        """
        Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
        """
        return pulumi.get(self, "all")

    @all.setter
    def all(self, value: Optional[bool]):
        pulumi.set(self, "all", value)

    @property
    @pulumi.getter(name="matchBy")
    def match_by(self) -> Optional[str]:
        """
        One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
        """
        return pulumi.get(self, "match_by")

    @match_by.setter
    def match_by(self, value: Optional[str]):
        pulumi.set(self, "match_by", value)


@pulumi.input_type
class GetRegionSortArgs:
    def __init__(__self__, *,
                 key: str,
                 direction: Optional[str] = None):
        """
        :param str key: Sort regions by this key. This may be one of `code`, `country`, `default`, `name`.
        :param str direction: The sort direction. This may be either `asc` or `desc`.
        """
        pulumi.set(__self__, "key", key)
        if direction is not None:
            pulumi.set(__self__, "direction", direction)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Sort regions by this key. This may be one of `code`, `country`, `default`, `name`.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def direction(self) -> Optional[str]:
        """
        The sort direction. This may be either `asc` or `desc`.
        """
        return pulumi.get(self, "direction")

    @direction.setter
    def direction(self, value: Optional[str]):
        pulumi.set(self, "direction", value)


@pulumi.input_type
class GetSizeFilterArgs:
    def __init__(__self__, *,
                 key: str,
                 values: Sequence[str],
                 all: Optional[bool] = None,
                 match_by: Optional[str] = None):
        """
        :param str key: Filter sizes by this key. This may be one of `cpu`, `description`, `disk`, `name`, `ram`, `selectable`, `type`.
        :param Sequence[str] values: Only retrieves `sizes` which keys has value that matches one of the values provided here
        :param bool all: Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
        :param str match_by: One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "values", values)
        if all is not None:
            pulumi.set(__self__, "all", all)
        if match_by is not None:
            pulumi.set(__self__, "match_by", match_by)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Filter sizes by this key. This may be one of `cpu`, `description`, `disk`, `name`, `ram`, `selectable`, `type`.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        """
        Only retrieves `sizes` which keys has value that matches one of the values provided here
        """
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def all(self) -> Optional[bool]:
        """
        Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
        """
        return pulumi.get(self, "all")

    @all.setter
    def all(self, value: Optional[bool]):
        pulumi.set(self, "all", value)

    @property
    @pulumi.getter(name="matchBy")
    def match_by(self) -> Optional[str]:
        """
        One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
        """
        return pulumi.get(self, "match_by")

    @match_by.setter
    def match_by(self, value: Optional[str]):
        pulumi.set(self, "match_by", value)


@pulumi.input_type
class GetSizeSortArgs:
    def __init__(__self__, *,
                 key: str,
                 direction: Optional[str] = None):
        """
        :param str key: Sort sizes by this key. This may be one of `cpu`, `description`, `disk`, `name`, `ram`, `selectable`, `type`.
        :param str direction: The sort direction. This may be either `asc` or `desc`.
        """
        pulumi.set(__self__, "key", key)
        if direction is not None:
            pulumi.set(__self__, "direction", direction)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Sort sizes by this key. This may be one of `cpu`, `description`, `disk`, `name`, `ram`, `selectable`, `type`.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def direction(self) -> Optional[str]:
        """
        The sort direction. This may be either `asc` or `desc`.
        """
        return pulumi.get(self, "direction")

    @direction.setter
    def direction(self, value: Optional[str]):
        pulumi.set(self, "direction", value)



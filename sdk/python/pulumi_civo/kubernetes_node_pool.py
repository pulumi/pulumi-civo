# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['KubernetesNodePoolArgs', 'KubernetesNodePool']

@pulumi.input_type
class KubernetesNodePoolArgs:
    def __init__(__self__, *,
                 cluster_id: pulumi.Input[str],
                 region: pulumi.Input[str],
                 label: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 node_count: Optional[pulumi.Input[int]] = None,
                 public_ip_node_pool: Optional[pulumi.Input[bool]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 taints: Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesNodePoolTaintArgs']]]] = None):
        """
        The set of arguments for constructing a KubernetesNodePool resource.
        :param pulumi.Input[str] cluster_id: The ID of your cluster
        :param pulumi.Input[str] region: The region of the node pool, has to match that of the cluster
        :param pulumi.Input[str] label: Node pool label, if you don't provide one, we will generate one for you
        :param pulumi.Input[int] node_count: the number of instances to create (optional, the default at the time of writing is 3)
        :param pulumi.Input[bool] public_ip_node_pool: Node pool belongs to the public ip node pool
        :param pulumi.Input[str] size: the size of each node (optional, the default is currently g4s.kube.medium)
        """
        pulumi.set(__self__, "cluster_id", cluster_id)
        pulumi.set(__self__, "region", region)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if node_count is not None:
            pulumi.set(__self__, "node_count", node_count)
        if public_ip_node_pool is not None:
            pulumi.set(__self__, "public_ip_node_pool", public_ip_node_pool)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if taints is not None:
            pulumi.set(__self__, "taints", taints)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[str]:
        """
        The ID of your cluster
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        """
        The region of the node pool, has to match that of the cluster
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)

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

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[pulumi.Input[int]]:
        """
        the number of instances to create (optional, the default at the time of writing is 3)
        """
        return pulumi.get(self, "node_count")

    @node_count.setter
    def node_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "node_count", value)

    @property
    @pulumi.getter(name="publicIpNodePool")
    def public_ip_node_pool(self) -> Optional[pulumi.Input[bool]]:
        """
        Node pool belongs to the public ip node pool
        """
        return pulumi.get(self, "public_ip_node_pool")

    @public_ip_node_pool.setter
    def public_ip_node_pool(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "public_ip_node_pool", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[str]]:
        """
        the size of each node (optional, the default is currently g4s.kube.medium)
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def taints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesNodePoolTaintArgs']]]]:
        return pulumi.get(self, "taints")

    @taints.setter
    def taints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesNodePoolTaintArgs']]]]):
        pulumi.set(self, "taints", value)


@pulumi.input_type
class _KubernetesNodePoolState:
    def __init__(__self__, *,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 instance_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 node_count: Optional[pulumi.Input[int]] = None,
                 public_ip_node_pool: Optional[pulumi.Input[bool]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 taints: Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesNodePoolTaintArgs']]]] = None):
        """
        Input properties used for looking up and filtering KubernetesNodePool resources.
        :param pulumi.Input[str] cluster_id: The ID of your cluster
        :param pulumi.Input[Sequence[pulumi.Input[str]]] instance_names: Instance names in the nodepool
        :param pulumi.Input[str] label: Node pool label, if you don't provide one, we will generate one for you
        :param pulumi.Input[int] node_count: the number of instances to create (optional, the default at the time of writing is 3)
        :param pulumi.Input[bool] public_ip_node_pool: Node pool belongs to the public ip node pool
        :param pulumi.Input[str] region: The region of the node pool, has to match that of the cluster
        :param pulumi.Input[str] size: the size of each node (optional, the default is currently g4s.kube.medium)
        """
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if instance_names is not None:
            pulumi.set(__self__, "instance_names", instance_names)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if node_count is not None:
            pulumi.set(__self__, "node_count", node_count)
        if public_ip_node_pool is not None:
            pulumi.set(__self__, "public_ip_node_pool", public_ip_node_pool)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if taints is not None:
            pulumi.set(__self__, "taints", taints)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of your cluster
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

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

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[pulumi.Input[int]]:
        """
        the number of instances to create (optional, the default at the time of writing is 3)
        """
        return pulumi.get(self, "node_count")

    @node_count.setter
    def node_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "node_count", value)

    @property
    @pulumi.getter(name="publicIpNodePool")
    def public_ip_node_pool(self) -> Optional[pulumi.Input[bool]]:
        """
        Node pool belongs to the public ip node pool
        """
        return pulumi.get(self, "public_ip_node_pool")

    @public_ip_node_pool.setter
    def public_ip_node_pool(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "public_ip_node_pool", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region of the node pool, has to match that of the cluster
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[str]]:
        """
        the size of each node (optional, the default is currently g4s.kube.medium)
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def taints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesNodePoolTaintArgs']]]]:
        return pulumi.get(self, "taints")

    @taints.setter
    def taints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesNodePoolTaintArgs']]]]):
        pulumi.set(self, "taints", value)


class KubernetesNodePool(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 node_count: Optional[pulumi.Input[int]] = None,
                 public_ip_node_pool: Optional[pulumi.Input[bool]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 taints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KubernetesNodePoolTaintArgs']]]]] = None,
                 __props__=None):
        """
        ## Import

        ```sh
         $ pulumi import civo:index/kubernetesNodePool:KubernetesNodePool my-pool 1b8b2100-0e9f-4e8f-ad78-9eb578c2a0af:502c1130-cb9b-4a88-b6d2-307bd96d946a
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: The ID of your cluster
        :param pulumi.Input[str] label: Node pool label, if you don't provide one, we will generate one for you
        :param pulumi.Input[int] node_count: the number of instances to create (optional, the default at the time of writing is 3)
        :param pulumi.Input[bool] public_ip_node_pool: Node pool belongs to the public ip node pool
        :param pulumi.Input[str] region: The region of the node pool, has to match that of the cluster
        :param pulumi.Input[str] size: the size of each node (optional, the default is currently g4s.kube.medium)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: KubernetesNodePoolArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        ```sh
         $ pulumi import civo:index/kubernetesNodePool:KubernetesNodePool my-pool 1b8b2100-0e9f-4e8f-ad78-9eb578c2a0af:502c1130-cb9b-4a88-b6d2-307bd96d946a
        ```

        :param str resource_name: The name of the resource.
        :param KubernetesNodePoolArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KubernetesNodePoolArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 node_count: Optional[pulumi.Input[int]] = None,
                 public_ip_node_pool: Optional[pulumi.Input[bool]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 taints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KubernetesNodePoolTaintArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = KubernetesNodePoolArgs.__new__(KubernetesNodePoolArgs)

            if cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_id'")
            __props__.__dict__["cluster_id"] = cluster_id
            __props__.__dict__["label"] = label
            __props__.__dict__["labels"] = labels
            __props__.__dict__["node_count"] = node_count
            __props__.__dict__["public_ip_node_pool"] = public_ip_node_pool
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__.__dict__["region"] = region
            __props__.__dict__["size"] = size
            __props__.__dict__["taints"] = taints
            __props__.__dict__["instance_names"] = None
        super(KubernetesNodePool, __self__).__init__(
            'civo:index/kubernetesNodePool:KubernetesNodePool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            instance_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            label: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            node_count: Optional[pulumi.Input[int]] = None,
            public_ip_node_pool: Optional[pulumi.Input[bool]] = None,
            region: Optional[pulumi.Input[str]] = None,
            size: Optional[pulumi.Input[str]] = None,
            taints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KubernetesNodePoolTaintArgs']]]]] = None) -> 'KubernetesNodePool':
        """
        Get an existing KubernetesNodePool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: The ID of your cluster
        :param pulumi.Input[Sequence[pulumi.Input[str]]] instance_names: Instance names in the nodepool
        :param pulumi.Input[str] label: Node pool label, if you don't provide one, we will generate one for you
        :param pulumi.Input[int] node_count: the number of instances to create (optional, the default at the time of writing is 3)
        :param pulumi.Input[bool] public_ip_node_pool: Node pool belongs to the public ip node pool
        :param pulumi.Input[str] region: The region of the node pool, has to match that of the cluster
        :param pulumi.Input[str] size: the size of each node (optional, the default is currently g4s.kube.medium)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _KubernetesNodePoolState.__new__(_KubernetesNodePoolState)

        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["instance_names"] = instance_names
        __props__.__dict__["label"] = label
        __props__.__dict__["labels"] = labels
        __props__.__dict__["node_count"] = node_count
        __props__.__dict__["public_ip_node_pool"] = public_ip_node_pool
        __props__.__dict__["region"] = region
        __props__.__dict__["size"] = size
        __props__.__dict__["taints"] = taints
        return KubernetesNodePool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        The ID of your cluster
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="instanceNames")
    def instance_names(self) -> pulumi.Output[Sequence[str]]:
        """
        Instance names in the nodepool
        """
        return pulumi.get(self, "instance_names")

    @property
    @pulumi.getter
    def label(self) -> pulumi.Output[str]:
        """
        Node pool label, if you don't provide one, we will generate one for you
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> pulumi.Output[int]:
        """
        the number of instances to create (optional, the default at the time of writing is 3)
        """
        return pulumi.get(self, "node_count")

    @property
    @pulumi.getter(name="publicIpNodePool")
    def public_ip_node_pool(self) -> pulumi.Output[bool]:
        """
        Node pool belongs to the public ip node pool
        """
        return pulumi.get(self, "public_ip_node_pool")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region of the node pool, has to match that of the cluster
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[str]:
        """
        the size of each node (optional, the default is currently g4s.kube.medium)
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def taints(self) -> pulumi.Output[Optional[Sequence['outputs.KubernetesNodePoolTaint']]]:
        return pulumi.get(self, "taints")


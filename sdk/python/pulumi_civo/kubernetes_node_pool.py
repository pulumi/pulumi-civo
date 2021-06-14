# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['KubernetesNodePoolArgs', 'KubernetesNodePool']

@pulumi.input_type
class KubernetesNodePoolArgs:
    def __init__(__self__, *,
                 cluster_id: pulumi.Input[str],
                 num_target_nodes: Optional[pulumi.Input[int]] = None,
                 target_nodes_size: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a KubernetesNodePool resource.
        :param pulumi.Input[str] cluster_id: The ID of the Kubernetes cluster to which the node pool is associated.
        :param pulumi.Input[int] num_target_nodes: The number of instances to create (The default at the time of writing is 3).
        :param pulumi.Input[str] target_nodes_size: The size of each node.
        """
        pulumi.set(__self__, "cluster_id", cluster_id)
        if num_target_nodes is not None:
            pulumi.set(__self__, "num_target_nodes", num_target_nodes)
        if target_nodes_size is not None:
            pulumi.set(__self__, "target_nodes_size", target_nodes_size)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[str]:
        """
        The ID of the Kubernetes cluster to which the node pool is associated.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="numTargetNodes")
    def num_target_nodes(self) -> Optional[pulumi.Input[int]]:
        """
        The number of instances to create (The default at the time of writing is 3).
        """
        return pulumi.get(self, "num_target_nodes")

    @num_target_nodes.setter
    def num_target_nodes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "num_target_nodes", value)

    @property
    @pulumi.getter(name="targetNodesSize")
    def target_nodes_size(self) -> Optional[pulumi.Input[str]]:
        """
        The size of each node.
        """
        return pulumi.get(self, "target_nodes_size")

    @target_nodes_size.setter
    def target_nodes_size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_nodes_size", value)


@pulumi.input_type
class _KubernetesNodePoolState:
    def __init__(__self__, *,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 num_target_nodes: Optional[pulumi.Input[int]] = None,
                 target_nodes_size: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering KubernetesNodePool resources.
        :param pulumi.Input[str] cluster_id: The ID of the Kubernetes cluster to which the node pool is associated.
        :param pulumi.Input[int] num_target_nodes: The number of instances to create (The default at the time of writing is 3).
        :param pulumi.Input[str] target_nodes_size: The size of each node.
        """
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if num_target_nodes is not None:
            pulumi.set(__self__, "num_target_nodes", num_target_nodes)
        if target_nodes_size is not None:
            pulumi.set(__self__, "target_nodes_size", target_nodes_size)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Kubernetes cluster to which the node pool is associated.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="numTargetNodes")
    def num_target_nodes(self) -> Optional[pulumi.Input[int]]:
        """
        The number of instances to create (The default at the time of writing is 3).
        """
        return pulumi.get(self, "num_target_nodes")

    @num_target_nodes.setter
    def num_target_nodes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "num_target_nodes", value)

    @property
    @pulumi.getter(name="targetNodesSize")
    def target_nodes_size(self) -> Optional[pulumi.Input[str]]:
        """
        The size of each node.
        """
        return pulumi.get(self, "target_nodes_size")

    @target_nodes_size.setter
    def target_nodes_size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_nodes_size", value)


class KubernetesNodePool(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 num_target_nodes: Optional[pulumi.Input[int]] = None,
                 target_nodes_size: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Civo Kubernetes node pool resource. While the default node pool must be defined in the KubernetesCluster resource, this resource can be used to add additional ones to a cluster.

        ## Import

        Then the Kubernetes cluster node pool can be imported using the cluster's and pool id `cluster_id:node_pool_id`, e.g.

        ```sh
         $ pulumi import civo:index/kubernetesNodePool:KubernetesNodePool my-pool 1b8b2100-0e9f-4e8f-ad78-9eb578c2a0af:502c1130-cb9b-4a88-b6d2-307bd96d946a
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: The ID of the Kubernetes cluster to which the node pool is associated.
        :param pulumi.Input[int] num_target_nodes: The number of instances to create (The default at the time of writing is 3).
        :param pulumi.Input[str] target_nodes_size: The size of each node.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: KubernetesNodePoolArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Civo Kubernetes node pool resource. While the default node pool must be defined in the KubernetesCluster resource, this resource can be used to add additional ones to a cluster.

        ## Import

        Then the Kubernetes cluster node pool can be imported using the cluster's and pool id `cluster_id:node_pool_id`, e.g.

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
                 num_target_nodes: Optional[pulumi.Input[int]] = None,
                 target_nodes_size: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = KubernetesNodePoolArgs.__new__(KubernetesNodePoolArgs)

            if cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_id'")
            __props__.__dict__["cluster_id"] = cluster_id
            __props__.__dict__["num_target_nodes"] = num_target_nodes
            __props__.__dict__["target_nodes_size"] = target_nodes_size
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
            num_target_nodes: Optional[pulumi.Input[int]] = None,
            target_nodes_size: Optional[pulumi.Input[str]] = None) -> 'KubernetesNodePool':
        """
        Get an existing KubernetesNodePool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: The ID of the Kubernetes cluster to which the node pool is associated.
        :param pulumi.Input[int] num_target_nodes: The number of instances to create (The default at the time of writing is 3).
        :param pulumi.Input[str] target_nodes_size: The size of each node.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _KubernetesNodePoolState.__new__(_KubernetesNodePoolState)

        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["num_target_nodes"] = num_target_nodes
        __props__.__dict__["target_nodes_size"] = target_nodes_size
        return KubernetesNodePool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        The ID of the Kubernetes cluster to which the node pool is associated.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="numTargetNodes")
    def num_target_nodes(self) -> pulumi.Output[int]:
        """
        The number of instances to create (The default at the time of writing is 3).
        """
        return pulumi.get(self, "num_target_nodes")

    @property
    @pulumi.getter(name="targetNodesSize")
    def target_nodes_size(self) -> pulumi.Output[str]:
        """
        The size of each node.
        """
        return pulumi.get(self, "target_nodes_size")

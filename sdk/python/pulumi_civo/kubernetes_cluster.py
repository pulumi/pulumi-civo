# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['KubernetesClusterArgs', 'KubernetesCluster']

@pulumi.input_type
class KubernetesClusterArgs:
    def __init__(__self__, *,
                 firewall_id: pulumi.Input[str],
                 applications: Optional[pulumi.Input[str]] = None,
                 kubernetes_version: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 num_target_nodes: Optional[pulumi.Input[int]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[str]] = None,
                 target_nodes_size: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a KubernetesCluster resource.
        :param pulumi.Input[str] firewall_id: The existing firewall ID to use for this cluster
        :param pulumi.Input[str] applications: Comma separated list of applications to install. Spaces within application names are fine, but shouldn't be either side of the comma. Application names are case-sensitive; the available applications can be listed with the Civo CLI: 'civo kubernetes applications ls'. If you want to remove a default installed application, prefix it with a '-', e.g. -Traefik. For application that supports plans, you can use 'app*name:app*plan' format e.g. 'Linkerd:Linkerd & Jaeger' or 'MariaDB:5GB'.
        :param pulumi.Input[str] kubernetes_version: The version of k3s to install (optional, the default is currently the latest available)
        :param pulumi.Input[str] name: Name for your cluster, must be unique within your account
        :param pulumi.Input[str] network_id: The network for the cluster, if not declare we use the default one
        :param pulumi.Input[int] num_target_nodes: The number of instances to create (optional, the default at the time of writing is 3)
        :param pulumi.Input[str] region: The region for the cluster, if not declare we use the region in declared in the provider
        :param pulumi.Input[str] tags: Space separated list of tags, to be used freely as required
        :param pulumi.Input[str] target_nodes_size: The size of each node (optional, the default is currently g3.k3s.medium)
        """
        pulumi.set(__self__, "firewall_id", firewall_id)
        if applications is not None:
            pulumi.set(__self__, "applications", applications)
        if kubernetes_version is not None:
            pulumi.set(__self__, "kubernetes_version", kubernetes_version)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network_id is not None:
            pulumi.set(__self__, "network_id", network_id)
        if num_target_nodes is not None:
            pulumi.set(__self__, "num_target_nodes", num_target_nodes)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if target_nodes_size is not None:
            pulumi.set(__self__, "target_nodes_size", target_nodes_size)

    @property
    @pulumi.getter(name="firewallId")
    def firewall_id(self) -> pulumi.Input[str]:
        """
        The existing firewall ID to use for this cluster
        """
        return pulumi.get(self, "firewall_id")

    @firewall_id.setter
    def firewall_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "firewall_id", value)

    @property
    @pulumi.getter
    def applications(self) -> Optional[pulumi.Input[str]]:
        """
        Comma separated list of applications to install. Spaces within application names are fine, but shouldn't be either side of the comma. Application names are case-sensitive; the available applications can be listed with the Civo CLI: 'civo kubernetes applications ls'. If you want to remove a default installed application, prefix it with a '-', e.g. -Traefik. For application that supports plans, you can use 'app*name:app*plan' format e.g. 'Linkerd:Linkerd & Jaeger' or 'MariaDB:5GB'.
        """
        return pulumi.get(self, "applications")

    @applications.setter
    def applications(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "applications", value)

    @property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of k3s to install (optional, the default is currently the latest available)
        """
        return pulumi.get(self, "kubernetes_version")

    @kubernetes_version.setter
    def kubernetes_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kubernetes_version", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name for your cluster, must be unique within your account
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> Optional[pulumi.Input[str]]:
        """
        The network for the cluster, if not declare we use the default one
        """
        return pulumi.get(self, "network_id")

    @network_id.setter
    def network_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_id", value)

    @property
    @pulumi.getter(name="numTargetNodes")
    def num_target_nodes(self) -> Optional[pulumi.Input[int]]:
        """
        The number of instances to create (optional, the default at the time of writing is 3)
        """
        return pulumi.get(self, "num_target_nodes")

    @num_target_nodes.setter
    def num_target_nodes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "num_target_nodes", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region for the cluster, if not declare we use the region in declared in the provider
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[str]]:
        """
        Space separated list of tags, to be used freely as required
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="targetNodesSize")
    def target_nodes_size(self) -> Optional[pulumi.Input[str]]:
        """
        The size of each node (optional, the default is currently g3.k3s.medium)
        """
        return pulumi.get(self, "target_nodes_size")

    @target_nodes_size.setter
    def target_nodes_size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_nodes_size", value)


@pulumi.input_type
class _KubernetesClusterState:
    def __init__(__self__, *,
                 api_endpoint: Optional[pulumi.Input[str]] = None,
                 applications: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 dns_entry: Optional[pulumi.Input[str]] = None,
                 firewall_id: Optional[pulumi.Input[str]] = None,
                 installed_applications: Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesClusterInstalledApplicationArgs']]]] = None,
                 instances: Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesClusterInstanceArgs']]]] = None,
                 kubeconfig: Optional[pulumi.Input[str]] = None,
                 kubernetes_version: Optional[pulumi.Input[str]] = None,
                 master_ip: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 num_target_nodes: Optional[pulumi.Input[int]] = None,
                 pools: Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesClusterPoolArgs']]]] = None,
                 ready: Optional[pulumi.Input[bool]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[str]] = None,
                 target_nodes_size: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering KubernetesCluster resources.
        :param pulumi.Input[str] api_endpoint: The API server endpoint of the cluster
        :param pulumi.Input[str] applications: Comma separated list of applications to install. Spaces within application names are fine, but shouldn't be either side of the comma. Application names are case-sensitive; the available applications can be listed with the Civo CLI: 'civo kubernetes applications ls'. If you want to remove a default installed application, prefix it with a '-', e.g. -Traefik. For application that supports plans, you can use 'app*name:app*plan' format e.g. 'Linkerd:Linkerd & Jaeger' or 'MariaDB:5GB'.
        :param pulumi.Input[str] created_at: The timestamp when the cluster was created
        :param pulumi.Input[str] dns_entry: The DNS name of the cluster
        :param pulumi.Input[str] firewall_id: The existing firewall ID to use for this cluster
        :param pulumi.Input[str] kubeconfig: The kubeconfig of the cluster
        :param pulumi.Input[str] kubernetes_version: The version of k3s to install (optional, the default is currently the latest available)
        :param pulumi.Input[str] master_ip: The IP address of the master node
        :param pulumi.Input[str] name: Name for your cluster, must be unique within your account
        :param pulumi.Input[str] network_id: The network for the cluster, if not declare we use the default one
        :param pulumi.Input[int] num_target_nodes: The number of instances to create (optional, the default at the time of writing is 3)
        :param pulumi.Input[bool] ready: When cluster is ready, this will return `true`
        :param pulumi.Input[str] region: The region for the cluster, if not declare we use the region in declared in the provider
        :param pulumi.Input[str] status: Status of the cluster
        :param pulumi.Input[str] tags: Space separated list of tags, to be used freely as required
        :param pulumi.Input[str] target_nodes_size: The size of each node (optional, the default is currently g3.k3s.medium)
        """
        if api_endpoint is not None:
            pulumi.set(__self__, "api_endpoint", api_endpoint)
        if applications is not None:
            pulumi.set(__self__, "applications", applications)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if dns_entry is not None:
            pulumi.set(__self__, "dns_entry", dns_entry)
        if firewall_id is not None:
            pulumi.set(__self__, "firewall_id", firewall_id)
        if installed_applications is not None:
            pulumi.set(__self__, "installed_applications", installed_applications)
        if instances is not None:
            pulumi.set(__self__, "instances", instances)
        if kubeconfig is not None:
            pulumi.set(__self__, "kubeconfig", kubeconfig)
        if kubernetes_version is not None:
            pulumi.set(__self__, "kubernetes_version", kubernetes_version)
        if master_ip is not None:
            pulumi.set(__self__, "master_ip", master_ip)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network_id is not None:
            pulumi.set(__self__, "network_id", network_id)
        if num_target_nodes is not None:
            pulumi.set(__self__, "num_target_nodes", num_target_nodes)
        if pools is not None:
            pulumi.set(__self__, "pools", pools)
        if ready is not None:
            pulumi.set(__self__, "ready", ready)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if target_nodes_size is not None:
            pulumi.set(__self__, "target_nodes_size", target_nodes_size)

    @property
    @pulumi.getter(name="apiEndpoint")
    def api_endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        The API server endpoint of the cluster
        """
        return pulumi.get(self, "api_endpoint")

    @api_endpoint.setter
    def api_endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_endpoint", value)

    @property
    @pulumi.getter
    def applications(self) -> Optional[pulumi.Input[str]]:
        """
        Comma separated list of applications to install. Spaces within application names are fine, but shouldn't be either side of the comma. Application names are case-sensitive; the available applications can be listed with the Civo CLI: 'civo kubernetes applications ls'. If you want to remove a default installed application, prefix it with a '-', e.g. -Traefik. For application that supports plans, you can use 'app*name:app*plan' format e.g. 'Linkerd:Linkerd & Jaeger' or 'MariaDB:5GB'.
        """
        return pulumi.get(self, "applications")

    @applications.setter
    def applications(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "applications", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        The timestamp when the cluster was created
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="dnsEntry")
    def dns_entry(self) -> Optional[pulumi.Input[str]]:
        """
        The DNS name of the cluster
        """
        return pulumi.get(self, "dns_entry")

    @dns_entry.setter
    def dns_entry(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dns_entry", value)

    @property
    @pulumi.getter(name="firewallId")
    def firewall_id(self) -> Optional[pulumi.Input[str]]:
        """
        The existing firewall ID to use for this cluster
        """
        return pulumi.get(self, "firewall_id")

    @firewall_id.setter
    def firewall_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "firewall_id", value)

    @property
    @pulumi.getter(name="installedApplications")
    def installed_applications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesClusterInstalledApplicationArgs']]]]:
        return pulumi.get(self, "installed_applications")

    @installed_applications.setter
    def installed_applications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesClusterInstalledApplicationArgs']]]]):
        pulumi.set(self, "installed_applications", value)

    @property
    @pulumi.getter
    def instances(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesClusterInstanceArgs']]]]:
        return pulumi.get(self, "instances")

    @instances.setter
    def instances(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesClusterInstanceArgs']]]]):
        pulumi.set(self, "instances", value)

    @property
    @pulumi.getter
    def kubeconfig(self) -> Optional[pulumi.Input[str]]:
        """
        The kubeconfig of the cluster
        """
        return pulumi.get(self, "kubeconfig")

    @kubeconfig.setter
    def kubeconfig(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kubeconfig", value)

    @property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of k3s to install (optional, the default is currently the latest available)
        """
        return pulumi.get(self, "kubernetes_version")

    @kubernetes_version.setter
    def kubernetes_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kubernetes_version", value)

    @property
    @pulumi.getter(name="masterIp")
    def master_ip(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address of the master node
        """
        return pulumi.get(self, "master_ip")

    @master_ip.setter
    def master_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "master_ip", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name for your cluster, must be unique within your account
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> Optional[pulumi.Input[str]]:
        """
        The network for the cluster, if not declare we use the default one
        """
        return pulumi.get(self, "network_id")

    @network_id.setter
    def network_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_id", value)

    @property
    @pulumi.getter(name="numTargetNodes")
    def num_target_nodes(self) -> Optional[pulumi.Input[int]]:
        """
        The number of instances to create (optional, the default at the time of writing is 3)
        """
        return pulumi.get(self, "num_target_nodes")

    @num_target_nodes.setter
    def num_target_nodes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "num_target_nodes", value)

    @property
    @pulumi.getter
    def pools(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesClusterPoolArgs']]]]:
        return pulumi.get(self, "pools")

    @pools.setter
    def pools(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['KubernetesClusterPoolArgs']]]]):
        pulumi.set(self, "pools", value)

    @property
    @pulumi.getter
    def ready(self) -> Optional[pulumi.Input[bool]]:
        """
        When cluster is ready, this will return `true`
        """
        return pulumi.get(self, "ready")

    @ready.setter
    def ready(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ready", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region for the cluster, if not declare we use the region in declared in the provider
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Status of the cluster
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[str]]:
        """
        Space separated list of tags, to be used freely as required
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="targetNodesSize")
    def target_nodes_size(self) -> Optional[pulumi.Input[str]]:
        """
        The size of each node (optional, the default is currently g3.k3s.medium)
        """
        return pulumi.get(self, "target_nodes_size")

    @target_nodes_size.setter
    def target_nodes_size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_nodes_size", value)


class KubernetesCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 applications: Optional[pulumi.Input[str]] = None,
                 firewall_id: Optional[pulumi.Input[str]] = None,
                 kubernetes_version: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 num_target_nodes: Optional[pulumi.Input[int]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[str]] = None,
                 target_nodes_size: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Civo Kubernetes cluster resource. This can be used to create, delete, and modify clusters.

        ## Import

        # using ID

        ```sh
         $ pulumi import civo:index/kubernetesCluster:KubernetesCluster my-cluster 1b8b2100-0e9f-4e8f-ad78-9eb578c2a0af
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] applications: Comma separated list of applications to install. Spaces within application names are fine, but shouldn't be either side of the comma. Application names are case-sensitive; the available applications can be listed with the Civo CLI: 'civo kubernetes applications ls'. If you want to remove a default installed application, prefix it with a '-', e.g. -Traefik. For application that supports plans, you can use 'app*name:app*plan' format e.g. 'Linkerd:Linkerd & Jaeger' or 'MariaDB:5GB'.
        :param pulumi.Input[str] firewall_id: The existing firewall ID to use for this cluster
        :param pulumi.Input[str] kubernetes_version: The version of k3s to install (optional, the default is currently the latest available)
        :param pulumi.Input[str] name: Name for your cluster, must be unique within your account
        :param pulumi.Input[str] network_id: The network for the cluster, if not declare we use the default one
        :param pulumi.Input[int] num_target_nodes: The number of instances to create (optional, the default at the time of writing is 3)
        :param pulumi.Input[str] region: The region for the cluster, if not declare we use the region in declared in the provider
        :param pulumi.Input[str] tags: Space separated list of tags, to be used freely as required
        :param pulumi.Input[str] target_nodes_size: The size of each node (optional, the default is currently g3.k3s.medium)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: KubernetesClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Civo Kubernetes cluster resource. This can be used to create, delete, and modify clusters.

        ## Import

        # using ID

        ```sh
         $ pulumi import civo:index/kubernetesCluster:KubernetesCluster my-cluster 1b8b2100-0e9f-4e8f-ad78-9eb578c2a0af
        ```

        :param str resource_name: The name of the resource.
        :param KubernetesClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KubernetesClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 applications: Optional[pulumi.Input[str]] = None,
                 firewall_id: Optional[pulumi.Input[str]] = None,
                 kubernetes_version: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 num_target_nodes: Optional[pulumi.Input[int]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[str]] = None,
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
            __props__ = KubernetesClusterArgs.__new__(KubernetesClusterArgs)

            __props__.__dict__["applications"] = applications
            if firewall_id is None and not opts.urn:
                raise TypeError("Missing required property 'firewall_id'")
            __props__.__dict__["firewall_id"] = firewall_id
            __props__.__dict__["kubernetes_version"] = kubernetes_version
            __props__.__dict__["name"] = name
            __props__.__dict__["network_id"] = network_id
            __props__.__dict__["num_target_nodes"] = num_target_nodes
            __props__.__dict__["region"] = region
            __props__.__dict__["tags"] = tags
            __props__.__dict__["target_nodes_size"] = target_nodes_size
            __props__.__dict__["api_endpoint"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["dns_entry"] = None
            __props__.__dict__["installed_applications"] = None
            __props__.__dict__["instances"] = None
            __props__.__dict__["kubeconfig"] = None
            __props__.__dict__["master_ip"] = None
            __props__.__dict__["pools"] = None
            __props__.__dict__["ready"] = None
            __props__.__dict__["status"] = None
        super(KubernetesCluster, __self__).__init__(
            'civo:index/kubernetesCluster:KubernetesCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_endpoint: Optional[pulumi.Input[str]] = None,
            applications: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            dns_entry: Optional[pulumi.Input[str]] = None,
            firewall_id: Optional[pulumi.Input[str]] = None,
            installed_applications: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KubernetesClusterInstalledApplicationArgs']]]]] = None,
            instances: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KubernetesClusterInstanceArgs']]]]] = None,
            kubeconfig: Optional[pulumi.Input[str]] = None,
            kubernetes_version: Optional[pulumi.Input[str]] = None,
            master_ip: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network_id: Optional[pulumi.Input[str]] = None,
            num_target_nodes: Optional[pulumi.Input[int]] = None,
            pools: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KubernetesClusterPoolArgs']]]]] = None,
            ready: Optional[pulumi.Input[bool]] = None,
            region: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[str]] = None,
            target_nodes_size: Optional[pulumi.Input[str]] = None) -> 'KubernetesCluster':
        """
        Get an existing KubernetesCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_endpoint: The API server endpoint of the cluster
        :param pulumi.Input[str] applications: Comma separated list of applications to install. Spaces within application names are fine, but shouldn't be either side of the comma. Application names are case-sensitive; the available applications can be listed with the Civo CLI: 'civo kubernetes applications ls'. If you want to remove a default installed application, prefix it with a '-', e.g. -Traefik. For application that supports plans, you can use 'app*name:app*plan' format e.g. 'Linkerd:Linkerd & Jaeger' or 'MariaDB:5GB'.
        :param pulumi.Input[str] created_at: The timestamp when the cluster was created
        :param pulumi.Input[str] dns_entry: The DNS name of the cluster
        :param pulumi.Input[str] firewall_id: The existing firewall ID to use for this cluster
        :param pulumi.Input[str] kubeconfig: The kubeconfig of the cluster
        :param pulumi.Input[str] kubernetes_version: The version of k3s to install (optional, the default is currently the latest available)
        :param pulumi.Input[str] master_ip: The IP address of the master node
        :param pulumi.Input[str] name: Name for your cluster, must be unique within your account
        :param pulumi.Input[str] network_id: The network for the cluster, if not declare we use the default one
        :param pulumi.Input[int] num_target_nodes: The number of instances to create (optional, the default at the time of writing is 3)
        :param pulumi.Input[bool] ready: When cluster is ready, this will return `true`
        :param pulumi.Input[str] region: The region for the cluster, if not declare we use the region in declared in the provider
        :param pulumi.Input[str] status: Status of the cluster
        :param pulumi.Input[str] tags: Space separated list of tags, to be used freely as required
        :param pulumi.Input[str] target_nodes_size: The size of each node (optional, the default is currently g3.k3s.medium)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _KubernetesClusterState.__new__(_KubernetesClusterState)

        __props__.__dict__["api_endpoint"] = api_endpoint
        __props__.__dict__["applications"] = applications
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["dns_entry"] = dns_entry
        __props__.__dict__["firewall_id"] = firewall_id
        __props__.__dict__["installed_applications"] = installed_applications
        __props__.__dict__["instances"] = instances
        __props__.__dict__["kubeconfig"] = kubeconfig
        __props__.__dict__["kubernetes_version"] = kubernetes_version
        __props__.__dict__["master_ip"] = master_ip
        __props__.__dict__["name"] = name
        __props__.__dict__["network_id"] = network_id
        __props__.__dict__["num_target_nodes"] = num_target_nodes
        __props__.__dict__["pools"] = pools
        __props__.__dict__["ready"] = ready
        __props__.__dict__["region"] = region
        __props__.__dict__["status"] = status
        __props__.__dict__["tags"] = tags
        __props__.__dict__["target_nodes_size"] = target_nodes_size
        return KubernetesCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiEndpoint")
    def api_endpoint(self) -> pulumi.Output[str]:
        """
        The API server endpoint of the cluster
        """
        return pulumi.get(self, "api_endpoint")

    @property
    @pulumi.getter
    def applications(self) -> pulumi.Output[Optional[str]]:
        """
        Comma separated list of applications to install. Spaces within application names are fine, but shouldn't be either side of the comma. Application names are case-sensitive; the available applications can be listed with the Civo CLI: 'civo kubernetes applications ls'. If you want to remove a default installed application, prefix it with a '-', e.g. -Traefik. For application that supports plans, you can use 'app*name:app*plan' format e.g. 'Linkerd:Linkerd & Jaeger' or 'MariaDB:5GB'.
        """
        return pulumi.get(self, "applications")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The timestamp when the cluster was created
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="dnsEntry")
    def dns_entry(self) -> pulumi.Output[str]:
        """
        The DNS name of the cluster
        """
        return pulumi.get(self, "dns_entry")

    @property
    @pulumi.getter(name="firewallId")
    def firewall_id(self) -> pulumi.Output[str]:
        """
        The existing firewall ID to use for this cluster
        """
        return pulumi.get(self, "firewall_id")

    @property
    @pulumi.getter(name="installedApplications")
    def installed_applications(self) -> pulumi.Output[Sequence['outputs.KubernetesClusterInstalledApplication']]:
        return pulumi.get(self, "installed_applications")

    @property
    @pulumi.getter
    def instances(self) -> pulumi.Output[Sequence['outputs.KubernetesClusterInstance']]:
        return pulumi.get(self, "instances")

    @property
    @pulumi.getter
    def kubeconfig(self) -> pulumi.Output[str]:
        """
        The kubeconfig of the cluster
        """
        return pulumi.get(self, "kubeconfig")

    @property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> pulumi.Output[str]:
        """
        The version of k3s to install (optional, the default is currently the latest available)
        """
        return pulumi.get(self, "kubernetes_version")

    @property
    @pulumi.getter(name="masterIp")
    def master_ip(self) -> pulumi.Output[str]:
        """
        The IP address of the master node
        """
        return pulumi.get(self, "master_ip")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name for your cluster, must be unique within your account
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Output[str]:
        """
        The network for the cluster, if not declare we use the default one
        """
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter(name="numTargetNodes")
    def num_target_nodes(self) -> pulumi.Output[int]:
        """
        The number of instances to create (optional, the default at the time of writing is 3)
        """
        return pulumi.get(self, "num_target_nodes")

    @property
    @pulumi.getter
    def pools(self) -> pulumi.Output[Sequence['outputs.KubernetesClusterPool']]:
        return pulumi.get(self, "pools")

    @property
    @pulumi.getter
    def ready(self) -> pulumi.Output[bool]:
        """
        When cluster is ready, this will return `true`
        """
        return pulumi.get(self, "ready")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region for the cluster, if not declare we use the region in declared in the provider
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Status of the cluster
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[str]]:
        """
        Space separated list of tags, to be used freely as required
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetNodesSize")
    def target_nodes_size(self) -> pulumi.Output[str]:
        """
        The size of each node (optional, the default is currently g3.k3s.medium)
        """
        return pulumi.get(self, "target_nodes_size")


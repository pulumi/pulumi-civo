# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetKubernetesClusterResult',
    'AwaitableGetKubernetesClusterResult',
    'get_kubernetes_cluster',
    'get_kubernetes_cluster_output',
]

@pulumi.output_type
class GetKubernetesClusterResult:
    """
    A collection of values returned by getKubernetesCluster.
    """
    def __init__(__self__, api_endpoint=None, applications=None, cni=None, created_at=None, dns_entry=None, id=None, installed_applications=None, instances=None, kubeconfig=None, kubernetes_version=None, master_ip=None, name=None, num_target_nodes=None, pools=None, ready=None, region=None, status=None, tags=None, target_nodes_size=None):
        if api_endpoint and not isinstance(api_endpoint, str):
            raise TypeError("Expected argument 'api_endpoint' to be a str")
        pulumi.set(__self__, "api_endpoint", api_endpoint)
        if applications and not isinstance(applications, str):
            raise TypeError("Expected argument 'applications' to be a str")
        pulumi.set(__self__, "applications", applications)
        if cni and not isinstance(cni, str):
            raise TypeError("Expected argument 'cni' to be a str")
        pulumi.set(__self__, "cni", cni)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if dns_entry and not isinstance(dns_entry, str):
            raise TypeError("Expected argument 'dns_entry' to be a str")
        pulumi.set(__self__, "dns_entry", dns_entry)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if installed_applications and not isinstance(installed_applications, list):
            raise TypeError("Expected argument 'installed_applications' to be a list")
        pulumi.set(__self__, "installed_applications", installed_applications)
        if instances and not isinstance(instances, list):
            raise TypeError("Expected argument 'instances' to be a list")
        pulumi.set(__self__, "instances", instances)
        if kubeconfig and not isinstance(kubeconfig, str):
            raise TypeError("Expected argument 'kubeconfig' to be a str")
        pulumi.set(__self__, "kubeconfig", kubeconfig)
        if kubernetes_version and not isinstance(kubernetes_version, str):
            raise TypeError("Expected argument 'kubernetes_version' to be a str")
        pulumi.set(__self__, "kubernetes_version", kubernetes_version)
        if master_ip and not isinstance(master_ip, str):
            raise TypeError("Expected argument 'master_ip' to be a str")
        pulumi.set(__self__, "master_ip", master_ip)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if num_target_nodes and not isinstance(num_target_nodes, int):
            raise TypeError("Expected argument 'num_target_nodes' to be a int")
        pulumi.set(__self__, "num_target_nodes", num_target_nodes)
        if pools and not isinstance(pools, list):
            raise TypeError("Expected argument 'pools' to be a list")
        pulumi.set(__self__, "pools", pools)
        if ready and not isinstance(ready, bool):
            raise TypeError("Expected argument 'ready' to be a bool")
        pulumi.set(__self__, "ready", ready)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, str):
            raise TypeError("Expected argument 'tags' to be a str")
        pulumi.set(__self__, "tags", tags)
        if target_nodes_size and not isinstance(target_nodes_size, str):
            raise TypeError("Expected argument 'target_nodes_size' to be a str")
        pulumi.set(__self__, "target_nodes_size", target_nodes_size)

    @property
    @pulumi.getter(name="apiEndpoint")
    def api_endpoint(self) -> str:
        """
        The base URL of the API server on the Kubernetes master node
        """
        return pulumi.get(self, "api_endpoint")

    @property
    @pulumi.getter
    def applications(self) -> str:
        """
        A list of application installed
        """
        return pulumi.get(self, "applications")

    @property
    @pulumi.getter
    def cni(self) -> str:
        """
        The cni for the k3s to install (the default is `flannel`) valid options are `cilium` or `flannel`
        """
        return pulumi.get(self, "cni")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        The date where the Kubernetes cluster was create
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="dnsEntry")
    def dns_entry(self) -> str:
        """
        The unique dns entry for the cluster in this case point to the master
        """
        return pulumi.get(self, "dns_entry")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="installedApplications")
    def installed_applications(self) -> Sequence['outputs.GetKubernetesClusterInstalledApplicationResult']:
        return pulumi.get(self, "installed_applications")

    @property
    @pulumi.getter
    def instances(self) -> Sequence['outputs.GetKubernetesClusterInstanceResult']:
        return pulumi.get(self, "instances")

    @property
    @pulumi.getter
    def kubeconfig(self) -> str:
        """
        A representation of the Kubernetes cluster's kubeconfig in yaml format
        """
        return pulumi.get(self, "kubeconfig")

    @property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> str:
        """
        The version of Kubernetes
        """
        return pulumi.get(self, "kubernetes_version")

    @property
    @pulumi.getter(name="masterIp")
    def master_ip(self) -> str:
        """
        The IP of the Kubernetes master node
        """
        return pulumi.get(self, "master_ip")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the Kubernetes Cluster
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="numTargetNodes")
    def num_target_nodes(self) -> int:
        """
        The size of the Kubernetes cluster
        """
        return pulumi.get(self, "num_target_nodes")

    @property
    @pulumi.getter
    def pools(self) -> Sequence['outputs.GetKubernetesClusterPoolResult']:
        return pulumi.get(self, "pools")

    @property
    @pulumi.getter
    def ready(self) -> bool:
        """
        If the Kubernetes cluster is ready
        """
        return pulumi.get(self, "ready")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        """
        The region where cluster is running
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of Kubernetes cluster
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> str:
        """
        A list of tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetNodesSize")
    def target_nodes_size(self) -> str:
        """
        The size of each node
        """
        return pulumi.get(self, "target_nodes_size")


class AwaitableGetKubernetesClusterResult(GetKubernetesClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKubernetesClusterResult(
            api_endpoint=self.api_endpoint,
            applications=self.applications,
            cni=self.cni,
            created_at=self.created_at,
            dns_entry=self.dns_entry,
            id=self.id,
            installed_applications=self.installed_applications,
            instances=self.instances,
            kubeconfig=self.kubeconfig,
            kubernetes_version=self.kubernetes_version,
            master_ip=self.master_ip,
            name=self.name,
            num_target_nodes=self.num_target_nodes,
            pools=self.pools,
            ready=self.ready,
            region=self.region,
            status=self.status,
            tags=self.tags,
            target_nodes_size=self.target_nodes_size)


def get_kubernetes_cluster(id: Optional[str] = None,
                           name: Optional[str] = None,
                           region: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKubernetesClusterResult:
    """
    Provides a Civo Kubernetes cluster data source.

    Note: This data source returns a single Kubernetes cluster. When specifying a name, an error will be raised if more than one Kubernetes cluster found.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_civo as civo

    my_cluster = civo.get_kubernetes_cluster(name="my-super-cluster")
    pulumi.export("kubernetesClusterOutput", my_cluster.master_ip)
    ```


    :param str id: The ID of this resource.
    :param str name: The name of the Kubernetes Cluster
    :param str region: The region where cluster is running
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['region'] = region
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('civo:index/getKubernetesCluster:getKubernetesCluster', __args__, opts=opts, typ=GetKubernetesClusterResult).value

    return AwaitableGetKubernetesClusterResult(
        api_endpoint=__ret__.api_endpoint,
        applications=__ret__.applications,
        cni=__ret__.cni,
        created_at=__ret__.created_at,
        dns_entry=__ret__.dns_entry,
        id=__ret__.id,
        installed_applications=__ret__.installed_applications,
        instances=__ret__.instances,
        kubeconfig=__ret__.kubeconfig,
        kubernetes_version=__ret__.kubernetes_version,
        master_ip=__ret__.master_ip,
        name=__ret__.name,
        num_target_nodes=__ret__.num_target_nodes,
        pools=__ret__.pools,
        ready=__ret__.ready,
        region=__ret__.region,
        status=__ret__.status,
        tags=__ret__.tags,
        target_nodes_size=__ret__.target_nodes_size)


@_utilities.lift_output_func(get_kubernetes_cluster)
def get_kubernetes_cluster_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                                  name: Optional[pulumi.Input[Optional[str]]] = None,
                                  region: Optional[pulumi.Input[Optional[str]]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetKubernetesClusterResult]:
    """
    Provides a Civo Kubernetes cluster data source.

    Note: This data source returns a single Kubernetes cluster. When specifying a name, an error will be raised if more than one Kubernetes cluster found.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_civo as civo

    my_cluster = civo.get_kubernetes_cluster(name="my-super-cluster")
    pulumi.export("kubernetesClusterOutput", my_cluster.master_ip)
    ```


    :param str id: The ID of this resource.
    :param str name: The name of the Kubernetes Cluster
    :param str region: The region where cluster is running
    """
    ...

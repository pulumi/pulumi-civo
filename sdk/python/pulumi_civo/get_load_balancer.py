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

__all__ = [
    'GetLoadBalancerResult',
    'AwaitableGetLoadBalancerResult',
    'get_load_balancer',
    'get_load_balancer_output',
]

@pulumi.output_type
class GetLoadBalancerResult:
    """
    A collection of values returned by getLoadBalancer.
    """
    def __init__(__self__, algorithm=None, backends=None, cluster_id=None, enable_proxy_protocol=None, external_traffic_policy=None, firewall_id=None, id=None, name=None, private_ip=None, public_ip=None, region=None, session_affinity=None, session_affinity_config_timeout=None, state=None):
        if algorithm and not isinstance(algorithm, str):
            raise TypeError("Expected argument 'algorithm' to be a str")
        pulumi.set(__self__, "algorithm", algorithm)
        if backends and not isinstance(backends, list):
            raise TypeError("Expected argument 'backends' to be a list")
        pulumi.set(__self__, "backends", backends)
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if enable_proxy_protocol and not isinstance(enable_proxy_protocol, str):
            raise TypeError("Expected argument 'enable_proxy_protocol' to be a str")
        pulumi.set(__self__, "enable_proxy_protocol", enable_proxy_protocol)
        if external_traffic_policy and not isinstance(external_traffic_policy, str):
            raise TypeError("Expected argument 'external_traffic_policy' to be a str")
        pulumi.set(__self__, "external_traffic_policy", external_traffic_policy)
        if firewall_id and not isinstance(firewall_id, str):
            raise TypeError("Expected argument 'firewall_id' to be a str")
        pulumi.set(__self__, "firewall_id", firewall_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if private_ip and not isinstance(private_ip, str):
            raise TypeError("Expected argument 'private_ip' to be a str")
        pulumi.set(__self__, "private_ip", private_ip)
        if public_ip and not isinstance(public_ip, str):
            raise TypeError("Expected argument 'public_ip' to be a str")
        pulumi.set(__self__, "public_ip", public_ip)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if session_affinity and not isinstance(session_affinity, str):
            raise TypeError("Expected argument 'session_affinity' to be a str")
        pulumi.set(__self__, "session_affinity", session_affinity)
        if session_affinity_config_timeout and not isinstance(session_affinity_config_timeout, int):
            raise TypeError("Expected argument 'session_affinity_config_timeout' to be a int")
        pulumi.set(__self__, "session_affinity_config_timeout", session_affinity_config_timeout)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter
    def algorithm(self) -> str:
        return pulumi.get(self, "algorithm")

    @property
    @pulumi.getter
    def backends(self) -> Sequence['outputs.GetLoadBalancerBackendResult']:
        return pulumi.get(self, "backends")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="enableProxyProtocol")
    def enable_proxy_protocol(self) -> str:
        return pulumi.get(self, "enable_proxy_protocol")

    @property
    @pulumi.getter(name="externalTrafficPolicy")
    def external_traffic_policy(self) -> str:
        return pulumi.get(self, "external_traffic_policy")

    @property
    @pulumi.getter(name="firewallId")
    def firewall_id(self) -> str:
        return pulumi.get(self, "firewall_id")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> str:
        return pulumi.get(self, "private_ip")

    @property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> str:
        return pulumi.get(self, "public_ip")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="sessionAffinity")
    def session_affinity(self) -> str:
        return pulumi.get(self, "session_affinity")

    @property
    @pulumi.getter(name="sessionAffinityConfigTimeout")
    def session_affinity_config_timeout(self) -> int:
        return pulumi.get(self, "session_affinity_config_timeout")

    @property
    @pulumi.getter
    def state(self) -> str:
        return pulumi.get(self, "state")


class AwaitableGetLoadBalancerResult(GetLoadBalancerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLoadBalancerResult(
            algorithm=self.algorithm,
            backends=self.backends,
            cluster_id=self.cluster_id,
            enable_proxy_protocol=self.enable_proxy_protocol,
            external_traffic_policy=self.external_traffic_policy,
            firewall_id=self.firewall_id,
            id=self.id,
            name=self.name,
            private_ip=self.private_ip,
            public_ip=self.public_ip,
            region=self.region,
            session_affinity=self.session_affinity,
            session_affinity_config_timeout=self.session_affinity_config_timeout,
            state=self.state)


def get_load_balancer(id: Optional[str] = None,
                      name: Optional[str] = None,
                      region: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLoadBalancerResult:
    """
    Get information on a load balancer for use in other resources. This data source provides all of the load balancers properties as configured on your Civo account.

    An error will be raised if the provided load balancer name does not exist in your Civo account.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_civo as civo

    my_lb = civo.get_load_balancer(name="lb-name",
        region="LON1")
    pulumi.export("civoLoadbalancerOutput", my_lb.public_ip)
    ```
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['region'] = region
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('civo:index/getLoadBalancer:getLoadBalancer', __args__, opts=opts, typ=GetLoadBalancerResult).value

    return AwaitableGetLoadBalancerResult(
        algorithm=__ret__.algorithm,
        backends=__ret__.backends,
        cluster_id=__ret__.cluster_id,
        enable_proxy_protocol=__ret__.enable_proxy_protocol,
        external_traffic_policy=__ret__.external_traffic_policy,
        firewall_id=__ret__.firewall_id,
        id=__ret__.id,
        name=__ret__.name,
        private_ip=__ret__.private_ip,
        public_ip=__ret__.public_ip,
        region=__ret__.region,
        session_affinity=__ret__.session_affinity,
        session_affinity_config_timeout=__ret__.session_affinity_config_timeout,
        state=__ret__.state)


@_utilities.lift_output_func(get_load_balancer)
def get_load_balancer_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                             name: Optional[pulumi.Input[Optional[str]]] = None,
                             region: Optional[pulumi.Input[Optional[str]]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLoadBalancerResult]:
    """
    Get information on a load balancer for use in other resources. This data source provides all of the load balancers properties as configured on your Civo account.

    An error will be raised if the provided load balancer name does not exist in your Civo account.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_civo as civo

    my_lb = civo.get_load_balancer(name="lb-name",
        region="LON1")
    pulumi.export("civoLoadbalancerOutput", my_lb.public_ip)
    ```
    """
    ...

# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetNetworkResult',
    'AwaitableGetNetworkResult',
    'get_network',
    'get_network_output',
]

@pulumi.output_type
class GetNetworkResult:
    """
    A collection of values returned by getNetwork.
    """
    def __init__(__self__, default=None, id=None, label=None, name=None, region=None):
        if default and not isinstance(default, bool):
            raise TypeError("Expected argument 'default' to be a bool")
        pulumi.set(__self__, "default", default)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if label and not isinstance(label, str):
            raise TypeError("Expected argument 'label' to be a str")
        pulumi.set(__self__, "label", label)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter
    def default(self) -> bool:
        """
        If is the default network
        """
        return pulumi.get(self, "default")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def label(self) -> Optional[str]:
        """
        The label of an existing network
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the network
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        """
        The region of an existing network
        """
        return pulumi.get(self, "region")


class AwaitableGetNetworkResult(GetNetworkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkResult(
            default=self.default,
            id=self.id,
            label=self.label,
            name=self.name,
            region=self.region)


def get_network(id: Optional[str] = None,
                label: Optional[str] = None,
                region: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkResult:
    """
    Retrieve information about a network for use in other resources.

    This data source provides all of the network's properties as configured on your Civo account.

    Networks may be looked up by id or label, and you can optionally pass region if you want to make a lookup for an expecific network inside that region.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_civo as civo

    test = civo.get_network(label="test-network",
        region="NYC1")
    ```


    :param str id: The ID of this resource.
    :param str label: The label of an existing network
    :param str region: The region of an existing network
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['label'] = label
    __args__['region'] = region
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('civo:index/getNetwork:getNetwork', __args__, opts=opts, typ=GetNetworkResult).value

    return AwaitableGetNetworkResult(
        default=__ret__.default,
        id=__ret__.id,
        label=__ret__.label,
        name=__ret__.name,
        region=__ret__.region)


@_utilities.lift_output_func(get_network)
def get_network_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                       label: Optional[pulumi.Input[Optional[str]]] = None,
                       region: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkResult]:
    """
    Retrieve information about a network for use in other resources.

    This data source provides all of the network's properties as configured on your Civo account.

    Networks may be looked up by id or label, and you can optionally pass region if you want to make a lookup for an expecific network inside that region.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_civo as civo

    test = civo.get_network(label="test-network",
        region="NYC1")
    ```


    :param str id: The ID of this resource.
    :param str label: The label of an existing network
    :param str region: The region of an existing network
    """
    ...

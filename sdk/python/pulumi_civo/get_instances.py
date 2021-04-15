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

__all__ = [
    'GetInstancesResult',
    'AwaitableGetInstancesResult',
    'get_instances',
]

@pulumi.output_type
class GetInstancesResult:
    """
    A collection of values returned by getInstances.
    """
    def __init__(__self__, filters=None, id=None, instances=None, sorts=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instances and not isinstance(instances, list):
            raise TypeError("Expected argument 'instances' to be a list")
        pulumi.set(__self__, "instances", instances)
        if sorts and not isinstance(sorts, list):
            raise TypeError("Expected argument 'sorts' to be a list")
        pulumi.set(__self__, "sorts", sorts)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetInstancesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def instances(self) -> Sequence['outputs.GetInstancesInstanceResult']:
        """
        A list of Instances satisfying any `filter` and `sort` criteria. Each instance has the following attributes:
        """
        return pulumi.get(self, "instances")

    @property
    @pulumi.getter
    def sorts(self) -> Optional[Sequence['outputs.GetInstancesSortResult']]:
        return pulumi.get(self, "sorts")


class AwaitableGetInstancesResult(GetInstancesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstancesResult(
            filters=self.filters,
            id=self.id,
            instances=self.instances,
            sorts=self.sorts)


def get_instances(filters: Optional[Sequence[pulumi.InputType['GetInstancesFilterArgs']]] = None,
                  sorts: Optional[Sequence[pulumi.InputType['GetInstancesSortArgs']]] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstancesResult:
    """
    Use this data source to access information about an existing resource.

    :param Sequence[pulumi.InputType['GetInstancesFilterArgs']] filters: Filter the results.
           The `filter` block is documented below.
    :param Sequence[pulumi.InputType['GetInstancesSortArgs']] sorts: Sort the results.
           The `sort` block is documented below.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['sorts'] = sorts
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('civo:index/getInstances:getInstances', __args__, opts=opts, typ=GetInstancesResult).value

    return AwaitableGetInstancesResult(
        filters=__ret__.filters,
        id=__ret__.id,
        instances=__ret__.instances,
        sorts=__ret__.sorts)

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
    'GetInstancesSizeResult',
    'AwaitableGetInstancesSizeResult',
    'get_instances_size',
    'get_instances_size_output',
]

@pulumi.output_type
class GetInstancesSizeResult:
    """
    A collection of values returned by getInstancesSize.
    """
    def __init__(__self__, filters=None, id=None, sizes=None, sorts=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if sizes and not isinstance(sizes, list):
            raise TypeError("Expected argument 'sizes' to be a list")
        pulumi.set(__self__, "sizes", sizes)
        if sorts and not isinstance(sorts, list):
            raise TypeError("Expected argument 'sorts' to be a list")
        pulumi.set(__self__, "sorts", sorts)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetInstancesSizeFilterResult']]:
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
    def sizes(self) -> Sequence['outputs.GetInstancesSizeSizeResult']:
        return pulumi.get(self, "sizes")

    @property
    @pulumi.getter
    def sorts(self) -> Optional[Sequence['outputs.GetInstancesSizeSortResult']]:
        return pulumi.get(self, "sorts")


class AwaitableGetInstancesSizeResult(GetInstancesSizeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstancesSizeResult(
            filters=self.filters,
            id=self.id,
            sizes=self.sizes,
            sorts=self.sorts)


def get_instances_size(filters: Optional[Sequence[pulumi.InputType['GetInstancesSizeFilterArgs']]] = None,
                       sorts: Optional[Sequence[pulumi.InputType['GetInstancesSizeSortArgs']]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstancesSizeResult:
    """
    Retrieves information about the instance sizes that Civo supports, with the ability to filter the results.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['sorts'] = sorts
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('civo:index/getInstancesSize:getInstancesSize', __args__, opts=opts, typ=GetInstancesSizeResult).value

    return AwaitableGetInstancesSizeResult(
        filters=__ret__.filters,
        id=__ret__.id,
        sizes=__ret__.sizes,
        sorts=__ret__.sorts)


@_utilities.lift_output_func(get_instances_size)
def get_instances_size_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetInstancesSizeFilterArgs']]]]] = None,
                              sorts: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetInstancesSizeSortArgs']]]]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstancesSizeResult]:
    """
    Retrieves information about the instance sizes that Civo supports, with the ability to filter the results.
    """
    ...

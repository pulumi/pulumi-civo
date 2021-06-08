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
    'GetRegionResult',
    'AwaitableGetRegionResult',
    'get_region',
]

@pulumi.output_type
class GetRegionResult:
    """
    A collection of values returned by getRegion.
    """
    def __init__(__self__, filters=None, id=None, regions=None, sorts=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if regions and not isinstance(regions, list):
            raise TypeError("Expected argument 'regions' to be a list")
        pulumi.set(__self__, "regions", regions)
        if sorts and not isinstance(sorts, list):
            raise TypeError("Expected argument 'sorts' to be a list")
        pulumi.set(__self__, "sorts", sorts)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetRegionFilterResult']]:
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
    def regions(self) -> Sequence['outputs.GetRegionRegionResult']:
        return pulumi.get(self, "regions")

    @property
    @pulumi.getter
    def sorts(self) -> Optional[Sequence['outputs.GetRegionSortResult']]:
        return pulumi.get(self, "sorts")


class AwaitableGetRegionResult(GetRegionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRegionResult(
            filters=self.filters,
            id=self.id,
            regions=self.regions,
            sorts=self.sorts)


def get_region(filters: Optional[Sequence[pulumi.InputType['GetRegionFilterArgs']]] = None,
               sorts: Optional[Sequence[pulumi.InputType['GetRegionSortArgs']]] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRegionResult:
    """
    Retrieves information about the Region that Civo supports,
    with the ability to filter the results.


    :param Sequence[pulumi.InputType['GetRegionFilterArgs']] filters: Filter the results.
           The `filter` block is documented below.
    :param Sequence[pulumi.InputType['GetRegionSortArgs']] sorts: Sort the results.
           The `sort` block is documented below.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['sorts'] = sorts
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('civo:index/getRegion:getRegion', __args__, opts=opts, typ=GetRegionResult).value

    return AwaitableGetRegionResult(
        filters=__ret__.filters,
        id=__ret__.id,
        regions=__ret__.regions,
        sorts=__ret__.sorts)

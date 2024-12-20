# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetDiskImageResult',
    'AwaitableGetDiskImageResult',
    'get_disk_image',
    'get_disk_image_output',
]

@pulumi.output_type
class GetDiskImageResult:
    """
    A collection of values returned by getDiskImage.
    """
    def __init__(__self__, diskimages=None, filters=None, id=None, region=None, sorts=None):
        if diskimages and not isinstance(diskimages, list):
            raise TypeError("Expected argument 'diskimages' to be a list")
        pulumi.set(__self__, "diskimages", diskimages)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if sorts and not isinstance(sorts, list):
            raise TypeError("Expected argument 'sorts' to be a list")
        pulumi.set(__self__, "sorts", sorts)

    @property
    @pulumi.getter
    def diskimages(self) -> Sequence['outputs.GetDiskImageDiskimageResult']:
        return pulumi.get(self, "diskimages")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetDiskImageFilterResult']]:
        """
        One or more key/value pairs on which to filter results
        """
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
    def region(self) -> Optional[str]:
        """
        If is used, all disk image will be from this region. Required if no region is set in provider.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def sorts(self) -> Optional[Sequence['outputs.GetDiskImageSortResult']]:
        """
        One or more key/direction pairs on which to sort results
        """
        return pulumi.get(self, "sorts")


class AwaitableGetDiskImageResult(GetDiskImageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDiskImageResult(
            diskimages=self.diskimages,
            filters=self.filters,
            id=self.id,
            region=self.region,
            sorts=self.sorts)


def get_disk_image(filters: Optional[Sequence[Union['GetDiskImageFilterArgs', 'GetDiskImageFilterArgsDict']]] = None,
                   region: Optional[str] = None,
                   sorts: Optional[Sequence[Union['GetDiskImageSortArgs', 'GetDiskImageSortArgsDict']]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDiskImageResult:
    """
    Get information on an disk image for use in other resources (e.g. creating a instance) with the ability to filter the results.


    :param Sequence[Union['GetDiskImageFilterArgs', 'GetDiskImageFilterArgsDict']] filters: One or more key/value pairs on which to filter results
    :param str region: If is used, all disk image will be from this region. Required if no region is set in provider.
    :param Sequence[Union['GetDiskImageSortArgs', 'GetDiskImageSortArgsDict']] sorts: One or more key/direction pairs on which to sort results
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['region'] = region
    __args__['sorts'] = sorts
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('civo:index/getDiskImage:getDiskImage', __args__, opts=opts, typ=GetDiskImageResult).value

    return AwaitableGetDiskImageResult(
        diskimages=pulumi.get(__ret__, 'diskimages'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        region=pulumi.get(__ret__, 'region'),
        sorts=pulumi.get(__ret__, 'sorts'))
def get_disk_image_output(filters: Optional[pulumi.Input[Optional[Sequence[Union['GetDiskImageFilterArgs', 'GetDiskImageFilterArgsDict']]]]] = None,
                          region: Optional[pulumi.Input[Optional[str]]] = None,
                          sorts: Optional[pulumi.Input[Optional[Sequence[Union['GetDiskImageSortArgs', 'GetDiskImageSortArgsDict']]]]] = None,
                          opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetDiskImageResult]:
    """
    Get information on an disk image for use in other resources (e.g. creating a instance) with the ability to filter the results.


    :param Sequence[Union['GetDiskImageFilterArgs', 'GetDiskImageFilterArgsDict']] filters: One or more key/value pairs on which to filter results
    :param str region: If is used, all disk image will be from this region. Required if no region is set in provider.
    :param Sequence[Union['GetDiskImageSortArgs', 'GetDiskImageSortArgsDict']] sorts: One or more key/direction pairs on which to sort results
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['region'] = region
    __args__['sorts'] = sorts
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('civo:index/getDiskImage:getDiskImage', __args__, opts=opts, typ=GetDiskImageResult)
    return __ret__.apply(lambda __response__: GetDiskImageResult(
        diskimages=pulumi.get(__response__, 'diskimages'),
        filters=pulumi.get(__response__, 'filters'),
        id=pulumi.get(__response__, 'id'),
        region=pulumi.get(__response__, 'region'),
        sorts=pulumi.get(__response__, 'sorts')))

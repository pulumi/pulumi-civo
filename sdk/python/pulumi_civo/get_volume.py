# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetVolumeResult',
    'AwaitableGetVolumeResult',
    'get_volume',
    'get_volume_output',
]

@pulumi.output_type
class GetVolumeResult:
    """
    A collection of values returned by getVolume.
    """
    def __init__(__self__, created_at=None, id=None, mount_point=None, name=None, region=None, size_gb=None):
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if mount_point and not isinstance(mount_point, str):
            raise TypeError("Expected argument 'mount_point' to be a str")
        pulumi.set(__self__, "mount_point", mount_point)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if size_gb and not isinstance(size_gb, int):
            raise TypeError("Expected argument 'size_gb' to be a int")
        pulumi.set(__self__, "size_gb", size_gb)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="mountPoint")
    def mount_point(self) -> str:
        return pulumi.get(self, "mount_point")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> int:
        return pulumi.get(self, "size_gb")


class AwaitableGetVolumeResult(GetVolumeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVolumeResult(
            created_at=self.created_at,
            id=self.id,
            mount_point=self.mount_point,
            name=self.name,
            region=self.region,
            size_gb=self.size_gb)


def get_volume(id: Optional[str] = None,
               name: Optional[str] = None,
               region: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVolumeResult:
    """
    Get information on a volume for use in other resources. This data source provides all of the volumes properties as configured on your Civo account.

    An error will be raised if the provided volume name does not exist in your Civo account.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_civo as civo

    mysql = civo.get_volume(name="database-mysql")
    ```
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['region'] = region
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('civo:index/getVolume:getVolume', __args__, opts=opts, typ=GetVolumeResult).value

    return AwaitableGetVolumeResult(
        created_at=__ret__.created_at,
        id=__ret__.id,
        mount_point=__ret__.mount_point,
        name=__ret__.name,
        region=__ret__.region,
        size_gb=__ret__.size_gb)


@_utilities.lift_output_func(get_volume)
def get_volume_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                      name: Optional[pulumi.Input[Optional[str]]] = None,
                      region: Optional[pulumi.Input[Optional[str]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVolumeResult]:
    """
    Get information on a volume for use in other resources. This data source provides all of the volumes properties as configured on your Civo account.

    An error will be raised if the provided volume name does not exist in your Civo account.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_civo as civo

    mysql = civo.get_volume(name="database-mysql")
    ```
    """
    ...

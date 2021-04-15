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
]

@pulumi.output_type
class GetVolumeResult:
    """
    A collection of values returned by getVolume.
    """
    def __init__(__self__, bootable=None, created_at=None, id=None, mount_point=None, name=None, size_gb=None):
        if bootable and not isinstance(bootable, bool):
            raise TypeError("Expected argument 'bootable' to be a bool")
        pulumi.set(__self__, "bootable", bootable)
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
        if size_gb and not isinstance(size_gb, int):
            raise TypeError("Expected argument 'size_gb' to be a int")
        pulumi.set(__self__, "size_gb", size_gb)

    @property
    @pulumi.getter
    def bootable(self) -> bool:
        """
        if is bootable or not.
        """
        return pulumi.get(self, "bootable")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        The date of the creation of the volume.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The unique identifier for the volume.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="mountPoint")
    def mount_point(self) -> str:
        """
        The mount point of the volume.
        """
        return pulumi.get(self, "mount_point")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of the volume.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> int:
        """
        The size of the volume.
        """
        return pulumi.get(self, "size_gb")


class AwaitableGetVolumeResult(GetVolumeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVolumeResult(
            bootable=self.bootable,
            created_at=self.created_at,
            id=self.id,
            mount_point=self.mount_point,
            name=self.name,
            size_gb=self.size_gb)


def get_volume(id: Optional[str] = None,
               name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVolumeResult:
    """
    Use this data source to access information about an existing resource.

    :param str id: The unique identifier for the volume.
    :param str name: The name of the volume.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('civo:index/getVolume:getVolume', __args__, opts=opts, typ=GetVolumeResult).value

    return AwaitableGetVolumeResult(
        bootable=__ret__.bootable,
        created_at=__ret__.created_at,
        id=__ret__.id,
        mount_point=__ret__.mount_point,
        name=__ret__.name,
        size_gb=__ret__.size_gb)

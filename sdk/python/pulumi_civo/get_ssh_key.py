# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetSshKeyResult',
    'AwaitableGetSshKeyResult',
    'get_ssh_key',
    'get_ssh_key_output',
]

@pulumi.output_type
class GetSshKeyResult:
    """
    A collection of values returned by getSshKey.
    """
    def __init__(__self__, fingerprint=None, id=None, name=None):
        if fingerprint and not isinstance(fingerprint, str):
            raise TypeError("Expected argument 'fingerprint' to be a str")
        pulumi.set(__self__, "fingerprint", fingerprint)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def fingerprint(self) -> str:
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")


class AwaitableGetSshKeyResult(GetSshKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSshKeyResult(
            fingerprint=self.fingerprint,
            id=self.id,
            name=self.name)


def get_ssh_key(id: Optional[str] = None,
                name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSshKeyResult:
    """
    Get information on a SSH key. This data source provides the name, and fingerprint as configured on your Civo account.

    An error will be raised if the provided SSH key name does not exist in your Civo account.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('civo:index/getSshKey:getSshKey', __args__, opts=opts, typ=GetSshKeyResult).value

    return AwaitableGetSshKeyResult(
        fingerprint=__ret__.fingerprint,
        id=__ret__.id,
        name=__ret__.name)


@_utilities.lift_output_func(get_ssh_key)
def get_ssh_key_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                       name: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSshKeyResult]:
    """
    Get information on a SSH key. This data source provides the name, and fingerprint as configured on your Civo account.

    An error will be raised if the provided SSH key name does not exist in your Civo account.
    """
    ...

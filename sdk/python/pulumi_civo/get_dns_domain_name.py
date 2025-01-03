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

__all__ = [
    'GetDnsDomainNameResult',
    'AwaitableGetDnsDomainNameResult',
    'get_dns_domain_name',
    'get_dns_domain_name_output',
]

@pulumi.output_type
class GetDnsDomainNameResult:
    """
    A collection of values returned by getDnsDomainName.
    """
    def __init__(__self__, id=None, name=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the domain
        """
        return pulumi.get(self, "name")


class AwaitableGetDnsDomainNameResult(GetDnsDomainNameResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDnsDomainNameResult(
            id=self.id,
            name=self.name)


def get_dns_domain_name(id: Optional[str] = None,
                        name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDnsDomainNameResult:
    """
    Get information on a domain. This data source provides the name and the id.

    An error will be raised if the provided domain name is not in your Civo account.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_civo as civo

    domain = civo.get_dns_domain_name(name="domain.com")
    pulumi.export("domainOutput", domain.name)
    pulumi.export("domainIdOutput", domain.id)
    ```


    :param str id: The ID of this resource.
    :param str name: The name of the domain
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('civo:index/getDnsDomainName:getDnsDomainName', __args__, opts=opts, typ=GetDnsDomainNameResult).value

    return AwaitableGetDnsDomainNameResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'))
def get_dns_domain_name_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                               name: Optional[pulumi.Input[Optional[str]]] = None,
                               opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetDnsDomainNameResult]:
    """
    Get information on a domain. This data source provides the name and the id.

    An error will be raised if the provided domain name is not in your Civo account.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_civo as civo

    domain = civo.get_dns_domain_name(name="domain.com")
    pulumi.export("domainOutput", domain.name)
    pulumi.export("domainIdOutput", domain.id)
    ```


    :param str id: The ID of this resource.
    :param str name: The name of the domain
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('civo:index/getDnsDomainName:getDnsDomainName', __args__, opts=opts, typ=GetDnsDomainNameResult)
    return __ret__.apply(lambda __response__: GetDnsDomainNameResult(
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name')))

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
    'GetDnsDomainRecordResult',
    'AwaitableGetDnsDomainRecordResult',
    'get_dns_domain_record',
    'get_dns_domain_record_output',
]

@pulumi.output_type
class GetDnsDomainRecordResult:
    """
    A collection of values returned by getDnsDomainRecord.
    """
    def __init__(__self__, account_id=None, created_at=None, domain_id=None, id=None, name=None, priority=None, ttl=None, type=None, updated_at=None, value=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if domain_id and not isinstance(domain_id, str):
            raise TypeError("Expected argument 'domain_id' to be a str")
        pulumi.set(__self__, "domain_id", domain_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if priority and not isinstance(priority, int):
            raise TypeError("Expected argument 'priority' to be a int")
        pulumi.set(__self__, "priority", priority)
        if ttl and not isinstance(ttl, int):
            raise TypeError("Expected argument 'ttl' to be a int")
        pulumi.set(__self__, "ttl", ttl)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)
        if value and not isinstance(value, str):
            raise TypeError("Expected argument 'value' to be a str")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        """
        The ID account of the domain
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        The date when it was created in UTC format
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> str:
        """
        The ID of the domain
        """
        return pulumi.get(self, "domain_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the record
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def priority(self) -> int:
        """
        The priority of the record
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def ttl(self) -> int:
        """
        How long caching DNS servers should cache this record
        """
        return pulumi.get(self, "ttl")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The choice of record type from A, CNAME, MX, SRV or TXT
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        """
        The date when it was updated in UTC format
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record
        """
        return pulumi.get(self, "value")


class AwaitableGetDnsDomainRecordResult(GetDnsDomainRecordResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDnsDomainRecordResult(
            account_id=self.account_id,
            created_at=self.created_at,
            domain_id=self.domain_id,
            id=self.id,
            name=self.name,
            priority=self.priority,
            ttl=self.ttl,
            type=self.type,
            updated_at=self.updated_at,
            value=self.value)


def get_dns_domain_record(domain_id: Optional[str] = None,
                          name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDnsDomainRecordResult:
    """
    Get information on a DNS record. This data source provides the name, TTL, and zone file as configured on your Civo account.

    An error will be raised if the provided domain name or record are not in your Civo account.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_civo as civo

    domain = civo.get_dns_domain_name(name="domain.com")
    www = civo.get_dns_domain_record(domain_id=domain.id,
        name="www")
    pulumi.export("recordType", www.type)
    pulumi.export("recordTtl", www.ttl)
    ```


    :param str domain_id: The ID of the domain
    :param str name: The name of the record
    """
    __args__ = dict()
    __args__['domainId'] = domain_id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('civo:index/getDnsDomainRecord:getDnsDomainRecord', __args__, opts=opts, typ=GetDnsDomainRecordResult).value

    return AwaitableGetDnsDomainRecordResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        created_at=pulumi.get(__ret__, 'created_at'),
        domain_id=pulumi.get(__ret__, 'domain_id'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        priority=pulumi.get(__ret__, 'priority'),
        ttl=pulumi.get(__ret__, 'ttl'),
        type=pulumi.get(__ret__, 'type'),
        updated_at=pulumi.get(__ret__, 'updated_at'),
        value=pulumi.get(__ret__, 'value'))
def get_dns_domain_record_output(domain_id: Optional[pulumi.Input[str]] = None,
                                 name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetDnsDomainRecordResult]:
    """
    Get information on a DNS record. This data source provides the name, TTL, and zone file as configured on your Civo account.

    An error will be raised if the provided domain name or record are not in your Civo account.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_civo as civo

    domain = civo.get_dns_domain_name(name="domain.com")
    www = civo.get_dns_domain_record(domain_id=domain.id,
        name="www")
    pulumi.export("recordType", www.type)
    pulumi.export("recordTtl", www.ttl)
    ```


    :param str domain_id: The ID of the domain
    :param str name: The name of the record
    """
    __args__ = dict()
    __args__['domainId'] = domain_id
    __args__['name'] = name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('civo:index/getDnsDomainRecord:getDnsDomainRecord', __args__, opts=opts, typ=GetDnsDomainRecordResult)
    return __ret__.apply(lambda __response__: GetDnsDomainRecordResult(
        account_id=pulumi.get(__response__, 'account_id'),
        created_at=pulumi.get(__response__, 'created_at'),
        domain_id=pulumi.get(__response__, 'domain_id'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        priority=pulumi.get(__response__, 'priority'),
        ttl=pulumi.get(__response__, 'ttl'),
        type=pulumi.get(__response__, 'type'),
        updated_at=pulumi.get(__response__, 'updated_at'),
        value=pulumi.get(__response__, 'value')))

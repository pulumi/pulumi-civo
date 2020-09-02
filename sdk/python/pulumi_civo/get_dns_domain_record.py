# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from . import _utilities, _tables

__all__ = [
    'GetDnsDomainRecordResult',
    'AwaitableGetDnsDomainRecordResult',
    'get_dns_domain_record',
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
        if priority and not isinstance(priority, float):
            raise TypeError("Expected argument 'priority' to be a float")
        pulumi.set(__self__, "priority", priority)
        if ttl and not isinstance(ttl, float):
            raise TypeError("Expected argument 'ttl' to be a float")
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
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> str:
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
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def priority(self) -> float:
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def ttl(self) -> float:
        return pulumi.get(self, "ttl")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter
    def value(self) -> str:
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
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['domainId'] = domain_id
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('civo:index/getDnsDomainRecord:getDnsDomainRecord', __args__, opts=opts, typ=GetDnsDomainRecordResult).value

    return AwaitableGetDnsDomainRecordResult(
        account_id=__ret__.account_id,
        created_at=__ret__.created_at,
        domain_id=__ret__.domain_id,
        id=__ret__.id,
        name=__ret__.name,
        priority=__ret__.priority,
        ttl=__ret__.ttl,
        type=__ret__.type,
        updated_at=__ret__.updated_at,
        value=__ret__.value)

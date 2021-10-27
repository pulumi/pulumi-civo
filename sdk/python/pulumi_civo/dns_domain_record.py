# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DnsDomainRecordArgs', 'DnsDomainRecord']

@pulumi.input_type
class DnsDomainRecordArgs:
    def __init__(__self__, *,
                 domain_id: pulumi.Input[str],
                 ttl: pulumi.Input[int],
                 type: pulumi.Input[str],
                 value: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a DnsDomainRecord resource.
        :param pulumi.Input[str] domain_id: ID from domain name
        :param pulumi.Input[int] ttl: How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified
               is 600)
        :param pulumi.Input[str] type: The choice of RR type from a, cname, mx or txt
        :param pulumi.Input[str] value: The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record
        :param pulumi.Input[str] name: The portion before the domain name (e.g. www) or an @ for the apex/root domain (you cannot use an A record with an
               amex/root domain)
        :param pulumi.Input[int] priority: Useful for MX records only, the priority mail should be attempted it (defaults to 10)
        """
        pulumi.set(__self__, "domain_id", domain_id)
        pulumi.set(__self__, "ttl", ttl)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "value", value)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Input[str]:
        """
        ID from domain name
        """
        return pulumi.get(self, "domain_id")

    @domain_id.setter
    def domain_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_id", value)

    @property
    @pulumi.getter
    def ttl(self) -> pulumi.Input[int]:
        """
        How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified
        is 600)
        """
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: pulumi.Input[int]):
        pulumi.set(self, "ttl", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The choice of RR type from a, cname, mx or txt
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The portion before the domain name (e.g. www) or an @ for the apex/root domain (you cannot use an A record with an
        amex/root domain)
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        Useful for MX records only, the priority mail should be attempted it (defaults to 10)
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)


@pulumi.input_type
class _DnsDomainRecordState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 domain_id: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DnsDomainRecord resources.
        :param pulumi.Input[str] account_id: The account ID of this resource
        :param pulumi.Input[str] created_at: Timestamp when this resource was created
        :param pulumi.Input[str] domain_id: ID from domain name
        :param pulumi.Input[str] id: The ID of this resource.
        :param pulumi.Input[str] name: The portion before the domain name (e.g. www) or an @ for the apex/root domain (you cannot use an A record with an
               amex/root domain)
        :param pulumi.Input[int] priority: Useful for MX records only, the priority mail should be attempted it (defaults to 10)
        :param pulumi.Input[int] ttl: How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified
               is 600)
        :param pulumi.Input[str] type: The choice of RR type from a, cname, mx or txt
        :param pulumi.Input[str] updated_at: Timestamp when this resource was updated
        :param pulumi.Input[str] value: The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if domain_id is not None:
            pulumi.set(__self__, "domain_id", domain_id)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if ttl is not None:
            pulumi.set(__self__, "ttl", ttl)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The account ID of this resource
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        Timestamp when this resource was created
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID from domain name
        """
        return pulumi.get(self, "domain_id")

    @domain_id.setter
    def domain_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_id", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The portion before the domain name (e.g. www) or an @ for the apex/root domain (you cannot use an A record with an
        amex/root domain)
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        Useful for MX records only, the priority mail should be attempted it (defaults to 10)
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[int]]:
        """
        How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified
        is 600)
        """
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ttl", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The choice of RR type from a, cname, mx or txt
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[str]]:
        """
        Timestamp when this resource was updated
        """
        return pulumi.get(self, "updated_at")

    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_at", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


class DnsDomainRecord(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Civo DNS domain record resource.

        ## Schema

        ### Required

        - **domain_id** (String) ID from domain name
        - **name** (String) The portion before the domain name (e.g. www) or an @ for the apex/root domain (you cannot use an A record with an amex/root domain)
        - **ttl** (Number) How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified is 600)
        - **type** (String) The choice of RR type from a, cname, mx or txt
        - **value** (String) The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record

        ### Optional

        - **priority** (Number) Useful for MX records only, the priority mail should be attempted it (defaults to 10)

        ### Read-Only

        - **account_id** (String) The account ID of this resource
        - **created_at** (String) Timestamp when this resource was created
        - **id** (String) The ID of this resource.
        - **updated_at** (String) Timestamp when this resource was updated

        ## Import

        Import is supported using the following syntax# using domain_id:domain_record_id

        ```sh
         $ pulumi import civo:index/dnsDomainRecord:DnsDomainRecord www a3cd6832-9577-4017-afd7-17d239fc0bf0:c9a39d14-ee1b-4870-8fb0-a2d4f465e822
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_id: ID from domain name
        :param pulumi.Input[str] name: The portion before the domain name (e.g. www) or an @ for the apex/root domain (you cannot use an A record with an
               amex/root domain)
        :param pulumi.Input[int] priority: Useful for MX records only, the priority mail should be attempted it (defaults to 10)
        :param pulumi.Input[int] ttl: How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified
               is 600)
        :param pulumi.Input[str] type: The choice of RR type from a, cname, mx or txt
        :param pulumi.Input[str] value: The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DnsDomainRecordArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Civo DNS domain record resource.

        ## Schema

        ### Required

        - **domain_id** (String) ID from domain name
        - **name** (String) The portion before the domain name (e.g. www) or an @ for the apex/root domain (you cannot use an A record with an amex/root domain)
        - **ttl** (Number) How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified is 600)
        - **type** (String) The choice of RR type from a, cname, mx or txt
        - **value** (String) The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record

        ### Optional

        - **priority** (Number) Useful for MX records only, the priority mail should be attempted it (defaults to 10)

        ### Read-Only

        - **account_id** (String) The account ID of this resource
        - **created_at** (String) Timestamp when this resource was created
        - **id** (String) The ID of this resource.
        - **updated_at** (String) Timestamp when this resource was updated

        ## Import

        Import is supported using the following syntax# using domain_id:domain_record_id

        ```sh
         $ pulumi import civo:index/dnsDomainRecord:DnsDomainRecord www a3cd6832-9577-4017-afd7-17d239fc0bf0:c9a39d14-ee1b-4870-8fb0-a2d4f465e822
        ```

        :param str resource_name: The name of the resource.
        :param DnsDomainRecordArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DnsDomainRecordArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DnsDomainRecordArgs.__new__(DnsDomainRecordArgs)

            if domain_id is None and not opts.urn:
                raise TypeError("Missing required property 'domain_id'")
            __props__.__dict__["domain_id"] = domain_id
            __props__.__dict__["name"] = name
            __props__.__dict__["priority"] = priority
            if ttl is None and not opts.urn:
                raise TypeError("Missing required property 'ttl'")
            __props__.__dict__["ttl"] = ttl
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            if value is None and not opts.urn:
                raise TypeError("Missing required property 'value'")
            __props__.__dict__["value"] = value
            __props__.__dict__["account_id"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["id"] = None
            __props__.__dict__["updated_at"] = None
        super(DnsDomainRecord, __self__).__init__(
            'civo:index/dnsDomainRecord:DnsDomainRecord',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            domain_id: Optional[pulumi.Input[str]] = None,
            id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            ttl: Optional[pulumi.Input[int]] = None,
            type: Optional[pulumi.Input[str]] = None,
            updated_at: Optional[pulumi.Input[str]] = None,
            value: Optional[pulumi.Input[str]] = None) -> 'DnsDomainRecord':
        """
        Get an existing DnsDomainRecord resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account ID of this resource
        :param pulumi.Input[str] created_at: Timestamp when this resource was created
        :param pulumi.Input[str] domain_id: ID from domain name
        :param pulumi.Input[str] id: The ID of this resource.
        :param pulumi.Input[str] name: The portion before the domain name (e.g. www) or an @ for the apex/root domain (you cannot use an A record with an
               amex/root domain)
        :param pulumi.Input[int] priority: Useful for MX records only, the priority mail should be attempted it (defaults to 10)
        :param pulumi.Input[int] ttl: How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified
               is 600)
        :param pulumi.Input[str] type: The choice of RR type from a, cname, mx or txt
        :param pulumi.Input[str] updated_at: Timestamp when this resource was updated
        :param pulumi.Input[str] value: The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DnsDomainRecordState.__new__(_DnsDomainRecordState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["domain_id"] = domain_id
        __props__.__dict__["id"] = id
        __props__.__dict__["name"] = name
        __props__.__dict__["priority"] = priority
        __props__.__dict__["ttl"] = ttl
        __props__.__dict__["type"] = type
        __props__.__dict__["updated_at"] = updated_at
        __props__.__dict__["value"] = value
        return DnsDomainRecord(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        The account ID of this resource
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Timestamp when this resource was created
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Output[str]:
        """
        ID from domain name
        """
        return pulumi.get(self, "domain_id")

    @property
    @pulumi.getter
    def id(self) -> pulumi.Output[str]:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The portion before the domain name (e.g. www) or an @ for the apex/root domain (you cannot use an A record with an
        amex/root domain)
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[int]]:
        """
        Useful for MX records only, the priority mail should be attempted it (defaults to 10)
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def ttl(self) -> pulumi.Output[int]:
        """
        How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified
        is 600)
        """
        return pulumi.get(self, "ttl")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The choice of RR type from a, cname, mx or txt
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        Timestamp when this resource was updated
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        """
        The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record
        """
        return pulumi.get(self, "value")


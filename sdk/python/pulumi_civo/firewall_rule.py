# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['FirewallRuleArgs', 'FirewallRule']

@pulumi.input_type
class FirewallRuleArgs:
    def __init__(__self__, *,
                 cidrs: pulumi.Input[Sequence[pulumi.Input[str]]],
                 direction: pulumi.Input[str],
                 end_port: pulumi.Input[str],
                 firewall_id: pulumi.Input[str],
                 protocol: pulumi.Input[str],
                 start_port: pulumi.Input[str],
                 label: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a FirewallRule resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] cidrs: the IP address of the other end (i.e. not your instance) to affect, or a valid network CIDR (defaults to being globally applied, i.e. 0.0.0.0/0).
        :param pulumi.Input[str] direction: will this rule affect ingress traffic
        :param pulumi.Input[str] end_port: The end port where traffic to be allowed.
        :param pulumi.Input[str] firewall_id: The Firewall id
        :param pulumi.Input[str] protocol: This may be one of "tcp", "udp", or "icmp".
        :param pulumi.Input[str] start_port: The start port where traffic to be allowed.
        :param pulumi.Input[str] label: a string that will be the displayed name/reference for this rule (optional)
        """
        pulumi.set(__self__, "cidrs", cidrs)
        pulumi.set(__self__, "direction", direction)
        pulumi.set(__self__, "end_port", end_port)
        pulumi.set(__self__, "firewall_id", firewall_id)
        pulumi.set(__self__, "protocol", protocol)
        pulumi.set(__self__, "start_port", start_port)
        if label is not None:
            pulumi.set(__self__, "label", label)

    @property
    @pulumi.getter
    def cidrs(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        the IP address of the other end (i.e. not your instance) to affect, or a valid network CIDR (defaults to being globally applied, i.e. 0.0.0.0/0).
        """
        return pulumi.get(self, "cidrs")

    @cidrs.setter
    def cidrs(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "cidrs", value)

    @property
    @pulumi.getter
    def direction(self) -> pulumi.Input[str]:
        """
        will this rule affect ingress traffic
        """
        return pulumi.get(self, "direction")

    @direction.setter
    def direction(self, value: pulumi.Input[str]):
        pulumi.set(self, "direction", value)

    @property
    @pulumi.getter(name="endPort")
    def end_port(self) -> pulumi.Input[str]:
        """
        The end port where traffic to be allowed.
        """
        return pulumi.get(self, "end_port")

    @end_port.setter
    def end_port(self, value: pulumi.Input[str]):
        pulumi.set(self, "end_port", value)

    @property
    @pulumi.getter(name="firewallId")
    def firewall_id(self) -> pulumi.Input[str]:
        """
        The Firewall id
        """
        return pulumi.get(self, "firewall_id")

    @firewall_id.setter
    def firewall_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "firewall_id", value)

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[str]:
        """
        This may be one of "tcp", "udp", or "icmp".
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: pulumi.Input[str]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter(name="startPort")
    def start_port(self) -> pulumi.Input[str]:
        """
        The start port where traffic to be allowed.
        """
        return pulumi.get(self, "start_port")

    @start_port.setter
    def start_port(self, value: pulumi.Input[str]):
        pulumi.set(self, "start_port", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        """
        a string that will be the displayed name/reference for this rule (optional)
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)


@pulumi.input_type
class _FirewallRuleState:
    def __init__(__self__, *,
                 cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 direction: Optional[pulumi.Input[str]] = None,
                 end_port: Optional[pulumi.Input[str]] = None,
                 firewall_id: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 start_port: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering FirewallRule resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] cidrs: the IP address of the other end (i.e. not your instance) to affect, or a valid network CIDR (defaults to being globally applied, i.e. 0.0.0.0/0).
        :param pulumi.Input[str] direction: will this rule affect ingress traffic
        :param pulumi.Input[str] end_port: The end port where traffic to be allowed.
        :param pulumi.Input[str] firewall_id: The Firewall id
        :param pulumi.Input[str] label: a string that will be the displayed name/reference for this rule (optional)
        :param pulumi.Input[str] protocol: This may be one of "tcp", "udp", or "icmp".
        :param pulumi.Input[str] start_port: The start port where traffic to be allowed.
        """
        if cidrs is not None:
            pulumi.set(__self__, "cidrs", cidrs)
        if direction is not None:
            pulumi.set(__self__, "direction", direction)
        if end_port is not None:
            pulumi.set(__self__, "end_port", end_port)
        if firewall_id is not None:
            pulumi.set(__self__, "firewall_id", firewall_id)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)
        if start_port is not None:
            pulumi.set(__self__, "start_port", start_port)

    @property
    @pulumi.getter
    def cidrs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        the IP address of the other end (i.e. not your instance) to affect, or a valid network CIDR (defaults to being globally applied, i.e. 0.0.0.0/0).
        """
        return pulumi.get(self, "cidrs")

    @cidrs.setter
    def cidrs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "cidrs", value)

    @property
    @pulumi.getter
    def direction(self) -> Optional[pulumi.Input[str]]:
        """
        will this rule affect ingress traffic
        """
        return pulumi.get(self, "direction")

    @direction.setter
    def direction(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "direction", value)

    @property
    @pulumi.getter(name="endPort")
    def end_port(self) -> Optional[pulumi.Input[str]]:
        """
        The end port where traffic to be allowed.
        """
        return pulumi.get(self, "end_port")

    @end_port.setter
    def end_port(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_port", value)

    @property
    @pulumi.getter(name="firewallId")
    def firewall_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Firewall id
        """
        return pulumi.get(self, "firewall_id")

    @firewall_id.setter
    def firewall_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "firewall_id", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        """
        a string that will be the displayed name/reference for this rule (optional)
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[str]]:
        """
        This may be one of "tcp", "udp", or "icmp".
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter(name="startPort")
    def start_port(self) -> Optional[pulumi.Input[str]]:
        """
        The start port where traffic to be allowed.
        """
        return pulumi.get(self, "start_port")

    @start_port.setter
    def start_port(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_port", value)


class FirewallRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 direction: Optional[pulumi.Input[str]] = None,
                 end_port: Optional[pulumi.Input[str]] = None,
                 firewall_id: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 start_port: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Civo Cloud Firewall Rule resource.
        This can be used to create, modify, and delete Firewalls Rules.
        This resource don't have an update option because the backend don't have the
        support for that, so in this case we use ForceNew for all object in the resource.

        ## Import

        Firewalls can be imported using the firewall `firewall_id:firewall_rule_id`, e.g.

        ```sh
         $ pulumi import civo:index/firewallRule:FirewallRule http b8ecd2ab-2267-4a5e-8692-cbf1d32583e3:4b0022ee-00b2-4f81-a40d-b4f8728923a7
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] cidrs: the IP address of the other end (i.e. not your instance) to affect, or a valid network CIDR (defaults to being globally applied, i.e. 0.0.0.0/0).
        :param pulumi.Input[str] direction: will this rule affect ingress traffic
        :param pulumi.Input[str] end_port: The end port where traffic to be allowed.
        :param pulumi.Input[str] firewall_id: The Firewall id
        :param pulumi.Input[str] label: a string that will be the displayed name/reference for this rule (optional)
        :param pulumi.Input[str] protocol: This may be one of "tcp", "udp", or "icmp".
        :param pulumi.Input[str] start_port: The start port where traffic to be allowed.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FirewallRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Civo Cloud Firewall Rule resource.
        This can be used to create, modify, and delete Firewalls Rules.
        This resource don't have an update option because the backend don't have the
        support for that, so in this case we use ForceNew for all object in the resource.

        ## Import

        Firewalls can be imported using the firewall `firewall_id:firewall_rule_id`, e.g.

        ```sh
         $ pulumi import civo:index/firewallRule:FirewallRule http b8ecd2ab-2267-4a5e-8692-cbf1d32583e3:4b0022ee-00b2-4f81-a40d-b4f8728923a7
        ```

        :param str resource_name: The name of the resource.
        :param FirewallRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FirewallRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 direction: Optional[pulumi.Input[str]] = None,
                 end_port: Optional[pulumi.Input[str]] = None,
                 firewall_id: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 start_port: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FirewallRuleArgs.__new__(FirewallRuleArgs)

            if cidrs is None and not opts.urn:
                raise TypeError("Missing required property 'cidrs'")
            __props__.__dict__["cidrs"] = cidrs
            if direction is None and not opts.urn:
                raise TypeError("Missing required property 'direction'")
            __props__.__dict__["direction"] = direction
            if end_port is None and not opts.urn:
                raise TypeError("Missing required property 'end_port'")
            __props__.__dict__["end_port"] = end_port
            if firewall_id is None and not opts.urn:
                raise TypeError("Missing required property 'firewall_id'")
            __props__.__dict__["firewall_id"] = firewall_id
            __props__.__dict__["label"] = label
            if protocol is None and not opts.urn:
                raise TypeError("Missing required property 'protocol'")
            __props__.__dict__["protocol"] = protocol
            if start_port is None and not opts.urn:
                raise TypeError("Missing required property 'start_port'")
            __props__.__dict__["start_port"] = start_port
        super(FirewallRule, __self__).__init__(
            'civo:index/firewallRule:FirewallRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            direction: Optional[pulumi.Input[str]] = None,
            end_port: Optional[pulumi.Input[str]] = None,
            firewall_id: Optional[pulumi.Input[str]] = None,
            label: Optional[pulumi.Input[str]] = None,
            protocol: Optional[pulumi.Input[str]] = None,
            start_port: Optional[pulumi.Input[str]] = None) -> 'FirewallRule':
        """
        Get an existing FirewallRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] cidrs: the IP address of the other end (i.e. not your instance) to affect, or a valid network CIDR (defaults to being globally applied, i.e. 0.0.0.0/0).
        :param pulumi.Input[str] direction: will this rule affect ingress traffic
        :param pulumi.Input[str] end_port: The end port where traffic to be allowed.
        :param pulumi.Input[str] firewall_id: The Firewall id
        :param pulumi.Input[str] label: a string that will be the displayed name/reference for this rule (optional)
        :param pulumi.Input[str] protocol: This may be one of "tcp", "udp", or "icmp".
        :param pulumi.Input[str] start_port: The start port where traffic to be allowed.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FirewallRuleState.__new__(_FirewallRuleState)

        __props__.__dict__["cidrs"] = cidrs
        __props__.__dict__["direction"] = direction
        __props__.__dict__["end_port"] = end_port
        __props__.__dict__["firewall_id"] = firewall_id
        __props__.__dict__["label"] = label
        __props__.__dict__["protocol"] = protocol
        __props__.__dict__["start_port"] = start_port
        return FirewallRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def cidrs(self) -> pulumi.Output[Sequence[str]]:
        """
        the IP address of the other end (i.e. not your instance) to affect, or a valid network CIDR (defaults to being globally applied, i.e. 0.0.0.0/0).
        """
        return pulumi.get(self, "cidrs")

    @property
    @pulumi.getter
    def direction(self) -> pulumi.Output[str]:
        """
        will this rule affect ingress traffic
        """
        return pulumi.get(self, "direction")

    @property
    @pulumi.getter(name="endPort")
    def end_port(self) -> pulumi.Output[str]:
        """
        The end port where traffic to be allowed.
        """
        return pulumi.get(self, "end_port")

    @property
    @pulumi.getter(name="firewallId")
    def firewall_id(self) -> pulumi.Output[str]:
        """
        The Firewall id
        """
        return pulumi.get(self, "firewall_id")

    @property
    @pulumi.getter
    def label(self) -> pulumi.Output[Optional[str]]:
        """
        a string that will be the displayed name/reference for this rule (optional)
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[str]:
        """
        This may be one of "tcp", "udp", or "icmp".
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="startPort")
    def start_port(self) -> pulumi.Output[str]:
        """
        The start port where traffic to be allowed.
        """
        return pulumi.get(self, "start_port")


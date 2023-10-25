# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['FirewallRuleArgs', 'FirewallRule']

@pulumi.input_type
class FirewallRuleArgs:
    def __init__(__self__, *,
                 action: pulumi.Input[str],
                 cidrs: pulumi.Input[Sequence[pulumi.Input[str]]],
                 direction: pulumi.Input[str],
                 firewall_id: pulumi.Input[str],
                 end_port: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 start_port: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a FirewallRule resource.
        :param pulumi.Input[str] action: The action of the rule can be allow or deny. When we set the `action = 'allow'`, this is going to add a rule to allow traffic. Similarly, setting `action = 'deny'` will deny the traffic.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] cidrs: The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32 to open just for a specific IP address)
        :param pulumi.Input[str] direction: The direction of the rule can be ingress or egress
        :param pulumi.Input[str] firewall_id: The Firewall ID
        :param pulumi.Input[str] end_port: The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
        :param pulumi.Input[str] label: A string that will be the displayed name/reference for this rule
        :param pulumi.Input[str] protocol: The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
        :param pulumi.Input[str] region: The region for this rule
        :param pulumi.Input[str] start_port: The start of the port range to configure for this rule (or the single port if required)
        """
        FirewallRuleArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            action=action,
            cidrs=cidrs,
            direction=direction,
            firewall_id=firewall_id,
            end_port=end_port,
            label=label,
            protocol=protocol,
            region=region,
            start_port=start_port,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             action: Optional[pulumi.Input[str]] = None,
             cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             direction: Optional[pulumi.Input[str]] = None,
             firewall_id: Optional[pulumi.Input[str]] = None,
             end_port: Optional[pulumi.Input[str]] = None,
             label: Optional[pulumi.Input[str]] = None,
             protocol: Optional[pulumi.Input[str]] = None,
             region: Optional[pulumi.Input[str]] = None,
             start_port: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if action is None:
            raise TypeError("Missing 'action' argument")
        if cidrs is None:
            raise TypeError("Missing 'cidrs' argument")
        if direction is None:
            raise TypeError("Missing 'direction' argument")
        if firewall_id is None and 'firewallId' in kwargs:
            firewall_id = kwargs['firewallId']
        if firewall_id is None:
            raise TypeError("Missing 'firewall_id' argument")
        if end_port is None and 'endPort' in kwargs:
            end_port = kwargs['endPort']
        if start_port is None and 'startPort' in kwargs:
            start_port = kwargs['startPort']

        _setter("action", action)
        _setter("cidrs", cidrs)
        _setter("direction", direction)
        _setter("firewall_id", firewall_id)
        if end_port is not None:
            _setter("end_port", end_port)
        if label is not None:
            _setter("label", label)
        if protocol is not None:
            _setter("protocol", protocol)
        if region is not None:
            _setter("region", region)
        if start_port is not None:
            _setter("start_port", start_port)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Input[str]:
        """
        The action of the rule can be allow or deny. When we set the `action = 'allow'`, this is going to add a rule to allow traffic. Similarly, setting `action = 'deny'` will deny the traffic.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: pulumi.Input[str]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter
    def cidrs(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32 to open just for a specific IP address)
        """
        return pulumi.get(self, "cidrs")

    @cidrs.setter
    def cidrs(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "cidrs", value)

    @property
    @pulumi.getter
    def direction(self) -> pulumi.Input[str]:
        """
        The direction of the rule can be ingress or egress
        """
        return pulumi.get(self, "direction")

    @direction.setter
    def direction(self, value: pulumi.Input[str]):
        pulumi.set(self, "direction", value)

    @property
    @pulumi.getter(name="firewallId")
    def firewall_id(self) -> pulumi.Input[str]:
        """
        The Firewall ID
        """
        return pulumi.get(self, "firewall_id")

    @firewall_id.setter
    def firewall_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "firewall_id", value)

    @property
    @pulumi.getter(name="endPort")
    def end_port(self) -> Optional[pulumi.Input[str]]:
        """
        The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
        """
        return pulumi.get(self, "end_port")

    @end_port.setter
    def end_port(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_port", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        """
        A string that will be the displayed name/reference for this rule
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[str]]:
        """
        The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region for this rule
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="startPort")
    def start_port(self) -> Optional[pulumi.Input[str]]:
        """
        The start of the port range to configure for this rule (or the single port if required)
        """
        return pulumi.get(self, "start_port")

    @start_port.setter
    def start_port(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_port", value)


@pulumi.input_type
class _FirewallRuleState:
    def __init__(__self__, *,
                 action: Optional[pulumi.Input[str]] = None,
                 cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 direction: Optional[pulumi.Input[str]] = None,
                 end_port: Optional[pulumi.Input[str]] = None,
                 firewall_id: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 start_port: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering FirewallRule resources.
        :param pulumi.Input[str] action: The action of the rule can be allow or deny. When we set the `action = 'allow'`, this is going to add a rule to allow traffic. Similarly, setting `action = 'deny'` will deny the traffic.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] cidrs: The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32 to open just for a specific IP address)
        :param pulumi.Input[str] direction: The direction of the rule can be ingress or egress
        :param pulumi.Input[str] end_port: The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
        :param pulumi.Input[str] firewall_id: The Firewall ID
        :param pulumi.Input[str] label: A string that will be the displayed name/reference for this rule
        :param pulumi.Input[str] protocol: The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
        :param pulumi.Input[str] region: The region for this rule
        :param pulumi.Input[str] start_port: The start of the port range to configure for this rule (or the single port if required)
        """
        _FirewallRuleState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            action=action,
            cidrs=cidrs,
            direction=direction,
            end_port=end_port,
            firewall_id=firewall_id,
            label=label,
            protocol=protocol,
            region=region,
            start_port=start_port,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             action: Optional[pulumi.Input[str]] = None,
             cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             direction: Optional[pulumi.Input[str]] = None,
             end_port: Optional[pulumi.Input[str]] = None,
             firewall_id: Optional[pulumi.Input[str]] = None,
             label: Optional[pulumi.Input[str]] = None,
             protocol: Optional[pulumi.Input[str]] = None,
             region: Optional[pulumi.Input[str]] = None,
             start_port: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if end_port is None and 'endPort' in kwargs:
            end_port = kwargs['endPort']
        if firewall_id is None and 'firewallId' in kwargs:
            firewall_id = kwargs['firewallId']
        if start_port is None and 'startPort' in kwargs:
            start_port = kwargs['startPort']

        if action is not None:
            _setter("action", action)
        if cidrs is not None:
            _setter("cidrs", cidrs)
        if direction is not None:
            _setter("direction", direction)
        if end_port is not None:
            _setter("end_port", end_port)
        if firewall_id is not None:
            _setter("firewall_id", firewall_id)
        if label is not None:
            _setter("label", label)
        if protocol is not None:
            _setter("protocol", protocol)
        if region is not None:
            _setter("region", region)
        if start_port is not None:
            _setter("start_port", start_port)

    @property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[str]]:
        """
        The action of the rule can be allow or deny. When we set the `action = 'allow'`, this is going to add a rule to allow traffic. Similarly, setting `action = 'deny'` will deny the traffic.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter
    def cidrs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32 to open just for a specific IP address)
        """
        return pulumi.get(self, "cidrs")

    @cidrs.setter
    def cidrs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "cidrs", value)

    @property
    @pulumi.getter
    def direction(self) -> Optional[pulumi.Input[str]]:
        """
        The direction of the rule can be ingress or egress
        """
        return pulumi.get(self, "direction")

    @direction.setter
    def direction(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "direction", value)

    @property
    @pulumi.getter(name="endPort")
    def end_port(self) -> Optional[pulumi.Input[str]]:
        """
        The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
        """
        return pulumi.get(self, "end_port")

    @end_port.setter
    def end_port(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_port", value)

    @property
    @pulumi.getter(name="firewallId")
    def firewall_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Firewall ID
        """
        return pulumi.get(self, "firewall_id")

    @firewall_id.setter
    def firewall_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "firewall_id", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        """
        A string that will be the displayed name/reference for this rule
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[str]]:
        """
        The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region for this rule
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="startPort")
    def start_port(self) -> Optional[pulumi.Input[str]]:
        """
        The start of the port range to configure for this rule (or the single port if required)
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
                 action: Optional[pulumi.Input[str]] = None,
                 cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 direction: Optional[pulumi.Input[str]] = None,
                 end_port: Optional[pulumi.Input[str]] = None,
                 firewall_id: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 start_port: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Civo firewall rule resource. This can be used to create, modify, and delete firewalls rules. This resource don't have an update option because Civo backend doesn't support it at this moment. In that case, we use `ForceNew` for all object in the resource.

        ## Import

        using firewall_id:firewall_rule_id

        ```sh
         $ pulumi import civo:index/firewallRule:FirewallRule http b8ecd2ab-2267-4a5e-8692-cbf1d32583e3:4b0022ee-00b2-4f81-a40d-b4f8728923a7
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action: The action of the rule can be allow or deny. When we set the `action = 'allow'`, this is going to add a rule to allow traffic. Similarly, setting `action = 'deny'` will deny the traffic.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] cidrs: The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32 to open just for a specific IP address)
        :param pulumi.Input[str] direction: The direction of the rule can be ingress or egress
        :param pulumi.Input[str] end_port: The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
        :param pulumi.Input[str] firewall_id: The Firewall ID
        :param pulumi.Input[str] label: A string that will be the displayed name/reference for this rule
        :param pulumi.Input[str] protocol: The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
        :param pulumi.Input[str] region: The region for this rule
        :param pulumi.Input[str] start_port: The start of the port range to configure for this rule (or the single port if required)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FirewallRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Civo firewall rule resource. This can be used to create, modify, and delete firewalls rules. This resource don't have an update option because Civo backend doesn't support it at this moment. In that case, we use `ForceNew` for all object in the resource.

        ## Import

        using firewall_id:firewall_rule_id

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
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            FirewallRuleArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[str]] = None,
                 cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 direction: Optional[pulumi.Input[str]] = None,
                 end_port: Optional[pulumi.Input[str]] = None,
                 firewall_id: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 start_port: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FirewallRuleArgs.__new__(FirewallRuleArgs)

            if action is None and not opts.urn:
                raise TypeError("Missing required property 'action'")
            __props__.__dict__["action"] = action
            if cidrs is None and not opts.urn:
                raise TypeError("Missing required property 'cidrs'")
            __props__.__dict__["cidrs"] = cidrs
            if direction is None and not opts.urn:
                raise TypeError("Missing required property 'direction'")
            __props__.__dict__["direction"] = direction
            __props__.__dict__["end_port"] = end_port
            if firewall_id is None and not opts.urn:
                raise TypeError("Missing required property 'firewall_id'")
            __props__.__dict__["firewall_id"] = firewall_id
            __props__.__dict__["label"] = label
            __props__.__dict__["protocol"] = protocol
            __props__.__dict__["region"] = region
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
            action: Optional[pulumi.Input[str]] = None,
            cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            direction: Optional[pulumi.Input[str]] = None,
            end_port: Optional[pulumi.Input[str]] = None,
            firewall_id: Optional[pulumi.Input[str]] = None,
            label: Optional[pulumi.Input[str]] = None,
            protocol: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            start_port: Optional[pulumi.Input[str]] = None) -> 'FirewallRule':
        """
        Get an existing FirewallRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action: The action of the rule can be allow or deny. When we set the `action = 'allow'`, this is going to add a rule to allow traffic. Similarly, setting `action = 'deny'` will deny the traffic.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] cidrs: The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32 to open just for a specific IP address)
        :param pulumi.Input[str] direction: The direction of the rule can be ingress or egress
        :param pulumi.Input[str] end_port: The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
        :param pulumi.Input[str] firewall_id: The Firewall ID
        :param pulumi.Input[str] label: A string that will be the displayed name/reference for this rule
        :param pulumi.Input[str] protocol: The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
        :param pulumi.Input[str] region: The region for this rule
        :param pulumi.Input[str] start_port: The start of the port range to configure for this rule (or the single port if required)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FirewallRuleState.__new__(_FirewallRuleState)

        __props__.__dict__["action"] = action
        __props__.__dict__["cidrs"] = cidrs
        __props__.__dict__["direction"] = direction
        __props__.__dict__["end_port"] = end_port
        __props__.__dict__["firewall_id"] = firewall_id
        __props__.__dict__["label"] = label
        __props__.__dict__["protocol"] = protocol
        __props__.__dict__["region"] = region
        __props__.__dict__["start_port"] = start_port
        return FirewallRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Output[str]:
        """
        The action of the rule can be allow or deny. When we set the `action = 'allow'`, this is going to add a rule to allow traffic. Similarly, setting `action = 'deny'` will deny the traffic.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter
    def cidrs(self) -> pulumi.Output[Sequence[str]]:
        """
        The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32 to open just for a specific IP address)
        """
        return pulumi.get(self, "cidrs")

    @property
    @pulumi.getter
    def direction(self) -> pulumi.Output[str]:
        """
        The direction of the rule can be ingress or egress
        """
        return pulumi.get(self, "direction")

    @property
    @pulumi.getter(name="endPort")
    def end_port(self) -> pulumi.Output[str]:
        """
        The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
        """
        return pulumi.get(self, "end_port")

    @property
    @pulumi.getter(name="firewallId")
    def firewall_id(self) -> pulumi.Output[str]:
        """
        The Firewall ID
        """
        return pulumi.get(self, "firewall_id")

    @property
    @pulumi.getter
    def label(self) -> pulumi.Output[str]:
        """
        A string that will be the displayed name/reference for this rule
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[str]:
        """
        The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region for this rule
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="startPort")
    def start_port(self) -> pulumi.Output[str]:
        """
        The start of the port range to configure for this rule (or the single port if required)
        """
        return pulumi.get(self, "start_port")


# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['FirewallArgs', 'Firewall']

@pulumi.input_type
class FirewallArgs:
    def __init__(__self__, *,
                 create_default_rules: Optional[pulumi.Input[bool]] = None,
                 egress_rules: Optional[pulumi.Input[Sequence[pulumi.Input['FirewallEgressRuleArgs']]]] = None,
                 ingress_rules: Optional[pulumi.Input[Sequence[pulumi.Input['FirewallIngressRuleArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Firewall resource.
        :param pulumi.Input[bool] create_default_rules: The create rules flag is used to create the default firewall rules, if is not defined will be set to true, and if you
               set to false you need to define at least one ingress or egress rule
        :param pulumi.Input[Sequence[pulumi.Input['FirewallEgressRuleArgs']]] egress_rules: The egress rules, this is a list of rules that will be applied to the firewall
        :param pulumi.Input[Sequence[pulumi.Input['FirewallIngressRuleArgs']]] ingress_rules: The ingress rules, this is a list of rules that will be applied to the firewall
        :param pulumi.Input[str] name: The firewall name
        :param pulumi.Input[str] network_id: The firewall network, if is not defined we use the default network
        :param pulumi.Input[str] region: The firewall region, if is not defined we use the global defined in the provider
        """
        if create_default_rules is not None:
            pulumi.set(__self__, "create_default_rules", create_default_rules)
        if egress_rules is not None:
            pulumi.set(__self__, "egress_rules", egress_rules)
        if ingress_rules is not None:
            pulumi.set(__self__, "ingress_rules", ingress_rules)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network_id is not None:
            pulumi.set(__self__, "network_id", network_id)
        if region is not None:
            pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter(name="createDefaultRules")
    def create_default_rules(self) -> Optional[pulumi.Input[bool]]:
        """
        The create rules flag is used to create the default firewall rules, if is not defined will be set to true, and if you
        set to false you need to define at least one ingress or egress rule
        """
        return pulumi.get(self, "create_default_rules")

    @create_default_rules.setter
    def create_default_rules(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "create_default_rules", value)

    @property
    @pulumi.getter(name="egressRules")
    def egress_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FirewallEgressRuleArgs']]]]:
        """
        The egress rules, this is a list of rules that will be applied to the firewall
        """
        return pulumi.get(self, "egress_rules")

    @egress_rules.setter
    def egress_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FirewallEgressRuleArgs']]]]):
        pulumi.set(self, "egress_rules", value)

    @property
    @pulumi.getter(name="ingressRules")
    def ingress_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FirewallIngressRuleArgs']]]]:
        """
        The ingress rules, this is a list of rules that will be applied to the firewall
        """
        return pulumi.get(self, "ingress_rules")

    @ingress_rules.setter
    def ingress_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FirewallIngressRuleArgs']]]]):
        pulumi.set(self, "ingress_rules", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The firewall name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> Optional[pulumi.Input[str]]:
        """
        The firewall network, if is not defined we use the default network
        """
        return pulumi.get(self, "network_id")

    @network_id.setter
    def network_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_id", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The firewall region, if is not defined we use the global defined in the provider
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)


@pulumi.input_type
class _FirewallState:
    def __init__(__self__, *,
                 create_default_rules: Optional[pulumi.Input[bool]] = None,
                 egress_rules: Optional[pulumi.Input[Sequence[pulumi.Input['FirewallEgressRuleArgs']]]] = None,
                 ingress_rules: Optional[pulumi.Input[Sequence[pulumi.Input['FirewallIngressRuleArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Firewall resources.
        :param pulumi.Input[bool] create_default_rules: The create rules flag is used to create the default firewall rules, if is not defined will be set to true, and if you
               set to false you need to define at least one ingress or egress rule
        :param pulumi.Input[Sequence[pulumi.Input['FirewallEgressRuleArgs']]] egress_rules: The egress rules, this is a list of rules that will be applied to the firewall
        :param pulumi.Input[Sequence[pulumi.Input['FirewallIngressRuleArgs']]] ingress_rules: The ingress rules, this is a list of rules that will be applied to the firewall
        :param pulumi.Input[str] name: The firewall name
        :param pulumi.Input[str] network_id: The firewall network, if is not defined we use the default network
        :param pulumi.Input[str] region: The firewall region, if is not defined we use the global defined in the provider
        """
        if create_default_rules is not None:
            pulumi.set(__self__, "create_default_rules", create_default_rules)
        if egress_rules is not None:
            pulumi.set(__self__, "egress_rules", egress_rules)
        if ingress_rules is not None:
            pulumi.set(__self__, "ingress_rules", ingress_rules)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network_id is not None:
            pulumi.set(__self__, "network_id", network_id)
        if region is not None:
            pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter(name="createDefaultRules")
    def create_default_rules(self) -> Optional[pulumi.Input[bool]]:
        """
        The create rules flag is used to create the default firewall rules, if is not defined will be set to true, and if you
        set to false you need to define at least one ingress or egress rule
        """
        return pulumi.get(self, "create_default_rules")

    @create_default_rules.setter
    def create_default_rules(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "create_default_rules", value)

    @property
    @pulumi.getter(name="egressRules")
    def egress_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FirewallEgressRuleArgs']]]]:
        """
        The egress rules, this is a list of rules that will be applied to the firewall
        """
        return pulumi.get(self, "egress_rules")

    @egress_rules.setter
    def egress_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FirewallEgressRuleArgs']]]]):
        pulumi.set(self, "egress_rules", value)

    @property
    @pulumi.getter(name="ingressRules")
    def ingress_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FirewallIngressRuleArgs']]]]:
        """
        The ingress rules, this is a list of rules that will be applied to the firewall
        """
        return pulumi.get(self, "ingress_rules")

    @ingress_rules.setter
    def ingress_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FirewallIngressRuleArgs']]]]):
        pulumi.set(self, "ingress_rules", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The firewall name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> Optional[pulumi.Input[str]]:
        """
        The firewall network, if is not defined we use the default network
        """
        return pulumi.get(self, "network_id")

    @network_id.setter
    def network_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_id", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The firewall region, if is not defined we use the global defined in the provider
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)


class Firewall(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 create_default_rules: Optional[pulumi.Input[bool]] = None,
                 egress_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallEgressRuleArgs']]]]] = None,
                 ingress_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallIngressRuleArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Civo firewall resource. This can be used to create, modify, and delete firewalls.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_civo as civo

        # Create a network
        custom_net = civo.Network("customNet", label="my-custom-network")
        # Create a firewall
        www_firewall = civo.Firewall("wwwFirewall", network_id=custom_net.id)
        # Create a firewall with the default rules
        www_index_firewall_firewall = civo.Firewall("wwwIndex/firewallFirewall",
            network_id=custom_net.id,
            create_default_rules=True)
        # Create a firewall withouth the default rules but with a custom rule
        www_civo_index_firewall_firewall = civo.Firewall("wwwCivoIndex/firewallFirewall",
            network_id=custom_net.id,
            create_default_rules=False,
            ingress_rules=[
                civo.FirewallIngressRuleArgs(
                    label="k8s",
                    protocol="tcp",
                    port_range="6443",
                    cidrs=[
                        "192.168.1.1/32",
                        "192.168.10.4/32",
                        "192.168.10.10/32",
                    ],
                    action="allow",
                ),
                civo.FirewallIngressRuleArgs(
                    label="ssh",
                    protocol="tcp",
                    port_range="22",
                    cidrs=[
                        "192.168.1.1/32",
                        "192.168.10.4/32",
                        "192.168.10.10/32",
                    ],
                    action="allow",
                ),
            ],
            egress_rules=[civo.FirewallEgressRuleArgs(
                label="all",
                protocol="tcp",
                port_range="1-65535",
                cidrs=["0.0.0.0/0"],
                action="allow",
            )])
        ```

        ## Import

        # using ID

        ```sh
         $ pulumi import civo:index/firewall:Firewall www b8ecd2ab-2267-4a5e-8692-cbf1d32583e3
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] create_default_rules: The create rules flag is used to create the default firewall rules, if is not defined will be set to true, and if you
               set to false you need to define at least one ingress or egress rule
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallEgressRuleArgs']]]] egress_rules: The egress rules, this is a list of rules that will be applied to the firewall
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallIngressRuleArgs']]]] ingress_rules: The ingress rules, this is a list of rules that will be applied to the firewall
        :param pulumi.Input[str] name: The firewall name
        :param pulumi.Input[str] network_id: The firewall network, if is not defined we use the default network
        :param pulumi.Input[str] region: The firewall region, if is not defined we use the global defined in the provider
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[FirewallArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Civo firewall resource. This can be used to create, modify, and delete firewalls.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_civo as civo

        # Create a network
        custom_net = civo.Network("customNet", label="my-custom-network")
        # Create a firewall
        www_firewall = civo.Firewall("wwwFirewall", network_id=custom_net.id)
        # Create a firewall with the default rules
        www_index_firewall_firewall = civo.Firewall("wwwIndex/firewallFirewall",
            network_id=custom_net.id,
            create_default_rules=True)
        # Create a firewall withouth the default rules but with a custom rule
        www_civo_index_firewall_firewall = civo.Firewall("wwwCivoIndex/firewallFirewall",
            network_id=custom_net.id,
            create_default_rules=False,
            ingress_rules=[
                civo.FirewallIngressRuleArgs(
                    label="k8s",
                    protocol="tcp",
                    port_range="6443",
                    cidrs=[
                        "192.168.1.1/32",
                        "192.168.10.4/32",
                        "192.168.10.10/32",
                    ],
                    action="allow",
                ),
                civo.FirewallIngressRuleArgs(
                    label="ssh",
                    protocol="tcp",
                    port_range="22",
                    cidrs=[
                        "192.168.1.1/32",
                        "192.168.10.4/32",
                        "192.168.10.10/32",
                    ],
                    action="allow",
                ),
            ],
            egress_rules=[civo.FirewallEgressRuleArgs(
                label="all",
                protocol="tcp",
                port_range="1-65535",
                cidrs=["0.0.0.0/0"],
                action="allow",
            )])
        ```

        ## Import

        # using ID

        ```sh
         $ pulumi import civo:index/firewall:Firewall www b8ecd2ab-2267-4a5e-8692-cbf1d32583e3
        ```

        :param str resource_name: The name of the resource.
        :param FirewallArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FirewallArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 create_default_rules: Optional[pulumi.Input[bool]] = None,
                 egress_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallEgressRuleArgs']]]]] = None,
                 ingress_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallIngressRuleArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FirewallArgs.__new__(FirewallArgs)

            __props__.__dict__["create_default_rules"] = create_default_rules
            __props__.__dict__["egress_rules"] = egress_rules
            __props__.__dict__["ingress_rules"] = ingress_rules
            __props__.__dict__["name"] = name
            __props__.__dict__["network_id"] = network_id
            __props__.__dict__["region"] = region
        super(Firewall, __self__).__init__(
            'civo:index/firewall:Firewall',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            create_default_rules: Optional[pulumi.Input[bool]] = None,
            egress_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallEgressRuleArgs']]]]] = None,
            ingress_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallIngressRuleArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network_id: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None) -> 'Firewall':
        """
        Get an existing Firewall resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] create_default_rules: The create rules flag is used to create the default firewall rules, if is not defined will be set to true, and if you
               set to false you need to define at least one ingress or egress rule
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallEgressRuleArgs']]]] egress_rules: The egress rules, this is a list of rules that will be applied to the firewall
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallIngressRuleArgs']]]] ingress_rules: The ingress rules, this is a list of rules that will be applied to the firewall
        :param pulumi.Input[str] name: The firewall name
        :param pulumi.Input[str] network_id: The firewall network, if is not defined we use the default network
        :param pulumi.Input[str] region: The firewall region, if is not defined we use the global defined in the provider
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FirewallState.__new__(_FirewallState)

        __props__.__dict__["create_default_rules"] = create_default_rules
        __props__.__dict__["egress_rules"] = egress_rules
        __props__.__dict__["ingress_rules"] = ingress_rules
        __props__.__dict__["name"] = name
        __props__.__dict__["network_id"] = network_id
        __props__.__dict__["region"] = region
        return Firewall(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createDefaultRules")
    def create_default_rules(self) -> pulumi.Output[Optional[bool]]:
        """
        The create rules flag is used to create the default firewall rules, if is not defined will be set to true, and if you
        set to false you need to define at least one ingress or egress rule
        """
        return pulumi.get(self, "create_default_rules")

    @property
    @pulumi.getter(name="egressRules")
    def egress_rules(self) -> pulumi.Output[Sequence['outputs.FirewallEgressRule']]:
        """
        The egress rules, this is a list of rules that will be applied to the firewall
        """
        return pulumi.get(self, "egress_rules")

    @property
    @pulumi.getter(name="ingressRules")
    def ingress_rules(self) -> pulumi.Output[Sequence['outputs.FirewallIngressRule']]:
        """
        The ingress rules, this is a list of rules that will be applied to the firewall
        """
        return pulumi.get(self, "ingress_rules")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The firewall name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Output[str]:
        """
        The firewall network, if is not defined we use the default network
        """
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[str]]:
        """
        The firewall region, if is not defined we use the global defined in the provider
        """
        return pulumi.get(self, "region")


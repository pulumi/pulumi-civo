# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities, _tables

__all__ = ['InstanceArgs', 'Instance']

@pulumi.input_type
class InstanceArgs:
    def __init__(__self__, *,
                 hostname: pulumi.Input[str],
                 firewall_id: Optional[pulumi.Input[str]] = None,
                 initial_user: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 public_ip_required: Optional[pulumi.Input[str]] = None,
                 reverse_dns: Optional[pulumi.Input[str]] = None,
                 script: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 sshkey_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 template: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Instance resource.
        :param pulumi.Input[str] hostname: The Instance hostname.
        :param pulumi.Input[str] firewall_id: The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all).
        :param pulumi.Input[str] initial_user: The name of the initial user created on the server (optional; this will default to the template's default_username and fallback to civo).
        :param pulumi.Input[str] network_id: This must be the ID of the network from the network listing (optional; default network used when not specified).
        :param pulumi.Input[str] notes: Add some notes to the instance.
        :param pulumi.Input[str] public_ip_required: This should be either false, true or `move_ip_from:intances_id`.
        :param pulumi.Input[str] reverse_dns: A fully qualified domain name that should be used as the instance's IP's reverse DNS (optional, uses the hostname if unspecified).
        :param pulumi.Input[str] script: the contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance, read/write/executable only by root and then will be executed at the end of the cloud initialization
        :param pulumi.Input[str] size: The name of the size, from the current list, e.g. g2.small (required).
        :param pulumi.Input[str] sshkey_id: The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn't provided a random password will be set and returned in the initial_password field).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: An optional list of tags, represented as a key, value pair.
        :param pulumi.Input[str] template: The ID for the template to use to build the instance.
        """
        pulumi.set(__self__, "hostname", hostname)
        if firewall_id is not None:
            pulumi.set(__self__, "firewall_id", firewall_id)
        if initial_user is not None:
            pulumi.set(__self__, "initial_user", initial_user)
        if network_id is not None:
            pulumi.set(__self__, "network_id", network_id)
        if notes is not None:
            pulumi.set(__self__, "notes", notes)
        if public_ip_required is not None:
            pulumi.set(__self__, "public_ip_required", public_ip_required)
        if reverse_dns is not None:
            pulumi.set(__self__, "reverse_dns", reverse_dns)
        if script is not None:
            pulumi.set(__self__, "script", script)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if sshkey_id is not None:
            pulumi.set(__self__, "sshkey_id", sshkey_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if template is not None:
            pulumi.set(__self__, "template", template)

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Input[str]:
        """
        The Instance hostname.
        """
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: pulumi.Input[str]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter(name="firewallId")
    def firewall_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all).
        """
        return pulumi.get(self, "firewall_id")

    @firewall_id.setter
    def firewall_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "firewall_id", value)

    @property
    @pulumi.getter(name="initialUser")
    def initial_user(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the initial user created on the server (optional; this will default to the template's default_username and fallback to civo).
        """
        return pulumi.get(self, "initial_user")

    @initial_user.setter
    def initial_user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "initial_user", value)

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> Optional[pulumi.Input[str]]:
        """
        This must be the ID of the network from the network listing (optional; default network used when not specified).
        """
        return pulumi.get(self, "network_id")

    @network_id.setter
    def network_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_id", value)

    @property
    @pulumi.getter
    def notes(self) -> Optional[pulumi.Input[str]]:
        """
        Add some notes to the instance.
        """
        return pulumi.get(self, "notes")

    @notes.setter
    def notes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notes", value)

    @property
    @pulumi.getter(name="publicIpRequired")
    def public_ip_required(self) -> Optional[pulumi.Input[str]]:
        """
        This should be either false, true or `move_ip_from:intances_id`.
        """
        return pulumi.get(self, "public_ip_required")

    @public_ip_required.setter
    def public_ip_required(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_ip_required", value)

    @property
    @pulumi.getter(name="reverseDns")
    def reverse_dns(self) -> Optional[pulumi.Input[str]]:
        """
        A fully qualified domain name that should be used as the instance's IP's reverse DNS (optional, uses the hostname if unspecified).
        """
        return pulumi.get(self, "reverse_dns")

    @reverse_dns.setter
    def reverse_dns(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reverse_dns", value)

    @property
    @pulumi.getter
    def script(self) -> Optional[pulumi.Input[str]]:
        """
        the contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance, read/write/executable only by root and then will be executed at the end of the cloud initialization
        """
        return pulumi.get(self, "script")

    @script.setter
    def script(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "script", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the size, from the current list, e.g. g2.small (required).
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter(name="sshkeyId")
    def sshkey_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn't provided a random password will be set and returned in the initial_password field).
        """
        return pulumi.get(self, "sshkey_id")

    @sshkey_id.setter
    def sshkey_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sshkey_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An optional list of tags, represented as a key, value pair.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def template(self) -> Optional[pulumi.Input[str]]:
        """
        The ID for the template to use to build the instance.
        """
        return pulumi.get(self, "template")

    @template.setter
    def template(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template", value)


class Instance(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 firewall_id: Optional[pulumi.Input[str]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 initial_user: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 public_ip_required: Optional[pulumi.Input[str]] = None,
                 reverse_dns: Optional[pulumi.Input[str]] = None,
                 script: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 sshkey_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 template: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Civo Instance resource. This can be used to create,
        modify, and delete Instances.

        ## Import

        Instances can be imported using the instance `id`, e.g.

        ```sh
         $ pulumi import civo:index/instance:Instance myintance 18bd98ad-1b6e-4f87-b48f-e690b4fd7413
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] firewall_id: The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all).
        :param pulumi.Input[str] hostname: The Instance hostname.
        :param pulumi.Input[str] initial_user: The name of the initial user created on the server (optional; this will default to the template's default_username and fallback to civo).
        :param pulumi.Input[str] network_id: This must be the ID of the network from the network listing (optional; default network used when not specified).
        :param pulumi.Input[str] notes: Add some notes to the instance.
        :param pulumi.Input[str] public_ip_required: This should be either false, true or `move_ip_from:intances_id`.
        :param pulumi.Input[str] reverse_dns: A fully qualified domain name that should be used as the instance's IP's reverse DNS (optional, uses the hostname if unspecified).
        :param pulumi.Input[str] script: the contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance, read/write/executable only by root and then will be executed at the end of the cloud initialization
        :param pulumi.Input[str] size: The name of the size, from the current list, e.g. g2.small (required).
        :param pulumi.Input[str] sshkey_id: The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn't provided a random password will be set and returned in the initial_password field).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: An optional list of tags, represented as a key, value pair.
        :param pulumi.Input[str] template: The ID for the template to use to build the instance.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InstanceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Civo Instance resource. This can be used to create,
        modify, and delete Instances.

        ## Import

        Instances can be imported using the instance `id`, e.g.

        ```sh
         $ pulumi import civo:index/instance:Instance myintance 18bd98ad-1b6e-4f87-b48f-e690b4fd7413
        ```

        :param str resource_name: The name of the resource.
        :param InstanceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstanceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 firewall_id: Optional[pulumi.Input[str]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 initial_user: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 public_ip_required: Optional[pulumi.Input[str]] = None,
                 reverse_dns: Optional[pulumi.Input[str]] = None,
                 script: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 sshkey_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 template: Optional[pulumi.Input[str]] = None,
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
            __props__ = dict()

            __props__['firewall_id'] = firewall_id
            if hostname is None and not opts.urn:
                raise TypeError("Missing required property 'hostname'")
            __props__['hostname'] = hostname
            __props__['initial_user'] = initial_user
            __props__['network_id'] = network_id
            __props__['notes'] = notes
            __props__['public_ip_required'] = public_ip_required
            __props__['reverse_dns'] = reverse_dns
            __props__['script'] = script
            __props__['size'] = size
            __props__['sshkey_id'] = sshkey_id
            __props__['tags'] = tags
            __props__['template'] = template
            __props__['cpu_cores'] = None
            __props__['created_at'] = None
            __props__['disk_gb'] = None
            __props__['initial_password'] = None
            __props__['private_ip'] = None
            __props__['pseudo_ip'] = None
            __props__['public_ip'] = None
            __props__['ram_mb'] = None
            __props__['status'] = None
        super(Instance, __self__).__init__(
            'civo:index/instance:Instance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cpu_cores: Optional[pulumi.Input[int]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            disk_gb: Optional[pulumi.Input[int]] = None,
            firewall_id: Optional[pulumi.Input[str]] = None,
            hostname: Optional[pulumi.Input[str]] = None,
            initial_password: Optional[pulumi.Input[str]] = None,
            initial_user: Optional[pulumi.Input[str]] = None,
            network_id: Optional[pulumi.Input[str]] = None,
            notes: Optional[pulumi.Input[str]] = None,
            private_ip: Optional[pulumi.Input[str]] = None,
            pseudo_ip: Optional[pulumi.Input[str]] = None,
            public_ip: Optional[pulumi.Input[str]] = None,
            public_ip_required: Optional[pulumi.Input[str]] = None,
            ram_mb: Optional[pulumi.Input[int]] = None,
            reverse_dns: Optional[pulumi.Input[str]] = None,
            script: Optional[pulumi.Input[str]] = None,
            size: Optional[pulumi.Input[str]] = None,
            sshkey_id: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            template: Optional[pulumi.Input[str]] = None) -> 'Instance':
        """
        Get an existing Instance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] cpu_cores: Total cpu of the inatance.
        :param pulumi.Input[str] created_at: The date of creation of the instance
        :param pulumi.Input[int] disk_gb: The size of the disk.
        :param pulumi.Input[str] firewall_id: The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all).
        :param pulumi.Input[str] hostname: The Instance hostname.
        :param pulumi.Input[str] initial_password: Instance initial password
        :param pulumi.Input[str] initial_user: The name of the initial user created on the server (optional; this will default to the template's default_username and fallback to civo).
        :param pulumi.Input[str] network_id: This must be the ID of the network from the network listing (optional; default network used when not specified).
        :param pulumi.Input[str] notes: Add some notes to the instance.
        :param pulumi.Input[str] private_ip: The private ip.
        :param pulumi.Input[str] pseudo_ip: Is the ip that is used to route the public ip from the internet to the instance using NAT
        :param pulumi.Input[str] public_ip: The public ip.
        :param pulumi.Input[str] public_ip_required: This should be either false, true or `move_ip_from:intances_id`.
        :param pulumi.Input[int] ram_mb: Total ram of the instance.
        :param pulumi.Input[str] reverse_dns: A fully qualified domain name that should be used as the instance's IP's reverse DNS (optional, uses the hostname if unspecified).
        :param pulumi.Input[str] script: the contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance, read/write/executable only by root and then will be executed at the end of the cloud initialization
        :param pulumi.Input[str] size: The name of the size, from the current list, e.g. g2.small (required).
        :param pulumi.Input[str] sshkey_id: The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn't provided a random password will be set and returned in the initial_password field).
        :param pulumi.Input[str] status: The status of the instance
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: An optional list of tags, represented as a key, value pair.
        :param pulumi.Input[str] template: The ID for the template to use to build the instance.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cpu_cores"] = cpu_cores
        __props__["created_at"] = created_at
        __props__["disk_gb"] = disk_gb
        __props__["firewall_id"] = firewall_id
        __props__["hostname"] = hostname
        __props__["initial_password"] = initial_password
        __props__["initial_user"] = initial_user
        __props__["network_id"] = network_id
        __props__["notes"] = notes
        __props__["private_ip"] = private_ip
        __props__["pseudo_ip"] = pseudo_ip
        __props__["public_ip"] = public_ip
        __props__["public_ip_required"] = public_ip_required
        __props__["ram_mb"] = ram_mb
        __props__["reverse_dns"] = reverse_dns
        __props__["script"] = script
        __props__["size"] = size
        __props__["sshkey_id"] = sshkey_id
        __props__["status"] = status
        __props__["tags"] = tags
        __props__["template"] = template
        return Instance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cpuCores")
    def cpu_cores(self) -> pulumi.Output[int]:
        """
        Total cpu of the inatance.
        """
        return pulumi.get(self, "cpu_cores")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The date of creation of the instance
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="diskGb")
    def disk_gb(self) -> pulumi.Output[int]:
        """
        The size of the disk.
        """
        return pulumi.get(self, "disk_gb")

    @property
    @pulumi.getter(name="firewallId")
    def firewall_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all).
        """
        return pulumi.get(self, "firewall_id")

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Output[str]:
        """
        The Instance hostname.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter(name="initialPassword")
    def initial_password(self) -> pulumi.Output[str]:
        """
        Instance initial password
        """
        return pulumi.get(self, "initial_password")

    @property
    @pulumi.getter(name="initialUser")
    def initial_user(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the initial user created on the server (optional; this will default to the template's default_username and fallback to civo).
        """
        return pulumi.get(self, "initial_user")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Output[Optional[str]]:
        """
        This must be the ID of the network from the network listing (optional; default network used when not specified).
        """
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter
    def notes(self) -> pulumi.Output[Optional[str]]:
        """
        Add some notes to the instance.
        """
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> pulumi.Output[str]:
        """
        The private ip.
        """
        return pulumi.get(self, "private_ip")

    @property
    @pulumi.getter(name="pseudoIp")
    def pseudo_ip(self) -> pulumi.Output[str]:
        """
        Is the ip that is used to route the public ip from the internet to the instance using NAT
        """
        return pulumi.get(self, "pseudo_ip")

    @property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> pulumi.Output[str]:
        """
        The public ip.
        """
        return pulumi.get(self, "public_ip")

    @property
    @pulumi.getter(name="publicIpRequired")
    def public_ip_required(self) -> pulumi.Output[Optional[str]]:
        """
        This should be either false, true or `move_ip_from:intances_id`.
        """
        return pulumi.get(self, "public_ip_required")

    @property
    @pulumi.getter(name="ramMb")
    def ram_mb(self) -> pulumi.Output[int]:
        """
        Total ram of the instance.
        """
        return pulumi.get(self, "ram_mb")

    @property
    @pulumi.getter(name="reverseDns")
    def reverse_dns(self) -> pulumi.Output[Optional[str]]:
        """
        A fully qualified domain name that should be used as the instance's IP's reverse DNS (optional, uses the hostname if unspecified).
        """
        return pulumi.get(self, "reverse_dns")

    @property
    @pulumi.getter
    def script(self) -> pulumi.Output[Optional[str]]:
        """
        the contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance, read/write/executable only by root and then will be executed at the end of the cloud initialization
        """
        return pulumi.get(self, "script")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the size, from the current list, e.g. g2.small (required).
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter(name="sshkeyId")
    def sshkey_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn't provided a random password will be set and returned in the initial_password field).
        """
        return pulumi.get(self, "sshkey_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the instance
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        An optional list of tags, represented as a key, value pair.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def template(self) -> pulumi.Output[Optional[str]]:
        """
        The ID for the template to use to build the instance.
        """
        return pulumi.get(self, "template")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


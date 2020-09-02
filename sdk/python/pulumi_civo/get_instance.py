# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from . import _utilities, _tables

__all__ = [
    'GetInstanceResult',
    'AwaitableGetInstanceResult',
    'get_instance',
]

@pulumi.output_type
class GetInstanceResult:
    """
    A collection of values returned by getInstance.
    """
    def __init__(__self__, cpu_cores=None, created_at=None, disk_gb=None, firewall_id=None, hostname=None, id=None, initial_password=None, initial_user=None, network_id=None, notes=None, private_ip=None, pseudo_ip=None, public_ip=None, ram_mb=None, reverse_dns=None, script=None, size=None, sshkey_id=None, status=None, tags=None, template=None):
        if cpu_cores and not isinstance(cpu_cores, float):
            raise TypeError("Expected argument 'cpu_cores' to be a float")
        pulumi.set(__self__, "cpu_cores", cpu_cores)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if disk_gb and not isinstance(disk_gb, float):
            raise TypeError("Expected argument 'disk_gb' to be a float")
        pulumi.set(__self__, "disk_gb", disk_gb)
        if firewall_id and not isinstance(firewall_id, str):
            raise TypeError("Expected argument 'firewall_id' to be a str")
        pulumi.set(__self__, "firewall_id", firewall_id)
        if hostname and not isinstance(hostname, str):
            raise TypeError("Expected argument 'hostname' to be a str")
        pulumi.set(__self__, "hostname", hostname)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if initial_password and not isinstance(initial_password, str):
            raise TypeError("Expected argument 'initial_password' to be a str")
        pulumi.set(__self__, "initial_password", initial_password)
        if initial_user and not isinstance(initial_user, str):
            raise TypeError("Expected argument 'initial_user' to be a str")
        pulumi.set(__self__, "initial_user", initial_user)
        if network_id and not isinstance(network_id, str):
            raise TypeError("Expected argument 'network_id' to be a str")
        pulumi.set(__self__, "network_id", network_id)
        if notes and not isinstance(notes, str):
            raise TypeError("Expected argument 'notes' to be a str")
        pulumi.set(__self__, "notes", notes)
        if private_ip and not isinstance(private_ip, str):
            raise TypeError("Expected argument 'private_ip' to be a str")
        pulumi.set(__self__, "private_ip", private_ip)
        if pseudo_ip and not isinstance(pseudo_ip, str):
            raise TypeError("Expected argument 'pseudo_ip' to be a str")
        pulumi.set(__self__, "pseudo_ip", pseudo_ip)
        if public_ip and not isinstance(public_ip, str):
            raise TypeError("Expected argument 'public_ip' to be a str")
        pulumi.set(__self__, "public_ip", public_ip)
        if ram_mb and not isinstance(ram_mb, float):
            raise TypeError("Expected argument 'ram_mb' to be a float")
        pulumi.set(__self__, "ram_mb", ram_mb)
        if reverse_dns and not isinstance(reverse_dns, str):
            raise TypeError("Expected argument 'reverse_dns' to be a str")
        pulumi.set(__self__, "reverse_dns", reverse_dns)
        if script and not isinstance(script, str):
            raise TypeError("Expected argument 'script' to be a str")
        pulumi.set(__self__, "script", script)
        if size and not isinstance(size, str):
            raise TypeError("Expected argument 'size' to be a str")
        pulumi.set(__self__, "size", size)
        if sshkey_id and not isinstance(sshkey_id, str):
            raise TypeError("Expected argument 'sshkey_id' to be a str")
        pulumi.set(__self__, "sshkey_id", sshkey_id)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if template and not isinstance(template, str):
            raise TypeError("Expected argument 'template' to be a str")
        pulumi.set(__self__, "template", template)

    @property
    @pulumi.getter(name="cpuCores")
    def cpu_cores(self) -> float:
        return pulumi.get(self, "cpu_cores")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="diskGb")
    def disk_gb(self) -> float:
        return pulumi.get(self, "disk_gb")

    @property
    @pulumi.getter(name="firewallId")
    def firewall_id(self) -> str:
        return pulumi.get(self, "firewall_id")

    @property
    @pulumi.getter
    def hostname(self) -> Optional[str]:
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="initialPassword")
    def initial_password(self) -> str:
        return pulumi.get(self, "initial_password")

    @property
    @pulumi.getter(name="initialUser")
    def initial_user(self) -> str:
        return pulumi.get(self, "initial_user")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> str:
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter
    def notes(self) -> str:
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> str:
        return pulumi.get(self, "private_ip")

    @property
    @pulumi.getter(name="pseudoIp")
    def pseudo_ip(self) -> str:
        return pulumi.get(self, "pseudo_ip")

    @property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> str:
        return pulumi.get(self, "public_ip")

    @property
    @pulumi.getter(name="ramMb")
    def ram_mb(self) -> float:
        return pulumi.get(self, "ram_mb")

    @property
    @pulumi.getter(name="reverseDns")
    def reverse_dns(self) -> str:
        return pulumi.get(self, "reverse_dns")

    @property
    @pulumi.getter
    def script(self) -> str:
        return pulumi.get(self, "script")

    @property
    @pulumi.getter
    def size(self) -> str:
        return pulumi.get(self, "size")

    @property
    @pulumi.getter(name="sshkeyId")
    def sshkey_id(self) -> str:
        return pulumi.get(self, "sshkey_id")

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> List[str]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def template(self) -> str:
        return pulumi.get(self, "template")


class AwaitableGetInstanceResult(GetInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceResult(
            cpu_cores=self.cpu_cores,
            created_at=self.created_at,
            disk_gb=self.disk_gb,
            firewall_id=self.firewall_id,
            hostname=self.hostname,
            id=self.id,
            initial_password=self.initial_password,
            initial_user=self.initial_user,
            network_id=self.network_id,
            notes=self.notes,
            private_ip=self.private_ip,
            pseudo_ip=self.pseudo_ip,
            public_ip=self.public_ip,
            ram_mb=self.ram_mb,
            reverse_dns=self.reverse_dns,
            script=self.script,
            size=self.size,
            sshkey_id=self.sshkey_id,
            status=self.status,
            tags=self.tags,
            template=self.template)


def get_instance(hostname: Optional[str] = None,
                 id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['hostname'] = hostname
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('civo:index/getInstance:getInstance', __args__, opts=opts, typ=GetInstanceResult).value

    return AwaitableGetInstanceResult(
        cpu_cores=__ret__.cpu_cores,
        created_at=__ret__.created_at,
        disk_gb=__ret__.disk_gb,
        firewall_id=__ret__.firewall_id,
        hostname=__ret__.hostname,
        id=__ret__.id,
        initial_password=__ret__.initial_password,
        initial_user=__ret__.initial_user,
        network_id=__ret__.network_id,
        notes=__ret__.notes,
        private_ip=__ret__.private_ip,
        pseudo_ip=__ret__.pseudo_ip,
        public_ip=__ret__.public_ip,
        ram_mb=__ret__.ram_mb,
        reverse_dns=__ret__.reverse_dns,
        script=__ret__.script,
        size=__ret__.size,
        sshkey_id=__ret__.sshkey_id,
        status=__ret__.status,
        tags=__ret__.tags,
        template=__ret__.template)

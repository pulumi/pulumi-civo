# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['VolumeAttachmentArgs', 'VolumeAttachment']

@pulumi.input_type
class VolumeAttachmentArgs:
    def __init__(__self__, *,
                 instance_id: pulumi.Input[str],
                 volume_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a VolumeAttachment resource.
        :param pulumi.Input[str] instance_id: ID of the instance to attach the volume to.
        :param pulumi.Input[str] volume_id: ID of the Volume to be attached to the instance.
        """
        pulumi.set(__self__, "instance_id", instance_id)
        pulumi.set(__self__, "volume_id", volume_id)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[str]:
        """
        ID of the instance to attach the volume to.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> pulumi.Input[str]:
        """
        ID of the Volume to be attached to the instance.
        """
        return pulumi.get(self, "volume_id")

    @volume_id.setter
    def volume_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "volume_id", value)


@pulumi.input_type
class _VolumeAttachmentState:
    def __init__(__self__, *,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 volume_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering VolumeAttachment resources.
        :param pulumi.Input[str] instance_id: ID of the instance to attach the volume to.
        :param pulumi.Input[str] volume_id: ID of the Volume to be attached to the instance.
        """
        if instance_id is not None:
            pulumi.set(__self__, "instance_id", instance_id)
        if volume_id is not None:
            pulumi.set(__self__, "volume_id", volume_id)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the instance to attach the volume to.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the Volume to be attached to the instance.
        """
        return pulumi.get(self, "volume_id")

    @volume_id.setter
    def volume_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_id", value)


class VolumeAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 volume_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages attaching a Volume to a Instance.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_civo as civo

        db = civo.Volume("db",
            size_gb=60,
            bootable=False)
        foobar = civo.VolumeAttachment("foobar",
            instance_id=civo_instance["my-test-instance"]["id"],
            volume_id=db.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance_id: ID of the instance to attach the volume to.
        :param pulumi.Input[str] volume_id: ID of the Volume to be attached to the instance.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VolumeAttachmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages attaching a Volume to a Instance.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_civo as civo

        db = civo.Volume("db",
            size_gb=60,
            bootable=False)
        foobar = civo.VolumeAttachment("foobar",
            instance_id=civo_instance["my-test-instance"]["id"],
            volume_id=db.id)
        ```

        :param str resource_name: The name of the resource.
        :param VolumeAttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VolumeAttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 volume_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = VolumeAttachmentArgs.__new__(VolumeAttachmentArgs)

            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__.__dict__["instance_id"] = instance_id
            if volume_id is None and not opts.urn:
                raise TypeError("Missing required property 'volume_id'")
            __props__.__dict__["volume_id"] = volume_id
        super(VolumeAttachment, __self__).__init__(
            'civo:index/volumeAttachment:VolumeAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            instance_id: Optional[pulumi.Input[str]] = None,
            volume_id: Optional[pulumi.Input[str]] = None) -> 'VolumeAttachment':
        """
        Get an existing VolumeAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance_id: ID of the instance to attach the volume to.
        :param pulumi.Input[str] volume_id: ID of the Volume to be attached to the instance.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VolumeAttachmentState.__new__(_VolumeAttachmentState)

        __props__.__dict__["instance_id"] = instance_id
        __props__.__dict__["volume_id"] = volume_id
        return VolumeAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[str]:
        """
        ID of the instance to attach the volume to.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> pulumi.Output[str]:
        """
        ID of the Volume to be attached to the instance.
        """
        return pulumi.get(self, "volume_id")


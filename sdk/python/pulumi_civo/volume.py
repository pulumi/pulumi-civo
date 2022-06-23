# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['VolumeArgs', 'Volume']

@pulumi.input_type
class VolumeArgs:
    def __init__(__self__, *,
                 network_id: pulumi.Input[str],
                 size_gb: pulumi.Input[int],
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Volume resource.
        :param pulumi.Input[str] network_id: The network that the volume belongs to
        :param pulumi.Input[int] size_gb: A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes
        :param pulumi.Input[str] name: A name that you wish to use to refer to this volume
        :param pulumi.Input[str] region: The region for the volume, if not declare we use the region in declared in the provider.
        """
        pulumi.set(__self__, "network_id", network_id)
        pulumi.set(__self__, "size_gb", size_gb)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if region is not None:
            pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Input[str]:
        """
        The network that the volume belongs to
        """
        return pulumi.get(self, "network_id")

    @network_id.setter
    def network_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_id", value)

    @property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> pulumi.Input[int]:
        """
        A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes
        """
        return pulumi.get(self, "size_gb")

    @size_gb.setter
    def size_gb(self, value: pulumi.Input[int]):
        pulumi.set(self, "size_gb", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A name that you wish to use to refer to this volume
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region for the volume, if not declare we use the region in declared in the provider.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)


@pulumi.input_type
class _VolumeState:
    def __init__(__self__, *,
                 mount_point: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 size_gb: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Volume resources.
        :param pulumi.Input[str] mount_point: The mount point of the volume (from instance's perspective)
        :param pulumi.Input[str] name: A name that you wish to use to refer to this volume
        :param pulumi.Input[str] network_id: The network that the volume belongs to
        :param pulumi.Input[str] region: The region for the volume, if not declare we use the region in declared in the provider.
        :param pulumi.Input[int] size_gb: A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes
        """
        if mount_point is not None:
            pulumi.set(__self__, "mount_point", mount_point)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network_id is not None:
            pulumi.set(__self__, "network_id", network_id)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if size_gb is not None:
            pulumi.set(__self__, "size_gb", size_gb)

    @property
    @pulumi.getter(name="mountPoint")
    def mount_point(self) -> Optional[pulumi.Input[str]]:
        """
        The mount point of the volume (from instance's perspective)
        """
        return pulumi.get(self, "mount_point")

    @mount_point.setter
    def mount_point(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mount_point", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A name that you wish to use to refer to this volume
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> Optional[pulumi.Input[str]]:
        """
        The network that the volume belongs to
        """
        return pulumi.get(self, "network_id")

    @network_id.setter
    def network_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_id", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region for the volume, if not declare we use the region in declared in the provider.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> Optional[pulumi.Input[int]]:
        """
        A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes
        """
        return pulumi.get(self, "size_gb")

    @size_gb.setter
    def size_gb(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "size_gb", value)


class Volume(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 size_gb: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Provides a Civo volume which can be attached to an instance in order to provide expanded storage.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_civo as civo

        default_network = civo.get_network(label="Default")
        # Create volume
        db = civo.Volume("db",
            size_gb=5,
            network_id=default_network.id,
            opts=pulumi.ResourceOptions(depends_on=[default_network]))
        ```

        ## Import

        # using ID

        ```sh
         $ pulumi import civo:index/volume:Volume db 506f78a4-e098-11e5-ad9f-000f53306ae1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: A name that you wish to use to refer to this volume
        :param pulumi.Input[str] network_id: The network that the volume belongs to
        :param pulumi.Input[str] region: The region for the volume, if not declare we use the region in declared in the provider.
        :param pulumi.Input[int] size_gb: A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VolumeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Civo volume which can be attached to an instance in order to provide expanded storage.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_civo as civo

        default_network = civo.get_network(label="Default")
        # Create volume
        db = civo.Volume("db",
            size_gb=5,
            network_id=default_network.id,
            opts=pulumi.ResourceOptions(depends_on=[default_network]))
        ```

        ## Import

        # using ID

        ```sh
         $ pulumi import civo:index/volume:Volume db 506f78a4-e098-11e5-ad9f-000f53306ae1
        ```

        :param str resource_name: The name of the resource.
        :param VolumeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VolumeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 size_gb: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VolumeArgs.__new__(VolumeArgs)

            __props__.__dict__["name"] = name
            if network_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_id'")
            __props__.__dict__["network_id"] = network_id
            __props__.__dict__["region"] = region
            if size_gb is None and not opts.urn:
                raise TypeError("Missing required property 'size_gb'")
            __props__.__dict__["size_gb"] = size_gb
            __props__.__dict__["mount_point"] = None
        super(Volume, __self__).__init__(
            'civo:index/volume:Volume',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            mount_point: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network_id: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            size_gb: Optional[pulumi.Input[int]] = None) -> 'Volume':
        """
        Get an existing Volume resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] mount_point: The mount point of the volume (from instance's perspective)
        :param pulumi.Input[str] name: A name that you wish to use to refer to this volume
        :param pulumi.Input[str] network_id: The network that the volume belongs to
        :param pulumi.Input[str] region: The region for the volume, if not declare we use the region in declared in the provider.
        :param pulumi.Input[int] size_gb: A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VolumeState.__new__(_VolumeState)

        __props__.__dict__["mount_point"] = mount_point
        __props__.__dict__["name"] = name
        __props__.__dict__["network_id"] = network_id
        __props__.__dict__["region"] = region
        __props__.__dict__["size_gb"] = size_gb
        return Volume(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="mountPoint")
    def mount_point(self) -> pulumi.Output[str]:
        """
        The mount point of the volume (from instance's perspective)
        """
        return pulumi.get(self, "mount_point")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A name that you wish to use to refer to this volume
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Output[str]:
        """
        The network that the volume belongs to
        """
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[str]]:
        """
        The region for the volume, if not declare we use the region in declared in the provider.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> pulumi.Output[int]:
        """
        A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes
        """
        return pulumi.get(self, "size_gb")


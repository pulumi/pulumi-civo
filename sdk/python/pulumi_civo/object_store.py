# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ObjectStoreArgs', 'ObjectStore']

@pulumi.input_type
class ObjectStoreArgs:
    def __init__(__self__, *,
                 access_key_id: Optional[pulumi.Input[str]] = None,
                 max_size_gb: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ObjectStore resource.
        :param pulumi.Input[str] access_key_id: The access key ID from the Object Store credential. If this is not set, a new credential will be created.
        :param pulumi.Input[int] max_size_gb: The maximum size of the Object Store. Default is 500GB.
        :param pulumi.Input[str] name: The name of the Object Store. Must be unique.
        :param pulumi.Input[str] region: The region for the Object Store, if not declared we use the region as declared in the provider (Defaults to LON1)
        """
        if access_key_id is not None:
            pulumi.set(__self__, "access_key_id", access_key_id)
        if max_size_gb is not None:
            pulumi.set(__self__, "max_size_gb", max_size_gb)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if region is not None:
            pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter(name="accessKeyId")
    def access_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        The access key ID from the Object Store credential. If this is not set, a new credential will be created.
        """
        return pulumi.get(self, "access_key_id")

    @access_key_id.setter
    def access_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_key_id", value)

    @property
    @pulumi.getter(name="maxSizeGb")
    def max_size_gb(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum size of the Object Store. Default is 500GB.
        """
        return pulumi.get(self, "max_size_gb")

    @max_size_gb.setter
    def max_size_gb(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_size_gb", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Object Store. Must be unique.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region for the Object Store, if not declared we use the region as declared in the provider (Defaults to LON1)
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)


@pulumi.input_type
class _ObjectStoreState:
    def __init__(__self__, *,
                 access_key_id: Optional[pulumi.Input[str]] = None,
                 bucket_url: Optional[pulumi.Input[str]] = None,
                 max_size_gb: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ObjectStore resources.
        :param pulumi.Input[str] access_key_id: The access key ID from the Object Store credential. If this is not set, a new credential will be created.
        :param pulumi.Input[str] bucket_url: The endpoint of the Object Store. It is generated by the provider.
        :param pulumi.Input[int] max_size_gb: The maximum size of the Object Store. Default is 500GB.
        :param pulumi.Input[str] name: The name of the Object Store. Must be unique.
        :param pulumi.Input[str] region: The region for the Object Store, if not declared we use the region as declared in the provider (Defaults to LON1)
        :param pulumi.Input[str] status: The status of the Object Store.
        """
        if access_key_id is not None:
            pulumi.set(__self__, "access_key_id", access_key_id)
        if bucket_url is not None:
            pulumi.set(__self__, "bucket_url", bucket_url)
        if max_size_gb is not None:
            pulumi.set(__self__, "max_size_gb", max_size_gb)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="accessKeyId")
    def access_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        The access key ID from the Object Store credential. If this is not set, a new credential will be created.
        """
        return pulumi.get(self, "access_key_id")

    @access_key_id.setter
    def access_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_key_id", value)

    @property
    @pulumi.getter(name="bucketUrl")
    def bucket_url(self) -> Optional[pulumi.Input[str]]:
        """
        The endpoint of the Object Store. It is generated by the provider.
        """
        return pulumi.get(self, "bucket_url")

    @bucket_url.setter
    def bucket_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket_url", value)

    @property
    @pulumi.getter(name="maxSizeGb")
    def max_size_gb(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum size of the Object Store. Default is 500GB.
        """
        return pulumi.get(self, "max_size_gb")

    @max_size_gb.setter
    def max_size_gb(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_size_gb", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Object Store. Must be unique.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region for the Object Store, if not declared we use the region as declared in the provider (Defaults to LON1)
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the Object Store.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class ObjectStore(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_key_id: Optional[pulumi.Input[str]] = None,
                 max_size_gb: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides an Object Store resource. This can be used to create, modify, and delete object stores.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_civo as civo

        backup = civo.ObjectStore("backup",
            max_size_gb=500,
            region="LON1")
        ```

        ## Import

        # using ID

        ```sh
         $ pulumi import civo:index/objectStore:ObjectStore custom_object b8ecd2ab-2267-4a5e-8692-cbf1d32583e3
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_key_id: The access key ID from the Object Store credential. If this is not set, a new credential will be created.
        :param pulumi.Input[int] max_size_gb: The maximum size of the Object Store. Default is 500GB.
        :param pulumi.Input[str] name: The name of the Object Store. Must be unique.
        :param pulumi.Input[str] region: The region for the Object Store, if not declared we use the region as declared in the provider (Defaults to LON1)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ObjectStoreArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an Object Store resource. This can be used to create, modify, and delete object stores.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_civo as civo

        backup = civo.ObjectStore("backup",
            max_size_gb=500,
            region="LON1")
        ```

        ## Import

        # using ID

        ```sh
         $ pulumi import civo:index/objectStore:ObjectStore custom_object b8ecd2ab-2267-4a5e-8692-cbf1d32583e3
        ```

        :param str resource_name: The name of the resource.
        :param ObjectStoreArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ObjectStoreArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_key_id: Optional[pulumi.Input[str]] = None,
                 max_size_gb: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ObjectStoreArgs.__new__(ObjectStoreArgs)

            __props__.__dict__["access_key_id"] = access_key_id
            __props__.__dict__["max_size_gb"] = max_size_gb
            __props__.__dict__["name"] = name
            __props__.__dict__["region"] = region
            __props__.__dict__["bucket_url"] = None
            __props__.__dict__["status"] = None
        super(ObjectStore, __self__).__init__(
            'civo:index/objectStore:ObjectStore',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access_key_id: Optional[pulumi.Input[str]] = None,
            bucket_url: Optional[pulumi.Input[str]] = None,
            max_size_gb: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'ObjectStore':
        """
        Get an existing ObjectStore resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_key_id: The access key ID from the Object Store credential. If this is not set, a new credential will be created.
        :param pulumi.Input[str] bucket_url: The endpoint of the Object Store. It is generated by the provider.
        :param pulumi.Input[int] max_size_gb: The maximum size of the Object Store. Default is 500GB.
        :param pulumi.Input[str] name: The name of the Object Store. Must be unique.
        :param pulumi.Input[str] region: The region for the Object Store, if not declared we use the region as declared in the provider (Defaults to LON1)
        :param pulumi.Input[str] status: The status of the Object Store.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ObjectStoreState.__new__(_ObjectStoreState)

        __props__.__dict__["access_key_id"] = access_key_id
        __props__.__dict__["bucket_url"] = bucket_url
        __props__.__dict__["max_size_gb"] = max_size_gb
        __props__.__dict__["name"] = name
        __props__.__dict__["region"] = region
        __props__.__dict__["status"] = status
        return ObjectStore(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessKeyId")
    def access_key_id(self) -> pulumi.Output[str]:
        """
        The access key ID from the Object Store credential. If this is not set, a new credential will be created.
        """
        return pulumi.get(self, "access_key_id")

    @property
    @pulumi.getter(name="bucketUrl")
    def bucket_url(self) -> pulumi.Output[str]:
        """
        The endpoint of the Object Store. It is generated by the provider.
        """
        return pulumi.get(self, "bucket_url")

    @property
    @pulumi.getter(name="maxSizeGb")
    def max_size_gb(self) -> pulumi.Output[Optional[int]]:
        """
        The maximum size of the Object Store. Default is 500GB.
        """
        return pulumi.get(self, "max_size_gb")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Object Store. Must be unique.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[str]]:
        """
        The region for the Object Store, if not declared we use the region as declared in the provider (Defaults to LON1)
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the Object Store.
        """
        return pulumi.get(self, "status")


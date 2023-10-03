# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ObjectStoreCredentialArgs', 'ObjectStoreCredential']

@pulumi.input_type
class ObjectStoreCredentialArgs:
    def __init__(__self__, *,
                 access_key_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 secret_access_key: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ObjectStoreCredential resource.
        :param pulumi.Input[str] access_key_id: The access key id of the Object Store Credential. It is generated by the provider.
        :param pulumi.Input[str] name: The name of the Object Store Credential. Must be unique.
        :param pulumi.Input[str] region: The region where the Object Store Credential will be created.
        :param pulumi.Input[str] secret_access_key: The secret access key of the Object Store Credential. It is generated by the provider.
        """
        ObjectStoreCredentialArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            access_key_id=access_key_id,
            name=name,
            region=region,
            secret_access_key=secret_access_key,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             access_key_id: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             region: Optional[pulumi.Input[str]] = None,
             secret_access_key: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if access_key_id is not None:
            _setter("access_key_id", access_key_id)
        if name is not None:
            _setter("name", name)
        if region is not None:
            _setter("region", region)
        if secret_access_key is not None:
            _setter("secret_access_key", secret_access_key)

    @property
    @pulumi.getter(name="accessKeyId")
    def access_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        The access key id of the Object Store Credential. It is generated by the provider.
        """
        return pulumi.get(self, "access_key_id")

    @access_key_id.setter
    def access_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_key_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Object Store Credential. Must be unique.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region where the Object Store Credential will be created.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="secretAccessKey")
    def secret_access_key(self) -> Optional[pulumi.Input[str]]:
        """
        The secret access key of the Object Store Credential. It is generated by the provider.
        """
        return pulumi.get(self, "secret_access_key")

    @secret_access_key.setter
    def secret_access_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_access_key", value)


@pulumi.input_type
class _ObjectStoreCredentialState:
    def __init__(__self__, *,
                 access_key_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 secret_access_key: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ObjectStoreCredential resources.
        :param pulumi.Input[str] access_key_id: The access key id of the Object Store Credential. It is generated by the provider.
        :param pulumi.Input[str] name: The name of the Object Store Credential. Must be unique.
        :param pulumi.Input[str] region: The region where the Object Store Credential will be created.
        :param pulumi.Input[str] secret_access_key: The secret access key of the Object Store Credential. It is generated by the provider.
        :param pulumi.Input[str] status: The status of the Object Store Credential.
        """
        _ObjectStoreCredentialState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            access_key_id=access_key_id,
            name=name,
            region=region,
            secret_access_key=secret_access_key,
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             access_key_id: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             region: Optional[pulumi.Input[str]] = None,
             secret_access_key: Optional[pulumi.Input[str]] = None,
             status: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if access_key_id is not None:
            _setter("access_key_id", access_key_id)
        if name is not None:
            _setter("name", name)
        if region is not None:
            _setter("region", region)
        if secret_access_key is not None:
            _setter("secret_access_key", secret_access_key)
        if status is not None:
            _setter("status", status)

    @property
    @pulumi.getter(name="accessKeyId")
    def access_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        The access key id of the Object Store Credential. It is generated by the provider.
        """
        return pulumi.get(self, "access_key_id")

    @access_key_id.setter
    def access_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_key_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Object Store Credential. Must be unique.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region where the Object Store Credential will be created.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="secretAccessKey")
    def secret_access_key(self) -> Optional[pulumi.Input[str]]:
        """
        The secret access key of the Object Store Credential. It is generated by the provider.
        """
        return pulumi.get(self, "secret_access_key")

    @secret_access_key.setter
    def secret_access_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_access_key", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the Object Store Credential.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class ObjectStoreCredential(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_key_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 secret_access_key: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides an Object Store Credential resource. This can be used to create, modify, and delete object stores credential.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_civo as civo

        backup_object_store_credential = civo.get_object_store_credential(name="backup-server")
        # Create a credential for the object store with a specific access key and secret key
        backup_index_object_store_credential_object_store_credential = civo.ObjectStoreCredential("backupIndex/objectStoreCredentialObjectStoreCredential",
            access_key_id="my-access-key",
            secret_access_key="my-secret-key")
        # Use the credential to create a bucket
        backup_object_store = civo.ObjectStore("backupObjectStore",
            max_size_gb=500,
            region="LON1",
            access_key_id=backup_index / object_store_credential_object_store_credential["accessKeyId"])
        ```

        ## Import

        using ID

        ```sh
         $ pulumi import civo:index/objectStoreCredential:ObjectStoreCredential custom_object b8ecd2ab-2267-4a5e-8692-cbf1d32583e3
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_key_id: The access key id of the Object Store Credential. It is generated by the provider.
        :param pulumi.Input[str] name: The name of the Object Store Credential. Must be unique.
        :param pulumi.Input[str] region: The region where the Object Store Credential will be created.
        :param pulumi.Input[str] secret_access_key: The secret access key of the Object Store Credential. It is generated by the provider.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ObjectStoreCredentialArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an Object Store Credential resource. This can be used to create, modify, and delete object stores credential.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_civo as civo

        backup_object_store_credential = civo.get_object_store_credential(name="backup-server")
        # Create a credential for the object store with a specific access key and secret key
        backup_index_object_store_credential_object_store_credential = civo.ObjectStoreCredential("backupIndex/objectStoreCredentialObjectStoreCredential",
            access_key_id="my-access-key",
            secret_access_key="my-secret-key")
        # Use the credential to create a bucket
        backup_object_store = civo.ObjectStore("backupObjectStore",
            max_size_gb=500,
            region="LON1",
            access_key_id=backup_index / object_store_credential_object_store_credential["accessKeyId"])
        ```

        ## Import

        using ID

        ```sh
         $ pulumi import civo:index/objectStoreCredential:ObjectStoreCredential custom_object b8ecd2ab-2267-4a5e-8692-cbf1d32583e3
        ```

        :param str resource_name: The name of the resource.
        :param ObjectStoreCredentialArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ObjectStoreCredentialArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ObjectStoreCredentialArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_key_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 secret_access_key: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ObjectStoreCredentialArgs.__new__(ObjectStoreCredentialArgs)

            __props__.__dict__["access_key_id"] = access_key_id
            __props__.__dict__["name"] = name
            __props__.__dict__["region"] = region
            __props__.__dict__["secret_access_key"] = secret_access_key
            __props__.__dict__["status"] = None
        super(ObjectStoreCredential, __self__).__init__(
            'civo:index/objectStoreCredential:ObjectStoreCredential',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access_key_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            secret_access_key: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'ObjectStoreCredential':
        """
        Get an existing ObjectStoreCredential resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_key_id: The access key id of the Object Store Credential. It is generated by the provider.
        :param pulumi.Input[str] name: The name of the Object Store Credential. Must be unique.
        :param pulumi.Input[str] region: The region where the Object Store Credential will be created.
        :param pulumi.Input[str] secret_access_key: The secret access key of the Object Store Credential. It is generated by the provider.
        :param pulumi.Input[str] status: The status of the Object Store Credential.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ObjectStoreCredentialState.__new__(_ObjectStoreCredentialState)

        __props__.__dict__["access_key_id"] = access_key_id
        __props__.__dict__["name"] = name
        __props__.__dict__["region"] = region
        __props__.__dict__["secret_access_key"] = secret_access_key
        __props__.__dict__["status"] = status
        return ObjectStoreCredential(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessKeyId")
    def access_key_id(self) -> pulumi.Output[str]:
        """
        The access key id of the Object Store Credential. It is generated by the provider.
        """
        return pulumi.get(self, "access_key_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Object Store Credential. Must be unique.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[str]]:
        """
        The region where the Object Store Credential will be created.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="secretAccessKey")
    def secret_access_key(self) -> pulumi.Output[str]:
        """
        The secret access key of the Object Store Credential. It is generated by the provider.
        """
        return pulumi.get(self, "secret_access_key")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the Object Store Credential.
        """
        return pulumi.get(self, "status")


# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['LoadBalancerArgs', 'LoadBalancer']

@pulumi.input_type
class LoadBalancerArgs:
    def __init__(__self__, *,
                 backends: pulumi.Input[Sequence[pulumi.Input['LoadBalancerBackendArgs']]],
                 fail_timeout: pulumi.Input[int],
                 hostname: pulumi.Input[str],
                 max_conns: pulumi.Input[int],
                 max_request_size: pulumi.Input[int],
                 policy: pulumi.Input[str],
                 port: pulumi.Input[int],
                 protocol: pulumi.Input[str],
                 health_check_path: Optional[pulumi.Input[str]] = None,
                 ignore_invalid_backend_tls: Optional[pulumi.Input[bool]] = None,
                 tls_certificate: Optional[pulumi.Input[str]] = None,
                 tls_key: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a LoadBalancer resource.
        :param pulumi.Input[Sequence[pulumi.Input['LoadBalancerBackendArgs']]] backends: a list of backend instances, each containing an instance_id, protocol (http or https) and port
        :param pulumi.Input[int] fail_timeout: how long to wait in seconds before determining a backend has failed, defaults to 30
        :param pulumi.Input[str] hostname: the hostname to receive traffic for, e.g. www.example.com (optional: sets hostname to loadbalancer-uuid.civo.com if
               blank)
        :param pulumi.Input[int] max_conns: how many concurrent connections can each backend handle, defaults to 10
        :param pulumi.Input[int] max_request_size: the size in megabytes of the maximum request content that will be accepted, defaults to 20
        :param pulumi.Input[str] policy: one of: least_conn (sends new requests to the least busy server), random (sends new requests to a random backend),
               round_robin (sends new requests to the next backend in order), ip_hash (sends requests from a given IP address to the
               same backend), default is random
        :param pulumi.Input[int] port: you can listen on any port, the default is 80 to match the default protocol of http,if not you must specify it here
               (commonly 80 for HTTP or 443 for HTTPS)
        :param pulumi.Input[str] protocol: either http or https. If you specify https then you must also provide the next two fields, the default is http
        :param pulumi.Input[str] health_check_path: what URL should be used on the backends to determine if it's OK (2xx/3xx status), defaults to /
        :param pulumi.Input[bool] ignore_invalid_backend_tls: should self-signed/invalid certificates be ignored from the backend servers, defaults to true
        :param pulumi.Input[str] tls_certificate: if your protocol is https then you should send the TLS certificate in Base64-encoded PEM format
        :param pulumi.Input[str] tls_key: if your protocol is https then you should send the TLS private key in Base64-encoded PEM format
        """
        pulumi.set(__self__, "backends", backends)
        pulumi.set(__self__, "fail_timeout", fail_timeout)
        pulumi.set(__self__, "hostname", hostname)
        pulumi.set(__self__, "max_conns", max_conns)
        pulumi.set(__self__, "max_request_size", max_request_size)
        pulumi.set(__self__, "policy", policy)
        pulumi.set(__self__, "port", port)
        pulumi.set(__self__, "protocol", protocol)
        if health_check_path is not None:
            pulumi.set(__self__, "health_check_path", health_check_path)
        if ignore_invalid_backend_tls is not None:
            pulumi.set(__self__, "ignore_invalid_backend_tls", ignore_invalid_backend_tls)
        if tls_certificate is not None:
            pulumi.set(__self__, "tls_certificate", tls_certificate)
        if tls_key is not None:
            pulumi.set(__self__, "tls_key", tls_key)

    @property
    @pulumi.getter
    def backends(self) -> pulumi.Input[Sequence[pulumi.Input['LoadBalancerBackendArgs']]]:
        """
        a list of backend instances, each containing an instance_id, protocol (http or https) and port
        """
        return pulumi.get(self, "backends")

    @backends.setter
    def backends(self, value: pulumi.Input[Sequence[pulumi.Input['LoadBalancerBackendArgs']]]):
        pulumi.set(self, "backends", value)

    @property
    @pulumi.getter(name="failTimeout")
    def fail_timeout(self) -> pulumi.Input[int]:
        """
        how long to wait in seconds before determining a backend has failed, defaults to 30
        """
        return pulumi.get(self, "fail_timeout")

    @fail_timeout.setter
    def fail_timeout(self, value: pulumi.Input[int]):
        pulumi.set(self, "fail_timeout", value)

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Input[str]:
        """
        the hostname to receive traffic for, e.g. www.example.com (optional: sets hostname to loadbalancer-uuid.civo.com if
        blank)
        """
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: pulumi.Input[str]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter(name="maxConns")
    def max_conns(self) -> pulumi.Input[int]:
        """
        how many concurrent connections can each backend handle, defaults to 10
        """
        return pulumi.get(self, "max_conns")

    @max_conns.setter
    def max_conns(self, value: pulumi.Input[int]):
        pulumi.set(self, "max_conns", value)

    @property
    @pulumi.getter(name="maxRequestSize")
    def max_request_size(self) -> pulumi.Input[int]:
        """
        the size in megabytes of the maximum request content that will be accepted, defaults to 20
        """
        return pulumi.get(self, "max_request_size")

    @max_request_size.setter
    def max_request_size(self, value: pulumi.Input[int]):
        pulumi.set(self, "max_request_size", value)

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Input[str]:
        """
        one of: least_conn (sends new requests to the least busy server), random (sends new requests to a random backend),
        round_robin (sends new requests to the next backend in order), ip_hash (sends requests from a given IP address to the
        same backend), default is random
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter
    def port(self) -> pulumi.Input[int]:
        """
        you can listen on any port, the default is 80 to match the default protocol of http,if not you must specify it here
        (commonly 80 for HTTP or 443 for HTTPS)
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: pulumi.Input[int]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[str]:
        """
        either http or https. If you specify https then you must also provide the next two fields, the default is http
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: pulumi.Input[str]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter(name="healthCheckPath")
    def health_check_path(self) -> Optional[pulumi.Input[str]]:
        """
        what URL should be used on the backends to determine if it's OK (2xx/3xx status), defaults to /
        """
        return pulumi.get(self, "health_check_path")

    @health_check_path.setter
    def health_check_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "health_check_path", value)

    @property
    @pulumi.getter(name="ignoreInvalidBackendTls")
    def ignore_invalid_backend_tls(self) -> Optional[pulumi.Input[bool]]:
        """
        should self-signed/invalid certificates be ignored from the backend servers, defaults to true
        """
        return pulumi.get(self, "ignore_invalid_backend_tls")

    @ignore_invalid_backend_tls.setter
    def ignore_invalid_backend_tls(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore_invalid_backend_tls", value)

    @property
    @pulumi.getter(name="tlsCertificate")
    def tls_certificate(self) -> Optional[pulumi.Input[str]]:
        """
        if your protocol is https then you should send the TLS certificate in Base64-encoded PEM format
        """
        return pulumi.get(self, "tls_certificate")

    @tls_certificate.setter
    def tls_certificate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tls_certificate", value)

    @property
    @pulumi.getter(name="tlsKey")
    def tls_key(self) -> Optional[pulumi.Input[str]]:
        """
        if your protocol is https then you should send the TLS private key in Base64-encoded PEM format
        """
        return pulumi.get(self, "tls_key")

    @tls_key.setter
    def tls_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tls_key", value)


@pulumi.input_type
class _LoadBalancerState:
    def __init__(__self__, *,
                 backends: Optional[pulumi.Input[Sequence[pulumi.Input['LoadBalancerBackendArgs']]]] = None,
                 fail_timeout: Optional[pulumi.Input[int]] = None,
                 health_check_path: Optional[pulumi.Input[str]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 ignore_invalid_backend_tls: Optional[pulumi.Input[bool]] = None,
                 max_conns: Optional[pulumi.Input[int]] = None,
                 max_request_size: Optional[pulumi.Input[int]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 tls_certificate: Optional[pulumi.Input[str]] = None,
                 tls_key: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering LoadBalancer resources.
        :param pulumi.Input[Sequence[pulumi.Input['LoadBalancerBackendArgs']]] backends: a list of backend instances, each containing an instance_id, protocol (http or https) and port
        :param pulumi.Input[int] fail_timeout: how long to wait in seconds before determining a backend has failed, defaults to 30
        :param pulumi.Input[str] health_check_path: what URL should be used on the backends to determine if it's OK (2xx/3xx status), defaults to /
        :param pulumi.Input[str] hostname: the hostname to receive traffic for, e.g. www.example.com (optional: sets hostname to loadbalancer-uuid.civo.com if
               blank)
        :param pulumi.Input[bool] ignore_invalid_backend_tls: should self-signed/invalid certificates be ignored from the backend servers, defaults to true
        :param pulumi.Input[int] max_conns: how many concurrent connections can each backend handle, defaults to 10
        :param pulumi.Input[int] max_request_size: the size in megabytes of the maximum request content that will be accepted, defaults to 20
        :param pulumi.Input[str] policy: one of: least_conn (sends new requests to the least busy server), random (sends new requests to a random backend),
               round_robin (sends new requests to the next backend in order), ip_hash (sends requests from a given IP address to the
               same backend), default is random
        :param pulumi.Input[int] port: you can listen on any port, the default is 80 to match the default protocol of http,if not you must specify it here
               (commonly 80 for HTTP or 443 for HTTPS)
        :param pulumi.Input[str] protocol: either http or https. If you specify https then you must also provide the next two fields, the default is http
        :param pulumi.Input[str] tls_certificate: if your protocol is https then you should send the TLS certificate in Base64-encoded PEM format
        :param pulumi.Input[str] tls_key: if your protocol is https then you should send the TLS private key in Base64-encoded PEM format
        """
        if backends is not None:
            pulumi.set(__self__, "backends", backends)
        if fail_timeout is not None:
            pulumi.set(__self__, "fail_timeout", fail_timeout)
        if health_check_path is not None:
            pulumi.set(__self__, "health_check_path", health_check_path)
        if hostname is not None:
            pulumi.set(__self__, "hostname", hostname)
        if ignore_invalid_backend_tls is not None:
            pulumi.set(__self__, "ignore_invalid_backend_tls", ignore_invalid_backend_tls)
        if max_conns is not None:
            pulumi.set(__self__, "max_conns", max_conns)
        if max_request_size is not None:
            pulumi.set(__self__, "max_request_size", max_request_size)
        if policy is not None:
            pulumi.set(__self__, "policy", policy)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)
        if tls_certificate is not None:
            pulumi.set(__self__, "tls_certificate", tls_certificate)
        if tls_key is not None:
            pulumi.set(__self__, "tls_key", tls_key)

    @property
    @pulumi.getter
    def backends(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LoadBalancerBackendArgs']]]]:
        """
        a list of backend instances, each containing an instance_id, protocol (http or https) and port
        """
        return pulumi.get(self, "backends")

    @backends.setter
    def backends(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LoadBalancerBackendArgs']]]]):
        pulumi.set(self, "backends", value)

    @property
    @pulumi.getter(name="failTimeout")
    def fail_timeout(self) -> Optional[pulumi.Input[int]]:
        """
        how long to wait in seconds before determining a backend has failed, defaults to 30
        """
        return pulumi.get(self, "fail_timeout")

    @fail_timeout.setter
    def fail_timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "fail_timeout", value)

    @property
    @pulumi.getter(name="healthCheckPath")
    def health_check_path(self) -> Optional[pulumi.Input[str]]:
        """
        what URL should be used on the backends to determine if it's OK (2xx/3xx status), defaults to /
        """
        return pulumi.get(self, "health_check_path")

    @health_check_path.setter
    def health_check_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "health_check_path", value)

    @property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[str]]:
        """
        the hostname to receive traffic for, e.g. www.example.com (optional: sets hostname to loadbalancer-uuid.civo.com if
        blank)
        """
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter(name="ignoreInvalidBackendTls")
    def ignore_invalid_backend_tls(self) -> Optional[pulumi.Input[bool]]:
        """
        should self-signed/invalid certificates be ignored from the backend servers, defaults to true
        """
        return pulumi.get(self, "ignore_invalid_backend_tls")

    @ignore_invalid_backend_tls.setter
    def ignore_invalid_backend_tls(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore_invalid_backend_tls", value)

    @property
    @pulumi.getter(name="maxConns")
    def max_conns(self) -> Optional[pulumi.Input[int]]:
        """
        how many concurrent connections can each backend handle, defaults to 10
        """
        return pulumi.get(self, "max_conns")

    @max_conns.setter
    def max_conns(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_conns", value)

    @property
    @pulumi.getter(name="maxRequestSize")
    def max_request_size(self) -> Optional[pulumi.Input[int]]:
        """
        the size in megabytes of the maximum request content that will be accepted, defaults to 20
        """
        return pulumi.get(self, "max_request_size")

    @max_request_size.setter
    def max_request_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_request_size", value)

    @property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[str]]:
        """
        one of: least_conn (sends new requests to the least busy server), random (sends new requests to a random backend),
        round_robin (sends new requests to the next backend in order), ip_hash (sends requests from a given IP address to the
        same backend), default is random
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        you can listen on any port, the default is 80 to match the default protocol of http,if not you must specify it here
        (commonly 80 for HTTP or 443 for HTTPS)
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[str]]:
        """
        either http or https. If you specify https then you must also provide the next two fields, the default is http
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter(name="tlsCertificate")
    def tls_certificate(self) -> Optional[pulumi.Input[str]]:
        """
        if your protocol is https then you should send the TLS certificate in Base64-encoded PEM format
        """
        return pulumi.get(self, "tls_certificate")

    @tls_certificate.setter
    def tls_certificate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tls_certificate", value)

    @property
    @pulumi.getter(name="tlsKey")
    def tls_key(self) -> Optional[pulumi.Input[str]]:
        """
        if your protocol is https then you should send the TLS private key in Base64-encoded PEM format
        """
        return pulumi.get(self, "tls_key")

    @tls_key.setter
    def tls_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tls_key", value)


class LoadBalancer(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backends: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LoadBalancerBackendArgs']]]]] = None,
                 fail_timeout: Optional[pulumi.Input[int]] = None,
                 health_check_path: Optional[pulumi.Input[str]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 ignore_invalid_backend_tls: Optional[pulumi.Input[bool]] = None,
                 max_conns: Optional[pulumi.Input[int]] = None,
                 max_request_size: Optional[pulumi.Input[int]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 tls_certificate: Optional[pulumi.Input[str]] = None,
                 tls_key: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a LoadBalancer resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LoadBalancerBackendArgs']]]] backends: a list of backend instances, each containing an instance_id, protocol (http or https) and port
        :param pulumi.Input[int] fail_timeout: how long to wait in seconds before determining a backend has failed, defaults to 30
        :param pulumi.Input[str] health_check_path: what URL should be used on the backends to determine if it's OK (2xx/3xx status), defaults to /
        :param pulumi.Input[str] hostname: the hostname to receive traffic for, e.g. www.example.com (optional: sets hostname to loadbalancer-uuid.civo.com if
               blank)
        :param pulumi.Input[bool] ignore_invalid_backend_tls: should self-signed/invalid certificates be ignored from the backend servers, defaults to true
        :param pulumi.Input[int] max_conns: how many concurrent connections can each backend handle, defaults to 10
        :param pulumi.Input[int] max_request_size: the size in megabytes of the maximum request content that will be accepted, defaults to 20
        :param pulumi.Input[str] policy: one of: least_conn (sends new requests to the least busy server), random (sends new requests to a random backend),
               round_robin (sends new requests to the next backend in order), ip_hash (sends requests from a given IP address to the
               same backend), default is random
        :param pulumi.Input[int] port: you can listen on any port, the default is 80 to match the default protocol of http,if not you must specify it here
               (commonly 80 for HTTP or 443 for HTTPS)
        :param pulumi.Input[str] protocol: either http or https. If you specify https then you must also provide the next two fields, the default is http
        :param pulumi.Input[str] tls_certificate: if your protocol is https then you should send the TLS certificate in Base64-encoded PEM format
        :param pulumi.Input[str] tls_key: if your protocol is https then you should send the TLS private key in Base64-encoded PEM format
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LoadBalancerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a LoadBalancer resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param LoadBalancerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LoadBalancerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backends: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LoadBalancerBackendArgs']]]]] = None,
                 fail_timeout: Optional[pulumi.Input[int]] = None,
                 health_check_path: Optional[pulumi.Input[str]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 ignore_invalid_backend_tls: Optional[pulumi.Input[bool]] = None,
                 max_conns: Optional[pulumi.Input[int]] = None,
                 max_request_size: Optional[pulumi.Input[int]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 tls_certificate: Optional[pulumi.Input[str]] = None,
                 tls_key: Optional[pulumi.Input[str]] = None,
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
            __props__ = LoadBalancerArgs.__new__(LoadBalancerArgs)

            if backends is None and not opts.urn:
                raise TypeError("Missing required property 'backends'")
            __props__.__dict__["backends"] = backends
            if fail_timeout is None and not opts.urn:
                raise TypeError("Missing required property 'fail_timeout'")
            __props__.__dict__["fail_timeout"] = fail_timeout
            __props__.__dict__["health_check_path"] = health_check_path
            if hostname is None and not opts.urn:
                raise TypeError("Missing required property 'hostname'")
            __props__.__dict__["hostname"] = hostname
            __props__.__dict__["ignore_invalid_backend_tls"] = ignore_invalid_backend_tls
            if max_conns is None and not opts.urn:
                raise TypeError("Missing required property 'max_conns'")
            __props__.__dict__["max_conns"] = max_conns
            if max_request_size is None and not opts.urn:
                raise TypeError("Missing required property 'max_request_size'")
            __props__.__dict__["max_request_size"] = max_request_size
            if policy is None and not opts.urn:
                raise TypeError("Missing required property 'policy'")
            __props__.__dict__["policy"] = policy
            if port is None and not opts.urn:
                raise TypeError("Missing required property 'port'")
            __props__.__dict__["port"] = port
            if protocol is None and not opts.urn:
                raise TypeError("Missing required property 'protocol'")
            __props__.__dict__["protocol"] = protocol
            __props__.__dict__["tls_certificate"] = tls_certificate
            __props__.__dict__["tls_key"] = tls_key
        super(LoadBalancer, __self__).__init__(
            'civo:index/loadBalancer:LoadBalancer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            backends: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LoadBalancerBackendArgs']]]]] = None,
            fail_timeout: Optional[pulumi.Input[int]] = None,
            health_check_path: Optional[pulumi.Input[str]] = None,
            hostname: Optional[pulumi.Input[str]] = None,
            ignore_invalid_backend_tls: Optional[pulumi.Input[bool]] = None,
            max_conns: Optional[pulumi.Input[int]] = None,
            max_request_size: Optional[pulumi.Input[int]] = None,
            policy: Optional[pulumi.Input[str]] = None,
            port: Optional[pulumi.Input[int]] = None,
            protocol: Optional[pulumi.Input[str]] = None,
            tls_certificate: Optional[pulumi.Input[str]] = None,
            tls_key: Optional[pulumi.Input[str]] = None) -> 'LoadBalancer':
        """
        Get an existing LoadBalancer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LoadBalancerBackendArgs']]]] backends: a list of backend instances, each containing an instance_id, protocol (http or https) and port
        :param pulumi.Input[int] fail_timeout: how long to wait in seconds before determining a backend has failed, defaults to 30
        :param pulumi.Input[str] health_check_path: what URL should be used on the backends to determine if it's OK (2xx/3xx status), defaults to /
        :param pulumi.Input[str] hostname: the hostname to receive traffic for, e.g. www.example.com (optional: sets hostname to loadbalancer-uuid.civo.com if
               blank)
        :param pulumi.Input[bool] ignore_invalid_backend_tls: should self-signed/invalid certificates be ignored from the backend servers, defaults to true
        :param pulumi.Input[int] max_conns: how many concurrent connections can each backend handle, defaults to 10
        :param pulumi.Input[int] max_request_size: the size in megabytes of the maximum request content that will be accepted, defaults to 20
        :param pulumi.Input[str] policy: one of: least_conn (sends new requests to the least busy server), random (sends new requests to a random backend),
               round_robin (sends new requests to the next backend in order), ip_hash (sends requests from a given IP address to the
               same backend), default is random
        :param pulumi.Input[int] port: you can listen on any port, the default is 80 to match the default protocol of http,if not you must specify it here
               (commonly 80 for HTTP or 443 for HTTPS)
        :param pulumi.Input[str] protocol: either http or https. If you specify https then you must also provide the next two fields, the default is http
        :param pulumi.Input[str] tls_certificate: if your protocol is https then you should send the TLS certificate in Base64-encoded PEM format
        :param pulumi.Input[str] tls_key: if your protocol is https then you should send the TLS private key in Base64-encoded PEM format
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _LoadBalancerState.__new__(_LoadBalancerState)

        __props__.__dict__["backends"] = backends
        __props__.__dict__["fail_timeout"] = fail_timeout
        __props__.__dict__["health_check_path"] = health_check_path
        __props__.__dict__["hostname"] = hostname
        __props__.__dict__["ignore_invalid_backend_tls"] = ignore_invalid_backend_tls
        __props__.__dict__["max_conns"] = max_conns
        __props__.__dict__["max_request_size"] = max_request_size
        __props__.__dict__["policy"] = policy
        __props__.__dict__["port"] = port
        __props__.__dict__["protocol"] = protocol
        __props__.__dict__["tls_certificate"] = tls_certificate
        __props__.__dict__["tls_key"] = tls_key
        return LoadBalancer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def backends(self) -> pulumi.Output[Sequence['outputs.LoadBalancerBackend']]:
        """
        a list of backend instances, each containing an instance_id, protocol (http or https) and port
        """
        return pulumi.get(self, "backends")

    @property
    @pulumi.getter(name="failTimeout")
    def fail_timeout(self) -> pulumi.Output[int]:
        """
        how long to wait in seconds before determining a backend has failed, defaults to 30
        """
        return pulumi.get(self, "fail_timeout")

    @property
    @pulumi.getter(name="healthCheckPath")
    def health_check_path(self) -> pulumi.Output[Optional[str]]:
        """
        what URL should be used on the backends to determine if it's OK (2xx/3xx status), defaults to /
        """
        return pulumi.get(self, "health_check_path")

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Output[str]:
        """
        the hostname to receive traffic for, e.g. www.example.com (optional: sets hostname to loadbalancer-uuid.civo.com if
        blank)
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter(name="ignoreInvalidBackendTls")
    def ignore_invalid_backend_tls(self) -> pulumi.Output[Optional[bool]]:
        """
        should self-signed/invalid certificates be ignored from the backend servers, defaults to true
        """
        return pulumi.get(self, "ignore_invalid_backend_tls")

    @property
    @pulumi.getter(name="maxConns")
    def max_conns(self) -> pulumi.Output[int]:
        """
        how many concurrent connections can each backend handle, defaults to 10
        """
        return pulumi.get(self, "max_conns")

    @property
    @pulumi.getter(name="maxRequestSize")
    def max_request_size(self) -> pulumi.Output[int]:
        """
        the size in megabytes of the maximum request content that will be accepted, defaults to 20
        """
        return pulumi.get(self, "max_request_size")

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output[str]:
        """
        one of: least_conn (sends new requests to the least busy server), random (sends new requests to a random backend),
        round_robin (sends new requests to the next backend in order), ip_hash (sends requests from a given IP address to the
        same backend), default is random
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[int]:
        """
        you can listen on any port, the default is 80 to match the default protocol of http,if not you must specify it here
        (commonly 80 for HTTP or 443 for HTTPS)
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[str]:
        """
        either http or https. If you specify https then you must also provide the next two fields, the default is http
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="tlsCertificate")
    def tls_certificate(self) -> pulumi.Output[Optional[str]]:
        """
        if your protocol is https then you should send the TLS certificate in Base64-encoded PEM format
        """
        return pulumi.get(self, "tls_certificate")

    @property
    @pulumi.getter(name="tlsKey")
    def tls_key(self) -> pulumi.Output[Optional[str]]:
        """
        if your protocol is https then you should send the TLS private key in Base64-encoded PEM format
        """
        return pulumi.get(self, "tls_key")


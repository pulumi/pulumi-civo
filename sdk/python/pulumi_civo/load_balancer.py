# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import _utilities, _tables


class LoadBalancer(pulumi.CustomResource):
    backends: pulumi.Output[list]
    """
    a list of backend instances, each containing an instance_id, protocol (http or https) and port

      * `instance_id` (`str`)
      * `port` (`float`)
      * `protocol` (`str`)
    """
    fail_timeout: pulumi.Output[float]
    """
    how long to wait in seconds before determining a backend has failed, defaults to 30
    """
    health_check_path: pulumi.Output[str]
    """
    what URL should be used on the backends to determine if it's OK (2xx/3xx status), defaults to /
    """
    hostname: pulumi.Output[str]
    """
    the hostname to receive traffic for, e.g. www.example.com (optional: sets hostname to loadbalancer-uuid.civo.com if
    blank)
    """
    ignore_invalid_backend_tls: pulumi.Output[bool]
    """
    should self-signed/invalid certificates be ignored from the backend servers, defaults to true
    """
    max_conns: pulumi.Output[float]
    """
    how many concurrent connections can each backend handle, defaults to 10
    """
    max_request_size: pulumi.Output[float]
    """
    the size in megabytes of the maximum request content that will be accepted, defaults to 20
    """
    policy: pulumi.Output[str]
    """
    one of: least_conn (sends new requests to the least busy server), random (sends new requests to a random backend),
    round_robin (sends new requests to the next backend in order), ip_hash (sends requests from a given IP address to the
    same backend), default is random
    """
    port: pulumi.Output[float]
    """
    you can listen on any port, the default is 80 to match the default protocol of http,if not you must specify it here
    (commonly 80 for HTTP or 443 for HTTPS)
    """
    protocol: pulumi.Output[str]
    """
    either http or https. If you specify https then you must also provide the next two fields, the default is http
    """
    tls_certificate: pulumi.Output[str]
    """
    if your protocol is https then you should send the TLS certificate in Base64-encoded PEM format
    """
    tls_key: pulumi.Output[str]
    """
    if your protocol is https then you should send the TLS private key in Base64-encoded PEM format
    """
    def __init__(__self__, resource_name, opts=None, backends=None, fail_timeout=None, health_check_path=None, hostname=None, ignore_invalid_backend_tls=None, max_conns=None, max_request_size=None, policy=None, port=None, protocol=None, tls_certificate=None, tls_key=None, __props__=None, __name__=None, __opts__=None):
        """
        Create a LoadBalancer resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] backends: a list of backend instances, each containing an instance_id, protocol (http or https) and port
        :param pulumi.Input[float] fail_timeout: how long to wait in seconds before determining a backend has failed, defaults to 30
        :param pulumi.Input[str] health_check_path: what URL should be used on the backends to determine if it's OK (2xx/3xx status), defaults to /
        :param pulumi.Input[str] hostname: the hostname to receive traffic for, e.g. www.example.com (optional: sets hostname to loadbalancer-uuid.civo.com if
               blank)
        :param pulumi.Input[bool] ignore_invalid_backend_tls: should self-signed/invalid certificates be ignored from the backend servers, defaults to true
        :param pulumi.Input[float] max_conns: how many concurrent connections can each backend handle, defaults to 10
        :param pulumi.Input[float] max_request_size: the size in megabytes of the maximum request content that will be accepted, defaults to 20
        :param pulumi.Input[str] policy: one of: least_conn (sends new requests to the least busy server), random (sends new requests to a random backend),
               round_robin (sends new requests to the next backend in order), ip_hash (sends requests from a given IP address to the
               same backend), default is random
        :param pulumi.Input[float] port: you can listen on any port, the default is 80 to match the default protocol of http,if not you must specify it here
               (commonly 80 for HTTP or 443 for HTTPS)
        :param pulumi.Input[str] protocol: either http or https. If you specify https then you must also provide the next two fields, the default is http
        :param pulumi.Input[str] tls_certificate: if your protocol is https then you should send the TLS certificate in Base64-encoded PEM format
        :param pulumi.Input[str] tls_key: if your protocol is https then you should send the TLS private key in Base64-encoded PEM format

        The **backends** object supports the following:

          * `instance_id` (`pulumi.Input[str]`)
          * `port` (`pulumi.Input[float]`)
          * `protocol` (`pulumi.Input[str]`)
        """
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

            if backends is None:
                raise TypeError("Missing required property 'backends'")
            __props__['backends'] = backends
            if fail_timeout is None:
                raise TypeError("Missing required property 'fail_timeout'")
            __props__['fail_timeout'] = fail_timeout
            __props__['health_check_path'] = health_check_path
            if hostname is None:
                raise TypeError("Missing required property 'hostname'")
            __props__['hostname'] = hostname
            __props__['ignore_invalid_backend_tls'] = ignore_invalid_backend_tls
            if max_conns is None:
                raise TypeError("Missing required property 'max_conns'")
            __props__['max_conns'] = max_conns
            if max_request_size is None:
                raise TypeError("Missing required property 'max_request_size'")
            __props__['max_request_size'] = max_request_size
            if policy is None:
                raise TypeError("Missing required property 'policy'")
            __props__['policy'] = policy
            if port is None:
                raise TypeError("Missing required property 'port'")
            __props__['port'] = port
            if protocol is None:
                raise TypeError("Missing required property 'protocol'")
            __props__['protocol'] = protocol
            __props__['tls_certificate'] = tls_certificate
            __props__['tls_key'] = tls_key
        super(LoadBalancer, __self__).__init__(
            'civo:index/loadBalancer:LoadBalancer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, backends=None, fail_timeout=None, health_check_path=None, hostname=None, ignore_invalid_backend_tls=None, max_conns=None, max_request_size=None, policy=None, port=None, protocol=None, tls_certificate=None, tls_key=None):
        """
        Get an existing LoadBalancer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] backends: a list of backend instances, each containing an instance_id, protocol (http or https) and port
        :param pulumi.Input[float] fail_timeout: how long to wait in seconds before determining a backend has failed, defaults to 30
        :param pulumi.Input[str] health_check_path: what URL should be used on the backends to determine if it's OK (2xx/3xx status), defaults to /
        :param pulumi.Input[str] hostname: the hostname to receive traffic for, e.g. www.example.com (optional: sets hostname to loadbalancer-uuid.civo.com if
               blank)
        :param pulumi.Input[bool] ignore_invalid_backend_tls: should self-signed/invalid certificates be ignored from the backend servers, defaults to true
        :param pulumi.Input[float] max_conns: how many concurrent connections can each backend handle, defaults to 10
        :param pulumi.Input[float] max_request_size: the size in megabytes of the maximum request content that will be accepted, defaults to 20
        :param pulumi.Input[str] policy: one of: least_conn (sends new requests to the least busy server), random (sends new requests to a random backend),
               round_robin (sends new requests to the next backend in order), ip_hash (sends requests from a given IP address to the
               same backend), default is random
        :param pulumi.Input[float] port: you can listen on any port, the default is 80 to match the default protocol of http,if not you must specify it here
               (commonly 80 for HTTP or 443 for HTTPS)
        :param pulumi.Input[str] protocol: either http or https. If you specify https then you must also provide the next two fields, the default is http
        :param pulumi.Input[str] tls_certificate: if your protocol is https then you should send the TLS certificate in Base64-encoded PEM format
        :param pulumi.Input[str] tls_key: if your protocol is https then you should send the TLS private key in Base64-encoded PEM format

        The **backends** object supports the following:

          * `instance_id` (`pulumi.Input[str]`)
          * `port` (`pulumi.Input[float]`)
          * `protocol` (`pulumi.Input[str]`)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["backends"] = backends
        __props__["fail_timeout"] = fail_timeout
        __props__["health_check_path"] = health_check_path
        __props__["hostname"] = hostname
        __props__["ignore_invalid_backend_tls"] = ignore_invalid_backend_tls
        __props__["max_conns"] = max_conns
        __props__["max_request_size"] = max_request_size
        __props__["policy"] = policy
        __props__["port"] = port
        __props__["protocol"] = protocol
        __props__["tls_certificate"] = tls_certificate
        __props__["tls_key"] = tls_key
        return LoadBalancer(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Civo
{
    public static class GetReservedIp
    {
        public static Task<GetReservedIpResult> InvokeAsync(GetReservedIpArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetReservedIpResult>("civo:index/getReservedIp:getReservedIp", args ?? new GetReservedIpArgs(), options.WithDefaults());

        public static Output<GetReservedIpResult> Invoke(GetReservedIpInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetReservedIpResult>("civo:index/getReservedIp:getReservedIp", args ?? new GetReservedIpInvokeArgs(), options.WithDefaults());

        public static Output<GetReservedIpResult> Invoke(GetReservedIpInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetReservedIpResult>("civo:index/getReservedIp:getReservedIp", args ?? new GetReservedIpInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetReservedIpArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// ID for the ip address
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// Name for the ip address
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        public GetReservedIpArgs()
        {
        }
        public static new GetReservedIpArgs Empty => new GetReservedIpArgs();
    }

    public sealed class GetReservedIpInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// ID for the ip address
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Name for the ip address
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public GetReservedIpInvokeArgs()
        {
        }
        public static new GetReservedIpInvokeArgs Empty => new GetReservedIpInvokeArgs();
    }


    [OutputType]
    public sealed class GetReservedIpResult
    {
        /// <summary>
        /// ID for the ip address
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// The ID of the instance the IP is attached to
        /// </summary>
        public readonly string InstanceId;
        /// <summary>
        /// The name of the instance the IP is attached to
        /// </summary>
        public readonly string InstanceName;
        /// <summary>
        /// The IP Address requested
        /// </summary>
        public readonly string Ip;
        /// <summary>
        /// Name for the ip address
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// The region the ip address is in
        /// </summary>
        public readonly string Region;

        [OutputConstructor]
        private GetReservedIpResult(
            string? id,

            string instanceId,

            string instanceName,

            string ip,

            string? name,

            string region)
        {
            Id = id;
            InstanceId = instanceId;
            InstanceName = instanceName;
            Ip = ip;
            Name = name;
            Region = region;
        }
    }
}

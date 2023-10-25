// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Civo
{
    public static class GetDnsDomainRecord
    {
        /// <summary>
        /// Get information on a DNS record. This data source provides the name, TTL, and zone file as configured on your Civo account.
        /// 
        /// An error will be raised if the provided domain name or record are not in your Civo account.
        /// </summary>
        public static Task<GetDnsDomainRecordResult> InvokeAsync(GetDnsDomainRecordArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDnsDomainRecordResult>("civo:index/getDnsDomainRecord:getDnsDomainRecord", args ?? new GetDnsDomainRecordArgs(), options.WithDefaults());

        /// <summary>
        /// Get information on a DNS record. This data source provides the name, TTL, and zone file as configured on your Civo account.
        /// 
        /// An error will be raised if the provided domain name or record are not in your Civo account.
        /// </summary>
        public static Output<GetDnsDomainRecordResult> Invoke(GetDnsDomainRecordInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDnsDomainRecordResult>("civo:index/getDnsDomainRecord:getDnsDomainRecord", args ?? new GetDnsDomainRecordInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDnsDomainRecordArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the domain
        /// </summary>
        [Input("domainId", required: true)]
        public string DomainId { get; set; } = null!;

        /// <summary>
        /// The name of the record
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetDnsDomainRecordArgs()
        {
        }
        public static new GetDnsDomainRecordArgs Empty => new GetDnsDomainRecordArgs();
    }

    public sealed class GetDnsDomainRecordInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the domain
        /// </summary>
        [Input("domainId", required: true)]
        public Input<string> DomainId { get; set; } = null!;

        /// <summary>
        /// The name of the record
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetDnsDomainRecordInvokeArgs()
        {
        }
        public static new GetDnsDomainRecordInvokeArgs Empty => new GetDnsDomainRecordInvokeArgs();
    }


    [OutputType]
    public sealed class GetDnsDomainRecordResult
    {
        /// <summary>
        /// The ID account of the domain
        /// </summary>
        public readonly string AccountId;
        /// <summary>
        /// The date when it was created in UTC format
        /// </summary>
        public readonly string CreatedAt;
        /// <summary>
        /// The ID of the domain
        /// </summary>
        public readonly string DomainId;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The name of the record
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The priority of the record
        /// </summary>
        public readonly int Priority;
        /// <summary>
        /// How long caching DNS servers should cache this record
        /// </summary>
        public readonly int Ttl;
        /// <summary>
        /// The choice of record type from A, CNAME, MX, SRV or TXT
        /// </summary>
        public readonly string Type;
        /// <summary>
        /// The date when it was updated in UTC format
        /// </summary>
        public readonly string UpdatedAt;
        /// <summary>
        /// The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record
        /// </summary>
        public readonly string Value;

        [OutputConstructor]
        private GetDnsDomainRecordResult(
            string accountId,

            string createdAt,

            string domainId,

            string id,

            string name,

            int priority,

            int ttl,

            string type,

            string updatedAt,

            string value)
        {
            AccountId = accountId;
            CreatedAt = createdAt;
            DomainId = domainId;
            Id = id;
            Name = name;
            Priority = priority;
            Ttl = ttl;
            Type = type;
            UpdatedAt = updatedAt;
            Value = value;
        }
    }
}

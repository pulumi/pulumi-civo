// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Civo
{
    public static class GetInstance
    {
        public static Task<GetInstanceResult> InvokeAsync(GetInstanceArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetInstanceResult>("civo:index/getInstance:getInstance", args ?? new GetInstanceArgs(), options.WithVersion());
    }


    public sealed class GetInstanceArgs : Pulumi.InvokeArgs
    {
        [Input("hostname")]
        public string? Hostname { get; set; }

        [Input("id")]
        public string? Id { get; set; }

        public GetInstanceArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetInstanceResult
    {
        public readonly int CpuCores;
        public readonly string CreatedAt;
        public readonly int DiskGb;
        public readonly string FirewallId;
        public readonly string? Hostname;
        public readonly string? Id;
        public readonly string InitialPassword;
        public readonly string InitialUser;
        public readonly string NetworkId;
        public readonly string Notes;
        public readonly string PrivateIp;
        public readonly string PseudoIp;
        public readonly string PublicIp;
        public readonly int RamMb;
        public readonly string ReverseDns;
        public readonly string Script;
        public readonly string Size;
        public readonly string SshkeyId;
        public readonly string Status;
        public readonly ImmutableArray<string> Tags;
        public readonly string Template;

        [OutputConstructor]
        private GetInstanceResult(
            int cpuCores,

            string createdAt,

            int diskGb,

            string firewallId,

            string? hostname,

            string? id,

            string initialPassword,

            string initialUser,

            string networkId,

            string notes,

            string privateIp,

            string pseudoIp,

            string publicIp,

            int ramMb,

            string reverseDns,

            string script,

            string size,

            string sshkeyId,

            string status,

            ImmutableArray<string> tags,

            string template)
        {
            CpuCores = cpuCores;
            CreatedAt = createdAt;
            DiskGb = diskGb;
            FirewallId = firewallId;
            Hostname = hostname;
            Id = id;
            InitialPassword = initialPassword;
            InitialUser = initialUser;
            NetworkId = networkId;
            Notes = notes;
            PrivateIp = privateIp;
            PseudoIp = pseudoIp;
            PublicIp = publicIp;
            RamMb = ramMb;
            ReverseDns = reverseDns;
            Script = script;
            Size = size;
            SshkeyId = sshkeyId;
            Status = status;
            Tags = tags;
            Template = template;
        }
    }
}

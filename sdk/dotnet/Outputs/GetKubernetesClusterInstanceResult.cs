// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Civo.Outputs
{

    [OutputType]
    public sealed class GetKubernetesClusterInstanceResult
    {
        public readonly int CpuCores;
        public readonly string CreatedAt;
        public readonly int DiskGb;
        public readonly string FirewallId;
        public readonly string Hostname;
        public readonly string PublicIp;
        public readonly int RamMb;
        public readonly string Region;
        public readonly string Size;
        public readonly string Status;
        public readonly ImmutableArray<string> Tags;

        [OutputConstructor]
        private GetKubernetesClusterInstanceResult(
            int cpuCores,

            string createdAt,

            int diskGb,

            string firewallId,

            string hostname,

            string publicIp,

            int ramMb,

            string region,

            string size,

            string status,

            ImmutableArray<string> tags)
        {
            CpuCores = cpuCores;
            CreatedAt = createdAt;
            DiskGb = diskGb;
            FirewallId = firewallId;
            Hostname = hostname;
            PublicIp = publicIp;
            RamMb = ramMb;
            Region = region;
            Size = size;
            Status = status;
            Tags = tags;
        }
    }
}

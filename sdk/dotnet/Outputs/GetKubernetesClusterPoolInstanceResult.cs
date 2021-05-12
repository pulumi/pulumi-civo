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
    public sealed class GetKubernetesClusterPoolInstanceResult
    {
        /// <summary>
        /// Total cpu of the inatance.
        /// </summary>
        public readonly int CpuCores;
        /// <summary>
        /// The size of the disk.
        /// </summary>
        public readonly int DiskGb;
        /// <summary>
        /// The hostname of the instance.
        /// </summary>
        public readonly string Hostname;
        /// <summary>
        /// Total ram of the instance
        /// </summary>
        public readonly int RamMb;
        /// <summary>
        /// The size of the instance.
        /// </summary>
        public readonly string Size;
        /// <summary>
        /// The status of Kubernetes cluster.
        /// * `ready` -If the Kubernetes cluster is ready.
        /// </summary>
        public readonly string Status;
        /// <summary>
        /// The tag of the instances
        /// </summary>
        public readonly ImmutableArray<string> Tags;

        [OutputConstructor]
        private GetKubernetesClusterPoolInstanceResult(
            int cpuCores,

            int diskGb,

            string hostname,

            int ramMb,

            string size,

            string status,

            ImmutableArray<string> tags)
        {
            CpuCores = cpuCores;
            DiskGb = diskGb;
            Hostname = hostname;
            RamMb = ramMb;
            Size = size;
            Status = status;
            Tags = tags;
        }
    }
}

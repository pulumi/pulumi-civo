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
    public sealed class KubernetesClusterPools
    {
        /// <summary>
        /// Instance names in the nodepool
        /// </summary>
        public readonly ImmutableArray<string> InstanceNames;
        /// <summary>
        /// Node pool label, if you don't provide one, we will generate one for you
        /// </summary>
        public readonly string? Label;
        /// <summary>
        /// Number of nodes in the nodepool
        /// </summary>
        public readonly int NodeCount;
        /// <summary>
        /// Node pool belongs to the public ip node pool
        /// </summary>
        public readonly bool? PublicIpNodePool;
        /// <summary>
        /// Size of the nodes in the nodepool
        /// </summary>
        public readonly string Size;

        [OutputConstructor]
        private KubernetesClusterPools(
            ImmutableArray<string> instanceNames,

            string? label,

            int nodeCount,

            bool? publicIpNodePool,

            string size)
        {
            InstanceNames = instanceNames;
            Label = label;
            NodeCount = nodeCount;
            PublicIpNodePool = publicIpNodePool;
            Size = size;
        }
    }
}

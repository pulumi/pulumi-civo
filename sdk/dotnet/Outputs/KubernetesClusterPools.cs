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
        public readonly ImmutableDictionary<string, string>? Labels;
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
        public readonly ImmutableArray<Outputs.KubernetesClusterPoolsTaint> Taints;

        [OutputConstructor]
        private KubernetesClusterPools(
            ImmutableArray<string> instanceNames,

            string? label,

            ImmutableDictionary<string, string>? labels,

            int nodeCount,

            bool? publicIpNodePool,

            string size,

            ImmutableArray<Outputs.KubernetesClusterPoolsTaint> taints)
        {
            InstanceNames = instanceNames;
            Label = label;
            Labels = labels;
            NodeCount = nodeCount;
            PublicIpNodePool = publicIpNodePool;
            Size = size;
            Taints = taints;
        }
    }
}

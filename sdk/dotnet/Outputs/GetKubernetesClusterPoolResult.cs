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
    public sealed class GetKubernetesClusterPoolResult
    {
        public readonly ImmutableArray<string> InstanceNames;
        public readonly string Label;
        public readonly int NodeCount;
        public readonly bool PublicIpNodePool;
        public readonly string Size;

        [OutputConstructor]
        private GetKubernetesClusterPoolResult(
            ImmutableArray<string> instanceNames,

            string label,

            int nodeCount,

            bool publicIpNodePool,

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

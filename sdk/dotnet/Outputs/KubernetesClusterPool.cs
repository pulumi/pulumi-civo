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
    public sealed class KubernetesClusterPool
    {
        public readonly int? Count;
        /// <summary>
        /// The ID of this resource.
        /// </summary>
        public readonly string? Id;
        public readonly ImmutableArray<string> InstanceNames;
        public readonly ImmutableArray<Outputs.KubernetesClusterPoolInstance> Instances;
        public readonly string? Size;

        [OutputConstructor]
        private KubernetesClusterPool(
            int? count,

            string? id,

            ImmutableArray<string> instanceNames,

            ImmutableArray<Outputs.KubernetesClusterPoolInstance> instances,

            string? size)
        {
            Count = count;
            Id = id;
            InstanceNames = instanceNames;
            Instances = instances;
            Size = size;
        }
    }
}

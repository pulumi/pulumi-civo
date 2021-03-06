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
    public sealed class GetInstancesSortResult
    {
        /// <summary>
        /// The sort direction. This may be either `asc` or `desc`.
        /// </summary>
        public readonly string? Direction;
        /// <summary>
        /// Sort the Instance by this key. This may be one of `id`, `hostname`, `public_ip`, `private_ip`,
        /// `pseudo_ip`, `size`, `cpu_cores`, `ram_mb`, `disk_gb`, `template` or `created_at`.
        /// </summary>
        public readonly string Key;

        [OutputConstructor]
        private GetInstancesSortResult(
            string? direction,

            string key)
        {
            Direction = direction;
            Key = key;
        }
    }
}

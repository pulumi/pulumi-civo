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
    public sealed class GetInstancesFilterResult
    {
        public readonly bool? All;
        /// <summary>
        /// Filter the Instances by this key. This may be one of '`id`, `hostname`, `public_ip`, `private_ip`,
        /// `pseudo_ip`, `size`, `cpu_cores`, `ram_mb`, `disk_gb`, `template` or `created_at`.
        /// </summary>
        public readonly string Key;
        public readonly string? MatchBy;
        /// <summary>
        /// A list of values to match against the `key` field. Only retrieves Instances
        /// where the `key` field takes on one or more of the values provided here.
        /// </summary>
        public readonly ImmutableArray<string> Values;

        [OutputConstructor]
        private GetInstancesFilterResult(
            bool? all,

            string key,

            string? matchBy,

            ImmutableArray<string> values)
        {
            All = all;
            Key = key;
            MatchBy = matchBy;
            Values = values;
        }
    }
}

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
    public sealed class GetRegionSortResult
    {
        public readonly string? Direction;
        public readonly string Key;

        [OutputConstructor]
        private GetRegionSortResult(
            string? direction,

            string key)
        {
            Direction = direction;
            Key = key;
        }
    }
}

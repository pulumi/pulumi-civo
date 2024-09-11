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
    public sealed class GetRegionRegionResult
    {
        /// <summary>
        /// The code of the region
        /// </summary>
        public readonly string Code;
        /// <summary>
        /// The country of the region
        /// </summary>
        public readonly string Country;
        /// <summary>
        /// If the region is the default region, this will return `true`
        /// </summary>
        public readonly bool Default;
        /// <summary>
        /// A human name of the region
        /// </summary>
        public readonly string Name;

        [OutputConstructor]
        private GetRegionRegionResult(
            string code,

            string country,

            bool @default,

            string name)
        {
            Code = code;
            Country = country;
            Default = @default;
            Name = name;
        }
    }
}
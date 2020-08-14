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
    public sealed class GetTemplateFilterResult
    {
        /// <summary>
        /// Filter the sizes by this key. This may be one of `code`,
        /// `name`.
        /// </summary>
        public readonly string Key;
        /// <summary>
        /// Only retrieves the template which keys has value that matches
        /// one of the values provided here.
        /// </summary>
        public readonly ImmutableArray<string> Values;

        [OutputConstructor]
        private GetTemplateFilterResult(
            string key,

            ImmutableArray<string> values)
        {
            Key = key;
            Values = values;
        }
    }
}
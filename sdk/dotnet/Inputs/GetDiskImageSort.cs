// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Civo.Inputs
{

    public sealed class GetDiskImageSortArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The sort direction. This may be either `asc` or `desc`.
        /// </summary>
        [Input("direction")]
        public string? Direction { get; set; }

        /// <summary>
        /// Sort diskimages by this key. This may be one of `id`, `label`, `name`, `version`.
        /// </summary>
        [Input("key", required: true)]
        public string Key { get; set; } = null!;

        public GetDiskImageSortArgs()
        {
        }
        public static new GetDiskImageSortArgs Empty => new GetDiskImageSortArgs();
    }
}

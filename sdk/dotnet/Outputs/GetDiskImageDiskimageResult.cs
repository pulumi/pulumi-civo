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
    public sealed class GetDiskImageDiskimageResult
    {
        /// <summary>
        /// ID of disk image
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Label of disk image
        /// </summary>
        public readonly string Label;
        /// <summary>
        /// Name of disk image
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Version of disk image
        /// </summary>
        public readonly string Version;

        [OutputConstructor]
        private GetDiskImageDiskimageResult(
            string id,

            string label,

            string name,

            string version)
        {
            Id = id;
            Label = label;
            Name = name;
            Version = version;
        }
    }
}

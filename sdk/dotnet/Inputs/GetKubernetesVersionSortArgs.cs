// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Civo.Inputs
{

    public sealed class GetKubernetesVersionSortArgs : Pulumi.InvokeArgs
    {
        [Input("direction")]
        public string? Direction { get; set; }

        [Input("key", required: true)]
        public string Key { get; set; } = null!;

        public GetKubernetesVersionSortArgs()
        {
        }
    }
}

// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Civo.Inputs
{

    public sealed class KubernetesClusterPoolsTaintGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("effect", required: true)]
        public Input<string> Effect { get; set; } = null!;

        [Input("key", required: true)]
        public Input<string> Key { get; set; } = null!;

        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public KubernetesClusterPoolsTaintGetArgs()
        {
        }
        public static new KubernetesClusterPoolsTaintGetArgs Empty => new KubernetesClusterPoolsTaintGetArgs();
    }
}

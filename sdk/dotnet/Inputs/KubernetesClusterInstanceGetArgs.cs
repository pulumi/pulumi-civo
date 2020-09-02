// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Civo.Inputs
{

    public sealed class KubernetesClusterInstanceGetArgs : Pulumi.ResourceArgs
    {
        [Input("cpuCores")]
        public Input<int>? CpuCores { get; set; }

        [Input("createdAt")]
        public Input<string>? CreatedAt { get; set; }

        [Input("diskGb")]
        public Input<int>? DiskGb { get; set; }

        [Input("firewallId")]
        public Input<string>? FirewallId { get; set; }

        [Input("hostname")]
        public Input<string>? Hostname { get; set; }

        [Input("publicIp")]
        public Input<string>? PublicIp { get; set; }

        [Input("ramMb")]
        public Input<int>? RamMb { get; set; }

        [Input("region")]
        public Input<string>? Region { get; set; }

        [Input("size")]
        public Input<string>? Size { get; set; }

        [Input("status")]
        public Input<string>? Status { get; set; }

        [Input("tags")]
        private InputList<string>? _tags;
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        public KubernetesClusterInstanceGetArgs()
        {
        }
    }
}

// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Civo.Inputs
{

    public sealed class FirewallIngressRuleGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The action of the rule can be allow or deny. When we set the `action = 'allow'`, this is going to add a rule to allow traffic. Similarly, setting `action = 'deny'` will deny the traffic.
        /// </summary>
        [Input("action", required: true)]
        public Input<string> Action { get; set; } = null!;

        [Input("cidrs", required: true)]
        private InputList<string>? _cidrs;

        /// <summary>
        /// The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32 to open just for a specific IP address)
        /// </summary>
        public InputList<string> Cidrs
        {
            get => _cidrs ?? (_cidrs = new InputList<string>());
            set => _cidrs = value;
        }

        /// <summary>
        /// (String) The ID of this resource.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// A string that will be the displayed name/reference for this rule
        /// </summary>
        [Input("label")]
        public Input<string>? Label { get; set; }

        /// <summary>
        /// The port or port range to open, can be a single port or a range separated by a dash (`-`), e.g. `80` or `80-443`
        /// </summary>
        [Input("portRange")]
        public Input<string>? PortRange { get; set; }

        /// <summary>
        /// The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
        /// </summary>
        [Input("protocol")]
        public Input<string>? Protocol { get; set; }

        public FirewallIngressRuleGetArgs()
        {
        }
        public static new FirewallIngressRuleGetArgs Empty => new FirewallIngressRuleGetArgs();
    }
}

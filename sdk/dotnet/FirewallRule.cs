// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Civo
{
    public partial class FirewallRule : Pulumi.CustomResource
    {
        /// <summary>
        /// The IP address of the other end (i.e. not your instance) to affect, or a valid network CIDR (defaults to being globally
        /// applied, i.e. 0.0.0.0/0)
        /// </summary>
        [Output("cidrs")]
        public Output<ImmutableArray<string>> Cidrs { get; private set; } = null!;

        /// <summary>
        /// Will this rule affect ingress traffic
        /// </summary>
        [Output("direction")]
        public Output<string> Direction { get; private set; } = null!;

        /// <summary>
        /// The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
        /// </summary>
        [Output("endPort")]
        public Output<string> EndPort { get; private set; } = null!;

        [Output("firewallId")]
        public Output<string> FirewallId { get; private set; } = null!;

        /// <summary>
        /// A string that will be the displayed name/reference for this rule (optional)
        /// </summary>
        [Output("label")]
        public Output<string?> Label { get; private set; } = null!;

        /// <summary>
        /// The protocol choice from tcp, udp or icmp (the default if unspecified is tcp)
        /// </summary>
        [Output("protocol")]
        public Output<string> Protocol { get; private set; } = null!;

        /// <summary>
        /// The start of the port range to configure for this rule (or the single port if required)
        /// </summary>
        [Output("startPort")]
        public Output<string> StartPort { get; private set; } = null!;


        /// <summary>
        /// Create a FirewallRule resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public FirewallRule(string name, FirewallRuleArgs args, CustomResourceOptions? options = null)
            : base("civo:index/firewallRule:FirewallRule", name, args ?? new FirewallRuleArgs(), MakeResourceOptions(options, ""))
        {
        }

        private FirewallRule(string name, Input<string> id, FirewallRuleState? state = null, CustomResourceOptions? options = null)
            : base("civo:index/firewallRule:FirewallRule", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing FirewallRule resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static FirewallRule Get(string name, Input<string> id, FirewallRuleState? state = null, CustomResourceOptions? options = null)
        {
            return new FirewallRule(name, id, state, options);
        }
    }

    public sealed class FirewallRuleArgs : Pulumi.ResourceArgs
    {
        [Input("cidrs", required: true)]
        private InputList<string>? _cidrs;

        /// <summary>
        /// The IP address of the other end (i.e. not your instance) to affect, or a valid network CIDR (defaults to being globally
        /// applied, i.e. 0.0.0.0/0)
        /// </summary>
        public InputList<string> Cidrs
        {
            get => _cidrs ?? (_cidrs = new InputList<string>());
            set => _cidrs = value;
        }

        /// <summary>
        /// Will this rule affect ingress traffic
        /// </summary>
        [Input("direction", required: true)]
        public Input<string> Direction { get; set; } = null!;

        /// <summary>
        /// The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
        /// </summary>
        [Input("endPort", required: true)]
        public Input<string> EndPort { get; set; } = null!;

        [Input("firewallId", required: true)]
        public Input<string> FirewallId { get; set; } = null!;

        /// <summary>
        /// A string that will be the displayed name/reference for this rule (optional)
        /// </summary>
        [Input("label")]
        public Input<string>? Label { get; set; }

        /// <summary>
        /// The protocol choice from tcp, udp or icmp (the default if unspecified is tcp)
        /// </summary>
        [Input("protocol", required: true)]
        public Input<string> Protocol { get; set; } = null!;

        /// <summary>
        /// The start of the port range to configure for this rule (or the single port if required)
        /// </summary>
        [Input("startPort", required: true)]
        public Input<string> StartPort { get; set; } = null!;

        public FirewallRuleArgs()
        {
        }
    }

    public sealed class FirewallRuleState : Pulumi.ResourceArgs
    {
        [Input("cidrs")]
        private InputList<string>? _cidrs;

        /// <summary>
        /// The IP address of the other end (i.e. not your instance) to affect, or a valid network CIDR (defaults to being globally
        /// applied, i.e. 0.0.0.0/0)
        /// </summary>
        public InputList<string> Cidrs
        {
            get => _cidrs ?? (_cidrs = new InputList<string>());
            set => _cidrs = value;
        }

        /// <summary>
        /// Will this rule affect ingress traffic
        /// </summary>
        [Input("direction")]
        public Input<string>? Direction { get; set; }

        /// <summary>
        /// The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
        /// </summary>
        [Input("endPort")]
        public Input<string>? EndPort { get; set; }

        [Input("firewallId")]
        public Input<string>? FirewallId { get; set; }

        /// <summary>
        /// A string that will be the displayed name/reference for this rule (optional)
        /// </summary>
        [Input("label")]
        public Input<string>? Label { get; set; }

        /// <summary>
        /// The protocol choice from tcp, udp or icmp (the default if unspecified is tcp)
        /// </summary>
        [Input("protocol")]
        public Input<string>? Protocol { get; set; }

        /// <summary>
        /// The start of the port range to configure for this rule (or the single port if required)
        /// </summary>
        [Input("startPort")]
        public Input<string>? StartPort { get; set; }

        public FirewallRuleState()
        {
        }
    }
}

// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Civo
{
    /// <summary>
    /// Provides a Civo firewall rule resource. This can be used to create, modify, and delete firewalls rules. This resource don't have an update option because Civo backend doesn't support it at this moment. In that case, we use `ForceNew` for all object in the resource.
    /// 
    /// ## Schema
    /// 
    /// ### Required
    /// 
    /// - **cidr** (Set of String) The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32 to open just for a specific IP address)
    /// - **firewall_id** (String) The Firewall ID
    /// 
    /// ### Optional
    /// 
    /// - **direction** (String) Will this rule affect ingress traffic (only `ingress` is supported now)
    /// - **end_port** (String) The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
    /// - **id** (String) The ID of this resource.
    /// - **label** (String) A string that will be the displayed name/reference for this rule
    /// - **protocol** (String) The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
    /// - **region** (String) The region for this rule
    /// - **start_port** (String) The start of the port range to configure for this rule (or the single port if required)
    /// 
    /// ## Import
    /// 
    /// Import is supported using the following syntax# using firewall_id:firewall_rule_id
    /// 
    /// ```sh
    ///  $ pulumi import civo:index/firewallRule:FirewallRule http b8ecd2ab-2267-4a5e-8692-cbf1d32583e3:4b0022ee-00b2-4f81-a40d-b4f8728923a7
    /// ```
    /// </summary>
    [CivoResourceType("civo:index/firewallRule:FirewallRule")]
    public partial class FirewallRule : Pulumi.CustomResource
    {
        /// <summary>
        /// The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32
        /// to open just for a specific IP address)
        /// </summary>
        [Output("cidrs")]
        public Output<ImmutableArray<string>> Cidrs { get; private set; } = null!;

        /// <summary>
        /// Will this rule affect ingress traffic (only `ingress` is supported now)
        /// </summary>
        [Output("direction")]
        public Output<string> Direction { get; private set; } = null!;

        /// <summary>
        /// The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
        /// </summary>
        [Output("endPort")]
        public Output<string> EndPort { get; private set; } = null!;

        /// <summary>
        /// The Firewall ID
        /// </summary>
        [Output("firewallId")]
        public Output<string> FirewallId { get; private set; } = null!;

        /// <summary>
        /// A string that will be the displayed name/reference for this rule
        /// </summary>
        [Output("label")]
        public Output<string> Label { get; private set; } = null!;

        /// <summary>
        /// The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
        /// </summary>
        [Output("protocol")]
        public Output<string> Protocol { get; private set; } = null!;

        /// <summary>
        /// The region for this rule
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

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
        /// The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32
        /// to open just for a specific IP address)
        /// </summary>
        public InputList<string> Cidrs
        {
            get => _cidrs ?? (_cidrs = new InputList<string>());
            set => _cidrs = value;
        }

        /// <summary>
        /// Will this rule affect ingress traffic (only `ingress` is supported now)
        /// </summary>
        [Input("direction")]
        public Input<string>? Direction { get; set; }

        /// <summary>
        /// The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
        /// </summary>
        [Input("endPort")]
        public Input<string>? EndPort { get; set; }

        /// <summary>
        /// The Firewall ID
        /// </summary>
        [Input("firewallId", required: true)]
        public Input<string> FirewallId { get; set; } = null!;

        /// <summary>
        /// A string that will be the displayed name/reference for this rule
        /// </summary>
        [Input("label")]
        public Input<string>? Label { get; set; }

        /// <summary>
        /// The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
        /// </summary>
        [Input("protocol")]
        public Input<string>? Protocol { get; set; }

        /// <summary>
        /// The region for this rule
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The start of the port range to configure for this rule (or the single port if required)
        /// </summary>
        [Input("startPort")]
        public Input<string>? StartPort { get; set; }

        public FirewallRuleArgs()
        {
        }
    }

    public sealed class FirewallRuleState : Pulumi.ResourceArgs
    {
        [Input("cidrs")]
        private InputList<string>? _cidrs;

        /// <summary>
        /// The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32
        /// to open just for a specific IP address)
        /// </summary>
        public InputList<string> Cidrs
        {
            get => _cidrs ?? (_cidrs = new InputList<string>());
            set => _cidrs = value;
        }

        /// <summary>
        /// Will this rule affect ingress traffic (only `ingress` is supported now)
        /// </summary>
        [Input("direction")]
        public Input<string>? Direction { get; set; }

        /// <summary>
        /// The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
        /// </summary>
        [Input("endPort")]
        public Input<string>? EndPort { get; set; }

        /// <summary>
        /// The Firewall ID
        /// </summary>
        [Input("firewallId")]
        public Input<string>? FirewallId { get; set; }

        /// <summary>
        /// A string that will be the displayed name/reference for this rule
        /// </summary>
        [Input("label")]
        public Input<string>? Label { get; set; }

        /// <summary>
        /// The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
        /// </summary>
        [Input("protocol")]
        public Input<string>? Protocol { get; set; }

        /// <summary>
        /// The region for this rule
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

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

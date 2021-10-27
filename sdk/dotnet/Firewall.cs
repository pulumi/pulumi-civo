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
    /// Provides a Civo firewall resource. This can be used to create, modify, and delete firewalls.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Civo = Pulumi.Civo;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         // Create a network
    ///         var customNet = new Civo.Network("customNet", new Civo.NetworkArgs
    ///         {
    ///             Label = "my-custom-network",
    ///         });
    ///         // Create a firewall
    ///         var www = new Civo.Firewall("www", new Civo.FirewallArgs
    ///         {
    ///             NetworkId = customNet.Id,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// &lt;!-- schema generated by tfplugindocs --&gt;
    /// ## Schema
    /// 
    /// ### Required
    /// 
    /// - **name** (String) The firewall name
    /// 
    /// ### Optional
    /// 
    /// - **network_id** (String) The firewall network, if is not defined we use the default network
    /// - **region** (String) The firewall region, if is not defined we use the global defined in the provider
    /// 
    /// ### Read-Only
    /// 
    /// - **id** (String) The ID of this resource.
    /// 
    /// ## Import
    /// 
    /// Import is supported using the following syntax# using ID
    /// 
    /// ```sh
    ///  $ pulumi import civo:index/firewall:Firewall www b8ecd2ab-2267-4a5e-8692-cbf1d32583e3
    /// ```
    /// </summary>
    [CivoResourceType("civo:index/firewall:Firewall")]
    public partial class Firewall : Pulumi.CustomResource
    {
        /// <summary>
        /// The ID of this resource.
        /// </summary>
        [Output("id")]
        public Output<string> Id { get; private set; } = null!;

        /// <summary>
        /// The firewall name
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The firewall network, if is not defined we use the default network
        /// </summary>
        [Output("networkId")]
        public Output<string> NetworkId { get; private set; } = null!;

        /// <summary>
        /// The firewall region, if is not defined we use the global defined in the provider
        /// </summary>
        [Output("region")]
        public Output<string?> Region { get; private set; } = null!;


        /// <summary>
        /// Create a Firewall resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Firewall(string name, FirewallArgs? args = null, CustomResourceOptions? options = null)
            : base("civo:index/firewall:Firewall", name, args ?? new FirewallArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Firewall(string name, Input<string> id, FirewallState? state = null, CustomResourceOptions? options = null)
            : base("civo:index/firewall:Firewall", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Firewall resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Firewall Get(string name, Input<string> id, FirewallState? state = null, CustomResourceOptions? options = null)
        {
            return new Firewall(name, id, state, options);
        }
    }

    public sealed class FirewallArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The firewall name
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The firewall network, if is not defined we use the default network
        /// </summary>
        [Input("networkId")]
        public Input<string>? NetworkId { get; set; }

        /// <summary>
        /// The firewall region, if is not defined we use the global defined in the provider
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        public FirewallArgs()
        {
        }
    }

    public sealed class FirewallState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of this resource.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// The firewall name
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The firewall network, if is not defined we use the default network
        /// </summary>
        [Input("networkId")]
        public Input<string>? NetworkId { get; set; }

        /// <summary>
        /// The firewall region, if is not defined we use the global defined in the provider
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        public FirewallState()
        {
        }
    }
}

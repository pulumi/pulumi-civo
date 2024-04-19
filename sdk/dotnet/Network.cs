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
    /// Provides a Civo network resource. This can be used to create, modify, and delete networks.
    /// 
    /// ## Example Usage
    /// 
    /// &lt;!--Start PulumiCodeChooser --&gt;
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Civo = Pulumi.Civo;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var customNet = new Civo.Network("custom_net", new()
    ///     {
    ///         Label = "test_network",
    ///     });
    /// 
    /// });
    /// ```
    /// &lt;!--End PulumiCodeChooser --&gt;
    /// 
    /// ## Import
    /// 
    /// using ID
    /// 
    /// ```sh
    /// $ pulumi import civo:index/network:Network custom_net b8ecd2ab-2267-4a5e-8692-cbf1d32583e3
    /// ```
    /// </summary>
    [CivoResourceType("civo:index/network:Network")]
    public partial class Network : global::Pulumi.CustomResource
    {
        /// <summary>
        /// If the network is default, this will be `true`
        /// </summary>
        [Output("default")]
        public Output<bool> Default { get; private set; } = null!;

        /// <summary>
        /// Name for the network
        /// </summary>
        [Output("label")]
        public Output<string> Label { get; private set; } = null!;

        /// <summary>
        /// The name of the network
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The region of the network
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;


        /// <summary>
        /// Create a Network resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Network(string name, NetworkArgs args, CustomResourceOptions? options = null)
            : base("civo:index/network:Network", name, args ?? new NetworkArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Network(string name, Input<string> id, NetworkState? state = null, CustomResourceOptions? options = null)
            : base("civo:index/network:Network", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Network resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Network Get(string name, Input<string> id, NetworkState? state = null, CustomResourceOptions? options = null)
        {
            return new Network(name, id, state, options);
        }
    }

    public sealed class NetworkArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Name for the network
        /// </summary>
        [Input("label", required: true)]
        public Input<string> Label { get; set; } = null!;

        /// <summary>
        /// The region of the network
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        public NetworkArgs()
        {
        }
        public static new NetworkArgs Empty => new NetworkArgs();
    }

    public sealed class NetworkState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// If the network is default, this will be `true`
        /// </summary>
        [Input("default")]
        public Input<bool>? Default { get; set; }

        /// <summary>
        /// Name for the network
        /// </summary>
        [Input("label")]
        public Input<string>? Label { get; set; }

        /// <summary>
        /// The name of the network
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The region of the network
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        public NetworkState()
        {
        }
        public static new NetworkState Empty => new NetworkState();
    }
}

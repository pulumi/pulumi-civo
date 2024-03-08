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
    /// Provides a Civo volume which can be attached to an instance in order to provide expanded storage.
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
    ///     var defaultNetwork = Civo.GetNetwork.Invoke(new()
    ///     {
    ///         Label = "Default",
    ///     });
    /// 
    ///     // Create volume
    ///     var db = new Civo.Volume("db", new()
    ///     {
    ///         SizeGb = 5,
    ///         NetworkId = defaultNetwork.Apply(getNetworkResult =&gt; getNetworkResult.Id),
    ///     }, new CustomResourceOptions
    ///     {
    ///         DependsOn = new[]
    ///         {
    ///             defaultNetwork,
    ///         },
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
    /// $ pulumi import civo:index/volume:Volume db 506f78a4-e098-11e5-ad9f-000f53306ae1
    /// ```
    /// </summary>
    [CivoResourceType("civo:index/volume:Volume")]
    public partial class Volume : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The mount point of the volume (from instance's perspective)
        /// </summary>
        [Output("mountPoint")]
        public Output<string> MountPoint { get; private set; } = null!;

        /// <summary>
        /// A name that you wish to use to refer to this volume
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The network that the volume belongs to
        /// </summary>
        [Output("networkId")]
        public Output<string> NetworkId { get; private set; } = null!;

        /// <summary>
        /// The region for the volume, if not declare we use the region in declared in the provider.
        /// </summary>
        [Output("region")]
        public Output<string?> Region { get; private set; } = null!;

        /// <summary>
        /// A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes
        /// </summary>
        [Output("sizeGb")]
        public Output<int> SizeGb { get; private set; } = null!;


        /// <summary>
        /// Create a Volume resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Volume(string name, VolumeArgs args, CustomResourceOptions? options = null)
            : base("civo:index/volume:Volume", name, args ?? new VolumeArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Volume(string name, Input<string> id, VolumeState? state = null, CustomResourceOptions? options = null)
            : base("civo:index/volume:Volume", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Volume resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Volume Get(string name, Input<string> id, VolumeState? state = null, CustomResourceOptions? options = null)
        {
            return new Volume(name, id, state, options);
        }
    }

    public sealed class VolumeArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// A name that you wish to use to refer to this volume
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The network that the volume belongs to
        /// </summary>
        [Input("networkId", required: true)]
        public Input<string> NetworkId { get; set; } = null!;

        /// <summary>
        /// The region for the volume, if not declare we use the region in declared in the provider.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes
        /// </summary>
        [Input("sizeGb", required: true)]
        public Input<int> SizeGb { get; set; } = null!;

        public VolumeArgs()
        {
        }
        public static new VolumeArgs Empty => new VolumeArgs();
    }

    public sealed class VolumeState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The mount point of the volume (from instance's perspective)
        /// </summary>
        [Input("mountPoint")]
        public Input<string>? MountPoint { get; set; }

        /// <summary>
        /// A name that you wish to use to refer to this volume
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The network that the volume belongs to
        /// </summary>
        [Input("networkId")]
        public Input<string>? NetworkId { get; set; }

        /// <summary>
        /// The region for the volume, if not declare we use the region in declared in the provider.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes
        /// </summary>
        [Input("sizeGb")]
        public Input<int>? SizeGb { get; set; }

        public VolumeState()
        {
        }
        public static new VolumeState Empty => new VolumeState();
    }
}

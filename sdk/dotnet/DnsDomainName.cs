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
    /// Provides a Civo DNS domain name resource.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Civo = Pulumi.Civo;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     // Create a new domain name
    ///     var main = new Civo.DnsDomainName("main");
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// using domain name
    /// 
    /// ```sh
    ///  $ pulumi import civo:index/dnsDomainName:DnsDomainName main mydomain.com
    /// ```
    /// </summary>
    [CivoResourceType("civo:index/dnsDomainName:DnsDomainName")]
    public partial class DnsDomainName : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The account ID of the domain
        /// </summary>
        [Output("accountId")]
        public Output<string> AccountId { get; private set; } = null!;

        /// <summary>
        /// The name of the domain
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;


        /// <summary>
        /// Create a DnsDomainName resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DnsDomainName(string name, DnsDomainNameArgs? args = null, CustomResourceOptions? options = null)
            : base("civo:index/dnsDomainName:DnsDomainName", name, args ?? new DnsDomainNameArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DnsDomainName(string name, Input<string> id, DnsDomainNameState? state = null, CustomResourceOptions? options = null)
            : base("civo:index/dnsDomainName:DnsDomainName", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing DnsDomainName resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DnsDomainName Get(string name, Input<string> id, DnsDomainNameState? state = null, CustomResourceOptions? options = null)
        {
            return new DnsDomainName(name, id, state, options);
        }
    }

    public sealed class DnsDomainNameArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the domain
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public DnsDomainNameArgs()
        {
        }
        public static new DnsDomainNameArgs Empty => new DnsDomainNameArgs();
    }

    public sealed class DnsDomainNameState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The account ID of the domain
        /// </summary>
        [Input("accountId")]
        public Input<string>? AccountId { get; set; }

        /// <summary>
        /// The name of the domain
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public DnsDomainNameState()
        {
        }
        public static new DnsDomainNameState Empty => new DnsDomainNameState();
    }
}

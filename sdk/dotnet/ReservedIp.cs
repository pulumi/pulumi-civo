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
    /// Provides a Civo reserved IP to represent a publicly-accessible static IP addresses that can be mapped to one of your Instancesor Load Balancer.
    /// 
    /// ## Import
    /// 
    /// terrafom import civo_reserved_ip.www 9f0e86fc-b2c6-46b4-82ed-2f28419f8ae3
    /// </summary>
    [CivoResourceType("civo:index/reservedIp:ReservedIp")]
    public partial class ReservedIp : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The IP Address of the resource
        /// </summary>
        [Output("ip")]
        public Output<string> Ip { get; private set; } = null!;

        /// <summary>
        /// Name for the ip address
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The region of the ip
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;


        /// <summary>
        /// Create a ReservedIp resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ReservedIp(string name, ReservedIpArgs? args = null, CustomResourceOptions? options = null)
            : base("civo:index/reservedIp:ReservedIp", name, args ?? new ReservedIpArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ReservedIp(string name, Input<string> id, ReservedIpState? state = null, CustomResourceOptions? options = null)
            : base("civo:index/reservedIp:ReservedIp", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ReservedIp resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ReservedIp Get(string name, Input<string> id, ReservedIpState? state = null, CustomResourceOptions? options = null)
        {
            return new ReservedIp(name, id, state, options);
        }
    }

    public sealed class ReservedIpArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Name for the ip address
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The region of the ip
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        public ReservedIpArgs()
        {
        }
        public static new ReservedIpArgs Empty => new ReservedIpArgs();
    }

    public sealed class ReservedIpState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The IP Address of the resource
        /// </summary>
        [Input("ip")]
        public Input<string>? Ip { get; set; }

        /// <summary>
        /// Name for the ip address
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The region of the ip
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        public ReservedIpState()
        {
        }
        public static new ReservedIpState Empty => new ReservedIpState();
    }
}

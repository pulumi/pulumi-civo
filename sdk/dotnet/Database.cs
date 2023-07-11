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
    /// ## Import
    /// 
    /// using ID
    /// 
    /// ```sh
    ///  $ pulumi import civo:index/database:Database mydb 29fcd1c4-fb61-44c7-b49c-dc7b98e9927e
    /// ```
    /// </summary>
    [CivoResourceType("civo:index/database:Database")]
    public partial class Database : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The DNS endpoint of the database
        /// </summary>
        [Output("dnsEndpoint")]
        public Output<string> DnsEndpoint { get; private set; } = null!;

        /// <summary>
        /// The endpoint of the database
        /// </summary>
        [Output("endpoint")]
        public Output<string> Endpoint { get; private set; } = null!;

        /// <summary>
        /// The engine of the database
        /// </summary>
        [Output("engine")]
        public Output<string> Engine { get; private set; } = null!;

        /// <summary>
        /// The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all)
        /// </summary>
        [Output("firewallId")]
        public Output<string> FirewallId { get; private set; } = null!;

        /// <summary>
        /// Name of the database
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The id of the associated network
        /// </summary>
        [Output("networkId")]
        public Output<string> NetworkId { get; private set; } = null!;

        /// <summary>
        /// Count of nodes
        /// </summary>
        [Output("nodes")]
        public Output<int> Nodes { get; private set; } = null!;

        /// <summary>
        /// The password of the database
        /// </summary>
        [Output("password")]
        public Output<string> Password { get; private set; } = null!;

        /// <summary>
        /// The port of the database
        /// </summary>
        [Output("port")]
        public Output<int> Port { get; private set; } = null!;

        /// <summary>
        /// The region where the database will be created.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// Size of the database
        /// </summary>
        [Output("size")]
        public Output<string> Size { get; private set; } = null!;

        /// <summary>
        /// The status of the database
        /// </summary>
        [Output("status")]
        public Output<string> Status { get; private set; } = null!;

        /// <summary>
        /// The username of the database
        /// </summary>
        [Output("username")]
        public Output<string> Username { get; private set; } = null!;

        /// <summary>
        /// The version of the database
        /// </summary>
        [Output("version")]
        public Output<string> Version { get; private set; } = null!;


        /// <summary>
        /// Create a Database resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Database(string name, DatabaseArgs args, CustomResourceOptions? options = null)
            : base("civo:index/database:Database", name, args ?? new DatabaseArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Database(string name, Input<string> id, DatabaseState? state = null, CustomResourceOptions? options = null)
            : base("civo:index/database:Database", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Database resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Database Get(string name, Input<string> id, DatabaseState? state = null, CustomResourceOptions? options = null)
        {
            return new Database(name, id, state, options);
        }
    }

    public sealed class DatabaseArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The engine of the database
        /// </summary>
        [Input("engine", required: true)]
        public Input<string> Engine { get; set; } = null!;

        /// <summary>
        /// The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all)
        /// </summary>
        [Input("firewallId")]
        public Input<string>? FirewallId { get; set; }

        /// <summary>
        /// Name of the database
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The id of the associated network
        /// </summary>
        [Input("networkId")]
        public Input<string>? NetworkId { get; set; }

        /// <summary>
        /// Count of nodes
        /// </summary>
        [Input("nodes", required: true)]
        public Input<int> Nodes { get; set; } = null!;

        /// <summary>
        /// The region where the database will be created.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// Size of the database
        /// </summary>
        [Input("size", required: true)]
        public Input<string> Size { get; set; } = null!;

        /// <summary>
        /// The version of the database
        /// </summary>
        [Input("version", required: true)]
        public Input<string> Version { get; set; } = null!;

        public DatabaseArgs()
        {
        }
        public static new DatabaseArgs Empty => new DatabaseArgs();
    }

    public sealed class DatabaseState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The DNS endpoint of the database
        /// </summary>
        [Input("dnsEndpoint")]
        public Input<string>? DnsEndpoint { get; set; }

        /// <summary>
        /// The endpoint of the database
        /// </summary>
        [Input("endpoint")]
        public Input<string>? Endpoint { get; set; }

        /// <summary>
        /// The engine of the database
        /// </summary>
        [Input("engine")]
        public Input<string>? Engine { get; set; }

        /// <summary>
        /// The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all)
        /// </summary>
        [Input("firewallId")]
        public Input<string>? FirewallId { get; set; }

        /// <summary>
        /// Name of the database
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The id of the associated network
        /// </summary>
        [Input("networkId")]
        public Input<string>? NetworkId { get; set; }

        /// <summary>
        /// Count of nodes
        /// </summary>
        [Input("nodes")]
        public Input<int>? Nodes { get; set; }

        /// <summary>
        /// The password of the database
        /// </summary>
        [Input("password")]
        public Input<string>? Password { get; set; }

        /// <summary>
        /// The port of the database
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        /// <summary>
        /// The region where the database will be created.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// Size of the database
        /// </summary>
        [Input("size")]
        public Input<string>? Size { get; set; }

        /// <summary>
        /// The status of the database
        /// </summary>
        [Input("status")]
        public Input<string>? Status { get; set; }

        /// <summary>
        /// The username of the database
        /// </summary>
        [Input("username")]
        public Input<string>? Username { get; set; }

        /// <summary>
        /// The version of the database
        /// </summary>
        [Input("version")]
        public Input<string>? Version { get; set; }

        public DatabaseState()
        {
        }
        public static new DatabaseState Empty => new DatabaseState();
    }
}

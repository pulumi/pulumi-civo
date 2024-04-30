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
    /// Provides a Civo instance resource. This can be used to create, modify, and delete instances.
    /// 
    /// ## Import
    /// 
    /// using ID
    /// 
    /// ```sh
    /// $ pulumi import civo:index/instance:Instance myintance 18bd98ad-1b6e-4f87-b48f-e690b4fd7413
    /// ```
    /// </summary>
    [CivoResourceType("civo:index/instance:Instance")]
    public partial class Instance : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Instance's CPU cores
        /// </summary>
        [Output("cpuCores")]
        public Output<int> CpuCores { get; private set; } = null!;

        /// <summary>
        /// Timestamp when the instance was created
        /// </summary>
        [Output("createdAt")]
        public Output<string> CreatedAt { get; private set; } = null!;

        /// <summary>
        /// Instance's disk (GB)
        /// </summary>
        [Output("diskGb")]
        public Output<int> DiskGb { get; private set; } = null!;

        /// <summary>
        /// The ID for the disk image to use to build the instance
        /// </summary>
        [Output("diskImage")]
        public Output<string> DiskImage { get; private set; } = null!;

        /// <summary>
        /// The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all)
        /// </summary>
        [Output("firewallId")]
        public Output<string> FirewallId { get; private set; } = null!;

        /// <summary>
        /// A fully qualified domain name that should be set as the instance's hostname
        /// </summary>
        [Output("hostname")]
        public Output<string> Hostname { get; private set; } = null!;

        /// <summary>
        /// Initial password for login
        /// </summary>
        [Output("initialPassword")]
        public Output<string> InitialPassword { get; private set; } = null!;

        /// <summary>
        /// The name of the initial user created on the server (optional; this will default to the template's default_username and fallback to civo)
        /// </summary>
        [Output("initialUser")]
        public Output<string?> InitialUser { get; private set; } = null!;

        /// <summary>
        /// This must be the ID of the network from the network listing (optional; default network used when not specified)
        /// </summary>
        [Output("networkId")]
        public Output<string> NetworkId { get; private set; } = null!;

        /// <summary>
        /// Add some notes to the instance
        /// </summary>
        [Output("notes")]
        public Output<string?> Notes { get; private set; } = null!;

        /// <summary>
        /// Instance's private IP address
        /// </summary>
        [Output("privateIp")]
        public Output<string> PrivateIp { get; private set; } = null!;

        /// <summary>
        /// Instance's public IP address
        /// </summary>
        [Output("publicIp")]
        public Output<string> PublicIp { get; private set; } = null!;

        /// <summary>
        /// This should be either 'none' or 'create' (default: 'create')
        /// </summary>
        [Output("publicIpRequired")]
        public Output<string?> PublicIpRequired { get; private set; } = null!;

        /// <summary>
        /// Instance's RAM (MB)
        /// </summary>
        [Output("ramMb")]
        public Output<int> RamMb { get; private set; } = null!;

        /// <summary>
        /// The region for the instance, if not declare we use the region in declared in the provider
        /// </summary>
        [Output("region")]
        public Output<string?> Region { get; private set; } = null!;

        /// <summary>
        /// Can be either the UUID, name, or the IP address of the reserved IP
        /// </summary>
        [Output("reservedIpv4")]
        public Output<string?> ReservedIpv4 { get; private set; } = null!;

        /// <summary>
        /// A fully qualified domain name that should be used as the instance's IP's reverse DNS (optional, uses the hostname if unspecified)
        /// </summary>
        [Output("reverseDns")]
        public Output<string?> ReverseDns { get; private set; } = null!;

        /// <summary>
        /// The contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance, read/write/executable only by root and then will be executed at the end of the cloud initialization
        /// </summary>
        [Output("script")]
        public Output<string?> Script { get; private set; } = null!;

        /// <summary>
        /// The name of the size, from the current list, e.g. g3.xsmall
        /// </summary>
        [Output("size")]
        public Output<string?> Size { get; private set; } = null!;

        /// <summary>
        /// Instance's source ID
        /// </summary>
        [Output("sourceId")]
        public Output<string> SourceId { get; private set; } = null!;

        /// <summary>
        /// Instance's source type
        /// </summary>
        [Output("sourceType")]
        public Output<string> SourceType { get; private set; } = null!;

        /// <summary>
        /// The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn't provided a random password will be set and returned in the initial_password field)
        /// </summary>
        [Output("sshkeyId")]
        public Output<string> SshkeyId { get; private set; } = null!;

        /// <summary>
        /// Instance's status
        /// </summary>
        [Output("status")]
        public Output<string> Status { get; private set; } = null!;

        /// <summary>
        /// An optional list of tags, represented as a key, value pair
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<string>> Tags { get; private set; } = null!;

        /// <summary>
        /// The ID for the template to use to build the instance
        /// </summary>
        [Output("template")]
        public Output<string> Template { get; private set; } = null!;


        /// <summary>
        /// Create a Instance resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Instance(string name, InstanceArgs? args = null, CustomResourceOptions? options = null)
            : base("civo:index/instance:Instance", name, args ?? new InstanceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Instance(string name, Input<string> id, InstanceState? state = null, CustomResourceOptions? options = null)
            : base("civo:index/instance:Instance", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                AdditionalSecretOutputs =
                {
                    "initialPassword",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Instance resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Instance Get(string name, Input<string> id, InstanceState? state = null, CustomResourceOptions? options = null)
        {
            return new Instance(name, id, state, options);
        }
    }

    public sealed class InstanceArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID for the disk image to use to build the instance
        /// </summary>
        [Input("diskImage")]
        public Input<string>? DiskImage { get; set; }

        /// <summary>
        /// The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all)
        /// </summary>
        [Input("firewallId")]
        public Input<string>? FirewallId { get; set; }

        /// <summary>
        /// A fully qualified domain name that should be set as the instance's hostname
        /// </summary>
        [Input("hostname")]
        public Input<string>? Hostname { get; set; }

        /// <summary>
        /// The name of the initial user created on the server (optional; this will default to the template's default_username and fallback to civo)
        /// </summary>
        [Input("initialUser")]
        public Input<string>? InitialUser { get; set; }

        /// <summary>
        /// This must be the ID of the network from the network listing (optional; default network used when not specified)
        /// </summary>
        [Input("networkId")]
        public Input<string>? NetworkId { get; set; }

        /// <summary>
        /// Add some notes to the instance
        /// </summary>
        [Input("notes")]
        public Input<string>? Notes { get; set; }

        /// <summary>
        /// This should be either 'none' or 'create' (default: 'create')
        /// </summary>
        [Input("publicIpRequired")]
        public Input<string>? PublicIpRequired { get; set; }

        /// <summary>
        /// The region for the instance, if not declare we use the region in declared in the provider
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// Can be either the UUID, name, or the IP address of the reserved IP
        /// </summary>
        [Input("reservedIpv4")]
        public Input<string>? ReservedIpv4 { get; set; }

        /// <summary>
        /// A fully qualified domain name that should be used as the instance's IP's reverse DNS (optional, uses the hostname if unspecified)
        /// </summary>
        [Input("reverseDns")]
        public Input<string>? ReverseDns { get; set; }

        /// <summary>
        /// The contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance, read/write/executable only by root and then will be executed at the end of the cloud initialization
        /// </summary>
        [Input("script")]
        public Input<string>? Script { get; set; }

        /// <summary>
        /// The name of the size, from the current list, e.g. g3.xsmall
        /// </summary>
        [Input("size")]
        public Input<string>? Size { get; set; }

        /// <summary>
        /// The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn't provided a random password will be set and returned in the initial_password field)
        /// </summary>
        [Input("sshkeyId")]
        public Input<string>? SshkeyId { get; set; }

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// An optional list of tags, represented as a key, value pair
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The ID for the template to use to build the instance
        /// </summary>
        [Input("template")]
        public Input<string>? Template { get; set; }

        public InstanceArgs()
        {
        }
        public static new InstanceArgs Empty => new InstanceArgs();
    }

    public sealed class InstanceState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Instance's CPU cores
        /// </summary>
        [Input("cpuCores")]
        public Input<int>? CpuCores { get; set; }

        /// <summary>
        /// Timestamp when the instance was created
        /// </summary>
        [Input("createdAt")]
        public Input<string>? CreatedAt { get; set; }

        /// <summary>
        /// Instance's disk (GB)
        /// </summary>
        [Input("diskGb")]
        public Input<int>? DiskGb { get; set; }

        /// <summary>
        /// The ID for the disk image to use to build the instance
        /// </summary>
        [Input("diskImage")]
        public Input<string>? DiskImage { get; set; }

        /// <summary>
        /// The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all)
        /// </summary>
        [Input("firewallId")]
        public Input<string>? FirewallId { get; set; }

        /// <summary>
        /// A fully qualified domain name that should be set as the instance's hostname
        /// </summary>
        [Input("hostname")]
        public Input<string>? Hostname { get; set; }

        [Input("initialPassword")]
        private Input<string>? _initialPassword;

        /// <summary>
        /// Initial password for login
        /// </summary>
        public Input<string>? InitialPassword
        {
            get => _initialPassword;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _initialPassword = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// The name of the initial user created on the server (optional; this will default to the template's default_username and fallback to civo)
        /// </summary>
        [Input("initialUser")]
        public Input<string>? InitialUser { get; set; }

        /// <summary>
        /// This must be the ID of the network from the network listing (optional; default network used when not specified)
        /// </summary>
        [Input("networkId")]
        public Input<string>? NetworkId { get; set; }

        /// <summary>
        /// Add some notes to the instance
        /// </summary>
        [Input("notes")]
        public Input<string>? Notes { get; set; }

        /// <summary>
        /// Instance's private IP address
        /// </summary>
        [Input("privateIp")]
        public Input<string>? PrivateIp { get; set; }

        /// <summary>
        /// Instance's public IP address
        /// </summary>
        [Input("publicIp")]
        public Input<string>? PublicIp { get; set; }

        /// <summary>
        /// This should be either 'none' or 'create' (default: 'create')
        /// </summary>
        [Input("publicIpRequired")]
        public Input<string>? PublicIpRequired { get; set; }

        /// <summary>
        /// Instance's RAM (MB)
        /// </summary>
        [Input("ramMb")]
        public Input<int>? RamMb { get; set; }

        /// <summary>
        /// The region for the instance, if not declare we use the region in declared in the provider
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// Can be either the UUID, name, or the IP address of the reserved IP
        /// </summary>
        [Input("reservedIpv4")]
        public Input<string>? ReservedIpv4 { get; set; }

        /// <summary>
        /// A fully qualified domain name that should be used as the instance's IP's reverse DNS (optional, uses the hostname if unspecified)
        /// </summary>
        [Input("reverseDns")]
        public Input<string>? ReverseDns { get; set; }

        /// <summary>
        /// The contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance, read/write/executable only by root and then will be executed at the end of the cloud initialization
        /// </summary>
        [Input("script")]
        public Input<string>? Script { get; set; }

        /// <summary>
        /// The name of the size, from the current list, e.g. g3.xsmall
        /// </summary>
        [Input("size")]
        public Input<string>? Size { get; set; }

        /// <summary>
        /// Instance's source ID
        /// </summary>
        [Input("sourceId")]
        public Input<string>? SourceId { get; set; }

        /// <summary>
        /// Instance's source type
        /// </summary>
        [Input("sourceType")]
        public Input<string>? SourceType { get; set; }

        /// <summary>
        /// The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn't provided a random password will be set and returned in the initial_password field)
        /// </summary>
        [Input("sshkeyId")]
        public Input<string>? SshkeyId { get; set; }

        /// <summary>
        /// Instance's status
        /// </summary>
        [Input("status")]
        public Input<string>? Status { get; set; }

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// An optional list of tags, represented as a key, value pair
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The ID for the template to use to build the instance
        /// </summary>
        [Input("template")]
        public Input<string>? Template { get; set; }

        public InstanceState()
        {
        }
        public static new InstanceState Empty => new InstanceState();
    }
}

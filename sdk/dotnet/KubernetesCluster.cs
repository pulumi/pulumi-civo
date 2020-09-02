// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Civo
{
    public partial class KubernetesCluster : Pulumi.CustomResource
    {
        [Output("apiEndpoint")]
        public Output<string> ApiEndpoint { get; private set; } = null!;

        /// <summary>
        /// a comma separated list of applications to install.Spaces within application names are fine, but shouldn't be either side
        /// of the comma.If you want to remove a default installed application, prefix it with a '-', e.g. -traefik.
        /// </summary>
        [Output("applications")]
        public Output<string?> Applications { get; private set; } = null!;

        [Output("builtAt")]
        public Output<string> BuiltAt { get; private set; } = null!;

        [Output("createdAt")]
        public Output<string> CreatedAt { get; private set; } = null!;

        [Output("dnsEntry")]
        public Output<string> DnsEntry { get; private set; } = null!;

        [Output("installedApplications")]
        public Output<ImmutableArray<Outputs.KubernetesClusterInstalledApplication>> InstalledApplications { get; private set; } = null!;

        [Output("instances")]
        public Output<ImmutableArray<Outputs.KubernetesClusterInstance>> Instances { get; private set; } = null!;

        [Output("kubeconfig")]
        public Output<string> Kubeconfig { get; private set; } = null!;

        /// <summary>
        /// the version of k3s to install (optional, the default is currently the latest available)
        /// </summary>
        [Output("kubernetesVersion")]
        public Output<string?> KubernetesVersion { get; private set; } = null!;

        [Output("masterIp")]
        public Output<string> MasterIp { get; private set; } = null!;

        /// <summary>
        /// a name for your cluster, must be unique within your account (required)
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// the number of instances to create (optional, the default at the time of writing is 3)
        /// </summary>
        [Output("numTargetNodes")]
        public Output<int?> NumTargetNodes { get; private set; } = null!;

        [Output("ready")]
        public Output<bool> Ready { get; private set; } = null!;

        [Output("status")]
        public Output<string> Status { get; private set; } = null!;

        /// <summary>
        /// a space separated list of tags, to be used freely as required (optional)
        /// </summary>
        [Output("tags")]
        public Output<string?> Tags { get; private set; } = null!;

        /// <summary>
        /// the size of each node (optional, the default is currently g2.small)
        /// </summary>
        [Output("targetNodesSize")]
        public Output<string?> TargetNodesSize { get; private set; } = null!;


        /// <summary>
        /// Create a KubernetesCluster resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public KubernetesCluster(string name, KubernetesClusterArgs? args = null, CustomResourceOptions? options = null)
            : base("civo:index/kubernetesCluster:KubernetesCluster", name, args ?? new KubernetesClusterArgs(), MakeResourceOptions(options, ""))
        {
        }

        private KubernetesCluster(string name, Input<string> id, KubernetesClusterState? state = null, CustomResourceOptions? options = null)
            : base("civo:index/kubernetesCluster:KubernetesCluster", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing KubernetesCluster resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static KubernetesCluster Get(string name, Input<string> id, KubernetesClusterState? state = null, CustomResourceOptions? options = null)
        {
            return new KubernetesCluster(name, id, state, options);
        }
    }

    public sealed class KubernetesClusterArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// a comma separated list of applications to install.Spaces within application names are fine, but shouldn't be either side
        /// of the comma.If you want to remove a default installed application, prefix it with a '-', e.g. -traefik.
        /// </summary>
        [Input("applications")]
        public Input<string>? Applications { get; set; }

        /// <summary>
        /// the version of k3s to install (optional, the default is currently the latest available)
        /// </summary>
        [Input("kubernetesVersion")]
        public Input<string>? KubernetesVersion { get; set; }

        /// <summary>
        /// a name for your cluster, must be unique within your account (required)
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// the number of instances to create (optional, the default at the time of writing is 3)
        /// </summary>
        [Input("numTargetNodes")]
        public Input<int>? NumTargetNodes { get; set; }

        /// <summary>
        /// a space separated list of tags, to be used freely as required (optional)
        /// </summary>
        [Input("tags")]
        public Input<string>? Tags { get; set; }

        /// <summary>
        /// the size of each node (optional, the default is currently g2.small)
        /// </summary>
        [Input("targetNodesSize")]
        public Input<string>? TargetNodesSize { get; set; }

        public KubernetesClusterArgs()
        {
        }
    }

    public sealed class KubernetesClusterState : Pulumi.ResourceArgs
    {
        [Input("apiEndpoint")]
        public Input<string>? ApiEndpoint { get; set; }

        /// <summary>
        /// a comma separated list of applications to install.Spaces within application names are fine, but shouldn't be either side
        /// of the comma.If you want to remove a default installed application, prefix it with a '-', e.g. -traefik.
        /// </summary>
        [Input("applications")]
        public Input<string>? Applications { get; set; }

        [Input("builtAt")]
        public Input<string>? BuiltAt { get; set; }

        [Input("createdAt")]
        public Input<string>? CreatedAt { get; set; }

        [Input("dnsEntry")]
        public Input<string>? DnsEntry { get; set; }

        [Input("installedApplications")]
        private InputList<Inputs.KubernetesClusterInstalledApplicationGetArgs>? _installedApplications;
        public InputList<Inputs.KubernetesClusterInstalledApplicationGetArgs> InstalledApplications
        {
            get => _installedApplications ?? (_installedApplications = new InputList<Inputs.KubernetesClusterInstalledApplicationGetArgs>());
            set => _installedApplications = value;
        }

        [Input("instances")]
        private InputList<Inputs.KubernetesClusterInstanceGetArgs>? _instances;
        public InputList<Inputs.KubernetesClusterInstanceGetArgs> Instances
        {
            get => _instances ?? (_instances = new InputList<Inputs.KubernetesClusterInstanceGetArgs>());
            set => _instances = value;
        }

        [Input("kubeconfig")]
        public Input<string>? Kubeconfig { get; set; }

        /// <summary>
        /// the version of k3s to install (optional, the default is currently the latest available)
        /// </summary>
        [Input("kubernetesVersion")]
        public Input<string>? KubernetesVersion { get; set; }

        [Input("masterIp")]
        public Input<string>? MasterIp { get; set; }

        /// <summary>
        /// a name for your cluster, must be unique within your account (required)
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// the number of instances to create (optional, the default at the time of writing is 3)
        /// </summary>
        [Input("numTargetNodes")]
        public Input<int>? NumTargetNodes { get; set; }

        [Input("ready")]
        public Input<bool>? Ready { get; set; }

        [Input("status")]
        public Input<string>? Status { get; set; }

        /// <summary>
        /// a space separated list of tags, to be used freely as required (optional)
        /// </summary>
        [Input("tags")]
        public Input<string>? Tags { get; set; }

        /// <summary>
        /// the size of each node (optional, the default is currently g2.small)
        /// </summary>
        [Input("targetNodesSize")]
        public Input<string>? TargetNodesSize { get; set; }

        public KubernetesClusterState()
        {
        }
    }
}

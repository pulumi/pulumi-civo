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
    /// Then the Kubernetes cluster can be imported using the cluster's `id`, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import civo:index/kubernetesCluster:KubernetesCluster my-cluster 1b8b2100-0e9f-4e8f-ad78-9eb578c2a0af
    /// ```
    /// </summary>
    [CivoResourceType("civo:index/kubernetesCluster:KubernetesCluster")]
    public partial class KubernetesCluster : Pulumi.CustomResource
    {
        /// <summary>
        /// The base URL of the API server on the Kubernetes master node.
        /// </summary>
        [Output("apiEndpoint")]
        public Output<string> ApiEndpoint { get; private set; } = null!;

        /// <summary>
        /// A comma separated list of applications to install. Spaces within application names are fine, but shouldn't be either side of the comma. Application names are case-sensitive; the available applications can be listed with the civo CLI: 'civo kubernetes applications ls'. If you want to remove a default installed application, prefix it with a '-', e.g. -Traefik
        /// </summary>
        [Output("applications")]
        public Output<string?> Applications { get; private set; } = null!;

        /// <summary>
        /// The date where the Kubernetes cluster was build.
        /// </summary>
        [Output("builtAt")]
        public Output<string> BuiltAt { get; private set; } = null!;

        /// <summary>
        /// The date where the Kubernetes cluster was create.
        /// </summary>
        [Output("createdAt")]
        public Output<string> CreatedAt { get; private set; } = null!;

        /// <summary>
        /// The unique dns entry for the cluster in this case point to the master.
        /// </summary>
        [Output("dnsEntry")]
        public Output<string> DnsEntry { get; private set; } = null!;

        /// <summary>
        /// A unique ID that can be used to identify and reference a Kubernetes cluster.
        /// </summary>
        [Output("installedApplications")]
        public Output<ImmutableArray<Outputs.KubernetesClusterInstalledApplication>> InstalledApplications { get; private set; } = null!;

        /// <summary>
        /// A list of instance inside the pool
        /// </summary>
        [Output("instances")]
        public Output<ImmutableArray<Outputs.KubernetesClusterInstance>> Instances { get; private set; } = null!;

        /// <summary>
        /// A representation of the Kubernetes cluster's kubeconfig in yaml format.
        /// </summary>
        [Output("kubeconfig")]
        public Output<string> Kubeconfig { get; private set; } = null!;

        /// <summary>
        /// The version of k3s to install (The default is currently the latest available).
        /// </summary>
        [Output("kubernetesVersion")]
        public Output<string> KubernetesVersion { get; private set; } = null!;

        /// <summary>
        /// The Ip of the Kubernetes master node.
        /// </summary>
        [Output("masterIp")]
        public Output<string> MasterIp { get; private set; } = null!;

        /// <summary>
        /// A name for the Kubernetes cluster, if is not declare the provider will generate one for you.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The network for the cluster, if not declare we use the default one
        /// </summary>
        [Output("networkId")]
        public Output<string> NetworkId { get; private set; } = null!;

        /// <summary>
        /// The number of instances to create (The default at the time of writing is 3).
        /// </summary>
        [Output("numTargetNodes")]
        public Output<int> NumTargetNodes { get; private set; } = null!;

        /// <summary>
        /// A list of node pools associated with the cluster. Each node pool exports the following attributes:
        /// </summary>
        [Output("pools")]
        public Output<ImmutableArray<Outputs.KubernetesClusterPool>> Pools { get; private set; } = null!;

        [Output("ready")]
        public Output<bool> Ready { get; private set; } = null!;

        /// <summary>
        /// The region for the cluster.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// The status of Kubernetes cluster.
        /// * `ready` -If the Kubernetes cluster is ready.
        /// </summary>
        [Output("status")]
        public Output<string> Status { get; private set; } = null!;

        /// <summary>
        /// A space separated list of tags, to be used freely as required.
        /// </summary>
        [Output("tags")]
        public Output<string?> Tags { get; private set; } = null!;

        /// <summary>
        /// The size of each node (The default is currently g3.k3s.small)
        /// </summary>
        [Output("targetNodesSize")]
        public Output<string> TargetNodesSize { get; private set; } = null!;


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
        /// A comma separated list of applications to install. Spaces within application names are fine, but shouldn't be either side of the comma. Application names are case-sensitive; the available applications can be listed with the civo CLI: 'civo kubernetes applications ls'. If you want to remove a default installed application, prefix it with a '-', e.g. -Traefik
        /// </summary>
        [Input("applications")]
        public Input<string>? Applications { get; set; }

        /// <summary>
        /// The version of k3s to install (The default is currently the latest available).
        /// </summary>
        [Input("kubernetesVersion")]
        public Input<string>? KubernetesVersion { get; set; }

        /// <summary>
        /// A name for the Kubernetes cluster, if is not declare the provider will generate one for you.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The network for the cluster, if not declare we use the default one
        /// </summary>
        [Input("networkId")]
        public Input<string>? NetworkId { get; set; }

        /// <summary>
        /// The number of instances to create (The default at the time of writing is 3).
        /// </summary>
        [Input("numTargetNodes")]
        public Input<int>? NumTargetNodes { get; set; }

        /// <summary>
        /// The region for the cluster.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// A space separated list of tags, to be used freely as required.
        /// </summary>
        [Input("tags")]
        public Input<string>? Tags { get; set; }

        /// <summary>
        /// The size of each node (The default is currently g3.k3s.small)
        /// </summary>
        [Input("targetNodesSize")]
        public Input<string>? TargetNodesSize { get; set; }

        public KubernetesClusterArgs()
        {
        }
    }

    public sealed class KubernetesClusterState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The base URL of the API server on the Kubernetes master node.
        /// </summary>
        [Input("apiEndpoint")]
        public Input<string>? ApiEndpoint { get; set; }

        /// <summary>
        /// A comma separated list of applications to install. Spaces within application names are fine, but shouldn't be either side of the comma. Application names are case-sensitive; the available applications can be listed with the civo CLI: 'civo kubernetes applications ls'. If you want to remove a default installed application, prefix it with a '-', e.g. -Traefik
        /// </summary>
        [Input("applications")]
        public Input<string>? Applications { get; set; }

        /// <summary>
        /// The date where the Kubernetes cluster was build.
        /// </summary>
        [Input("builtAt")]
        public Input<string>? BuiltAt { get; set; }

        /// <summary>
        /// The date where the Kubernetes cluster was create.
        /// </summary>
        [Input("createdAt")]
        public Input<string>? CreatedAt { get; set; }

        /// <summary>
        /// The unique dns entry for the cluster in this case point to the master.
        /// </summary>
        [Input("dnsEntry")]
        public Input<string>? DnsEntry { get; set; }

        [Input("installedApplications")]
        private InputList<Inputs.KubernetesClusterInstalledApplicationGetArgs>? _installedApplications;

        /// <summary>
        /// A unique ID that can be used to identify and reference a Kubernetes cluster.
        /// </summary>
        public InputList<Inputs.KubernetesClusterInstalledApplicationGetArgs> InstalledApplications
        {
            get => _installedApplications ?? (_installedApplications = new InputList<Inputs.KubernetesClusterInstalledApplicationGetArgs>());
            set => _installedApplications = value;
        }

        [Input("instances")]
        private InputList<Inputs.KubernetesClusterInstanceGetArgs>? _instances;

        /// <summary>
        /// A list of instance inside the pool
        /// </summary>
        public InputList<Inputs.KubernetesClusterInstanceGetArgs> Instances
        {
            get => _instances ?? (_instances = new InputList<Inputs.KubernetesClusterInstanceGetArgs>());
            set => _instances = value;
        }

        /// <summary>
        /// A representation of the Kubernetes cluster's kubeconfig in yaml format.
        /// </summary>
        [Input("kubeconfig")]
        public Input<string>? Kubeconfig { get; set; }

        /// <summary>
        /// The version of k3s to install (The default is currently the latest available).
        /// </summary>
        [Input("kubernetesVersion")]
        public Input<string>? KubernetesVersion { get; set; }

        /// <summary>
        /// The Ip of the Kubernetes master node.
        /// </summary>
        [Input("masterIp")]
        public Input<string>? MasterIp { get; set; }

        /// <summary>
        /// A name for the Kubernetes cluster, if is not declare the provider will generate one for you.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The network for the cluster, if not declare we use the default one
        /// </summary>
        [Input("networkId")]
        public Input<string>? NetworkId { get; set; }

        /// <summary>
        /// The number of instances to create (The default at the time of writing is 3).
        /// </summary>
        [Input("numTargetNodes")]
        public Input<int>? NumTargetNodes { get; set; }

        [Input("pools")]
        private InputList<Inputs.KubernetesClusterPoolGetArgs>? _pools;

        /// <summary>
        /// A list of node pools associated with the cluster. Each node pool exports the following attributes:
        /// </summary>
        public InputList<Inputs.KubernetesClusterPoolGetArgs> Pools
        {
            get => _pools ?? (_pools = new InputList<Inputs.KubernetesClusterPoolGetArgs>());
            set => _pools = value;
        }

        [Input("ready")]
        public Input<bool>? Ready { get; set; }

        /// <summary>
        /// The region for the cluster.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The status of Kubernetes cluster.
        /// * `ready` -If the Kubernetes cluster is ready.
        /// </summary>
        [Input("status")]
        public Input<string>? Status { get; set; }

        /// <summary>
        /// A space separated list of tags, to be used freely as required.
        /// </summary>
        [Input("tags")]
        public Input<string>? Tags { get; set; }

        /// <summary>
        /// The size of each node (The default is currently g3.k3s.small)
        /// </summary>
        [Input("targetNodesSize")]
        public Input<string>? TargetNodesSize { get; set; }

        public KubernetesClusterState()
        {
        }
    }
}

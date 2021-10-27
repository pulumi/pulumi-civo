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
    /// Provides a Civo Kubernetes cluster resource. This can be used to create, delete, and modify clusters.
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
    ///         var xsmall = Output.Create(Civo.GetInstancesSize.InvokeAsync(new Civo.GetInstancesSizeArgs
    ///         {
    ///             Filters = 
    ///             {
    ///                 new Civo.Inputs.GetInstancesSizeFilterArgs
    ///                 {
    ///                     Key = "type",
    ///                     Values = 
    ///                     {
    ///                         "kubernetes",
    ///                     },
    ///                 },
    ///             },
    ///             Sorts = 
    ///             {
    ///                 new Civo.Inputs.GetInstancesSizeSortArgs
    ///                 {
    ///                     Key = "ram",
    ///                     Direction = "asc",
    ///                 },
    ///             },
    ///         }));
    ///         // Create a firewall
    ///         var my_firewall = new Civo.Firewall("my-firewall", new Civo.FirewallArgs
    ///         {
    ///         });
    ///         // Create a firewall rule
    ///         var kubernetes = new Civo.FirewallRule("kubernetes", new Civo.FirewallRuleArgs
    ///         {
    ///             FirewallId = my_firewall.Id,
    ///             Protocol = "tcp",
    ///             StartPort = "6443",
    ///             EndPort = "6443",
    ///             Cidrs = 
    ///             {
    ///                 "0.0.0.0/0",
    ///             },
    ///             Direction = "ingress",
    ///             Label = "kubernetes-api-server",
    ///         });
    ///         // Create a cluster
    ///         var my_cluster = new Civo.KubernetesCluster("my-cluster", new Civo.KubernetesClusterArgs
    ///         {
    ///             Applications = "Portainer,Linkerd:Linkerd &amp; Jaeger",
    ///             NumTargetNodes = 2,
    ///             TargetNodesSize = xsmall.Apply(xsmall =&gt; xsmall.Sizes)[0].Apply(sizes =&gt; sizes.Name),
    ///             FirewallId = my_firewall.Id,
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
    /// - **firewall_id** (String) The existing firewall ID to use for this cluster
    /// 
    /// ### Optional
    /// 
    /// - **applications** (String) Comma separated list of applications to install. Spaces within application names are fine, but shouldn't be either side of the comma. Application names are case-sensitive; the available applications can be listed with the Civo CLI: 'civo kubernetes applications ls'. If you want to remove a default installed application, prefix it with a '-', e.g. -Traefik. For application that supports plans, you can use 'app_name:app_plan' format e.g. 'Linkerd:Linkerd &amp; Jaeger' or 'MariaDB:5GB'.
    /// - **kubernetes_version** (String) The version of k3s to install (optional, the default is currently the latest available)
    /// - **name** (String) Name for your cluster, must be unique within your account
    /// - **network_id** (String) The network for the cluster, if not declare we use the default one
    /// - **num_target_nodes** (Number) The number of instances to create (optional, the default at the time of writing is 3)
    /// - **region** (String) The region for the cluster, if not declare we use the region in declared in the provider
    /// - **tags** (String) Space separated list of tags, to be used freely as required
    /// - **target_nodes_size** (String) The size of each node (optional, the default is currently g3.k3s.medium)
    /// 
    /// ### Read-Only
    /// 
    /// - **api_endpoint** (String) The API server endpoint of the cluster
    /// - **created_at** (String) The timestamp when the cluster was created
    /// - **dns_entry** (String) The DNS name of the cluster
    /// - **id** (String) The ID of this resource.
    /// - **installed_applications** (List of Object) (see below for nested schema)
    /// - **instances** (List of Object) (see below for nested schema)
    /// - **kubeconfig** (String, Sensitive) The kubeconfig of the cluster
    /// - **master_ip** (String) The IP address of the master node
    /// - **pools** (List of Object) (see below for nested schema)
    /// - **ready** (Boolean) When cluster is ready, this will return `true`
    /// - **status** (String) Status of the cluster
    /// 
    /// &lt;a id="nestedatt--installed_applications"&gt;&lt;/a&gt;
    /// ### Nested Schema for `installed_applications`
    /// 
    /// Read-Only:
    /// 
    /// - **application** (String)
    /// - **category** (String)
    /// - **installed** (Boolean)
    /// - **version** (String)
    /// 
    /// &lt;a id="nestedatt--instances"&gt;&lt;/a&gt;
    /// ### Nested Schema for `instances`
    /// 
    /// Read-Only:
    /// 
    /// - **cpu_cores** (Number)
    /// - **disk_gb** (Number)
    /// - **hostname** (String)
    /// - **ram_mb** (Number)
    /// - **size** (String)
    /// - **status** (String)
    /// - **tags** (Set of String)
    /// 
    /// &lt;a id="nestedatt--pools"&gt;&lt;/a&gt;
    /// ### Nested Schema for `pools`
    /// 
    /// Read-Only:
    /// 
    /// - **count** (Number)
    /// - **id** (String)
    /// - **instance_names** (Set of String)
    /// - **instances** (List of Object) (see below for nested schema)
    /// - **size** (String)
    /// 
    /// &lt;a id="nestedobjatt--pools--instances"&gt;&lt;/a&gt;
    /// ### Nested Schema for `pools.instances`
    /// 
    /// Read-Only:
    /// 
    /// - **cpu_cores** (Number)
    /// - **disk_gb** (Number)
    /// - **hostname** (String)
    /// - **ram_mb** (Number)
    /// - **size** (String)
    /// - **status** (String)
    /// - **tags** (Set of String)
    /// 
    /// ## Import
    /// 
    /// Import is supported using the following syntax# using ID
    /// 
    /// ```sh
    ///  $ pulumi import civo:index/kubernetesCluster:KubernetesCluster my-cluster 1b8b2100-0e9f-4e8f-ad78-9eb578c2a0af
    /// ```
    /// </summary>
    [CivoResourceType("civo:index/kubernetesCluster:KubernetesCluster")]
    public partial class KubernetesCluster : Pulumi.CustomResource
    {
        /// <summary>
        /// The API server endpoint of the cluster
        /// </summary>
        [Output("apiEndpoint")]
        public Output<string> ApiEndpoint { get; private set; } = null!;

        /// <summary>
        /// Comma separated list of applications to install. Spaces within application names are fine, but shouldn't be either side
        /// of the comma. Application names are case-sensitive; the available applications can be listed with the Civo CLI: 'civo
        /// kubernetes applications ls'. If you want to remove a default installed application, prefix it with a '-', e.g. -Traefik.
        /// For application that supports plans, you can use 'app_name:app_plan' format e.g. 'Linkerd:Linkerd &amp; Jaeger' or
        /// 'MariaDB:5GB'.
        /// </summary>
        [Output("applications")]
        public Output<string?> Applications { get; private set; } = null!;

        /// <summary>
        /// The timestamp when the cluster was created
        /// </summary>
        [Output("createdAt")]
        public Output<string> CreatedAt { get; private set; } = null!;

        /// <summary>
        /// The DNS name of the cluster
        /// </summary>
        [Output("dnsEntry")]
        public Output<string> DnsEntry { get; private set; } = null!;

        /// <summary>
        /// The existing firewall ID to use for this cluster
        /// </summary>
        [Output("firewallId")]
        public Output<string> FirewallId { get; private set; } = null!;

        /// <summary>
        /// The ID of this resource.
        /// </summary>
        [Output("id")]
        public Output<string> Id { get; private set; } = null!;

        [Output("installedApplications")]
        public Output<ImmutableArray<Outputs.KubernetesClusterInstalledApplication>> InstalledApplications { get; private set; } = null!;

        [Output("instances")]
        public Output<ImmutableArray<Outputs.KubernetesClusterInstance>> Instances { get; private set; } = null!;

        /// <summary>
        /// The kubeconfig of the cluster
        /// </summary>
        [Output("kubeconfig")]
        public Output<string> Kubeconfig { get; private set; } = null!;

        /// <summary>
        /// The version of k3s to install (optional, the default is currently the latest available)
        /// </summary>
        [Output("kubernetesVersion")]
        public Output<string> KubernetesVersion { get; private set; } = null!;

        /// <summary>
        /// The IP address of the master node
        /// </summary>
        [Output("masterIp")]
        public Output<string> MasterIp { get; private set; } = null!;

        /// <summary>
        /// Name for your cluster, must be unique within your account
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The network for the cluster, if not declare we use the default one
        /// </summary>
        [Output("networkId")]
        public Output<string> NetworkId { get; private set; } = null!;

        /// <summary>
        /// The number of instances to create (optional, the default at the time of writing is 3)
        /// </summary>
        [Output("numTargetNodes")]
        public Output<int> NumTargetNodes { get; private set; } = null!;

        [Output("pools")]
        public Output<ImmutableArray<Outputs.KubernetesClusterPool>> Pools { get; private set; } = null!;

        /// <summary>
        /// When cluster is ready, this will return `true`
        /// </summary>
        [Output("ready")]
        public Output<bool> Ready { get; private set; } = null!;

        /// <summary>
        /// The region for the cluster, if not declare we use the region in declared in the provider
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// Status of the cluster
        /// </summary>
        [Output("status")]
        public Output<string> Status { get; private set; } = null!;

        /// <summary>
        /// Space separated list of tags, to be used freely as required
        /// </summary>
        [Output("tags")]
        public Output<string?> Tags { get; private set; } = null!;

        /// <summary>
        /// The size of each node (optional, the default is currently g3.k3s.medium)
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
        public KubernetesCluster(string name, KubernetesClusterArgs args, CustomResourceOptions? options = null)
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
        /// Comma separated list of applications to install. Spaces within application names are fine, but shouldn't be either side
        /// of the comma. Application names are case-sensitive; the available applications can be listed with the Civo CLI: 'civo
        /// kubernetes applications ls'. If you want to remove a default installed application, prefix it with a '-', e.g. -Traefik.
        /// For application that supports plans, you can use 'app_name:app_plan' format e.g. 'Linkerd:Linkerd &amp; Jaeger' or
        /// 'MariaDB:5GB'.
        /// </summary>
        [Input("applications")]
        public Input<string>? Applications { get; set; }

        /// <summary>
        /// The existing firewall ID to use for this cluster
        /// </summary>
        [Input("firewallId", required: true)]
        public Input<string> FirewallId { get; set; } = null!;

        /// <summary>
        /// The version of k3s to install (optional, the default is currently the latest available)
        /// </summary>
        [Input("kubernetesVersion")]
        public Input<string>? KubernetesVersion { get; set; }

        /// <summary>
        /// Name for your cluster, must be unique within your account
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The network for the cluster, if not declare we use the default one
        /// </summary>
        [Input("networkId")]
        public Input<string>? NetworkId { get; set; }

        /// <summary>
        /// The number of instances to create (optional, the default at the time of writing is 3)
        /// </summary>
        [Input("numTargetNodes")]
        public Input<int>? NumTargetNodes { get; set; }

        /// <summary>
        /// The region for the cluster, if not declare we use the region in declared in the provider
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// Space separated list of tags, to be used freely as required
        /// </summary>
        [Input("tags")]
        public Input<string>? Tags { get; set; }

        /// <summary>
        /// The size of each node (optional, the default is currently g3.k3s.medium)
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
        /// The API server endpoint of the cluster
        /// </summary>
        [Input("apiEndpoint")]
        public Input<string>? ApiEndpoint { get; set; }

        /// <summary>
        /// Comma separated list of applications to install. Spaces within application names are fine, but shouldn't be either side
        /// of the comma. Application names are case-sensitive; the available applications can be listed with the Civo CLI: 'civo
        /// kubernetes applications ls'. If you want to remove a default installed application, prefix it with a '-', e.g. -Traefik.
        /// For application that supports plans, you can use 'app_name:app_plan' format e.g. 'Linkerd:Linkerd &amp; Jaeger' or
        /// 'MariaDB:5GB'.
        /// </summary>
        [Input("applications")]
        public Input<string>? Applications { get; set; }

        /// <summary>
        /// The timestamp when the cluster was created
        /// </summary>
        [Input("createdAt")]
        public Input<string>? CreatedAt { get; set; }

        /// <summary>
        /// The DNS name of the cluster
        /// </summary>
        [Input("dnsEntry")]
        public Input<string>? DnsEntry { get; set; }

        /// <summary>
        /// The existing firewall ID to use for this cluster
        /// </summary>
        [Input("firewallId")]
        public Input<string>? FirewallId { get; set; }

        /// <summary>
        /// The ID of this resource.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

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

        /// <summary>
        /// The kubeconfig of the cluster
        /// </summary>
        [Input("kubeconfig")]
        public Input<string>? Kubeconfig { get; set; }

        /// <summary>
        /// The version of k3s to install (optional, the default is currently the latest available)
        /// </summary>
        [Input("kubernetesVersion")]
        public Input<string>? KubernetesVersion { get; set; }

        /// <summary>
        /// The IP address of the master node
        /// </summary>
        [Input("masterIp")]
        public Input<string>? MasterIp { get; set; }

        /// <summary>
        /// Name for your cluster, must be unique within your account
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The network for the cluster, if not declare we use the default one
        /// </summary>
        [Input("networkId")]
        public Input<string>? NetworkId { get; set; }

        /// <summary>
        /// The number of instances to create (optional, the default at the time of writing is 3)
        /// </summary>
        [Input("numTargetNodes")]
        public Input<int>? NumTargetNodes { get; set; }

        [Input("pools")]
        private InputList<Inputs.KubernetesClusterPoolGetArgs>? _pools;
        public InputList<Inputs.KubernetesClusterPoolGetArgs> Pools
        {
            get => _pools ?? (_pools = new InputList<Inputs.KubernetesClusterPoolGetArgs>());
            set => _pools = value;
        }

        /// <summary>
        /// When cluster is ready, this will return `true`
        /// </summary>
        [Input("ready")]
        public Input<bool>? Ready { get; set; }

        /// <summary>
        /// The region for the cluster, if not declare we use the region in declared in the provider
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// Status of the cluster
        /// </summary>
        [Input("status")]
        public Input<string>? Status { get; set; }

        /// <summary>
        /// Space separated list of tags, to be used freely as required
        /// </summary>
        [Input("tags")]
        public Input<string>? Tags { get; set; }

        /// <summary>
        /// The size of each node (optional, the default is currently g3.k3s.medium)
        /// </summary>
        [Input("targetNodesSize")]
        public Input<string>? TargetNodesSize { get; set; }

        public KubernetesClusterState()
        {
        }
    }
}

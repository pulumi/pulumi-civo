// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Civo
{
    public static class GetKubernetesCluster
    {
        /// <summary>
        /// Provides a Civo Kubernetes cluster data source.
        /// 
        /// Note: This data source returns a single Kubernetes cluster. When specifying a name, an error will be raised if more than one Kubernetes cluster found.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Civo = Pulumi.Civo;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var my_cluster = Output.Create(Civo.GetKubernetesCluster.InvokeAsync(new Civo.GetKubernetesClusterArgs
        ///         {
        ///             Name = "my-super-cluster",
        ///         }));
        ///         this.KubernetesClusterOutput = my_cluster.Apply(my_cluster =&gt; my_cluster.MasterIp);
        ///     }
        /// 
        ///     [Output("kubernetesClusterOutput")]
        ///     public Output&lt;string&gt; KubernetesClusterOutput { get; set; }
        /// }
        /// ```
        /// 
        /// &lt;!-- schema generated by tfplugindocs --&gt;
        /// {{% /example %}}
        /// {{% /examples %}}
        /// ## Schema
        /// 
        /// ### Optional
        /// 
        /// - **id** (String) The ID of this resource.
        /// - **name** (String) The name of the Kubernetes Cluster
        /// - **region** (String) The region where cluster is running
        /// 
        /// ### Read-Only
        /// 
        /// - **api_endpoint** (String) The base URL of the API server on the Kubernetes master node
        /// - **applications** (String) A list of application installed
        /// - **created_at** (String) The date where the Kubernetes cluster was create
        /// - **dns_entry** (String) The unique dns entry for the cluster in this case point to the master
        /// - **installed_applications** (List of Object) (see below for nested schema)
        /// - **instances** (List of Object) (see below for nested schema)
        /// - **kubeconfig** (String) A representation of the Kubernetes cluster's kubeconfig in yaml format
        /// - **kubernetes_version** (String) The version of Kubernetes
        /// - **master_ip** (String) The IP of the Kubernetes master node
        /// - **num_target_nodes** (Number) The size of the Kubernetes cluster
        /// - **pools** (List of Object) (see below for nested schema)
        /// - **ready** (Boolean) If the Kubernetes cluster is ready
        /// - **status** (String) The status of Kubernetes cluster
        /// - **tags** (String) A list of tags
        /// - **target_nodes_size** (String) The size of each node
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
        /// </summary>
        public static Task<GetKubernetesClusterResult> InvokeAsync(GetKubernetesClusterArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetKubernetesClusterResult>("civo:index/getKubernetesCluster:getKubernetesCluster", args ?? new GetKubernetesClusterArgs(), options.WithVersion());
    }


    public sealed class GetKubernetesClusterArgs : Pulumi.InvokeArgs
    {
        [Input("id")]
        public string? Id { get; set; }

        [Input("name")]
        public string? Name { get; set; }

        [Input("region")]
        public string? Region { get; set; }

        public GetKubernetesClusterArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetKubernetesClusterResult
    {
        public readonly string ApiEndpoint;
        public readonly string Applications;
        public readonly string CreatedAt;
        public readonly string DnsEntry;
        public readonly string? Id;
        public readonly ImmutableArray<Outputs.GetKubernetesClusterInstalledApplicationResult> InstalledApplications;
        public readonly ImmutableArray<Outputs.GetKubernetesClusterInstanceResult> Instances;
        public readonly string Kubeconfig;
        public readonly string KubernetesVersion;
        public readonly string MasterIp;
        public readonly string? Name;
        public readonly int NumTargetNodes;
        public readonly ImmutableArray<Outputs.GetKubernetesClusterPoolResult> Pools;
        public readonly bool Ready;
        public readonly string? Region;
        public readonly string Status;
        public readonly string Tags;
        public readonly string TargetNodesSize;

        [OutputConstructor]
        private GetKubernetesClusterResult(
            string apiEndpoint,

            string applications,

            string createdAt,

            string dnsEntry,

            string? id,

            ImmutableArray<Outputs.GetKubernetesClusterInstalledApplicationResult> installedApplications,

            ImmutableArray<Outputs.GetKubernetesClusterInstanceResult> instances,

            string kubeconfig,

            string kubernetesVersion,

            string masterIp,

            string? name,

            int numTargetNodes,

            ImmutableArray<Outputs.GetKubernetesClusterPoolResult> pools,

            bool ready,

            string? region,

            string status,

            string tags,

            string targetNodesSize)
        {
            ApiEndpoint = apiEndpoint;
            Applications = applications;
            CreatedAt = createdAt;
            DnsEntry = dnsEntry;
            Id = id;
            InstalledApplications = installedApplications;
            Instances = instances;
            Kubeconfig = kubeconfig;
            KubernetesVersion = kubernetesVersion;
            MasterIp = masterIp;
            Name = name;
            NumTargetNodes = numTargetNodes;
            Pools = pools;
            Ready = ready;
            Region = region;
            Status = status;
            Tags = tags;
            TargetNodesSize = targetNodesSize;
        }
    }
}

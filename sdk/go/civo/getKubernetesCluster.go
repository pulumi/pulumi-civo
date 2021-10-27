// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides a Civo Kubernetes cluster data source.
//
// Note: This data source returns a single Kubernetes cluster. When specifying a name, an error will be raised if more than one Kubernetes cluster found.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-civo/sdk/v2/go/civo"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		opt0 := "my-super-cluster"
// 		my_cluster, err := civo.LookupKubernetesCluster(ctx, &civo.LookupKubernetesClusterArgs{
// 			Name: &opt0,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		ctx.Export("kubernetesClusterOutput", my_cluster.MasterIp)
// 		return nil
// 	})
// }
// ```
//
// <!-- schema generated by tfplugindocs -->
// ## Schema
//
// ### Optional
//
// - **id** (String) The ID of this resource.
// - **name** (String) The name of the Kubernetes Cluster
// - **region** (String) The region where cluster is running
//
// ### Read-Only
//
// - **api_endpoint** (String) The base URL of the API server on the Kubernetes master node
// - **applications** (String) A list of application installed
// - **created_at** (String) The date where the Kubernetes cluster was create
// - **dns_entry** (String) The unique dns entry for the cluster in this case point to the master
// - **installed_applications** (List of Object) (see below for nested schema)
// - **instances** (List of Object) (see below for nested schema)
// - **kubeconfig** (String) A representation of the Kubernetes cluster's kubeconfig in yaml format
// - **kubernetes_version** (String) The version of Kubernetes
// - **master_ip** (String) The IP of the Kubernetes master node
// - **num_target_nodes** (Number) The size of the Kubernetes cluster
// - **pools** (List of Object) (see below for nested schema)
// - **ready** (Boolean) If the Kubernetes cluster is ready
// - **status** (String) The status of Kubernetes cluster
// - **tags** (String) A list of tags
// - **target_nodes_size** (String) The size of each node
//
// <a id="nestedatt--installed_applications"></a>
// ### Nested Schema for `installedApplications`
//
// Read-Only:
//
// - **application** (String)
// - **category** (String)
// - **installed** (Boolean)
// - **version** (String)
//
// <a id="nestedatt--instances"></a>
// ### Nested Schema for `instances`
//
// Read-Only:
//
// - **cpu_cores** (Number)
// - **disk_gb** (Number)
// - **hostname** (String)
// - **ram_mb** (Number)
// - **size** (String)
// - **status** (String)
// - **tags** (Set of String)
//
// <a id="nestedatt--pools"></a>
// ### Nested Schema for `pools`
//
// Read-Only:
//
// - **count** (Number)
// - **id** (String)
// - **instance_names** (Set of String)
// - **instances** (List of Object) (see below for nested schema)
// - **size** (String)
//
// <a id="nestedobjatt--pools--instances"></a>
// ### Nested Schema for `pools.instances`
//
// Read-Only:
//
// - **cpu_cores** (Number)
// - **disk_gb** (Number)
// - **hostname** (String)
// - **ram_mb** (Number)
// - **size** (String)
// - **status** (String)
// - **tags** (Set of String)
func LookupKubernetesCluster(ctx *pulumi.Context, args *LookupKubernetesClusterArgs, opts ...pulumi.InvokeOption) (*LookupKubernetesClusterResult, error) {
	var rv LookupKubernetesClusterResult
	err := ctx.Invoke("civo:index/getKubernetesCluster:getKubernetesCluster", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getKubernetesCluster.
type LookupKubernetesClusterArgs struct {
	Id     *string `pulumi:"id"`
	Name   *string `pulumi:"name"`
	Region *string `pulumi:"region"`
}

// A collection of values returned by getKubernetesCluster.
type LookupKubernetesClusterResult struct {
	ApiEndpoint           string                                     `pulumi:"apiEndpoint"`
	Applications          string                                     `pulumi:"applications"`
	CreatedAt             string                                     `pulumi:"createdAt"`
	DnsEntry              string                                     `pulumi:"dnsEntry"`
	Id                    *string                                    `pulumi:"id"`
	InstalledApplications []GetKubernetesClusterInstalledApplication `pulumi:"installedApplications"`
	Instances             []GetKubernetesClusterInstance             `pulumi:"instances"`
	Kubeconfig            string                                     `pulumi:"kubeconfig"`
	KubernetesVersion     string                                     `pulumi:"kubernetesVersion"`
	MasterIp              string                                     `pulumi:"masterIp"`
	Name                  *string                                    `pulumi:"name"`
	NumTargetNodes        int                                        `pulumi:"numTargetNodes"`
	Pools                 []GetKubernetesClusterPool                 `pulumi:"pools"`
	Ready                 bool                                       `pulumi:"ready"`
	Region                *string                                    `pulumi:"region"`
	Status                string                                     `pulumi:"status"`
	Tags                  string                                     `pulumi:"tags"`
	TargetNodesSize       string                                     `pulumi:"targetNodesSize"`
}

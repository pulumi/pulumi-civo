// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides a Civo Kubernetes cluster resource. This can be used to create, delete, and modify clusters.
//
// ## Import
//
// using ID
//
// ```sh
//
//	$ pulumi import civo:index/kubernetesCluster:KubernetesCluster my-cluster 1b8b2100-0e9f-4e8f-ad78-9eb578c2a0af
//
// ```
type KubernetesCluster struct {
	pulumi.CustomResourceState

	// The API server endpoint of the cluster
	ApiEndpoint pulumi.StringOutput `pulumi:"apiEndpoint"`
	// Comma separated list of applications to install. Spaces within application names are fine, but shouldn't be either side of the comma. Application names are case-sensitive; the available applications can be listed with the Civo CLI: 'civo kubernetes applications ls'. If you want to remove a default installed application, prefix it with a '-', e.g. -Traefik. For application that supports plans, you can use 'app*name:app*plan' format e.g. 'Linkerd:Linkerd & Jaeger' or 'MariaDB:5GB'.
	Applications pulumi.StringPtrOutput `pulumi:"applications"`
	// The type of cluster to create, valid options are `k3s` or `talos` the default is `k3s`
	ClusterType pulumi.StringOutput `pulumi:"clusterType"`
	// The cni for the k3s to install (the default is `flannel`) valid options are `cilium` or `flannel`
	Cni pulumi.StringOutput `pulumi:"cni"`
	// The timestamp when the cluster was created
	CreatedAt pulumi.StringOutput `pulumi:"createdAt"`
	// The DNS name of the cluster
	DnsEntry pulumi.StringOutput `pulumi:"dnsEntry"`
	// The existing firewall ID to use for this cluster
	FirewallId            pulumi.StringOutput                              `pulumi:"firewallId"`
	InstalledApplications KubernetesClusterInstalledApplicationArrayOutput `pulumi:"installedApplications"`
	// The kubeconfig of the cluster
	Kubeconfig pulumi.StringOutput `pulumi:"kubeconfig"`
	// The version of k3s to install (optional, the default is currently the latest available)
	KubernetesVersion pulumi.StringOutput `pulumi:"kubernetesVersion"`
	// The IP address of the master node
	MasterIp pulumi.StringOutput `pulumi:"masterIp"`
	// Name for your cluster, must be unique within your account
	Name pulumi.StringOutput `pulumi:"name"`
	// The network for the cluster, if not declare we use the default one
	NetworkId pulumi.StringOutput `pulumi:"networkId"`
	// The number of instances to create (optional, the default at the time of writing is 3)
	//
	// Deprecated: This field will be deprecated in the next major release, please use the 'pools' field instead
	NumTargetNodes pulumi.IntOutput             `pulumi:"numTargetNodes"`
	Pools          KubernetesClusterPoolsOutput `pulumi:"pools"`
	// When cluster is ready, this will return `true`
	Ready pulumi.BoolOutput `pulumi:"ready"`
	// The region for the cluster, if not declare we use the region in declared in the provider
	Region pulumi.StringOutput `pulumi:"region"`
	// Status of the cluster
	Status pulumi.StringOutput `pulumi:"status"`
	// Space separated list of tags, to be used freely as required
	Tags pulumi.StringPtrOutput `pulumi:"tags"`
	// The size of each node (optional, the default is currently g4s.kube.medium)
	//
	// Deprecated: This field will be deprecated in the next major release, please use the 'pools' field instead
	TargetNodesSize pulumi.StringOutput `pulumi:"targetNodesSize"`
}

// NewKubernetesCluster registers a new resource with the given unique name, arguments, and options.
func NewKubernetesCluster(ctx *pulumi.Context,
	name string, args *KubernetesClusterArgs, opts ...pulumi.ResourceOption) (*KubernetesCluster, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.FirewallId == nil {
		return nil, errors.New("invalid value for required argument 'FirewallId'")
	}
	if args.Pools == nil {
		return nil, errors.New("invalid value for required argument 'Pools'")
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"kubeconfig",
	})
	opts = append(opts, secrets)
	var resource KubernetesCluster
	err := ctx.RegisterResource("civo:index/kubernetesCluster:KubernetesCluster", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetKubernetesCluster gets an existing KubernetesCluster resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetKubernetesCluster(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *KubernetesClusterState, opts ...pulumi.ResourceOption) (*KubernetesCluster, error) {
	var resource KubernetesCluster
	err := ctx.ReadResource("civo:index/kubernetesCluster:KubernetesCluster", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering KubernetesCluster resources.
type kubernetesClusterState struct {
	// The API server endpoint of the cluster
	ApiEndpoint *string `pulumi:"apiEndpoint"`
	// Comma separated list of applications to install. Spaces within application names are fine, but shouldn't be either side of the comma. Application names are case-sensitive; the available applications can be listed with the Civo CLI: 'civo kubernetes applications ls'. If you want to remove a default installed application, prefix it with a '-', e.g. -Traefik. For application that supports plans, you can use 'app*name:app*plan' format e.g. 'Linkerd:Linkerd & Jaeger' or 'MariaDB:5GB'.
	Applications *string `pulumi:"applications"`
	// The type of cluster to create, valid options are `k3s` or `talos` the default is `k3s`
	ClusterType *string `pulumi:"clusterType"`
	// The cni for the k3s to install (the default is `flannel`) valid options are `cilium` or `flannel`
	Cni *string `pulumi:"cni"`
	// The timestamp when the cluster was created
	CreatedAt *string `pulumi:"createdAt"`
	// The DNS name of the cluster
	DnsEntry *string `pulumi:"dnsEntry"`
	// The existing firewall ID to use for this cluster
	FirewallId            *string                                 `pulumi:"firewallId"`
	InstalledApplications []KubernetesClusterInstalledApplication `pulumi:"installedApplications"`
	// The kubeconfig of the cluster
	Kubeconfig *string `pulumi:"kubeconfig"`
	// The version of k3s to install (optional, the default is currently the latest available)
	KubernetesVersion *string `pulumi:"kubernetesVersion"`
	// The IP address of the master node
	MasterIp *string `pulumi:"masterIp"`
	// Name for your cluster, must be unique within your account
	Name *string `pulumi:"name"`
	// The network for the cluster, if not declare we use the default one
	NetworkId *string `pulumi:"networkId"`
	// The number of instances to create (optional, the default at the time of writing is 3)
	//
	// Deprecated: This field will be deprecated in the next major release, please use the 'pools' field instead
	NumTargetNodes *int                    `pulumi:"numTargetNodes"`
	Pools          *KubernetesClusterPools `pulumi:"pools"`
	// When cluster is ready, this will return `true`
	Ready *bool `pulumi:"ready"`
	// The region for the cluster, if not declare we use the region in declared in the provider
	Region *string `pulumi:"region"`
	// Status of the cluster
	Status *string `pulumi:"status"`
	// Space separated list of tags, to be used freely as required
	Tags *string `pulumi:"tags"`
	// The size of each node (optional, the default is currently g4s.kube.medium)
	//
	// Deprecated: This field will be deprecated in the next major release, please use the 'pools' field instead
	TargetNodesSize *string `pulumi:"targetNodesSize"`
}

type KubernetesClusterState struct {
	// The API server endpoint of the cluster
	ApiEndpoint pulumi.StringPtrInput
	// Comma separated list of applications to install. Spaces within application names are fine, but shouldn't be either side of the comma. Application names are case-sensitive; the available applications can be listed with the Civo CLI: 'civo kubernetes applications ls'. If you want to remove a default installed application, prefix it with a '-', e.g. -Traefik. For application that supports plans, you can use 'app*name:app*plan' format e.g. 'Linkerd:Linkerd & Jaeger' or 'MariaDB:5GB'.
	Applications pulumi.StringPtrInput
	// The type of cluster to create, valid options are `k3s` or `talos` the default is `k3s`
	ClusterType pulumi.StringPtrInput
	// The cni for the k3s to install (the default is `flannel`) valid options are `cilium` or `flannel`
	Cni pulumi.StringPtrInput
	// The timestamp when the cluster was created
	CreatedAt pulumi.StringPtrInput
	// The DNS name of the cluster
	DnsEntry pulumi.StringPtrInput
	// The existing firewall ID to use for this cluster
	FirewallId            pulumi.StringPtrInput
	InstalledApplications KubernetesClusterInstalledApplicationArrayInput
	// The kubeconfig of the cluster
	Kubeconfig pulumi.StringPtrInput
	// The version of k3s to install (optional, the default is currently the latest available)
	KubernetesVersion pulumi.StringPtrInput
	// The IP address of the master node
	MasterIp pulumi.StringPtrInput
	// Name for your cluster, must be unique within your account
	Name pulumi.StringPtrInput
	// The network for the cluster, if not declare we use the default one
	NetworkId pulumi.StringPtrInput
	// The number of instances to create (optional, the default at the time of writing is 3)
	//
	// Deprecated: This field will be deprecated in the next major release, please use the 'pools' field instead
	NumTargetNodes pulumi.IntPtrInput
	Pools          KubernetesClusterPoolsPtrInput
	// When cluster is ready, this will return `true`
	Ready pulumi.BoolPtrInput
	// The region for the cluster, if not declare we use the region in declared in the provider
	Region pulumi.StringPtrInput
	// Status of the cluster
	Status pulumi.StringPtrInput
	// Space separated list of tags, to be used freely as required
	Tags pulumi.StringPtrInput
	// The size of each node (optional, the default is currently g4s.kube.medium)
	//
	// Deprecated: This field will be deprecated in the next major release, please use the 'pools' field instead
	TargetNodesSize pulumi.StringPtrInput
}

func (KubernetesClusterState) ElementType() reflect.Type {
	return reflect.TypeOf((*kubernetesClusterState)(nil)).Elem()
}

type kubernetesClusterArgs struct {
	// Comma separated list of applications to install. Spaces within application names are fine, but shouldn't be either side of the comma. Application names are case-sensitive; the available applications can be listed with the Civo CLI: 'civo kubernetes applications ls'. If you want to remove a default installed application, prefix it with a '-', e.g. -Traefik. For application that supports plans, you can use 'app*name:app*plan' format e.g. 'Linkerd:Linkerd & Jaeger' or 'MariaDB:5GB'.
	Applications *string `pulumi:"applications"`
	// The type of cluster to create, valid options are `k3s` or `talos` the default is `k3s`
	ClusterType *string `pulumi:"clusterType"`
	// The cni for the k3s to install (the default is `flannel`) valid options are `cilium` or `flannel`
	Cni *string `pulumi:"cni"`
	// The existing firewall ID to use for this cluster
	FirewallId string `pulumi:"firewallId"`
	// The version of k3s to install (optional, the default is currently the latest available)
	KubernetesVersion *string `pulumi:"kubernetesVersion"`
	// Name for your cluster, must be unique within your account
	Name *string `pulumi:"name"`
	// The network for the cluster, if not declare we use the default one
	NetworkId *string `pulumi:"networkId"`
	// The number of instances to create (optional, the default at the time of writing is 3)
	//
	// Deprecated: This field will be deprecated in the next major release, please use the 'pools' field instead
	NumTargetNodes *int                   `pulumi:"numTargetNodes"`
	Pools          KubernetesClusterPools `pulumi:"pools"`
	// The region for the cluster, if not declare we use the region in declared in the provider
	Region *string `pulumi:"region"`
	// Space separated list of tags, to be used freely as required
	Tags *string `pulumi:"tags"`
	// The size of each node (optional, the default is currently g4s.kube.medium)
	//
	// Deprecated: This field will be deprecated in the next major release, please use the 'pools' field instead
	TargetNodesSize *string `pulumi:"targetNodesSize"`
}

// The set of arguments for constructing a KubernetesCluster resource.
type KubernetesClusterArgs struct {
	// Comma separated list of applications to install. Spaces within application names are fine, but shouldn't be either side of the comma. Application names are case-sensitive; the available applications can be listed with the Civo CLI: 'civo kubernetes applications ls'. If you want to remove a default installed application, prefix it with a '-', e.g. -Traefik. For application that supports plans, you can use 'app*name:app*plan' format e.g. 'Linkerd:Linkerd & Jaeger' or 'MariaDB:5GB'.
	Applications pulumi.StringPtrInput
	// The type of cluster to create, valid options are `k3s` or `talos` the default is `k3s`
	ClusterType pulumi.StringPtrInput
	// The cni for the k3s to install (the default is `flannel`) valid options are `cilium` or `flannel`
	Cni pulumi.StringPtrInput
	// The existing firewall ID to use for this cluster
	FirewallId pulumi.StringInput
	// The version of k3s to install (optional, the default is currently the latest available)
	KubernetesVersion pulumi.StringPtrInput
	// Name for your cluster, must be unique within your account
	Name pulumi.StringPtrInput
	// The network for the cluster, if not declare we use the default one
	NetworkId pulumi.StringPtrInput
	// The number of instances to create (optional, the default at the time of writing is 3)
	//
	// Deprecated: This field will be deprecated in the next major release, please use the 'pools' field instead
	NumTargetNodes pulumi.IntPtrInput
	Pools          KubernetesClusterPoolsInput
	// The region for the cluster, if not declare we use the region in declared in the provider
	Region pulumi.StringPtrInput
	// Space separated list of tags, to be used freely as required
	Tags pulumi.StringPtrInput
	// The size of each node (optional, the default is currently g4s.kube.medium)
	//
	// Deprecated: This field will be deprecated in the next major release, please use the 'pools' field instead
	TargetNodesSize pulumi.StringPtrInput
}

func (KubernetesClusterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*kubernetesClusterArgs)(nil)).Elem()
}

type KubernetesClusterInput interface {
	pulumi.Input

	ToKubernetesClusterOutput() KubernetesClusterOutput
	ToKubernetesClusterOutputWithContext(ctx context.Context) KubernetesClusterOutput
}

func (*KubernetesCluster) ElementType() reflect.Type {
	return reflect.TypeOf((**KubernetesCluster)(nil)).Elem()
}

func (i *KubernetesCluster) ToKubernetesClusterOutput() KubernetesClusterOutput {
	return i.ToKubernetesClusterOutputWithContext(context.Background())
}

func (i *KubernetesCluster) ToKubernetesClusterOutputWithContext(ctx context.Context) KubernetesClusterOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KubernetesClusterOutput)
}

// KubernetesClusterArrayInput is an input type that accepts KubernetesClusterArray and KubernetesClusterArrayOutput values.
// You can construct a concrete instance of `KubernetesClusterArrayInput` via:
//
//	KubernetesClusterArray{ KubernetesClusterArgs{...} }
type KubernetesClusterArrayInput interface {
	pulumi.Input

	ToKubernetesClusterArrayOutput() KubernetesClusterArrayOutput
	ToKubernetesClusterArrayOutputWithContext(context.Context) KubernetesClusterArrayOutput
}

type KubernetesClusterArray []KubernetesClusterInput

func (KubernetesClusterArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*KubernetesCluster)(nil)).Elem()
}

func (i KubernetesClusterArray) ToKubernetesClusterArrayOutput() KubernetesClusterArrayOutput {
	return i.ToKubernetesClusterArrayOutputWithContext(context.Background())
}

func (i KubernetesClusterArray) ToKubernetesClusterArrayOutputWithContext(ctx context.Context) KubernetesClusterArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KubernetesClusterArrayOutput)
}

// KubernetesClusterMapInput is an input type that accepts KubernetesClusterMap and KubernetesClusterMapOutput values.
// You can construct a concrete instance of `KubernetesClusterMapInput` via:
//
//	KubernetesClusterMap{ "key": KubernetesClusterArgs{...} }
type KubernetesClusterMapInput interface {
	pulumi.Input

	ToKubernetesClusterMapOutput() KubernetesClusterMapOutput
	ToKubernetesClusterMapOutputWithContext(context.Context) KubernetesClusterMapOutput
}

type KubernetesClusterMap map[string]KubernetesClusterInput

func (KubernetesClusterMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*KubernetesCluster)(nil)).Elem()
}

func (i KubernetesClusterMap) ToKubernetesClusterMapOutput() KubernetesClusterMapOutput {
	return i.ToKubernetesClusterMapOutputWithContext(context.Background())
}

func (i KubernetesClusterMap) ToKubernetesClusterMapOutputWithContext(ctx context.Context) KubernetesClusterMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KubernetesClusterMapOutput)
}

type KubernetesClusterOutput struct{ *pulumi.OutputState }

func (KubernetesClusterOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**KubernetesCluster)(nil)).Elem()
}

func (o KubernetesClusterOutput) ToKubernetesClusterOutput() KubernetesClusterOutput {
	return o
}

func (o KubernetesClusterOutput) ToKubernetesClusterOutputWithContext(ctx context.Context) KubernetesClusterOutput {
	return o
}

// The API server endpoint of the cluster
func (o KubernetesClusterOutput) ApiEndpoint() pulumi.StringOutput {
	return o.ApplyT(func(v *KubernetesCluster) pulumi.StringOutput { return v.ApiEndpoint }).(pulumi.StringOutput)
}

// Comma separated list of applications to install. Spaces within application names are fine, but shouldn't be either side of the comma. Application names are case-sensitive; the available applications can be listed with the Civo CLI: 'civo kubernetes applications ls'. If you want to remove a default installed application, prefix it with a '-', e.g. -Traefik. For application that supports plans, you can use 'app*name:app*plan' format e.g. 'Linkerd:Linkerd & Jaeger' or 'MariaDB:5GB'.
func (o KubernetesClusterOutput) Applications() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *KubernetesCluster) pulumi.StringPtrOutput { return v.Applications }).(pulumi.StringPtrOutput)
}

// The type of cluster to create, valid options are `k3s` or `talos` the default is `k3s`
func (o KubernetesClusterOutput) ClusterType() pulumi.StringOutput {
	return o.ApplyT(func(v *KubernetesCluster) pulumi.StringOutput { return v.ClusterType }).(pulumi.StringOutput)
}

// The cni for the k3s to install (the default is `flannel`) valid options are `cilium` or `flannel`
func (o KubernetesClusterOutput) Cni() pulumi.StringOutput {
	return o.ApplyT(func(v *KubernetesCluster) pulumi.StringOutput { return v.Cni }).(pulumi.StringOutput)
}

// The timestamp when the cluster was created
func (o KubernetesClusterOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *KubernetesCluster) pulumi.StringOutput { return v.CreatedAt }).(pulumi.StringOutput)
}

// The DNS name of the cluster
func (o KubernetesClusterOutput) DnsEntry() pulumi.StringOutput {
	return o.ApplyT(func(v *KubernetesCluster) pulumi.StringOutput { return v.DnsEntry }).(pulumi.StringOutput)
}

// The existing firewall ID to use for this cluster
func (o KubernetesClusterOutput) FirewallId() pulumi.StringOutput {
	return o.ApplyT(func(v *KubernetesCluster) pulumi.StringOutput { return v.FirewallId }).(pulumi.StringOutput)
}

func (o KubernetesClusterOutput) InstalledApplications() KubernetesClusterInstalledApplicationArrayOutput {
	return o.ApplyT(func(v *KubernetesCluster) KubernetesClusterInstalledApplicationArrayOutput {
		return v.InstalledApplications
	}).(KubernetesClusterInstalledApplicationArrayOutput)
}

// The kubeconfig of the cluster
func (o KubernetesClusterOutput) Kubeconfig() pulumi.StringOutput {
	return o.ApplyT(func(v *KubernetesCluster) pulumi.StringOutput { return v.Kubeconfig }).(pulumi.StringOutput)
}

// The version of k3s to install (optional, the default is currently the latest available)
func (o KubernetesClusterOutput) KubernetesVersion() pulumi.StringOutput {
	return o.ApplyT(func(v *KubernetesCluster) pulumi.StringOutput { return v.KubernetesVersion }).(pulumi.StringOutput)
}

// The IP address of the master node
func (o KubernetesClusterOutput) MasterIp() pulumi.StringOutput {
	return o.ApplyT(func(v *KubernetesCluster) pulumi.StringOutput { return v.MasterIp }).(pulumi.StringOutput)
}

// Name for your cluster, must be unique within your account
func (o KubernetesClusterOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *KubernetesCluster) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The network for the cluster, if not declare we use the default one
func (o KubernetesClusterOutput) NetworkId() pulumi.StringOutput {
	return o.ApplyT(func(v *KubernetesCluster) pulumi.StringOutput { return v.NetworkId }).(pulumi.StringOutput)
}

// The number of instances to create (optional, the default at the time of writing is 3)
//
// Deprecated: This field will be deprecated in the next major release, please use the 'pools' field instead
func (o KubernetesClusterOutput) NumTargetNodes() pulumi.IntOutput {
	return o.ApplyT(func(v *KubernetesCluster) pulumi.IntOutput { return v.NumTargetNodes }).(pulumi.IntOutput)
}

func (o KubernetesClusterOutput) Pools() KubernetesClusterPoolsOutput {
	return o.ApplyT(func(v *KubernetesCluster) KubernetesClusterPoolsOutput { return v.Pools }).(KubernetesClusterPoolsOutput)
}

// When cluster is ready, this will return `true`
func (o KubernetesClusterOutput) Ready() pulumi.BoolOutput {
	return o.ApplyT(func(v *KubernetesCluster) pulumi.BoolOutput { return v.Ready }).(pulumi.BoolOutput)
}

// The region for the cluster, if not declare we use the region in declared in the provider
func (o KubernetesClusterOutput) Region() pulumi.StringOutput {
	return o.ApplyT(func(v *KubernetesCluster) pulumi.StringOutput { return v.Region }).(pulumi.StringOutput)
}

// Status of the cluster
func (o KubernetesClusterOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v *KubernetesCluster) pulumi.StringOutput { return v.Status }).(pulumi.StringOutput)
}

// Space separated list of tags, to be used freely as required
func (o KubernetesClusterOutput) Tags() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *KubernetesCluster) pulumi.StringPtrOutput { return v.Tags }).(pulumi.StringPtrOutput)
}

// The size of each node (optional, the default is currently g4s.kube.medium)
//
// Deprecated: This field will be deprecated in the next major release, please use the 'pools' field instead
func (o KubernetesClusterOutput) TargetNodesSize() pulumi.StringOutput {
	return o.ApplyT(func(v *KubernetesCluster) pulumi.StringOutput { return v.TargetNodesSize }).(pulumi.StringOutput)
}

type KubernetesClusterArrayOutput struct{ *pulumi.OutputState }

func (KubernetesClusterArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*KubernetesCluster)(nil)).Elem()
}

func (o KubernetesClusterArrayOutput) ToKubernetesClusterArrayOutput() KubernetesClusterArrayOutput {
	return o
}

func (o KubernetesClusterArrayOutput) ToKubernetesClusterArrayOutputWithContext(ctx context.Context) KubernetesClusterArrayOutput {
	return o
}

func (o KubernetesClusterArrayOutput) Index(i pulumi.IntInput) KubernetesClusterOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *KubernetesCluster {
		return vs[0].([]*KubernetesCluster)[vs[1].(int)]
	}).(KubernetesClusterOutput)
}

type KubernetesClusterMapOutput struct{ *pulumi.OutputState }

func (KubernetesClusterMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*KubernetesCluster)(nil)).Elem()
}

func (o KubernetesClusterMapOutput) ToKubernetesClusterMapOutput() KubernetesClusterMapOutput {
	return o
}

func (o KubernetesClusterMapOutput) ToKubernetesClusterMapOutputWithContext(ctx context.Context) KubernetesClusterMapOutput {
	return o
}

func (o KubernetesClusterMapOutput) MapIndex(k pulumi.StringInput) KubernetesClusterOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *KubernetesCluster {
		return vs[0].(map[string]*KubernetesCluster)[vs[1].(string)]
	}).(KubernetesClusterOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*KubernetesClusterInput)(nil)).Elem(), &KubernetesCluster{})
	pulumi.RegisterInputType(reflect.TypeOf((*KubernetesClusterArrayInput)(nil)).Elem(), KubernetesClusterArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*KubernetesClusterMapInput)(nil)).Elem(), KubernetesClusterMap{})
	pulumi.RegisterOutputType(KubernetesClusterOutput{})
	pulumi.RegisterOutputType(KubernetesClusterArrayOutput{})
	pulumi.RegisterOutputType(KubernetesClusterMapOutput{})
}

// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides a Civo Kubernetes node pool resource. While the default node pool must be defined in the `KubernetesCluster` resource, this resource can be used to add additional ones to a cluster.
//
// ## Schema
//
// ### Required
//
// - **cluster_id** (String) The ID of your cluster
// - **region** (String) The region of the node pool, has to match that of the cluster
//
// ### Optional
//
// - **id** (String) The ID of this resource.
// - **num_target_nodes** (Number) the number of instances to create (optional, the default at the time of writing is 3)
// - **target_nodes_size** (String) the size of each node (optional, the default is currently g3.k3s.medium)
//
// ## Import
//
// Import is supported using the following syntax# using cluster_id:node_pool_id
//
// ```sh
//  $ pulumi import civo:index/kubernetesNodePool:KubernetesNodePool my-pool 1b8b2100-0e9f-4e8f-ad78-9eb578c2a0af:502c1130-cb9b-4a88-b6d2-307bd96d946a
// ```
type KubernetesNodePool struct {
	pulumi.CustomResourceState

	// The ID of your cluster
	ClusterId pulumi.StringOutput `pulumi:"clusterId"`
	// the number of instances to create (optional, the default at the time of writing is 3)
	NumTargetNodes pulumi.IntOutput `pulumi:"numTargetNodes"`
	// The region of the node pool, has to match that of the cluster
	Region pulumi.StringOutput `pulumi:"region"`
	// the size of each node (optional, the default is currently g3.k3s.medium)
	TargetNodesSize pulumi.StringOutput `pulumi:"targetNodesSize"`
}

// NewKubernetesNodePool registers a new resource with the given unique name, arguments, and options.
func NewKubernetesNodePool(ctx *pulumi.Context,
	name string, args *KubernetesNodePoolArgs, opts ...pulumi.ResourceOption) (*KubernetesNodePool, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ClusterId == nil {
		return nil, errors.New("invalid value for required argument 'ClusterId'")
	}
	if args.Region == nil {
		return nil, errors.New("invalid value for required argument 'Region'")
	}
	var resource KubernetesNodePool
	err := ctx.RegisterResource("civo:index/kubernetesNodePool:KubernetesNodePool", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetKubernetesNodePool gets an existing KubernetesNodePool resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetKubernetesNodePool(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *KubernetesNodePoolState, opts ...pulumi.ResourceOption) (*KubernetesNodePool, error) {
	var resource KubernetesNodePool
	err := ctx.ReadResource("civo:index/kubernetesNodePool:KubernetesNodePool", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering KubernetesNodePool resources.
type kubernetesNodePoolState struct {
	// The ID of your cluster
	ClusterId *string `pulumi:"clusterId"`
	// the number of instances to create (optional, the default at the time of writing is 3)
	NumTargetNodes *int `pulumi:"numTargetNodes"`
	// The region of the node pool, has to match that of the cluster
	Region *string `pulumi:"region"`
	// the size of each node (optional, the default is currently g3.k3s.medium)
	TargetNodesSize *string `pulumi:"targetNodesSize"`
}

type KubernetesNodePoolState struct {
	// The ID of your cluster
	ClusterId pulumi.StringPtrInput
	// the number of instances to create (optional, the default at the time of writing is 3)
	NumTargetNodes pulumi.IntPtrInput
	// The region of the node pool, has to match that of the cluster
	Region pulumi.StringPtrInput
	// the size of each node (optional, the default is currently g3.k3s.medium)
	TargetNodesSize pulumi.StringPtrInput
}

func (KubernetesNodePoolState) ElementType() reflect.Type {
	return reflect.TypeOf((*kubernetesNodePoolState)(nil)).Elem()
}

type kubernetesNodePoolArgs struct {
	// The ID of your cluster
	ClusterId string `pulumi:"clusterId"`
	// the number of instances to create (optional, the default at the time of writing is 3)
	NumTargetNodes *int `pulumi:"numTargetNodes"`
	// The region of the node pool, has to match that of the cluster
	Region string `pulumi:"region"`
	// the size of each node (optional, the default is currently g3.k3s.medium)
	TargetNodesSize *string `pulumi:"targetNodesSize"`
}

// The set of arguments for constructing a KubernetesNodePool resource.
type KubernetesNodePoolArgs struct {
	// The ID of your cluster
	ClusterId pulumi.StringInput
	// the number of instances to create (optional, the default at the time of writing is 3)
	NumTargetNodes pulumi.IntPtrInput
	// The region of the node pool, has to match that of the cluster
	Region pulumi.StringInput
	// the size of each node (optional, the default is currently g3.k3s.medium)
	TargetNodesSize pulumi.StringPtrInput
}

func (KubernetesNodePoolArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*kubernetesNodePoolArgs)(nil)).Elem()
}

type KubernetesNodePoolInput interface {
	pulumi.Input

	ToKubernetesNodePoolOutput() KubernetesNodePoolOutput
	ToKubernetesNodePoolOutputWithContext(ctx context.Context) KubernetesNodePoolOutput
}

func (*KubernetesNodePool) ElementType() reflect.Type {
	return reflect.TypeOf((*KubernetesNodePool)(nil))
}

func (i *KubernetesNodePool) ToKubernetesNodePoolOutput() KubernetesNodePoolOutput {
	return i.ToKubernetesNodePoolOutputWithContext(context.Background())
}

func (i *KubernetesNodePool) ToKubernetesNodePoolOutputWithContext(ctx context.Context) KubernetesNodePoolOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KubernetesNodePoolOutput)
}

func (i *KubernetesNodePool) ToKubernetesNodePoolPtrOutput() KubernetesNodePoolPtrOutput {
	return i.ToKubernetesNodePoolPtrOutputWithContext(context.Background())
}

func (i *KubernetesNodePool) ToKubernetesNodePoolPtrOutputWithContext(ctx context.Context) KubernetesNodePoolPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KubernetesNodePoolPtrOutput)
}

type KubernetesNodePoolPtrInput interface {
	pulumi.Input

	ToKubernetesNodePoolPtrOutput() KubernetesNodePoolPtrOutput
	ToKubernetesNodePoolPtrOutputWithContext(ctx context.Context) KubernetesNodePoolPtrOutput
}

type kubernetesNodePoolPtrType KubernetesNodePoolArgs

func (*kubernetesNodePoolPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**KubernetesNodePool)(nil))
}

func (i *kubernetesNodePoolPtrType) ToKubernetesNodePoolPtrOutput() KubernetesNodePoolPtrOutput {
	return i.ToKubernetesNodePoolPtrOutputWithContext(context.Background())
}

func (i *kubernetesNodePoolPtrType) ToKubernetesNodePoolPtrOutputWithContext(ctx context.Context) KubernetesNodePoolPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KubernetesNodePoolPtrOutput)
}

// KubernetesNodePoolArrayInput is an input type that accepts KubernetesNodePoolArray and KubernetesNodePoolArrayOutput values.
// You can construct a concrete instance of `KubernetesNodePoolArrayInput` via:
//
//          KubernetesNodePoolArray{ KubernetesNodePoolArgs{...} }
type KubernetesNodePoolArrayInput interface {
	pulumi.Input

	ToKubernetesNodePoolArrayOutput() KubernetesNodePoolArrayOutput
	ToKubernetesNodePoolArrayOutputWithContext(context.Context) KubernetesNodePoolArrayOutput
}

type KubernetesNodePoolArray []KubernetesNodePoolInput

func (KubernetesNodePoolArray) ElementType() reflect.Type {
	return reflect.TypeOf(([]*KubernetesNodePool)(nil))
}

func (i KubernetesNodePoolArray) ToKubernetesNodePoolArrayOutput() KubernetesNodePoolArrayOutput {
	return i.ToKubernetesNodePoolArrayOutputWithContext(context.Background())
}

func (i KubernetesNodePoolArray) ToKubernetesNodePoolArrayOutputWithContext(ctx context.Context) KubernetesNodePoolArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KubernetesNodePoolArrayOutput)
}

// KubernetesNodePoolMapInput is an input type that accepts KubernetesNodePoolMap and KubernetesNodePoolMapOutput values.
// You can construct a concrete instance of `KubernetesNodePoolMapInput` via:
//
//          KubernetesNodePoolMap{ "key": KubernetesNodePoolArgs{...} }
type KubernetesNodePoolMapInput interface {
	pulumi.Input

	ToKubernetesNodePoolMapOutput() KubernetesNodePoolMapOutput
	ToKubernetesNodePoolMapOutputWithContext(context.Context) KubernetesNodePoolMapOutput
}

type KubernetesNodePoolMap map[string]KubernetesNodePoolInput

func (KubernetesNodePoolMap) ElementType() reflect.Type {
	return reflect.TypeOf((map[string]*KubernetesNodePool)(nil))
}

func (i KubernetesNodePoolMap) ToKubernetesNodePoolMapOutput() KubernetesNodePoolMapOutput {
	return i.ToKubernetesNodePoolMapOutputWithContext(context.Background())
}

func (i KubernetesNodePoolMap) ToKubernetesNodePoolMapOutputWithContext(ctx context.Context) KubernetesNodePoolMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KubernetesNodePoolMapOutput)
}

type KubernetesNodePoolOutput struct {
	*pulumi.OutputState
}

func (KubernetesNodePoolOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*KubernetesNodePool)(nil))
}

func (o KubernetesNodePoolOutput) ToKubernetesNodePoolOutput() KubernetesNodePoolOutput {
	return o
}

func (o KubernetesNodePoolOutput) ToKubernetesNodePoolOutputWithContext(ctx context.Context) KubernetesNodePoolOutput {
	return o
}

func (o KubernetesNodePoolOutput) ToKubernetesNodePoolPtrOutput() KubernetesNodePoolPtrOutput {
	return o.ToKubernetesNodePoolPtrOutputWithContext(context.Background())
}

func (o KubernetesNodePoolOutput) ToKubernetesNodePoolPtrOutputWithContext(ctx context.Context) KubernetesNodePoolPtrOutput {
	return o.ApplyT(func(v KubernetesNodePool) *KubernetesNodePool {
		return &v
	}).(KubernetesNodePoolPtrOutput)
}

type KubernetesNodePoolPtrOutput struct {
	*pulumi.OutputState
}

func (KubernetesNodePoolPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**KubernetesNodePool)(nil))
}

func (o KubernetesNodePoolPtrOutput) ToKubernetesNodePoolPtrOutput() KubernetesNodePoolPtrOutput {
	return o
}

func (o KubernetesNodePoolPtrOutput) ToKubernetesNodePoolPtrOutputWithContext(ctx context.Context) KubernetesNodePoolPtrOutput {
	return o
}

type KubernetesNodePoolArrayOutput struct{ *pulumi.OutputState }

func (KubernetesNodePoolArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]KubernetesNodePool)(nil))
}

func (o KubernetesNodePoolArrayOutput) ToKubernetesNodePoolArrayOutput() KubernetesNodePoolArrayOutput {
	return o
}

func (o KubernetesNodePoolArrayOutput) ToKubernetesNodePoolArrayOutputWithContext(ctx context.Context) KubernetesNodePoolArrayOutput {
	return o
}

func (o KubernetesNodePoolArrayOutput) Index(i pulumi.IntInput) KubernetesNodePoolOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) KubernetesNodePool {
		return vs[0].([]KubernetesNodePool)[vs[1].(int)]
	}).(KubernetesNodePoolOutput)
}

type KubernetesNodePoolMapOutput struct{ *pulumi.OutputState }

func (KubernetesNodePoolMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]KubernetesNodePool)(nil))
}

func (o KubernetesNodePoolMapOutput) ToKubernetesNodePoolMapOutput() KubernetesNodePoolMapOutput {
	return o
}

func (o KubernetesNodePoolMapOutput) ToKubernetesNodePoolMapOutputWithContext(ctx context.Context) KubernetesNodePoolMapOutput {
	return o
}

func (o KubernetesNodePoolMapOutput) MapIndex(k pulumi.StringInput) KubernetesNodePoolOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) KubernetesNodePool {
		return vs[0].(map[string]KubernetesNodePool)[vs[1].(string)]
	}).(KubernetesNodePoolOutput)
}

func init() {
	pulumi.RegisterOutputType(KubernetesNodePoolOutput{})
	pulumi.RegisterOutputType(KubernetesNodePoolPtrOutput{})
	pulumi.RegisterOutputType(KubernetesNodePoolArrayOutput{})
	pulumi.RegisterOutputType(KubernetesNodePoolMapOutput{})
}

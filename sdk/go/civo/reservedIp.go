// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-civo/sdk/v2/go/civo/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides a Civo reserved IP to represent a publicly-accessible static IP addresses that can be mapped to one of your Instancesor Load Balancer.
//
// ## Example Usage
//
// <!--Start PulumiCodeChooser -->
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi-civo/sdk/v2/go/civo"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := civo.NewReservedIp(ctx, "www", nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
// <!--End PulumiCodeChooser -->
//
// ## Import
//
// terrafom import civo_reserved_ip.www 9f0e86fc-b2c6-46b4-82ed-2f28419f8ae3
type ReservedIp struct {
	pulumi.CustomResourceState

	// The IP Address of the resource
	Ip pulumi.StringOutput `pulumi:"ip"`
	// Name for the ip address
	Name pulumi.StringOutput `pulumi:"name"`
	// The region of the ip
	Region pulumi.StringOutput `pulumi:"region"`
}

// NewReservedIp registers a new resource with the given unique name, arguments, and options.
func NewReservedIp(ctx *pulumi.Context,
	name string, args *ReservedIpArgs, opts ...pulumi.ResourceOption) (*ReservedIp, error) {
	if args == nil {
		args = &ReservedIpArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ReservedIp
	err := ctx.RegisterResource("civo:index/reservedIp:ReservedIp", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetReservedIp gets an existing ReservedIp resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetReservedIp(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ReservedIpState, opts ...pulumi.ResourceOption) (*ReservedIp, error) {
	var resource ReservedIp
	err := ctx.ReadResource("civo:index/reservedIp:ReservedIp", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ReservedIp resources.
type reservedIpState struct {
	// The IP Address of the resource
	Ip *string `pulumi:"ip"`
	// Name for the ip address
	Name *string `pulumi:"name"`
	// The region of the ip
	Region *string `pulumi:"region"`
}

type ReservedIpState struct {
	// The IP Address of the resource
	Ip pulumi.StringPtrInput
	// Name for the ip address
	Name pulumi.StringPtrInput
	// The region of the ip
	Region pulumi.StringPtrInput
}

func (ReservedIpState) ElementType() reflect.Type {
	return reflect.TypeOf((*reservedIpState)(nil)).Elem()
}

type reservedIpArgs struct {
	// Name for the ip address
	Name *string `pulumi:"name"`
	// The region of the ip
	Region *string `pulumi:"region"`
}

// The set of arguments for constructing a ReservedIp resource.
type ReservedIpArgs struct {
	// Name for the ip address
	Name pulumi.StringPtrInput
	// The region of the ip
	Region pulumi.StringPtrInput
}

func (ReservedIpArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*reservedIpArgs)(nil)).Elem()
}

type ReservedIpInput interface {
	pulumi.Input

	ToReservedIpOutput() ReservedIpOutput
	ToReservedIpOutputWithContext(ctx context.Context) ReservedIpOutput
}

func (*ReservedIp) ElementType() reflect.Type {
	return reflect.TypeOf((**ReservedIp)(nil)).Elem()
}

func (i *ReservedIp) ToReservedIpOutput() ReservedIpOutput {
	return i.ToReservedIpOutputWithContext(context.Background())
}

func (i *ReservedIp) ToReservedIpOutputWithContext(ctx context.Context) ReservedIpOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ReservedIpOutput)
}

// ReservedIpArrayInput is an input type that accepts ReservedIpArray and ReservedIpArrayOutput values.
// You can construct a concrete instance of `ReservedIpArrayInput` via:
//
//	ReservedIpArray{ ReservedIpArgs{...} }
type ReservedIpArrayInput interface {
	pulumi.Input

	ToReservedIpArrayOutput() ReservedIpArrayOutput
	ToReservedIpArrayOutputWithContext(context.Context) ReservedIpArrayOutput
}

type ReservedIpArray []ReservedIpInput

func (ReservedIpArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ReservedIp)(nil)).Elem()
}

func (i ReservedIpArray) ToReservedIpArrayOutput() ReservedIpArrayOutput {
	return i.ToReservedIpArrayOutputWithContext(context.Background())
}

func (i ReservedIpArray) ToReservedIpArrayOutputWithContext(ctx context.Context) ReservedIpArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ReservedIpArrayOutput)
}

// ReservedIpMapInput is an input type that accepts ReservedIpMap and ReservedIpMapOutput values.
// You can construct a concrete instance of `ReservedIpMapInput` via:
//
//	ReservedIpMap{ "key": ReservedIpArgs{...} }
type ReservedIpMapInput interface {
	pulumi.Input

	ToReservedIpMapOutput() ReservedIpMapOutput
	ToReservedIpMapOutputWithContext(context.Context) ReservedIpMapOutput
}

type ReservedIpMap map[string]ReservedIpInput

func (ReservedIpMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ReservedIp)(nil)).Elem()
}

func (i ReservedIpMap) ToReservedIpMapOutput() ReservedIpMapOutput {
	return i.ToReservedIpMapOutputWithContext(context.Background())
}

func (i ReservedIpMap) ToReservedIpMapOutputWithContext(ctx context.Context) ReservedIpMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ReservedIpMapOutput)
}

type ReservedIpOutput struct{ *pulumi.OutputState }

func (ReservedIpOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ReservedIp)(nil)).Elem()
}

func (o ReservedIpOutput) ToReservedIpOutput() ReservedIpOutput {
	return o
}

func (o ReservedIpOutput) ToReservedIpOutputWithContext(ctx context.Context) ReservedIpOutput {
	return o
}

// The IP Address of the resource
func (o ReservedIpOutput) Ip() pulumi.StringOutput {
	return o.ApplyT(func(v *ReservedIp) pulumi.StringOutput { return v.Ip }).(pulumi.StringOutput)
}

// Name for the ip address
func (o ReservedIpOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *ReservedIp) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The region of the ip
func (o ReservedIpOutput) Region() pulumi.StringOutput {
	return o.ApplyT(func(v *ReservedIp) pulumi.StringOutput { return v.Region }).(pulumi.StringOutput)
}

type ReservedIpArrayOutput struct{ *pulumi.OutputState }

func (ReservedIpArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ReservedIp)(nil)).Elem()
}

func (o ReservedIpArrayOutput) ToReservedIpArrayOutput() ReservedIpArrayOutput {
	return o
}

func (o ReservedIpArrayOutput) ToReservedIpArrayOutputWithContext(ctx context.Context) ReservedIpArrayOutput {
	return o
}

func (o ReservedIpArrayOutput) Index(i pulumi.IntInput) ReservedIpOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *ReservedIp {
		return vs[0].([]*ReservedIp)[vs[1].(int)]
	}).(ReservedIpOutput)
}

type ReservedIpMapOutput struct{ *pulumi.OutputState }

func (ReservedIpMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ReservedIp)(nil)).Elem()
}

func (o ReservedIpMapOutput) ToReservedIpMapOutput() ReservedIpMapOutput {
	return o
}

func (o ReservedIpMapOutput) ToReservedIpMapOutputWithContext(ctx context.Context) ReservedIpMapOutput {
	return o
}

func (o ReservedIpMapOutput) MapIndex(k pulumi.StringInput) ReservedIpOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *ReservedIp {
		return vs[0].(map[string]*ReservedIp)[vs[1].(string)]
	}).(ReservedIpOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ReservedIpInput)(nil)).Elem(), &ReservedIp{})
	pulumi.RegisterInputType(reflect.TypeOf((*ReservedIpArrayInput)(nil)).Elem(), ReservedIpArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ReservedIpMapInput)(nil)).Elem(), ReservedIpMap{})
	pulumi.RegisterOutputType(ReservedIpOutput{})
	pulumi.RegisterOutputType(ReservedIpArrayOutput{})
	pulumi.RegisterOutputType(ReservedIpMapOutput{})
}

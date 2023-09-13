// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-civo/sdk/v2/go/civo/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// The instance reserved ip assignment resource schema definition
//
// ## Example Usage
//
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
//			_, err = civo.NewInstanceReservedIpAssignment(ctx, "webserver-www", &civo.InstanceReservedIpAssignmentArgs{
//				InstanceId:   pulumi.Any(civo_instance.Www.Id),
//				ReservedIpId: pulumi.Any(civo_reserved_ip.WebServer.Id),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
type InstanceReservedIpAssignment struct {
	pulumi.CustomResourceState

	// The instance id
	InstanceId pulumi.StringOutput `pulumi:"instanceId"`
	// The region of the ip
	Region pulumi.StringOutput `pulumi:"region"`
	// The reserved ip id
	ReservedIpId pulumi.StringOutput `pulumi:"reservedIpId"`
}

// NewInstanceReservedIpAssignment registers a new resource with the given unique name, arguments, and options.
func NewInstanceReservedIpAssignment(ctx *pulumi.Context,
	name string, args *InstanceReservedIpAssignmentArgs, opts ...pulumi.ResourceOption) (*InstanceReservedIpAssignment, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.InstanceId == nil {
		return nil, errors.New("invalid value for required argument 'InstanceId'")
	}
	if args.ReservedIpId == nil {
		return nil, errors.New("invalid value for required argument 'ReservedIpId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource InstanceReservedIpAssignment
	err := ctx.RegisterResource("civo:index/instanceReservedIpAssignment:InstanceReservedIpAssignment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetInstanceReservedIpAssignment gets an existing InstanceReservedIpAssignment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetInstanceReservedIpAssignment(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *InstanceReservedIpAssignmentState, opts ...pulumi.ResourceOption) (*InstanceReservedIpAssignment, error) {
	var resource InstanceReservedIpAssignment
	err := ctx.ReadResource("civo:index/instanceReservedIpAssignment:InstanceReservedIpAssignment", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering InstanceReservedIpAssignment resources.
type instanceReservedIpAssignmentState struct {
	// The instance id
	InstanceId *string `pulumi:"instanceId"`
	// The region of the ip
	Region *string `pulumi:"region"`
	// The reserved ip id
	ReservedIpId *string `pulumi:"reservedIpId"`
}

type InstanceReservedIpAssignmentState struct {
	// The instance id
	InstanceId pulumi.StringPtrInput
	// The region of the ip
	Region pulumi.StringPtrInput
	// The reserved ip id
	ReservedIpId pulumi.StringPtrInput
}

func (InstanceReservedIpAssignmentState) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceReservedIpAssignmentState)(nil)).Elem()
}

type instanceReservedIpAssignmentArgs struct {
	// The instance id
	InstanceId string `pulumi:"instanceId"`
	// The region of the ip
	Region *string `pulumi:"region"`
	// The reserved ip id
	ReservedIpId string `pulumi:"reservedIpId"`
}

// The set of arguments for constructing a InstanceReservedIpAssignment resource.
type InstanceReservedIpAssignmentArgs struct {
	// The instance id
	InstanceId pulumi.StringInput
	// The region of the ip
	Region pulumi.StringPtrInput
	// The reserved ip id
	ReservedIpId pulumi.StringInput
}

func (InstanceReservedIpAssignmentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceReservedIpAssignmentArgs)(nil)).Elem()
}

type InstanceReservedIpAssignmentInput interface {
	pulumi.Input

	ToInstanceReservedIpAssignmentOutput() InstanceReservedIpAssignmentOutput
	ToInstanceReservedIpAssignmentOutputWithContext(ctx context.Context) InstanceReservedIpAssignmentOutput
}

func (*InstanceReservedIpAssignment) ElementType() reflect.Type {
	return reflect.TypeOf((**InstanceReservedIpAssignment)(nil)).Elem()
}

func (i *InstanceReservedIpAssignment) ToInstanceReservedIpAssignmentOutput() InstanceReservedIpAssignmentOutput {
	return i.ToInstanceReservedIpAssignmentOutputWithContext(context.Background())
}

func (i *InstanceReservedIpAssignment) ToInstanceReservedIpAssignmentOutputWithContext(ctx context.Context) InstanceReservedIpAssignmentOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceReservedIpAssignmentOutput)
}

func (i *InstanceReservedIpAssignment) ToOutput(ctx context.Context) pulumix.Output[*InstanceReservedIpAssignment] {
	return pulumix.Output[*InstanceReservedIpAssignment]{
		OutputState: i.ToInstanceReservedIpAssignmentOutputWithContext(ctx).OutputState,
	}
}

// InstanceReservedIpAssignmentArrayInput is an input type that accepts InstanceReservedIpAssignmentArray and InstanceReservedIpAssignmentArrayOutput values.
// You can construct a concrete instance of `InstanceReservedIpAssignmentArrayInput` via:
//
//	InstanceReservedIpAssignmentArray{ InstanceReservedIpAssignmentArgs{...} }
type InstanceReservedIpAssignmentArrayInput interface {
	pulumi.Input

	ToInstanceReservedIpAssignmentArrayOutput() InstanceReservedIpAssignmentArrayOutput
	ToInstanceReservedIpAssignmentArrayOutputWithContext(context.Context) InstanceReservedIpAssignmentArrayOutput
}

type InstanceReservedIpAssignmentArray []InstanceReservedIpAssignmentInput

func (InstanceReservedIpAssignmentArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*InstanceReservedIpAssignment)(nil)).Elem()
}

func (i InstanceReservedIpAssignmentArray) ToInstanceReservedIpAssignmentArrayOutput() InstanceReservedIpAssignmentArrayOutput {
	return i.ToInstanceReservedIpAssignmentArrayOutputWithContext(context.Background())
}

func (i InstanceReservedIpAssignmentArray) ToInstanceReservedIpAssignmentArrayOutputWithContext(ctx context.Context) InstanceReservedIpAssignmentArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceReservedIpAssignmentArrayOutput)
}

func (i InstanceReservedIpAssignmentArray) ToOutput(ctx context.Context) pulumix.Output[[]*InstanceReservedIpAssignment] {
	return pulumix.Output[[]*InstanceReservedIpAssignment]{
		OutputState: i.ToInstanceReservedIpAssignmentArrayOutputWithContext(ctx).OutputState,
	}
}

// InstanceReservedIpAssignmentMapInput is an input type that accepts InstanceReservedIpAssignmentMap and InstanceReservedIpAssignmentMapOutput values.
// You can construct a concrete instance of `InstanceReservedIpAssignmentMapInput` via:
//
//	InstanceReservedIpAssignmentMap{ "key": InstanceReservedIpAssignmentArgs{...} }
type InstanceReservedIpAssignmentMapInput interface {
	pulumi.Input

	ToInstanceReservedIpAssignmentMapOutput() InstanceReservedIpAssignmentMapOutput
	ToInstanceReservedIpAssignmentMapOutputWithContext(context.Context) InstanceReservedIpAssignmentMapOutput
}

type InstanceReservedIpAssignmentMap map[string]InstanceReservedIpAssignmentInput

func (InstanceReservedIpAssignmentMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*InstanceReservedIpAssignment)(nil)).Elem()
}

func (i InstanceReservedIpAssignmentMap) ToInstanceReservedIpAssignmentMapOutput() InstanceReservedIpAssignmentMapOutput {
	return i.ToInstanceReservedIpAssignmentMapOutputWithContext(context.Background())
}

func (i InstanceReservedIpAssignmentMap) ToInstanceReservedIpAssignmentMapOutputWithContext(ctx context.Context) InstanceReservedIpAssignmentMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceReservedIpAssignmentMapOutput)
}

func (i InstanceReservedIpAssignmentMap) ToOutput(ctx context.Context) pulumix.Output[map[string]*InstanceReservedIpAssignment] {
	return pulumix.Output[map[string]*InstanceReservedIpAssignment]{
		OutputState: i.ToInstanceReservedIpAssignmentMapOutputWithContext(ctx).OutputState,
	}
}

type InstanceReservedIpAssignmentOutput struct{ *pulumi.OutputState }

func (InstanceReservedIpAssignmentOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**InstanceReservedIpAssignment)(nil)).Elem()
}

func (o InstanceReservedIpAssignmentOutput) ToInstanceReservedIpAssignmentOutput() InstanceReservedIpAssignmentOutput {
	return o
}

func (o InstanceReservedIpAssignmentOutput) ToInstanceReservedIpAssignmentOutputWithContext(ctx context.Context) InstanceReservedIpAssignmentOutput {
	return o
}

func (o InstanceReservedIpAssignmentOutput) ToOutput(ctx context.Context) pulumix.Output[*InstanceReservedIpAssignment] {
	return pulumix.Output[*InstanceReservedIpAssignment]{
		OutputState: o.OutputState,
	}
}

// The instance id
func (o InstanceReservedIpAssignmentOutput) InstanceId() pulumi.StringOutput {
	return o.ApplyT(func(v *InstanceReservedIpAssignment) pulumi.StringOutput { return v.InstanceId }).(pulumi.StringOutput)
}

// The region of the ip
func (o InstanceReservedIpAssignmentOutput) Region() pulumi.StringOutput {
	return o.ApplyT(func(v *InstanceReservedIpAssignment) pulumi.StringOutput { return v.Region }).(pulumi.StringOutput)
}

// The reserved ip id
func (o InstanceReservedIpAssignmentOutput) ReservedIpId() pulumi.StringOutput {
	return o.ApplyT(func(v *InstanceReservedIpAssignment) pulumi.StringOutput { return v.ReservedIpId }).(pulumi.StringOutput)
}

type InstanceReservedIpAssignmentArrayOutput struct{ *pulumi.OutputState }

func (InstanceReservedIpAssignmentArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*InstanceReservedIpAssignment)(nil)).Elem()
}

func (o InstanceReservedIpAssignmentArrayOutput) ToInstanceReservedIpAssignmentArrayOutput() InstanceReservedIpAssignmentArrayOutput {
	return o
}

func (o InstanceReservedIpAssignmentArrayOutput) ToInstanceReservedIpAssignmentArrayOutputWithContext(ctx context.Context) InstanceReservedIpAssignmentArrayOutput {
	return o
}

func (o InstanceReservedIpAssignmentArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]*InstanceReservedIpAssignment] {
	return pulumix.Output[[]*InstanceReservedIpAssignment]{
		OutputState: o.OutputState,
	}
}

func (o InstanceReservedIpAssignmentArrayOutput) Index(i pulumi.IntInput) InstanceReservedIpAssignmentOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *InstanceReservedIpAssignment {
		return vs[0].([]*InstanceReservedIpAssignment)[vs[1].(int)]
	}).(InstanceReservedIpAssignmentOutput)
}

type InstanceReservedIpAssignmentMapOutput struct{ *pulumi.OutputState }

func (InstanceReservedIpAssignmentMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*InstanceReservedIpAssignment)(nil)).Elem()
}

func (o InstanceReservedIpAssignmentMapOutput) ToInstanceReservedIpAssignmentMapOutput() InstanceReservedIpAssignmentMapOutput {
	return o
}

func (o InstanceReservedIpAssignmentMapOutput) ToInstanceReservedIpAssignmentMapOutputWithContext(ctx context.Context) InstanceReservedIpAssignmentMapOutput {
	return o
}

func (o InstanceReservedIpAssignmentMapOutput) ToOutput(ctx context.Context) pulumix.Output[map[string]*InstanceReservedIpAssignment] {
	return pulumix.Output[map[string]*InstanceReservedIpAssignment]{
		OutputState: o.OutputState,
	}
}

func (o InstanceReservedIpAssignmentMapOutput) MapIndex(k pulumi.StringInput) InstanceReservedIpAssignmentOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *InstanceReservedIpAssignment {
		return vs[0].(map[string]*InstanceReservedIpAssignment)[vs[1].(string)]
	}).(InstanceReservedIpAssignmentOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*InstanceReservedIpAssignmentInput)(nil)).Elem(), &InstanceReservedIpAssignment{})
	pulumi.RegisterInputType(reflect.TypeOf((*InstanceReservedIpAssignmentArrayInput)(nil)).Elem(), InstanceReservedIpAssignmentArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*InstanceReservedIpAssignmentMapInput)(nil)).Elem(), InstanceReservedIpAssignmentMap{})
	pulumi.RegisterOutputType(InstanceReservedIpAssignmentOutput{})
	pulumi.RegisterOutputType(InstanceReservedIpAssignmentArrayOutput{})
	pulumi.RegisterOutputType(InstanceReservedIpAssignmentMapOutput{})
}

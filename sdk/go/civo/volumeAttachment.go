// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages volume attachment/detachment to an instance.
type VolumeAttachment struct {
	pulumi.CustomResourceState

	// The ID of target instance for attachment
	InstanceId pulumi.StringOutput `pulumi:"instanceId"`
	// The region for the volume attachment
	Region pulumi.StringPtrOutput `pulumi:"region"`
	// The ID of target volume for attachment
	VolumeId pulumi.StringOutput `pulumi:"volumeId"`
}

// NewVolumeAttachment registers a new resource with the given unique name, arguments, and options.
func NewVolumeAttachment(ctx *pulumi.Context,
	name string, args *VolumeAttachmentArgs, opts ...pulumi.ResourceOption) (*VolumeAttachment, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.InstanceId == nil {
		return nil, errors.New("invalid value for required argument 'InstanceId'")
	}
	if args.VolumeId == nil {
		return nil, errors.New("invalid value for required argument 'VolumeId'")
	}
	var resource VolumeAttachment
	err := ctx.RegisterResource("civo:index/volumeAttachment:VolumeAttachment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVolumeAttachment gets an existing VolumeAttachment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVolumeAttachment(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VolumeAttachmentState, opts ...pulumi.ResourceOption) (*VolumeAttachment, error) {
	var resource VolumeAttachment
	err := ctx.ReadResource("civo:index/volumeAttachment:VolumeAttachment", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering VolumeAttachment resources.
type volumeAttachmentState struct {
	// The ID of target instance for attachment
	InstanceId *string `pulumi:"instanceId"`
	// The region for the volume attachment
	Region *string `pulumi:"region"`
	// The ID of target volume for attachment
	VolumeId *string `pulumi:"volumeId"`
}

type VolumeAttachmentState struct {
	// The ID of target instance for attachment
	InstanceId pulumi.StringPtrInput
	// The region for the volume attachment
	Region pulumi.StringPtrInput
	// The ID of target volume for attachment
	VolumeId pulumi.StringPtrInput
}

func (VolumeAttachmentState) ElementType() reflect.Type {
	return reflect.TypeOf((*volumeAttachmentState)(nil)).Elem()
}

type volumeAttachmentArgs struct {
	// The ID of target instance for attachment
	InstanceId string `pulumi:"instanceId"`
	// The region for the volume attachment
	Region *string `pulumi:"region"`
	// The ID of target volume for attachment
	VolumeId string `pulumi:"volumeId"`
}

// The set of arguments for constructing a VolumeAttachment resource.
type VolumeAttachmentArgs struct {
	// The ID of target instance for attachment
	InstanceId pulumi.StringInput
	// The region for the volume attachment
	Region pulumi.StringPtrInput
	// The ID of target volume for attachment
	VolumeId pulumi.StringInput
}

func (VolumeAttachmentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*volumeAttachmentArgs)(nil)).Elem()
}

type VolumeAttachmentInput interface {
	pulumi.Input

	ToVolumeAttachmentOutput() VolumeAttachmentOutput
	ToVolumeAttachmentOutputWithContext(ctx context.Context) VolumeAttachmentOutput
}

func (*VolumeAttachment) ElementType() reflect.Type {
	return reflect.TypeOf((**VolumeAttachment)(nil)).Elem()
}

func (i *VolumeAttachment) ToVolumeAttachmentOutput() VolumeAttachmentOutput {
	return i.ToVolumeAttachmentOutputWithContext(context.Background())
}

func (i *VolumeAttachment) ToVolumeAttachmentOutputWithContext(ctx context.Context) VolumeAttachmentOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VolumeAttachmentOutput)
}

// VolumeAttachmentArrayInput is an input type that accepts VolumeAttachmentArray and VolumeAttachmentArrayOutput values.
// You can construct a concrete instance of `VolumeAttachmentArrayInput` via:
//
//	VolumeAttachmentArray{ VolumeAttachmentArgs{...} }
type VolumeAttachmentArrayInput interface {
	pulumi.Input

	ToVolumeAttachmentArrayOutput() VolumeAttachmentArrayOutput
	ToVolumeAttachmentArrayOutputWithContext(context.Context) VolumeAttachmentArrayOutput
}

type VolumeAttachmentArray []VolumeAttachmentInput

func (VolumeAttachmentArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*VolumeAttachment)(nil)).Elem()
}

func (i VolumeAttachmentArray) ToVolumeAttachmentArrayOutput() VolumeAttachmentArrayOutput {
	return i.ToVolumeAttachmentArrayOutputWithContext(context.Background())
}

func (i VolumeAttachmentArray) ToVolumeAttachmentArrayOutputWithContext(ctx context.Context) VolumeAttachmentArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VolumeAttachmentArrayOutput)
}

// VolumeAttachmentMapInput is an input type that accepts VolumeAttachmentMap and VolumeAttachmentMapOutput values.
// You can construct a concrete instance of `VolumeAttachmentMapInput` via:
//
//	VolumeAttachmentMap{ "key": VolumeAttachmentArgs{...} }
type VolumeAttachmentMapInput interface {
	pulumi.Input

	ToVolumeAttachmentMapOutput() VolumeAttachmentMapOutput
	ToVolumeAttachmentMapOutputWithContext(context.Context) VolumeAttachmentMapOutput
}

type VolumeAttachmentMap map[string]VolumeAttachmentInput

func (VolumeAttachmentMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*VolumeAttachment)(nil)).Elem()
}

func (i VolumeAttachmentMap) ToVolumeAttachmentMapOutput() VolumeAttachmentMapOutput {
	return i.ToVolumeAttachmentMapOutputWithContext(context.Background())
}

func (i VolumeAttachmentMap) ToVolumeAttachmentMapOutputWithContext(ctx context.Context) VolumeAttachmentMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VolumeAttachmentMapOutput)
}

type VolumeAttachmentOutput struct{ *pulumi.OutputState }

func (VolumeAttachmentOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**VolumeAttachment)(nil)).Elem()
}

func (o VolumeAttachmentOutput) ToVolumeAttachmentOutput() VolumeAttachmentOutput {
	return o
}

func (o VolumeAttachmentOutput) ToVolumeAttachmentOutputWithContext(ctx context.Context) VolumeAttachmentOutput {
	return o
}

// The ID of target instance for attachment
func (o VolumeAttachmentOutput) InstanceId() pulumi.StringOutput {
	return o.ApplyT(func(v *VolumeAttachment) pulumi.StringOutput { return v.InstanceId }).(pulumi.StringOutput)
}

// The region for the volume attachment
func (o VolumeAttachmentOutput) Region() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VolumeAttachment) pulumi.StringPtrOutput { return v.Region }).(pulumi.StringPtrOutput)
}

// The ID of target volume for attachment
func (o VolumeAttachmentOutput) VolumeId() pulumi.StringOutput {
	return o.ApplyT(func(v *VolumeAttachment) pulumi.StringOutput { return v.VolumeId }).(pulumi.StringOutput)
}

type VolumeAttachmentArrayOutput struct{ *pulumi.OutputState }

func (VolumeAttachmentArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*VolumeAttachment)(nil)).Elem()
}

func (o VolumeAttachmentArrayOutput) ToVolumeAttachmentArrayOutput() VolumeAttachmentArrayOutput {
	return o
}

func (o VolumeAttachmentArrayOutput) ToVolumeAttachmentArrayOutputWithContext(ctx context.Context) VolumeAttachmentArrayOutput {
	return o
}

func (o VolumeAttachmentArrayOutput) Index(i pulumi.IntInput) VolumeAttachmentOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *VolumeAttachment {
		return vs[0].([]*VolumeAttachment)[vs[1].(int)]
	}).(VolumeAttachmentOutput)
}

type VolumeAttachmentMapOutput struct{ *pulumi.OutputState }

func (VolumeAttachmentMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*VolumeAttachment)(nil)).Elem()
}

func (o VolumeAttachmentMapOutput) ToVolumeAttachmentMapOutput() VolumeAttachmentMapOutput {
	return o
}

func (o VolumeAttachmentMapOutput) ToVolumeAttachmentMapOutputWithContext(ctx context.Context) VolumeAttachmentMapOutput {
	return o
}

func (o VolumeAttachmentMapOutput) MapIndex(k pulumi.StringInput) VolumeAttachmentOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *VolumeAttachment {
		return vs[0].(map[string]*VolumeAttachment)[vs[1].(string)]
	}).(VolumeAttachmentOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*VolumeAttachmentInput)(nil)).Elem(), &VolumeAttachment{})
	pulumi.RegisterInputType(reflect.TypeOf((*VolumeAttachmentArrayInput)(nil)).Elem(), VolumeAttachmentArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*VolumeAttachmentMapInput)(nil)).Elem(), VolumeAttachmentMap{})
	pulumi.RegisterOutputType(VolumeAttachmentOutput{})
	pulumi.RegisterOutputType(VolumeAttachmentArrayOutput{})
	pulumi.RegisterOutputType(VolumeAttachmentMapOutput{})
}

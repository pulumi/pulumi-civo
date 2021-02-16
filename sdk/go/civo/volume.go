// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a Civo volume which can be attached to a Instance in order to provide expanded storage.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-civo/sdk/go/civo"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := civo.NewVolume(ctx, "db", &civo.VolumeArgs{
// 			Bootable: pulumi.Bool(false),
// 			SizeGb:   pulumi.Int(60),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Import
//
// Volumes can be imported using the `volume id`, e.g.
//
// ```sh
//  $ pulumi import civo:index/volume:Volume db 506f78a4-e098-11e5-ad9f-000f53306ae1
// ```
type Volume struct {
	pulumi.CustomResourceState

	// Mark the volume as bootable.
	Bootable pulumi.BoolOutput `pulumi:"bootable"`
	// The date of the creation of the volume.
	CreatedAt pulumi.StringOutput `pulumi:"createdAt"`
	// The mount point of the volume.
	MountPoint pulumi.StringOutput `pulumi:"mountPoint"`
	// A name that you wish to use to refer to this volume .
	Name pulumi.StringOutput `pulumi:"name"`
	// A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes .
	SizeGb pulumi.IntOutput `pulumi:"sizeGb"`
}

// NewVolume registers a new resource with the given unique name, arguments, and options.
func NewVolume(ctx *pulumi.Context,
	name string, args *VolumeArgs, opts ...pulumi.ResourceOption) (*Volume, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Bootable == nil {
		return nil, errors.New("invalid value for required argument 'Bootable'")
	}
	if args.SizeGb == nil {
		return nil, errors.New("invalid value for required argument 'SizeGb'")
	}
	var resource Volume
	err := ctx.RegisterResource("civo:index/volume:Volume", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVolume gets an existing Volume resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVolume(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VolumeState, opts ...pulumi.ResourceOption) (*Volume, error) {
	var resource Volume
	err := ctx.ReadResource("civo:index/volume:Volume", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Volume resources.
type volumeState struct {
	// Mark the volume as bootable.
	Bootable *bool `pulumi:"bootable"`
	// The date of the creation of the volume.
	CreatedAt *string `pulumi:"createdAt"`
	// The mount point of the volume.
	MountPoint *string `pulumi:"mountPoint"`
	// A name that you wish to use to refer to this volume .
	Name *string `pulumi:"name"`
	// A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes .
	SizeGb *int `pulumi:"sizeGb"`
}

type VolumeState struct {
	// Mark the volume as bootable.
	Bootable pulumi.BoolPtrInput
	// The date of the creation of the volume.
	CreatedAt pulumi.StringPtrInput
	// The mount point of the volume.
	MountPoint pulumi.StringPtrInput
	// A name that you wish to use to refer to this volume .
	Name pulumi.StringPtrInput
	// A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes .
	SizeGb pulumi.IntPtrInput
}

func (VolumeState) ElementType() reflect.Type {
	return reflect.TypeOf((*volumeState)(nil)).Elem()
}

type volumeArgs struct {
	// Mark the volume as bootable.
	Bootable bool `pulumi:"bootable"`
	// A name that you wish to use to refer to this volume .
	Name *string `pulumi:"name"`
	// A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes .
	SizeGb int `pulumi:"sizeGb"`
}

// The set of arguments for constructing a Volume resource.
type VolumeArgs struct {
	// Mark the volume as bootable.
	Bootable pulumi.BoolInput
	// A name that you wish to use to refer to this volume .
	Name pulumi.StringPtrInput
	// A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes .
	SizeGb pulumi.IntInput
}

func (VolumeArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*volumeArgs)(nil)).Elem()
}

type VolumeInput interface {
	pulumi.Input

	ToVolumeOutput() VolumeOutput
	ToVolumeOutputWithContext(ctx context.Context) VolumeOutput
}

func (*Volume) ElementType() reflect.Type {
	return reflect.TypeOf((*Volume)(nil))
}

func (i *Volume) ToVolumeOutput() VolumeOutput {
	return i.ToVolumeOutputWithContext(context.Background())
}

func (i *Volume) ToVolumeOutputWithContext(ctx context.Context) VolumeOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VolumeOutput)
}

func (i *Volume) ToVolumePtrOutput() VolumePtrOutput {
	return i.ToVolumePtrOutputWithContext(context.Background())
}

func (i *Volume) ToVolumePtrOutputWithContext(ctx context.Context) VolumePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VolumePtrOutput)
}

type VolumePtrInput interface {
	pulumi.Input

	ToVolumePtrOutput() VolumePtrOutput
	ToVolumePtrOutputWithContext(ctx context.Context) VolumePtrOutput
}

type volumePtrType VolumeArgs

func (*volumePtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**Volume)(nil))
}

func (i *volumePtrType) ToVolumePtrOutput() VolumePtrOutput {
	return i.ToVolumePtrOutputWithContext(context.Background())
}

func (i *volumePtrType) ToVolumePtrOutputWithContext(ctx context.Context) VolumePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VolumePtrOutput)
}

// VolumeArrayInput is an input type that accepts VolumeArray and VolumeArrayOutput values.
// You can construct a concrete instance of `VolumeArrayInput` via:
//
//          VolumeArray{ VolumeArgs{...} }
type VolumeArrayInput interface {
	pulumi.Input

	ToVolumeArrayOutput() VolumeArrayOutput
	ToVolumeArrayOutputWithContext(context.Context) VolumeArrayOutput
}

type VolumeArray []VolumeInput

func (VolumeArray) ElementType() reflect.Type {
	return reflect.TypeOf(([]*Volume)(nil))
}

func (i VolumeArray) ToVolumeArrayOutput() VolumeArrayOutput {
	return i.ToVolumeArrayOutputWithContext(context.Background())
}

func (i VolumeArray) ToVolumeArrayOutputWithContext(ctx context.Context) VolumeArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VolumeArrayOutput)
}

// VolumeMapInput is an input type that accepts VolumeMap and VolumeMapOutput values.
// You can construct a concrete instance of `VolumeMapInput` via:
//
//          VolumeMap{ "key": VolumeArgs{...} }
type VolumeMapInput interface {
	pulumi.Input

	ToVolumeMapOutput() VolumeMapOutput
	ToVolumeMapOutputWithContext(context.Context) VolumeMapOutput
}

type VolumeMap map[string]VolumeInput

func (VolumeMap) ElementType() reflect.Type {
	return reflect.TypeOf((map[string]*Volume)(nil))
}

func (i VolumeMap) ToVolumeMapOutput() VolumeMapOutput {
	return i.ToVolumeMapOutputWithContext(context.Background())
}

func (i VolumeMap) ToVolumeMapOutputWithContext(ctx context.Context) VolumeMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VolumeMapOutput)
}

type VolumeOutput struct {
	*pulumi.OutputState
}

func (VolumeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Volume)(nil))
}

func (o VolumeOutput) ToVolumeOutput() VolumeOutput {
	return o
}

func (o VolumeOutput) ToVolumeOutputWithContext(ctx context.Context) VolumeOutput {
	return o
}

func (o VolumeOutput) ToVolumePtrOutput() VolumePtrOutput {
	return o.ToVolumePtrOutputWithContext(context.Background())
}

func (o VolumeOutput) ToVolumePtrOutputWithContext(ctx context.Context) VolumePtrOutput {
	return o.ApplyT(func(v Volume) *Volume {
		return &v
	}).(VolumePtrOutput)
}

type VolumePtrOutput struct {
	*pulumi.OutputState
}

func (VolumePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Volume)(nil))
}

func (o VolumePtrOutput) ToVolumePtrOutput() VolumePtrOutput {
	return o
}

func (o VolumePtrOutput) ToVolumePtrOutputWithContext(ctx context.Context) VolumePtrOutput {
	return o
}

type VolumeArrayOutput struct{ *pulumi.OutputState }

func (VolumeArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]Volume)(nil))
}

func (o VolumeArrayOutput) ToVolumeArrayOutput() VolumeArrayOutput {
	return o
}

func (o VolumeArrayOutput) ToVolumeArrayOutputWithContext(ctx context.Context) VolumeArrayOutput {
	return o
}

func (o VolumeArrayOutput) Index(i pulumi.IntInput) VolumeOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) Volume {
		return vs[0].([]Volume)[vs[1].(int)]
	}).(VolumeOutput)
}

type VolumeMapOutput struct{ *pulumi.OutputState }

func (VolumeMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]Volume)(nil))
}

func (o VolumeMapOutput) ToVolumeMapOutput() VolumeMapOutput {
	return o
}

func (o VolumeMapOutput) ToVolumeMapOutputWithContext(ctx context.Context) VolumeMapOutput {
	return o
}

func (o VolumeMapOutput) MapIndex(k pulumi.StringInput) VolumeOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) Volume {
		return vs[0].(map[string]Volume)[vs[1].(string)]
	}).(VolumeOutput)
}

func init() {
	pulumi.RegisterOutputType(VolumeOutput{})
	pulumi.RegisterOutputType(VolumePtrOutput{})
	pulumi.RegisterOutputType(VolumeArrayOutput{})
	pulumi.RegisterOutputType(VolumeMapOutput{})
}

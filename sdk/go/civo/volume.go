// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-civo/sdk/v2/go/civo/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides a Civo volume which can be attached to an instance in order to provide expanded storage.
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
//			// Get network
//			defaultNetwork, err := civo.LookupNetwork(ctx, &civo.LookupNetworkArgs{
//				Label: pulumi.StringRef("Default"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			// Create volume
//			_, err = civo.NewVolume(ctx, "db", &civo.VolumeArgs{
//				Name:      pulumi.String("backup-data"),
//				SizeGb:    pulumi.Int(5),
//				NetworkId: pulumi.String(defaultNetwork.Id),
//			}, pulumi.DependsOn([]pulumi.Resource{
//				defaultNetwork,
//			}))
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
// using ID
//
// ```sh
// $ pulumi import civo:index/volume:Volume db 506f78a4-e098-11e5-ad9f-000f53306ae1
// ```
type Volume struct {
	pulumi.CustomResourceState

	// The mount point of the volume (from instance's perspective)
	MountPoint pulumi.StringOutput `pulumi:"mountPoint"`
	// A name that you wish to use to refer to this volume
	Name pulumi.StringOutput `pulumi:"name"`
	// The network that the volume belongs to
	NetworkId pulumi.StringOutput `pulumi:"networkId"`
	// The region for the volume, if not declare we use the region in declared in the provider.
	Region pulumi.StringPtrOutput `pulumi:"region"`
	// A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes
	SizeGb pulumi.IntOutput `pulumi:"sizeGb"`
}

// NewVolume registers a new resource with the given unique name, arguments, and options.
func NewVolume(ctx *pulumi.Context,
	name string, args *VolumeArgs, opts ...pulumi.ResourceOption) (*Volume, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.NetworkId == nil {
		return nil, errors.New("invalid value for required argument 'NetworkId'")
	}
	if args.SizeGb == nil {
		return nil, errors.New("invalid value for required argument 'SizeGb'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
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
	// The mount point of the volume (from instance's perspective)
	MountPoint *string `pulumi:"mountPoint"`
	// A name that you wish to use to refer to this volume
	Name *string `pulumi:"name"`
	// The network that the volume belongs to
	NetworkId *string `pulumi:"networkId"`
	// The region for the volume, if not declare we use the region in declared in the provider.
	Region *string `pulumi:"region"`
	// A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes
	SizeGb *int `pulumi:"sizeGb"`
}

type VolumeState struct {
	// The mount point of the volume (from instance's perspective)
	MountPoint pulumi.StringPtrInput
	// A name that you wish to use to refer to this volume
	Name pulumi.StringPtrInput
	// The network that the volume belongs to
	NetworkId pulumi.StringPtrInput
	// The region for the volume, if not declare we use the region in declared in the provider.
	Region pulumi.StringPtrInput
	// A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes
	SizeGb pulumi.IntPtrInput
}

func (VolumeState) ElementType() reflect.Type {
	return reflect.TypeOf((*volumeState)(nil)).Elem()
}

type volumeArgs struct {
	// A name that you wish to use to refer to this volume
	Name *string `pulumi:"name"`
	// The network that the volume belongs to
	NetworkId string `pulumi:"networkId"`
	// The region for the volume, if not declare we use the region in declared in the provider.
	Region *string `pulumi:"region"`
	// A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes
	SizeGb int `pulumi:"sizeGb"`
}

// The set of arguments for constructing a Volume resource.
type VolumeArgs struct {
	// A name that you wish to use to refer to this volume
	Name pulumi.StringPtrInput
	// The network that the volume belongs to
	NetworkId pulumi.StringInput
	// The region for the volume, if not declare we use the region in declared in the provider.
	Region pulumi.StringPtrInput
	// A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes
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
	return reflect.TypeOf((**Volume)(nil)).Elem()
}

func (i *Volume) ToVolumeOutput() VolumeOutput {
	return i.ToVolumeOutputWithContext(context.Background())
}

func (i *Volume) ToVolumeOutputWithContext(ctx context.Context) VolumeOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VolumeOutput)
}

// VolumeArrayInput is an input type that accepts VolumeArray and VolumeArrayOutput values.
// You can construct a concrete instance of `VolumeArrayInput` via:
//
//	VolumeArray{ VolumeArgs{...} }
type VolumeArrayInput interface {
	pulumi.Input

	ToVolumeArrayOutput() VolumeArrayOutput
	ToVolumeArrayOutputWithContext(context.Context) VolumeArrayOutput
}

type VolumeArray []VolumeInput

func (VolumeArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Volume)(nil)).Elem()
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
//	VolumeMap{ "key": VolumeArgs{...} }
type VolumeMapInput interface {
	pulumi.Input

	ToVolumeMapOutput() VolumeMapOutput
	ToVolumeMapOutputWithContext(context.Context) VolumeMapOutput
}

type VolumeMap map[string]VolumeInput

func (VolumeMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Volume)(nil)).Elem()
}

func (i VolumeMap) ToVolumeMapOutput() VolumeMapOutput {
	return i.ToVolumeMapOutputWithContext(context.Background())
}

func (i VolumeMap) ToVolumeMapOutputWithContext(ctx context.Context) VolumeMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VolumeMapOutput)
}

type VolumeOutput struct{ *pulumi.OutputState }

func (VolumeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Volume)(nil)).Elem()
}

func (o VolumeOutput) ToVolumeOutput() VolumeOutput {
	return o
}

func (o VolumeOutput) ToVolumeOutputWithContext(ctx context.Context) VolumeOutput {
	return o
}

// The mount point of the volume (from instance's perspective)
func (o VolumeOutput) MountPoint() pulumi.StringOutput {
	return o.ApplyT(func(v *Volume) pulumi.StringOutput { return v.MountPoint }).(pulumi.StringOutput)
}

// A name that you wish to use to refer to this volume
func (o VolumeOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Volume) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The network that the volume belongs to
func (o VolumeOutput) NetworkId() pulumi.StringOutput {
	return o.ApplyT(func(v *Volume) pulumi.StringOutput { return v.NetworkId }).(pulumi.StringOutput)
}

// The region for the volume, if not declare we use the region in declared in the provider.
func (o VolumeOutput) Region() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Volume) pulumi.StringPtrOutput { return v.Region }).(pulumi.StringPtrOutput)
}

// A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes
func (o VolumeOutput) SizeGb() pulumi.IntOutput {
	return o.ApplyT(func(v *Volume) pulumi.IntOutput { return v.SizeGb }).(pulumi.IntOutput)
}

type VolumeArrayOutput struct{ *pulumi.OutputState }

func (VolumeArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Volume)(nil)).Elem()
}

func (o VolumeArrayOutput) ToVolumeArrayOutput() VolumeArrayOutput {
	return o
}

func (o VolumeArrayOutput) ToVolumeArrayOutputWithContext(ctx context.Context) VolumeArrayOutput {
	return o
}

func (o VolumeArrayOutput) Index(i pulumi.IntInput) VolumeOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Volume {
		return vs[0].([]*Volume)[vs[1].(int)]
	}).(VolumeOutput)
}

type VolumeMapOutput struct{ *pulumi.OutputState }

func (VolumeMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Volume)(nil)).Elem()
}

func (o VolumeMapOutput) ToVolumeMapOutput() VolumeMapOutput {
	return o
}

func (o VolumeMapOutput) ToVolumeMapOutputWithContext(ctx context.Context) VolumeMapOutput {
	return o
}

func (o VolumeMapOutput) MapIndex(k pulumi.StringInput) VolumeOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Volume {
		return vs[0].(map[string]*Volume)[vs[1].(string)]
	}).(VolumeOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*VolumeInput)(nil)).Elem(), &Volume{})
	pulumi.RegisterInputType(reflect.TypeOf((*VolumeArrayInput)(nil)).Elem(), VolumeArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*VolumeMapInput)(nil)).Elem(), VolumeMap{})
	pulumi.RegisterOutputType(VolumeOutput{})
	pulumi.RegisterOutputType(VolumeArrayOutput{})
	pulumi.RegisterOutputType(VolumeMapOutput{})
}

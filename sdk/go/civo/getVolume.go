// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Get information on a volume for use in other resources. This data source provides all of the volumes properties as configured on your Civo account.
//
// An error will be raised if the provided volume name does not exist in your Civo account.
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
//			_, err := civo.LookupVolume(ctx, &GetVolumeArgs{
//				Name: pulumi.StringRef("database-mysql"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupVolume(ctx *pulumi.Context, args *LookupVolumeArgs, opts ...pulumi.InvokeOption) (*LookupVolumeResult, error) {
	var rv LookupVolumeResult
	err := ctx.Invoke("civo:index/getVolume:getVolume", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getVolume.
type LookupVolumeArgs struct {
	Id     *string `pulumi:"id"`
	Name   *string `pulumi:"name"`
	Region *string `pulumi:"region"`
}

// A collection of values returned by getVolume.
type LookupVolumeResult struct {
	CreatedAt  string  `pulumi:"createdAt"`
	Id         *string `pulumi:"id"`
	MountPoint string  `pulumi:"mountPoint"`
	Name       *string `pulumi:"name"`
	Region     *string `pulumi:"region"`
	SizeGb     int     `pulumi:"sizeGb"`
}

func LookupVolumeOutput(ctx *pulumi.Context, args LookupVolumeOutputArgs, opts ...pulumi.InvokeOption) LookupVolumeResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupVolumeResult, error) {
			args := v.(LookupVolumeArgs)
			r, err := LookupVolume(ctx, &args, opts...)
			var s LookupVolumeResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupVolumeResultOutput)
}

// A collection of arguments for invoking getVolume.
type LookupVolumeOutputArgs struct {
	Id     pulumi.StringPtrInput `pulumi:"id"`
	Name   pulumi.StringPtrInput `pulumi:"name"`
	Region pulumi.StringPtrInput `pulumi:"region"`
}

func (LookupVolumeOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupVolumeArgs)(nil)).Elem()
}

// A collection of values returned by getVolume.
type LookupVolumeResultOutput struct{ *pulumi.OutputState }

func (LookupVolumeResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupVolumeResult)(nil)).Elem()
}

func (o LookupVolumeResultOutput) ToLookupVolumeResultOutput() LookupVolumeResultOutput {
	return o
}

func (o LookupVolumeResultOutput) ToLookupVolumeResultOutputWithContext(ctx context.Context) LookupVolumeResultOutput {
	return o
}

func (o LookupVolumeResultOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVolumeResult) string { return v.CreatedAt }).(pulumi.StringOutput)
}

func (o LookupVolumeResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupVolumeResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupVolumeResultOutput) MountPoint() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVolumeResult) string { return v.MountPoint }).(pulumi.StringOutput)
}

func (o LookupVolumeResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupVolumeResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupVolumeResultOutput) Region() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupVolumeResult) *string { return v.Region }).(pulumi.StringPtrOutput)
}

func (o LookupVolumeResultOutput) SizeGb() pulumi.IntOutput {
	return o.ApplyT(func(v LookupVolumeResult) int { return v.SizeGb }).(pulumi.IntOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupVolumeResultOutput{})
}

// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-civo/sdk/v2/go/civo/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Get information of an Object Store for use in other resources. This data source provides all of the Object Store's properties as configured on your Civo account.
//
// Note: This data source returns a single Object Store. When specifying a name, an error will be raised if more than one Object Stores with the same name found.
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
//			_, err := civo.LookupObjectStore(ctx, &civo.LookupObjectStoreArgs{
//				Name: pulumi.StringRef("backup-server"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupObjectStore(ctx *pulumi.Context, args *LookupObjectStoreArgs, opts ...pulumi.InvokeOption) (*LookupObjectStoreResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupObjectStoreResult
	err := ctx.Invoke("civo:index/getObjectStore:getObjectStore", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getObjectStore.
type LookupObjectStoreArgs struct {
	// The ID of the Object Store
	Id *string `pulumi:"id"`
	// The name of the Object Store
	Name *string `pulumi:"name"`
	// The region of an existing Object Store
	Region *string `pulumi:"region"`
}

// A collection of values returned by getObjectStore.
type LookupObjectStoreResult struct {
	// The access key ID from the Object Store credential. If this is not set, a new credential will be created.
	AccessKeyId string `pulumi:"accessKeyId"`
	// The endpoint of the Object Store
	BucketUrl string `pulumi:"bucketUrl"`
	// The ID of the Object Store
	Id *string `pulumi:"id"`
	// The maximum size of the Object Store
	MaxSizeGb int `pulumi:"maxSizeGb"`
	// The name of the Object Store
	Name *string `pulumi:"name"`
	// The region of an existing Object Store
	Region *string `pulumi:"region"`
	// The status of the Object Store
	Status string `pulumi:"status"`
}

func LookupObjectStoreOutput(ctx *pulumi.Context, args LookupObjectStoreOutputArgs, opts ...pulumi.InvokeOption) LookupObjectStoreResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupObjectStoreResultOutput, error) {
			args := v.(LookupObjectStoreArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv LookupObjectStoreResult
			secret, err := ctx.InvokePackageRaw("civo:index/getObjectStore:getObjectStore", args, &rv, "", opts...)
			if err != nil {
				return LookupObjectStoreResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(LookupObjectStoreResultOutput)
			if secret {
				return pulumi.ToSecret(output).(LookupObjectStoreResultOutput), nil
			}
			return output, nil
		}).(LookupObjectStoreResultOutput)
}

// A collection of arguments for invoking getObjectStore.
type LookupObjectStoreOutputArgs struct {
	// The ID of the Object Store
	Id pulumi.StringPtrInput `pulumi:"id"`
	// The name of the Object Store
	Name pulumi.StringPtrInput `pulumi:"name"`
	// The region of an existing Object Store
	Region pulumi.StringPtrInput `pulumi:"region"`
}

func (LookupObjectStoreOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupObjectStoreArgs)(nil)).Elem()
}

// A collection of values returned by getObjectStore.
type LookupObjectStoreResultOutput struct{ *pulumi.OutputState }

func (LookupObjectStoreResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupObjectStoreResult)(nil)).Elem()
}

func (o LookupObjectStoreResultOutput) ToLookupObjectStoreResultOutput() LookupObjectStoreResultOutput {
	return o
}

func (o LookupObjectStoreResultOutput) ToLookupObjectStoreResultOutputWithContext(ctx context.Context) LookupObjectStoreResultOutput {
	return o
}

// The access key ID from the Object Store credential. If this is not set, a new credential will be created.
func (o LookupObjectStoreResultOutput) AccessKeyId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupObjectStoreResult) string { return v.AccessKeyId }).(pulumi.StringOutput)
}

// The endpoint of the Object Store
func (o LookupObjectStoreResultOutput) BucketUrl() pulumi.StringOutput {
	return o.ApplyT(func(v LookupObjectStoreResult) string { return v.BucketUrl }).(pulumi.StringOutput)
}

// The ID of the Object Store
func (o LookupObjectStoreResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupObjectStoreResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// The maximum size of the Object Store
func (o LookupObjectStoreResultOutput) MaxSizeGb() pulumi.IntOutput {
	return o.ApplyT(func(v LookupObjectStoreResult) int { return v.MaxSizeGb }).(pulumi.IntOutput)
}

// The name of the Object Store
func (o LookupObjectStoreResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupObjectStoreResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

// The region of an existing Object Store
func (o LookupObjectStoreResultOutput) Region() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupObjectStoreResult) *string { return v.Region }).(pulumi.StringPtrOutput)
}

// The status of the Object Store
func (o LookupObjectStoreResultOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v LookupObjectStoreResult) string { return v.Status }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupObjectStoreResultOutput{})
}

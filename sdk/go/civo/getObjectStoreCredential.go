// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-civo/sdk/v2/go/civo/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Get information of an Object Store Credential for use in other resources. This data source provides all of the Object Store Credential's properties as configured on your Civo account.
//
// Note: This data source returns a single Object Store Credential. When specifying a name, an error will be raised if more than one Object Store Credentials with the same name found.
func LookupObjectStoreCredential(ctx *pulumi.Context, args *LookupObjectStoreCredentialArgs, opts ...pulumi.InvokeOption) (*LookupObjectStoreCredentialResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupObjectStoreCredentialResult
	err := ctx.Invoke("civo:index/getObjectStoreCredential:getObjectStoreCredential", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getObjectStoreCredential.
type LookupObjectStoreCredentialArgs struct {
	// The ID of the Object Store Credential
	Id *string `pulumi:"id"`
	// The name of the Object Store Credential
	Name *string `pulumi:"name"`
	// The region of an existing Object Store
	Region *string `pulumi:"region"`
}

// A collection of values returned by getObjectStoreCredential.
type LookupObjectStoreCredentialResult struct {
	// The access key id of the Object Store Credential
	AccessKeyId string `pulumi:"accessKeyId"`
	// The ID of the Object Store Credential
	Id *string `pulumi:"id"`
	// The name of the Object Store Credential
	Name *string `pulumi:"name"`
	// The region of an existing Object Store
	Region *string `pulumi:"region"`
	// The secret access key of the Object Store Credential
	SecretAccessKey string `pulumi:"secretAccessKey"`
	// The status of the Object Store Credential
	Status string `pulumi:"status"`
}

func LookupObjectStoreCredentialOutput(ctx *pulumi.Context, args LookupObjectStoreCredentialOutputArgs, opts ...pulumi.InvokeOption) LookupObjectStoreCredentialResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupObjectStoreCredentialResult, error) {
			args := v.(LookupObjectStoreCredentialArgs)
			r, err := LookupObjectStoreCredential(ctx, &args, opts...)
			var s LookupObjectStoreCredentialResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupObjectStoreCredentialResultOutput)
}

// A collection of arguments for invoking getObjectStoreCredential.
type LookupObjectStoreCredentialOutputArgs struct {
	// The ID of the Object Store Credential
	Id pulumi.StringPtrInput `pulumi:"id"`
	// The name of the Object Store Credential
	Name pulumi.StringPtrInput `pulumi:"name"`
	// The region of an existing Object Store
	Region pulumi.StringPtrInput `pulumi:"region"`
}

func (LookupObjectStoreCredentialOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupObjectStoreCredentialArgs)(nil)).Elem()
}

// A collection of values returned by getObjectStoreCredential.
type LookupObjectStoreCredentialResultOutput struct{ *pulumi.OutputState }

func (LookupObjectStoreCredentialResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupObjectStoreCredentialResult)(nil)).Elem()
}

func (o LookupObjectStoreCredentialResultOutput) ToLookupObjectStoreCredentialResultOutput() LookupObjectStoreCredentialResultOutput {
	return o
}

func (o LookupObjectStoreCredentialResultOutput) ToLookupObjectStoreCredentialResultOutputWithContext(ctx context.Context) LookupObjectStoreCredentialResultOutput {
	return o
}

func (o LookupObjectStoreCredentialResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupObjectStoreCredentialResult] {
	return pulumix.Output[LookupObjectStoreCredentialResult]{
		OutputState: o.OutputState,
	}
}

// The access key id of the Object Store Credential
func (o LookupObjectStoreCredentialResultOutput) AccessKeyId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupObjectStoreCredentialResult) string { return v.AccessKeyId }).(pulumi.StringOutput)
}

// The ID of the Object Store Credential
func (o LookupObjectStoreCredentialResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupObjectStoreCredentialResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// The name of the Object Store Credential
func (o LookupObjectStoreCredentialResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupObjectStoreCredentialResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

// The region of an existing Object Store
func (o LookupObjectStoreCredentialResultOutput) Region() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupObjectStoreCredentialResult) *string { return v.Region }).(pulumi.StringPtrOutput)
}

// The secret access key of the Object Store Credential
func (o LookupObjectStoreCredentialResultOutput) SecretAccessKey() pulumi.StringOutput {
	return o.ApplyT(func(v LookupObjectStoreCredentialResult) string { return v.SecretAccessKey }).(pulumi.StringOutput)
}

// The status of the Object Store Credential
func (o LookupObjectStoreCredentialResultOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v LookupObjectStoreCredentialResult) string { return v.Status }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupObjectStoreCredentialResultOutput{})
}

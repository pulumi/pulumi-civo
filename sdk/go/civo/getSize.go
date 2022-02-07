// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Retrieves information about the sizes that Civo supports, with the ability to filter the results.
func GetSize(ctx *pulumi.Context, args *GetSizeArgs, opts ...pulumi.InvokeOption) (*GetSizeResult, error) {
	var rv GetSizeResult
	err := ctx.Invoke("civo:index/getSize:getSize", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getSize.
type GetSizeArgs struct {
	// One or more key/value pairs on which to filter results
	Filters []GetSizeFilter `pulumi:"filters"`
	// One or more key/direction pairs on which to sort results
	Sorts []GetSizeSort `pulumi:"sorts"`
}

// A collection of values returned by getSize.
type GetSizeResult struct {
	// One or more key/value pairs on which to filter results
	Filters []GetSizeFilter `pulumi:"filters"`
	// The provider-assigned unique ID for this managed resource.
	Id    string        `pulumi:"id"`
	Sizes []GetSizeSize `pulumi:"sizes"`
	// One or more key/direction pairs on which to sort results
	Sorts []GetSizeSort `pulumi:"sorts"`
}

func GetSizeOutput(ctx *pulumi.Context, args GetSizeOutputArgs, opts ...pulumi.InvokeOption) GetSizeResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetSizeResult, error) {
			args := v.(GetSizeArgs)
			r, err := GetSize(ctx, &args, opts...)
			return *r, err
		}).(GetSizeResultOutput)
}

// A collection of arguments for invoking getSize.
type GetSizeOutputArgs struct {
	// One or more key/value pairs on which to filter results
	Filters GetSizeFilterArrayInput `pulumi:"filters"`
	// One or more key/direction pairs on which to sort results
	Sorts GetSizeSortArrayInput `pulumi:"sorts"`
}

func (GetSizeOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetSizeArgs)(nil)).Elem()
}

// A collection of values returned by getSize.
type GetSizeResultOutput struct{ *pulumi.OutputState }

func (GetSizeResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetSizeResult)(nil)).Elem()
}

func (o GetSizeResultOutput) ToGetSizeResultOutput() GetSizeResultOutput {
	return o
}

func (o GetSizeResultOutput) ToGetSizeResultOutputWithContext(ctx context.Context) GetSizeResultOutput {
	return o
}

// One or more key/value pairs on which to filter results
func (o GetSizeResultOutput) Filters() GetSizeFilterArrayOutput {
	return o.ApplyT(func(v GetSizeResult) []GetSizeFilter { return v.Filters }).(GetSizeFilterArrayOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetSizeResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetSizeResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetSizeResultOutput) Sizes() GetSizeSizeArrayOutput {
	return o.ApplyT(func(v GetSizeResult) []GetSizeSize { return v.Sizes }).(GetSizeSizeArrayOutput)
}

// One or more key/direction pairs on which to sort results
func (o GetSizeResultOutput) Sorts() GetSizeSortArrayOutput {
	return o.ApplyT(func(v GetSizeResult) []GetSizeSort { return v.Sorts }).(GetSizeSortArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetSizeResultOutput{})
}

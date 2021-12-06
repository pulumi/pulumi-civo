// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Get information on instances for use in other resources, with the ability to filter and sort the results. If no filters are specified, all instances will be returned.
//
// Note: You can use the `Instance` data source to obtain metadata about a single instance if you already know the id, unique hostname, or unique tag to retrieve.
func GetInstances(ctx *pulumi.Context, args *GetInstancesArgs, opts ...pulumi.InvokeOption) (*GetInstancesResult, error) {
	var rv GetInstancesResult
	err := ctx.Invoke("civo:index/getInstances:getInstances", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getInstances.
type GetInstancesArgs struct {
	// One or more key/value pairs on which to filter results
	Filters []GetInstancesFilter `pulumi:"filters"`
	// If used, all instances will be from the provided region
	Region *string `pulumi:"region"`
	// One or more key/direction pairs on which to sort results
	Sorts []GetInstancesSort `pulumi:"sorts"`
}

// A collection of values returned by getInstances.
type GetInstancesResult struct {
	// One or more key/value pairs on which to filter results
	Filters []GetInstancesFilter `pulumi:"filters"`
	// The provider-assigned unique ID for this managed resource.
	Id        string                 `pulumi:"id"`
	Instances []GetInstancesInstance `pulumi:"instances"`
	// If used, all instances will be from the provided region
	Region *string `pulumi:"region"`
	// One or more key/direction pairs on which to sort results
	Sorts []GetInstancesSort `pulumi:"sorts"`
}

func GetInstancesOutput(ctx *pulumi.Context, args GetInstancesOutputArgs, opts ...pulumi.InvokeOption) GetInstancesResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetInstancesResult, error) {
			args := v.(GetInstancesArgs)
			r, err := GetInstances(ctx, &args, opts...)
			return *r, err
		}).(GetInstancesResultOutput)
}

// A collection of arguments for invoking getInstances.
type GetInstancesOutputArgs struct {
	// One or more key/value pairs on which to filter results
	Filters GetInstancesFilterArrayInput `pulumi:"filters"`
	// If used, all instances will be from the provided region
	Region pulumi.StringPtrInput `pulumi:"region"`
	// One or more key/direction pairs on which to sort results
	Sorts GetInstancesSortArrayInput `pulumi:"sorts"`
}

func (GetInstancesOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetInstancesArgs)(nil)).Elem()
}

// A collection of values returned by getInstances.
type GetInstancesResultOutput struct{ *pulumi.OutputState }

func (GetInstancesResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetInstancesResult)(nil)).Elem()
}

func (o GetInstancesResultOutput) ToGetInstancesResultOutput() GetInstancesResultOutput {
	return o
}

func (o GetInstancesResultOutput) ToGetInstancesResultOutputWithContext(ctx context.Context) GetInstancesResultOutput {
	return o
}

// One or more key/value pairs on which to filter results
func (o GetInstancesResultOutput) Filters() GetInstancesFilterArrayOutput {
	return o.ApplyT(func(v GetInstancesResult) []GetInstancesFilter { return v.Filters }).(GetInstancesFilterArrayOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetInstancesResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetInstancesResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetInstancesResultOutput) Instances() GetInstancesInstanceArrayOutput {
	return o.ApplyT(func(v GetInstancesResult) []GetInstancesInstance { return v.Instances }).(GetInstancesInstanceArrayOutput)
}

// If used, all instances will be from the provided region
func (o GetInstancesResultOutput) Region() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetInstancesResult) *string { return v.Region }).(pulumi.StringPtrOutput)
}

// One or more key/direction pairs on which to sort results
func (o GetInstancesResultOutput) Sorts() GetInstancesSortArrayOutput {
	return o.ApplyT(func(v GetInstancesResult) []GetInstancesSort { return v.Sorts }).(GetInstancesSortArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetInstancesResultOutput{})
}

// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-civo/sdk/v2/go/civo/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Retrieves information about the database versions that Civo supports, with the ability to filter the results.
func GetDatabaseVersion(ctx *pulumi.Context, args *GetDatabaseVersionArgs, opts ...pulumi.InvokeOption) (*GetDatabaseVersionResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetDatabaseVersionResult
	err := ctx.Invoke("civo:index/getDatabaseVersion:getDatabaseVersion", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getDatabaseVersion.
type GetDatabaseVersionArgs struct {
	// One or more key/value pairs on which to filter results
	Filters []GetDatabaseVersionFilter `pulumi:"filters"`
	// One or more key/direction pairs on which to sort results
	Sorts []GetDatabaseVersionSort `pulumi:"sorts"`
}

// A collection of values returned by getDatabaseVersion.
type GetDatabaseVersionResult struct {
	// One or more key/value pairs on which to filter results
	Filters []GetDatabaseVersionFilter `pulumi:"filters"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// One or more key/direction pairs on which to sort results
	Sorts    []GetDatabaseVersionSort    `pulumi:"sorts"`
	Versions []GetDatabaseVersionVersion `pulumi:"versions"`
}

func GetDatabaseVersionOutput(ctx *pulumi.Context, args GetDatabaseVersionOutputArgs, opts ...pulumi.InvokeOption) GetDatabaseVersionResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (GetDatabaseVersionResultOutput, error) {
			args := v.(GetDatabaseVersionArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("civo:index/getDatabaseVersion:getDatabaseVersion", args, GetDatabaseVersionResultOutput{}, options).(GetDatabaseVersionResultOutput), nil
		}).(GetDatabaseVersionResultOutput)
}

// A collection of arguments for invoking getDatabaseVersion.
type GetDatabaseVersionOutputArgs struct {
	// One or more key/value pairs on which to filter results
	Filters GetDatabaseVersionFilterArrayInput `pulumi:"filters"`
	// One or more key/direction pairs on which to sort results
	Sorts GetDatabaseVersionSortArrayInput `pulumi:"sorts"`
}

func (GetDatabaseVersionOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetDatabaseVersionArgs)(nil)).Elem()
}

// A collection of values returned by getDatabaseVersion.
type GetDatabaseVersionResultOutput struct{ *pulumi.OutputState }

func (GetDatabaseVersionResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetDatabaseVersionResult)(nil)).Elem()
}

func (o GetDatabaseVersionResultOutput) ToGetDatabaseVersionResultOutput() GetDatabaseVersionResultOutput {
	return o
}

func (o GetDatabaseVersionResultOutput) ToGetDatabaseVersionResultOutputWithContext(ctx context.Context) GetDatabaseVersionResultOutput {
	return o
}

// One or more key/value pairs on which to filter results
func (o GetDatabaseVersionResultOutput) Filters() GetDatabaseVersionFilterArrayOutput {
	return o.ApplyT(func(v GetDatabaseVersionResult) []GetDatabaseVersionFilter { return v.Filters }).(GetDatabaseVersionFilterArrayOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetDatabaseVersionResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetDatabaseVersionResult) string { return v.Id }).(pulumi.StringOutput)
}

// One or more key/direction pairs on which to sort results
func (o GetDatabaseVersionResultOutput) Sorts() GetDatabaseVersionSortArrayOutput {
	return o.ApplyT(func(v GetDatabaseVersionResult) []GetDatabaseVersionSort { return v.Sorts }).(GetDatabaseVersionSortArrayOutput)
}

func (o GetDatabaseVersionResultOutput) Versions() GetDatabaseVersionVersionArrayOutput {
	return o.ApplyT(func(v GetDatabaseVersionResult) []GetDatabaseVersionVersion { return v.Versions }).(GetDatabaseVersionVersionArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetDatabaseVersionResultOutput{})
}

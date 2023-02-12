// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides access to the available Civo Kubernetes versions, with the ability to filter the results.
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
//			_, err := civo.GetKubernetesVersion(ctx, &civo.GetKubernetesVersionArgs{
//				Filters: []civo.GetKubernetesVersionFilter{
//					{
//						Key: "type",
//						Values: []string{
//							"stable",
//						},
//					},
//				},
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func GetKubernetesVersion(ctx *pulumi.Context, args *GetKubernetesVersionArgs, opts ...pulumi.InvokeOption) (*GetKubernetesVersionResult, error) {
	var rv GetKubernetesVersionResult
	err := ctx.Invoke("civo:index/getKubernetesVersion:getKubernetesVersion", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getKubernetesVersion.
type GetKubernetesVersionArgs struct {
	// One or more key/value pairs on which to filter results
	Filters []GetKubernetesVersionFilter `pulumi:"filters"`
	// One or more key/direction pairs on which to sort results
	Sorts []GetKubernetesVersionSort `pulumi:"sorts"`
}

// A collection of values returned by getKubernetesVersion.
type GetKubernetesVersionResult struct {
	// One or more key/value pairs on which to filter results
	Filters []GetKubernetesVersionFilter `pulumi:"filters"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// One or more key/direction pairs on which to sort results
	Sorts    []GetKubernetesVersionSort    `pulumi:"sorts"`
	Versions []GetKubernetesVersionVersion `pulumi:"versions"`
}

func GetKubernetesVersionOutput(ctx *pulumi.Context, args GetKubernetesVersionOutputArgs, opts ...pulumi.InvokeOption) GetKubernetesVersionResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetKubernetesVersionResult, error) {
			args := v.(GetKubernetesVersionArgs)
			r, err := GetKubernetesVersion(ctx, &args, opts...)
			var s GetKubernetesVersionResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetKubernetesVersionResultOutput)
}

// A collection of arguments for invoking getKubernetesVersion.
type GetKubernetesVersionOutputArgs struct {
	// One or more key/value pairs on which to filter results
	Filters GetKubernetesVersionFilterArrayInput `pulumi:"filters"`
	// One or more key/direction pairs on which to sort results
	Sorts GetKubernetesVersionSortArrayInput `pulumi:"sorts"`
}

func (GetKubernetesVersionOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetKubernetesVersionArgs)(nil)).Elem()
}

// A collection of values returned by getKubernetesVersion.
type GetKubernetesVersionResultOutput struct{ *pulumi.OutputState }

func (GetKubernetesVersionResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetKubernetesVersionResult)(nil)).Elem()
}

func (o GetKubernetesVersionResultOutput) ToGetKubernetesVersionResultOutput() GetKubernetesVersionResultOutput {
	return o
}

func (o GetKubernetesVersionResultOutput) ToGetKubernetesVersionResultOutputWithContext(ctx context.Context) GetKubernetesVersionResultOutput {
	return o
}

// One or more key/value pairs on which to filter results
func (o GetKubernetesVersionResultOutput) Filters() GetKubernetesVersionFilterArrayOutput {
	return o.ApplyT(func(v GetKubernetesVersionResult) []GetKubernetesVersionFilter { return v.Filters }).(GetKubernetesVersionFilterArrayOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetKubernetesVersionResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetKubernetesVersionResult) string { return v.Id }).(pulumi.StringOutput)
}

// One or more key/direction pairs on which to sort results
func (o GetKubernetesVersionResultOutput) Sorts() GetKubernetesVersionSortArrayOutput {
	return o.ApplyT(func(v GetKubernetesVersionResult) []GetKubernetesVersionSort { return v.Sorts }).(GetKubernetesVersionSortArrayOutput)
}

func (o GetKubernetesVersionResultOutput) Versions() GetKubernetesVersionVersionArrayOutput {
	return o.ApplyT(func(v GetKubernetesVersionResult) []GetKubernetesVersionVersion { return v.Versions }).(GetKubernetesVersionVersionArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetKubernetesVersionResultOutput{})
}

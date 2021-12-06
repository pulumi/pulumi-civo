// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Retrieve information about a network for use in other resources.
//
// This data source provides all of the network's properties as configured on your Civo account.
//
// Networks may be looked up by id or label, and you can optionally pass region if you want to make a lookup for an expecific network inside that region.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-civo/sdk/v2/go/civo"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		opt0 := "test-network"
// 		opt1 := "NYC1"
// 		_, err := civo.LookupNetwork(ctx, &GetNetworkArgs{
// 			Label:  &opt0,
// 			Region: &opt1,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func LookupNetwork(ctx *pulumi.Context, args *LookupNetworkArgs, opts ...pulumi.InvokeOption) (*LookupNetworkResult, error) {
	var rv LookupNetworkResult
	err := ctx.Invoke("civo:index/getNetwork:getNetwork", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getNetwork.
type LookupNetworkArgs struct {
	// The ID of this resource.
	Id *string `pulumi:"id"`
	// The label of an existing network
	Label *string `pulumi:"label"`
	// The region of an existing network
	Region *string `pulumi:"region"`
}

// A collection of values returned by getNetwork.
type LookupNetworkResult struct {
	// If is the default network
	Default bool `pulumi:"default"`
	// The ID of this resource.
	Id *string `pulumi:"id"`
	// The label of an existing network
	Label *string `pulumi:"label"`
	// The name of the network
	Name string `pulumi:"name"`
	// The region of an existing network
	Region *string `pulumi:"region"`
}

func LookupNetworkOutput(ctx *pulumi.Context, args LookupNetworkOutputArgs, opts ...pulumi.InvokeOption) LookupNetworkResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupNetworkResult, error) {
			args := v.(LookupNetworkArgs)
			r, err := LookupNetwork(ctx, &args, opts...)
			return *r, err
		}).(LookupNetworkResultOutput)
}

// A collection of arguments for invoking getNetwork.
type LookupNetworkOutputArgs struct {
	// The ID of this resource.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// The label of an existing network
	Label pulumi.StringPtrInput `pulumi:"label"`
	// The region of an existing network
	Region pulumi.StringPtrInput `pulumi:"region"`
}

func (LookupNetworkOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNetworkArgs)(nil)).Elem()
}

// A collection of values returned by getNetwork.
type LookupNetworkResultOutput struct{ *pulumi.OutputState }

func (LookupNetworkResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNetworkResult)(nil)).Elem()
}

func (o LookupNetworkResultOutput) ToLookupNetworkResultOutput() LookupNetworkResultOutput {
	return o
}

func (o LookupNetworkResultOutput) ToLookupNetworkResultOutputWithContext(ctx context.Context) LookupNetworkResultOutput {
	return o
}

// If is the default network
func (o LookupNetworkResultOutput) Default() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupNetworkResult) bool { return v.Default }).(pulumi.BoolOutput)
}

// The ID of this resource.
func (o LookupNetworkResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNetworkResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// The label of an existing network
func (o LookupNetworkResultOutput) Label() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNetworkResult) *string { return v.Label }).(pulumi.StringPtrOutput)
}

// The name of the network
func (o LookupNetworkResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNetworkResult) string { return v.Name }).(pulumi.StringOutput)
}

// The region of an existing network
func (o LookupNetworkResultOutput) Region() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNetworkResult) *string { return v.Region }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupNetworkResultOutput{})
}

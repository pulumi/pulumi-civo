// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Retrieve information about a firewall for use in other resources.
//
// This data source provides all of the firewall's properties as configured on your Civo account.
//
// Firewalls may be looked up by id or name, and you can optionally pass region if you want to make a lookup for an expecific firewall inside that region.
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
// 		_, err := civo.LookupFirewall(ctx, &GetFirewallArgs{
// 			Name:   pulumi.StringRef("test-firewall"),
// 			Region: pulumi.StringRef("NYC1"),
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func LookupFirewall(ctx *pulumi.Context, args *LookupFirewallArgs, opts ...pulumi.InvokeOption) (*LookupFirewallResult, error) {
	var rv LookupFirewallResult
	err := ctx.Invoke("civo:index/getFirewall:getFirewall", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getFirewall.
type LookupFirewallArgs struct {
	Id     *string `pulumi:"id"`
	Name   *string `pulumi:"name"`
	Region *string `pulumi:"region"`
}

// A collection of values returned by getFirewall.
type LookupFirewallResult struct {
	Id        *string `pulumi:"id"`
	Name      *string `pulumi:"name"`
	NetworkId string  `pulumi:"networkId"`
	Region    *string `pulumi:"region"`
}

func LookupFirewallOutput(ctx *pulumi.Context, args LookupFirewallOutputArgs, opts ...pulumi.InvokeOption) LookupFirewallResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupFirewallResult, error) {
			args := v.(LookupFirewallArgs)
			r, err := LookupFirewall(ctx, &args, opts...)
			var s LookupFirewallResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupFirewallResultOutput)
}

// A collection of arguments for invoking getFirewall.
type LookupFirewallOutputArgs struct {
	Id     pulumi.StringPtrInput `pulumi:"id"`
	Name   pulumi.StringPtrInput `pulumi:"name"`
	Region pulumi.StringPtrInput `pulumi:"region"`
}

func (LookupFirewallOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupFirewallArgs)(nil)).Elem()
}

// A collection of values returned by getFirewall.
type LookupFirewallResultOutput struct{ *pulumi.OutputState }

func (LookupFirewallResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupFirewallResult)(nil)).Elem()
}

func (o LookupFirewallResultOutput) ToLookupFirewallResultOutput() LookupFirewallResultOutput {
	return o
}

func (o LookupFirewallResultOutput) ToLookupFirewallResultOutputWithContext(ctx context.Context) LookupFirewallResultOutput {
	return o
}

func (o LookupFirewallResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFirewallResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupFirewallResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFirewallResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupFirewallResultOutput) NetworkId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupFirewallResult) string { return v.NetworkId }).(pulumi.StringOutput)
}

func (o LookupFirewallResultOutput) Region() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFirewallResult) *string { return v.Region }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupFirewallResultOutput{})
}

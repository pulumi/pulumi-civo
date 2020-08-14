// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a Civo Cloud Firewall resource. This can be used to create,
// modify, and delete Firewalls.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-civo/sdk/go/civo"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := civo.NewFirewall(ctx, "www", nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Firewall struct {
	pulumi.CustomResourceState

	// The Firewall name
	Name pulumi.StringOutput `pulumi:"name"`
	// The region where the firewall was create.
	Region pulumi.StringOutput `pulumi:"region"`
}

// NewFirewall registers a new resource with the given unique name, arguments, and options.
func NewFirewall(ctx *pulumi.Context,
	name string, args *FirewallArgs, opts ...pulumi.ResourceOption) (*Firewall, error) {
	if args == nil {
		args = &FirewallArgs{}
	}
	var resource Firewall
	err := ctx.RegisterResource("civo:index/firewall:Firewall", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFirewall gets an existing Firewall resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFirewall(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FirewallState, opts ...pulumi.ResourceOption) (*Firewall, error) {
	var resource Firewall
	err := ctx.ReadResource("civo:index/firewall:Firewall", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Firewall resources.
type firewallState struct {
	// The Firewall name
	Name *string `pulumi:"name"`
	// The region where the firewall was create.
	Region *string `pulumi:"region"`
}

type FirewallState struct {
	// The Firewall name
	Name pulumi.StringPtrInput
	// The region where the firewall was create.
	Region pulumi.StringPtrInput
}

func (FirewallState) ElementType() reflect.Type {
	return reflect.TypeOf((*firewallState)(nil)).Elem()
}

type firewallArgs struct {
	// The Firewall name
	Name *string `pulumi:"name"`
}

// The set of arguments for constructing a Firewall resource.
type FirewallArgs struct {
	// The Firewall name
	Name pulumi.StringPtrInput
}

func (FirewallArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*firewallArgs)(nil)).Elem()
}
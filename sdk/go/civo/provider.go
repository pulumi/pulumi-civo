// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-civo/sdk/v2/go/civo/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The provider type for the civo package. By default, resources use package-wide configuration
// settings, however an explicit `Provider` instance may be created and passed during resource
// construction to achieve fine-grained programmatic control over provider settings. See the
// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
type Provider struct {
	pulumi.ProviderResourceState

	// The Base URL to use for CIVO API.
	ApiEndpoint pulumi.StringPtrOutput `pulumi:"apiEndpoint"`
	// If region is not set, then no region will be used and them you need expensify in every resource even if you expensify
	// here you can overwrite in a resource.
	Region pulumi.StringPtrOutput `pulumi:"region"`
	// This is the Civo API token. Alternatively, this can also be specified using `CIVO_TOKEN` environment variable.
	Token pulumi.StringPtrOutput `pulumi:"token"`
}

// NewProvider registers a new resource with the given unique name, arguments, and options.
func NewProvider(ctx *pulumi.Context,
	name string, args *ProviderArgs, opts ...pulumi.ResourceOption) (*Provider, error) {
	if args == nil {
		args = &ProviderArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Provider
	err := ctx.RegisterResource("pulumi:providers:civo", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

type providerArgs struct {
	// The Base URL to use for CIVO API.
	ApiEndpoint *string `pulumi:"apiEndpoint"`
	// If region is not set, then no region will be used and them you need expensify in every resource even if you expensify
	// here you can overwrite in a resource.
	Region *string `pulumi:"region"`
	// This is the Civo API token. Alternatively, this can also be specified using `CIVO_TOKEN` environment variable.
	Token *string `pulumi:"token"`
}

// The set of arguments for constructing a Provider resource.
type ProviderArgs struct {
	// The Base URL to use for CIVO API.
	ApiEndpoint pulumi.StringPtrInput
	// If region is not set, then no region will be used and them you need expensify in every resource even if you expensify
	// here you can overwrite in a resource.
	Region pulumi.StringPtrInput
	// This is the Civo API token. Alternatively, this can also be specified using `CIVO_TOKEN` environment variable.
	Token pulumi.StringPtrInput
}

func (ProviderArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*providerArgs)(nil)).Elem()
}

type ProviderInput interface {
	pulumi.Input

	ToProviderOutput() ProviderOutput
	ToProviderOutputWithContext(ctx context.Context) ProviderOutput
}

func (*Provider) ElementType() reflect.Type {
	return reflect.TypeOf((**Provider)(nil)).Elem()
}

func (i *Provider) ToProviderOutput() ProviderOutput {
	return i.ToProviderOutputWithContext(context.Background())
}

func (i *Provider) ToProviderOutputWithContext(ctx context.Context) ProviderOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProviderOutput)
}

type ProviderOutput struct{ *pulumi.OutputState }

func (ProviderOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Provider)(nil)).Elem()
}

func (o ProviderOutput) ToProviderOutput() ProviderOutput {
	return o
}

func (o ProviderOutput) ToProviderOutputWithContext(ctx context.Context) ProviderOutput {
	return o
}

// The Base URL to use for CIVO API.
func (o ProviderOutput) ApiEndpoint() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.ApiEndpoint }).(pulumi.StringPtrOutput)
}

// If region is not set, then no region will be used and them you need expensify in every resource even if you expensify
// here you can overwrite in a resource.
func (o ProviderOutput) Region() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.Region }).(pulumi.StringPtrOutput)
}

// This is the Civo API token. Alternatively, this can also be specified using `CIVO_TOKEN` environment variable.
func (o ProviderOutput) Token() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.Token }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ProviderInput)(nil)).Elem(), &Provider{})
	pulumi.RegisterOutputType(ProviderOutput{})
}

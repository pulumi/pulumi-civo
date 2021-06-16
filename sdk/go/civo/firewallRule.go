// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides a Civo Cloud Firewall Rule resource.
// This can be used to create, modify, and delete Firewalls Rules.
// This resource don't have an update option because the backend don't have the
// support for that, so in this case we use ForceNew for all object in the resource.
//
// ## Import
//
// Firewalls can be imported using the firewall `firewall_id:firewall_rule_id`, e.g.
//
// ```sh
//  $ pulumi import civo:index/firewallRule:FirewallRule http b8ecd2ab-2267-4a5e-8692-cbf1d32583e3:4b0022ee-00b2-4f81-a40d-b4f8728923a7
// ```
type FirewallRule struct {
	pulumi.CustomResourceState

	// the IP address of the other end (i.e. not your instance) to affect, or a valid network CIDR (defaults to being globally applied, i.e. 0.0.0.0/0).
	Cidrs pulumi.StringArrayOutput `pulumi:"cidrs"`
	// will this rule affect ingress traffic
	Direction pulumi.StringOutput `pulumi:"direction"`
	// The end port where traffic to be allowed.
	EndPort pulumi.StringOutput `pulumi:"endPort"`
	// The Firewall id
	FirewallId pulumi.StringOutput `pulumi:"firewallId"`
	// a string that will be the displayed name/reference for this rule (optional)
	Label pulumi.StringOutput `pulumi:"label"`
	// This may be one of "tcp", "udp", or "icmp".
	Protocol pulumi.StringOutput `pulumi:"protocol"`
	// The region for this rule
	Region pulumi.StringOutput `pulumi:"region"`
	// The start port where traffic to be allowed.
	StartPort pulumi.StringOutput `pulumi:"startPort"`
}

// NewFirewallRule registers a new resource with the given unique name, arguments, and options.
func NewFirewallRule(ctx *pulumi.Context,
	name string, args *FirewallRuleArgs, opts ...pulumi.ResourceOption) (*FirewallRule, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.FirewallId == nil {
		return nil, errors.New("invalid value for required argument 'FirewallId'")
	}
	var resource FirewallRule
	err := ctx.RegisterResource("civo:index/firewallRule:FirewallRule", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFirewallRule gets an existing FirewallRule resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFirewallRule(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FirewallRuleState, opts ...pulumi.ResourceOption) (*FirewallRule, error) {
	var resource FirewallRule
	err := ctx.ReadResource("civo:index/firewallRule:FirewallRule", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering FirewallRule resources.
type firewallRuleState struct {
	// the IP address of the other end (i.e. not your instance) to affect, or a valid network CIDR (defaults to being globally applied, i.e. 0.0.0.0/0).
	Cidrs []string `pulumi:"cidrs"`
	// will this rule affect ingress traffic
	Direction *string `pulumi:"direction"`
	// The end port where traffic to be allowed.
	EndPort *string `pulumi:"endPort"`
	// The Firewall id
	FirewallId *string `pulumi:"firewallId"`
	// a string that will be the displayed name/reference for this rule (optional)
	Label *string `pulumi:"label"`
	// This may be one of "tcp", "udp", or "icmp".
	Protocol *string `pulumi:"protocol"`
	// The region for this rule
	Region *string `pulumi:"region"`
	// The start port where traffic to be allowed.
	StartPort *string `pulumi:"startPort"`
}

type FirewallRuleState struct {
	// the IP address of the other end (i.e. not your instance) to affect, or a valid network CIDR (defaults to being globally applied, i.e. 0.0.0.0/0).
	Cidrs pulumi.StringArrayInput
	// will this rule affect ingress traffic
	Direction pulumi.StringPtrInput
	// The end port where traffic to be allowed.
	EndPort pulumi.StringPtrInput
	// The Firewall id
	FirewallId pulumi.StringPtrInput
	// a string that will be the displayed name/reference for this rule (optional)
	Label pulumi.StringPtrInput
	// This may be one of "tcp", "udp", or "icmp".
	Protocol pulumi.StringPtrInput
	// The region for this rule
	Region pulumi.StringPtrInput
	// The start port where traffic to be allowed.
	StartPort pulumi.StringPtrInput
}

func (FirewallRuleState) ElementType() reflect.Type {
	return reflect.TypeOf((*firewallRuleState)(nil)).Elem()
}

type firewallRuleArgs struct {
	// the IP address of the other end (i.e. not your instance) to affect, or a valid network CIDR (defaults to being globally applied, i.e. 0.0.0.0/0).
	Cidrs []string `pulumi:"cidrs"`
	// will this rule affect ingress traffic
	Direction *string `pulumi:"direction"`
	// The end port where traffic to be allowed.
	EndPort *string `pulumi:"endPort"`
	// The Firewall id
	FirewallId string `pulumi:"firewallId"`
	// a string that will be the displayed name/reference for this rule (optional)
	Label *string `pulumi:"label"`
	// This may be one of "tcp", "udp", or "icmp".
	Protocol *string `pulumi:"protocol"`
	// The region for this rule
	Region *string `pulumi:"region"`
	// The start port where traffic to be allowed.
	StartPort *string `pulumi:"startPort"`
}

// The set of arguments for constructing a FirewallRule resource.
type FirewallRuleArgs struct {
	// the IP address of the other end (i.e. not your instance) to affect, or a valid network CIDR (defaults to being globally applied, i.e. 0.0.0.0/0).
	Cidrs pulumi.StringArrayInput
	// will this rule affect ingress traffic
	Direction pulumi.StringPtrInput
	// The end port where traffic to be allowed.
	EndPort pulumi.StringPtrInput
	// The Firewall id
	FirewallId pulumi.StringInput
	// a string that will be the displayed name/reference for this rule (optional)
	Label pulumi.StringPtrInput
	// This may be one of "tcp", "udp", or "icmp".
	Protocol pulumi.StringPtrInput
	// The region for this rule
	Region pulumi.StringPtrInput
	// The start port where traffic to be allowed.
	StartPort pulumi.StringPtrInput
}

func (FirewallRuleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*firewallRuleArgs)(nil)).Elem()
}

type FirewallRuleInput interface {
	pulumi.Input

	ToFirewallRuleOutput() FirewallRuleOutput
	ToFirewallRuleOutputWithContext(ctx context.Context) FirewallRuleOutput
}

func (*FirewallRule) ElementType() reflect.Type {
	return reflect.TypeOf((*FirewallRule)(nil))
}

func (i *FirewallRule) ToFirewallRuleOutput() FirewallRuleOutput {
	return i.ToFirewallRuleOutputWithContext(context.Background())
}

func (i *FirewallRule) ToFirewallRuleOutputWithContext(ctx context.Context) FirewallRuleOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FirewallRuleOutput)
}

func (i *FirewallRule) ToFirewallRulePtrOutput() FirewallRulePtrOutput {
	return i.ToFirewallRulePtrOutputWithContext(context.Background())
}

func (i *FirewallRule) ToFirewallRulePtrOutputWithContext(ctx context.Context) FirewallRulePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FirewallRulePtrOutput)
}

type FirewallRulePtrInput interface {
	pulumi.Input

	ToFirewallRulePtrOutput() FirewallRulePtrOutput
	ToFirewallRulePtrOutputWithContext(ctx context.Context) FirewallRulePtrOutput
}

type firewallRulePtrType FirewallRuleArgs

func (*firewallRulePtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**FirewallRule)(nil))
}

func (i *firewallRulePtrType) ToFirewallRulePtrOutput() FirewallRulePtrOutput {
	return i.ToFirewallRulePtrOutputWithContext(context.Background())
}

func (i *firewallRulePtrType) ToFirewallRulePtrOutputWithContext(ctx context.Context) FirewallRulePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FirewallRulePtrOutput)
}

// FirewallRuleArrayInput is an input type that accepts FirewallRuleArray and FirewallRuleArrayOutput values.
// You can construct a concrete instance of `FirewallRuleArrayInput` via:
//
//          FirewallRuleArray{ FirewallRuleArgs{...} }
type FirewallRuleArrayInput interface {
	pulumi.Input

	ToFirewallRuleArrayOutput() FirewallRuleArrayOutput
	ToFirewallRuleArrayOutputWithContext(context.Context) FirewallRuleArrayOutput
}

type FirewallRuleArray []FirewallRuleInput

func (FirewallRuleArray) ElementType() reflect.Type {
	return reflect.TypeOf(([]*FirewallRule)(nil))
}

func (i FirewallRuleArray) ToFirewallRuleArrayOutput() FirewallRuleArrayOutput {
	return i.ToFirewallRuleArrayOutputWithContext(context.Background())
}

func (i FirewallRuleArray) ToFirewallRuleArrayOutputWithContext(ctx context.Context) FirewallRuleArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FirewallRuleArrayOutput)
}

// FirewallRuleMapInput is an input type that accepts FirewallRuleMap and FirewallRuleMapOutput values.
// You can construct a concrete instance of `FirewallRuleMapInput` via:
//
//          FirewallRuleMap{ "key": FirewallRuleArgs{...} }
type FirewallRuleMapInput interface {
	pulumi.Input

	ToFirewallRuleMapOutput() FirewallRuleMapOutput
	ToFirewallRuleMapOutputWithContext(context.Context) FirewallRuleMapOutput
}

type FirewallRuleMap map[string]FirewallRuleInput

func (FirewallRuleMap) ElementType() reflect.Type {
	return reflect.TypeOf((map[string]*FirewallRule)(nil))
}

func (i FirewallRuleMap) ToFirewallRuleMapOutput() FirewallRuleMapOutput {
	return i.ToFirewallRuleMapOutputWithContext(context.Background())
}

func (i FirewallRuleMap) ToFirewallRuleMapOutputWithContext(ctx context.Context) FirewallRuleMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FirewallRuleMapOutput)
}

type FirewallRuleOutput struct {
	*pulumi.OutputState
}

func (FirewallRuleOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*FirewallRule)(nil))
}

func (o FirewallRuleOutput) ToFirewallRuleOutput() FirewallRuleOutput {
	return o
}

func (o FirewallRuleOutput) ToFirewallRuleOutputWithContext(ctx context.Context) FirewallRuleOutput {
	return o
}

func (o FirewallRuleOutput) ToFirewallRulePtrOutput() FirewallRulePtrOutput {
	return o.ToFirewallRulePtrOutputWithContext(context.Background())
}

func (o FirewallRuleOutput) ToFirewallRulePtrOutputWithContext(ctx context.Context) FirewallRulePtrOutput {
	return o.ApplyT(func(v FirewallRule) *FirewallRule {
		return &v
	}).(FirewallRulePtrOutput)
}

type FirewallRulePtrOutput struct {
	*pulumi.OutputState
}

func (FirewallRulePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**FirewallRule)(nil))
}

func (o FirewallRulePtrOutput) ToFirewallRulePtrOutput() FirewallRulePtrOutput {
	return o
}

func (o FirewallRulePtrOutput) ToFirewallRulePtrOutputWithContext(ctx context.Context) FirewallRulePtrOutput {
	return o
}

type FirewallRuleArrayOutput struct{ *pulumi.OutputState }

func (FirewallRuleArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]FirewallRule)(nil))
}

func (o FirewallRuleArrayOutput) ToFirewallRuleArrayOutput() FirewallRuleArrayOutput {
	return o
}

func (o FirewallRuleArrayOutput) ToFirewallRuleArrayOutputWithContext(ctx context.Context) FirewallRuleArrayOutput {
	return o
}

func (o FirewallRuleArrayOutput) Index(i pulumi.IntInput) FirewallRuleOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) FirewallRule {
		return vs[0].([]FirewallRule)[vs[1].(int)]
	}).(FirewallRuleOutput)
}

type FirewallRuleMapOutput struct{ *pulumi.OutputState }

func (FirewallRuleMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]FirewallRule)(nil))
}

func (o FirewallRuleMapOutput) ToFirewallRuleMapOutput() FirewallRuleMapOutput {
	return o
}

func (o FirewallRuleMapOutput) ToFirewallRuleMapOutputWithContext(ctx context.Context) FirewallRuleMapOutput {
	return o
}

func (o FirewallRuleMapOutput) MapIndex(k pulumi.StringInput) FirewallRuleOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) FirewallRule {
		return vs[0].(map[string]FirewallRule)[vs[1].(string)]
	}).(FirewallRuleOutput)
}

func init() {
	pulumi.RegisterOutputType(FirewallRuleOutput{})
	pulumi.RegisterOutputType(FirewallRulePtrOutput{})
	pulumi.RegisterOutputType(FirewallRuleArrayOutput{})
	pulumi.RegisterOutputType(FirewallRuleMapOutput{})
}

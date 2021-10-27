// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides a Civo firewall rule resource. This can be used to create, modify, and delete firewalls rules. This resource don't have an update option because Civo backend doesn't support it at this moment. In that case, we use `ForceNew` for all object in the resource.
//
// ## Schema
//
// ### Required
//
// - **cidr** (Set of String) The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32 to open just for a specific IP address)
// - **firewall_id** (String) The Firewall ID
//
// ### Optional
//
// - **direction** (String) Will this rule affect ingress traffic (only `ingress` is supported now)
// - **end_port** (String) The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
// - **label** (String) A string that will be the displayed name/reference for this rule
// - **protocol** (String) The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
// - **region** (String) The region for this rule
// - **start_port** (String) The start of the port range to configure for this rule (or the single port if required)
//
// ### Read-Only
//
// - **id** (String) The ID of this resource.
//
// ## Import
//
// Import is supported using the following syntax# using firewall_id:firewall_rule_id
//
// ```sh
//  $ pulumi import civo:index/firewallRule:FirewallRule http b8ecd2ab-2267-4a5e-8692-cbf1d32583e3:4b0022ee-00b2-4f81-a40d-b4f8728923a7
// ```
type FirewallRule struct {
	pulumi.CustomResourceState

	// The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32
	// to open just for a specific IP address)
	Cidrs pulumi.StringArrayOutput `pulumi:"cidrs"`
	// Will this rule affect ingress traffic (only `ingress` is supported now)
	Direction pulumi.StringOutput `pulumi:"direction"`
	// The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
	EndPort pulumi.StringOutput `pulumi:"endPort"`
	// The Firewall ID
	FirewallId pulumi.StringOutput `pulumi:"firewallId"`
	// The ID of this resource.
	Id pulumi.StringOutput `pulumi:"id"`
	// A string that will be the displayed name/reference for this rule
	Label pulumi.StringOutput `pulumi:"label"`
	// The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
	Protocol pulumi.StringOutput `pulumi:"protocol"`
	// The region for this rule
	Region pulumi.StringOutput `pulumi:"region"`
	// The start of the port range to configure for this rule (or the single port if required)
	StartPort pulumi.StringOutput `pulumi:"startPort"`
}

// NewFirewallRule registers a new resource with the given unique name, arguments, and options.
func NewFirewallRule(ctx *pulumi.Context,
	name string, args *FirewallRuleArgs, opts ...pulumi.ResourceOption) (*FirewallRule, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Cidrs == nil {
		return nil, errors.New("invalid value for required argument 'Cidrs'")
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
	// The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32
	// to open just for a specific IP address)
	Cidrs []string `pulumi:"cidrs"`
	// Will this rule affect ingress traffic (only `ingress` is supported now)
	Direction *string `pulumi:"direction"`
	// The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
	EndPort *string `pulumi:"endPort"`
	// The Firewall ID
	FirewallId *string `pulumi:"firewallId"`
	// The ID of this resource.
	Id *string `pulumi:"id"`
	// A string that will be the displayed name/reference for this rule
	Label *string `pulumi:"label"`
	// The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
	Protocol *string `pulumi:"protocol"`
	// The region for this rule
	Region *string `pulumi:"region"`
	// The start of the port range to configure for this rule (or the single port if required)
	StartPort *string `pulumi:"startPort"`
}

type FirewallRuleState struct {
	// The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32
	// to open just for a specific IP address)
	Cidrs pulumi.StringArrayInput
	// Will this rule affect ingress traffic (only `ingress` is supported now)
	Direction pulumi.StringPtrInput
	// The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
	EndPort pulumi.StringPtrInput
	// The Firewall ID
	FirewallId pulumi.StringPtrInput
	// The ID of this resource.
	Id pulumi.StringPtrInput
	// A string that will be the displayed name/reference for this rule
	Label pulumi.StringPtrInput
	// The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
	Protocol pulumi.StringPtrInput
	// The region for this rule
	Region pulumi.StringPtrInput
	// The start of the port range to configure for this rule (or the single port if required)
	StartPort pulumi.StringPtrInput
}

func (FirewallRuleState) ElementType() reflect.Type {
	return reflect.TypeOf((*firewallRuleState)(nil)).Elem()
}

type firewallRuleArgs struct {
	// The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32
	// to open just for a specific IP address)
	Cidrs []string `pulumi:"cidrs"`
	// Will this rule affect ingress traffic (only `ingress` is supported now)
	Direction *string `pulumi:"direction"`
	// The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
	EndPort *string `pulumi:"endPort"`
	// The Firewall ID
	FirewallId string `pulumi:"firewallId"`
	// A string that will be the displayed name/reference for this rule
	Label *string `pulumi:"label"`
	// The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
	Protocol *string `pulumi:"protocol"`
	// The region for this rule
	Region *string `pulumi:"region"`
	// The start of the port range to configure for this rule (or the single port if required)
	StartPort *string `pulumi:"startPort"`
}

// The set of arguments for constructing a FirewallRule resource.
type FirewallRuleArgs struct {
	// The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32
	// to open just for a specific IP address)
	Cidrs pulumi.StringArrayInput
	// Will this rule affect ingress traffic (only `ingress` is supported now)
	Direction pulumi.StringPtrInput
	// The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
	EndPort pulumi.StringPtrInput
	// The Firewall ID
	FirewallId pulumi.StringInput
	// A string that will be the displayed name/reference for this rule
	Label pulumi.StringPtrInput
	// The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
	Protocol pulumi.StringPtrInput
	// The region for this rule
	Region pulumi.StringPtrInput
	// The start of the port range to configure for this rule (or the single port if required)
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

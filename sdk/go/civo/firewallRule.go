// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-civo/sdk/v2/go/civo/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides a Civo firewall rule resource. This can be used to create, modify, and delete firewalls rules. This resource don't have an update option because Civo backend doesn't support it at this moment. In that case, we use `ForceNew` for all object in the resource.
//
// ## Import
//
// using firewall_id:firewall_rule_id
//
// ```sh
// $ pulumi import civo:index/firewallRule:FirewallRule http b8ecd2ab-2267-4a5e-8692-cbf1d32583e3:4b0022ee-00b2-4f81-a40d-b4f8728923a7
// ```
type FirewallRule struct {
	pulumi.CustomResourceState

	// The action of the rule can be allow or deny. When we set the `action = 'allow'`, this is going to add a rule to allow traffic. Similarly, setting `action = 'deny'` will deny the traffic.
	Action pulumi.StringOutput `pulumi:"action"`
	// The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32 to open just for a specific IP address)
	Cidrs pulumi.StringArrayOutput `pulumi:"cidrs"`
	// The direction of the rule can be ingress or egress
	Direction pulumi.StringOutput `pulumi:"direction"`
	// The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
	EndPort pulumi.StringOutput `pulumi:"endPort"`
	// The Firewall ID
	FirewallId pulumi.StringOutput `pulumi:"firewallId"`
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

	if args.Action == nil {
		return nil, errors.New("invalid value for required argument 'Action'")
	}
	if args.Cidrs == nil {
		return nil, errors.New("invalid value for required argument 'Cidrs'")
	}
	if args.Direction == nil {
		return nil, errors.New("invalid value for required argument 'Direction'")
	}
	if args.FirewallId == nil {
		return nil, errors.New("invalid value for required argument 'FirewallId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
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
	// The action of the rule can be allow or deny. When we set the `action = 'allow'`, this is going to add a rule to allow traffic. Similarly, setting `action = 'deny'` will deny the traffic.
	Action *string `pulumi:"action"`
	// The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32 to open just for a specific IP address)
	Cidrs []string `pulumi:"cidrs"`
	// The direction of the rule can be ingress or egress
	Direction *string `pulumi:"direction"`
	// The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
	EndPort *string `pulumi:"endPort"`
	// The Firewall ID
	FirewallId *string `pulumi:"firewallId"`
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
	// The action of the rule can be allow or deny. When we set the `action = 'allow'`, this is going to add a rule to allow traffic. Similarly, setting `action = 'deny'` will deny the traffic.
	Action pulumi.StringPtrInput
	// The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32 to open just for a specific IP address)
	Cidrs pulumi.StringArrayInput
	// The direction of the rule can be ingress or egress
	Direction pulumi.StringPtrInput
	// The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
	EndPort pulumi.StringPtrInput
	// The Firewall ID
	FirewallId pulumi.StringPtrInput
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
	// The action of the rule can be allow or deny. When we set the `action = 'allow'`, this is going to add a rule to allow traffic. Similarly, setting `action = 'deny'` will deny the traffic.
	Action string `pulumi:"action"`
	// The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32 to open just for a specific IP address)
	Cidrs []string `pulumi:"cidrs"`
	// The direction of the rule can be ingress or egress
	Direction string `pulumi:"direction"`
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
	// The action of the rule can be allow or deny. When we set the `action = 'allow'`, this is going to add a rule to allow traffic. Similarly, setting `action = 'deny'` will deny the traffic.
	Action pulumi.StringInput
	// The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32 to open just for a specific IP address)
	Cidrs pulumi.StringArrayInput
	// The direction of the rule can be ingress or egress
	Direction pulumi.StringInput
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
	return reflect.TypeOf((**FirewallRule)(nil)).Elem()
}

func (i *FirewallRule) ToFirewallRuleOutput() FirewallRuleOutput {
	return i.ToFirewallRuleOutputWithContext(context.Background())
}

func (i *FirewallRule) ToFirewallRuleOutputWithContext(ctx context.Context) FirewallRuleOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FirewallRuleOutput)
}

// FirewallRuleArrayInput is an input type that accepts FirewallRuleArray and FirewallRuleArrayOutput values.
// You can construct a concrete instance of `FirewallRuleArrayInput` via:
//
//	FirewallRuleArray{ FirewallRuleArgs{...} }
type FirewallRuleArrayInput interface {
	pulumi.Input

	ToFirewallRuleArrayOutput() FirewallRuleArrayOutput
	ToFirewallRuleArrayOutputWithContext(context.Context) FirewallRuleArrayOutput
}

type FirewallRuleArray []FirewallRuleInput

func (FirewallRuleArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*FirewallRule)(nil)).Elem()
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
//	FirewallRuleMap{ "key": FirewallRuleArgs{...} }
type FirewallRuleMapInput interface {
	pulumi.Input

	ToFirewallRuleMapOutput() FirewallRuleMapOutput
	ToFirewallRuleMapOutputWithContext(context.Context) FirewallRuleMapOutput
}

type FirewallRuleMap map[string]FirewallRuleInput

func (FirewallRuleMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*FirewallRule)(nil)).Elem()
}

func (i FirewallRuleMap) ToFirewallRuleMapOutput() FirewallRuleMapOutput {
	return i.ToFirewallRuleMapOutputWithContext(context.Background())
}

func (i FirewallRuleMap) ToFirewallRuleMapOutputWithContext(ctx context.Context) FirewallRuleMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FirewallRuleMapOutput)
}

type FirewallRuleOutput struct{ *pulumi.OutputState }

func (FirewallRuleOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**FirewallRule)(nil)).Elem()
}

func (o FirewallRuleOutput) ToFirewallRuleOutput() FirewallRuleOutput {
	return o
}

func (o FirewallRuleOutput) ToFirewallRuleOutputWithContext(ctx context.Context) FirewallRuleOutput {
	return o
}

// The action of the rule can be allow or deny. When we set the `action = 'allow'`, this is going to add a rule to allow traffic. Similarly, setting `action = 'deny'` will deny the traffic.
func (o FirewallRuleOutput) Action() pulumi.StringOutput {
	return o.ApplyT(func(v *FirewallRule) pulumi.StringOutput { return v.Action }).(pulumi.StringOutput)
}

// The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32 to open just for a specific IP address)
func (o FirewallRuleOutput) Cidrs() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *FirewallRule) pulumi.StringArrayOutput { return v.Cidrs }).(pulumi.StringArrayOutput)
}

// The direction of the rule can be ingress or egress
func (o FirewallRuleOutput) Direction() pulumi.StringOutput {
	return o.ApplyT(func(v *FirewallRule) pulumi.StringOutput { return v.Direction }).(pulumi.StringOutput)
}

// The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
func (o FirewallRuleOutput) EndPort() pulumi.StringOutput {
	return o.ApplyT(func(v *FirewallRule) pulumi.StringOutput { return v.EndPort }).(pulumi.StringOutput)
}

// The Firewall ID
func (o FirewallRuleOutput) FirewallId() pulumi.StringOutput {
	return o.ApplyT(func(v *FirewallRule) pulumi.StringOutput { return v.FirewallId }).(pulumi.StringOutput)
}

// A string that will be the displayed name/reference for this rule
func (o FirewallRuleOutput) Label() pulumi.StringOutput {
	return o.ApplyT(func(v *FirewallRule) pulumi.StringOutput { return v.Label }).(pulumi.StringOutput)
}

// The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
func (o FirewallRuleOutput) Protocol() pulumi.StringOutput {
	return o.ApplyT(func(v *FirewallRule) pulumi.StringOutput { return v.Protocol }).(pulumi.StringOutput)
}

// The region for this rule
func (o FirewallRuleOutput) Region() pulumi.StringOutput {
	return o.ApplyT(func(v *FirewallRule) pulumi.StringOutput { return v.Region }).(pulumi.StringOutput)
}

// The start of the port range to configure for this rule (or the single port if required)
func (o FirewallRuleOutput) StartPort() pulumi.StringOutput {
	return o.ApplyT(func(v *FirewallRule) pulumi.StringOutput { return v.StartPort }).(pulumi.StringOutput)
}

type FirewallRuleArrayOutput struct{ *pulumi.OutputState }

func (FirewallRuleArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*FirewallRule)(nil)).Elem()
}

func (o FirewallRuleArrayOutput) ToFirewallRuleArrayOutput() FirewallRuleArrayOutput {
	return o
}

func (o FirewallRuleArrayOutput) ToFirewallRuleArrayOutputWithContext(ctx context.Context) FirewallRuleArrayOutput {
	return o
}

func (o FirewallRuleArrayOutput) Index(i pulumi.IntInput) FirewallRuleOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *FirewallRule {
		return vs[0].([]*FirewallRule)[vs[1].(int)]
	}).(FirewallRuleOutput)
}

type FirewallRuleMapOutput struct{ *pulumi.OutputState }

func (FirewallRuleMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*FirewallRule)(nil)).Elem()
}

func (o FirewallRuleMapOutput) ToFirewallRuleMapOutput() FirewallRuleMapOutput {
	return o
}

func (o FirewallRuleMapOutput) ToFirewallRuleMapOutputWithContext(ctx context.Context) FirewallRuleMapOutput {
	return o
}

func (o FirewallRuleMapOutput) MapIndex(k pulumi.StringInput) FirewallRuleOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *FirewallRule {
		return vs[0].(map[string]*FirewallRule)[vs[1].(string)]
	}).(FirewallRuleOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*FirewallRuleInput)(nil)).Elem(), &FirewallRule{})
	pulumi.RegisterInputType(reflect.TypeOf((*FirewallRuleArrayInput)(nil)).Elem(), FirewallRuleArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*FirewallRuleMapInput)(nil)).Elem(), FirewallRuleMap{})
	pulumi.RegisterOutputType(FirewallRuleOutput{})
	pulumi.RegisterOutputType(FirewallRuleArrayOutput{})
	pulumi.RegisterOutputType(FirewallRuleMapOutput{})
}

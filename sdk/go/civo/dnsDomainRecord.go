// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides a Civo DNS domain record resource.
//
// ## Import
//
// # using domain_id:domain_record_id
//
// ```sh
//  $ pulumi import civo:index/dnsDomainRecord:DnsDomainRecord www a3cd6832-9577-4017-afd7-17d239fc0bf0:c9a39d14-ee1b-4870-8fb0-a2d4f465e822
// ```
type DnsDomainRecord struct {
	pulumi.CustomResourceState

	// The account ID of this resource
	AccountId pulumi.StringOutput `pulumi:"accountId"`
	// Timestamp when this resource was created
	CreatedAt pulumi.StringOutput `pulumi:"createdAt"`
	// ID from domain name
	DomainId pulumi.StringOutput `pulumi:"domainId"`
	// The portion before the domain name (e.g. www) or an @ for the apex/root domain (you cannot use an A record with an amex/root domain)
	Name pulumi.StringOutput `pulumi:"name"`
	// Useful for MX records only, the priority mail should be attempted it (defaults to 10)
	Priority pulumi.IntPtrOutput `pulumi:"priority"`
	// How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified is 600)
	Ttl pulumi.IntOutput `pulumi:"ttl"`
	// The choice of RR type from a, cname, mx or txt
	Type pulumi.StringOutput `pulumi:"type"`
	// Timestamp when this resource was updated
	UpdatedAt pulumi.StringOutput `pulumi:"updatedAt"`
	// The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record
	Value pulumi.StringOutput `pulumi:"value"`
}

// NewDnsDomainRecord registers a new resource with the given unique name, arguments, and options.
func NewDnsDomainRecord(ctx *pulumi.Context,
	name string, args *DnsDomainRecordArgs, opts ...pulumi.ResourceOption) (*DnsDomainRecord, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DomainId == nil {
		return nil, errors.New("invalid value for required argument 'DomainId'")
	}
	if args.Ttl == nil {
		return nil, errors.New("invalid value for required argument 'Ttl'")
	}
	if args.Type == nil {
		return nil, errors.New("invalid value for required argument 'Type'")
	}
	if args.Value == nil {
		return nil, errors.New("invalid value for required argument 'Value'")
	}
	var resource DnsDomainRecord
	err := ctx.RegisterResource("civo:index/dnsDomainRecord:DnsDomainRecord", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDnsDomainRecord gets an existing DnsDomainRecord resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDnsDomainRecord(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DnsDomainRecordState, opts ...pulumi.ResourceOption) (*DnsDomainRecord, error) {
	var resource DnsDomainRecord
	err := ctx.ReadResource("civo:index/dnsDomainRecord:DnsDomainRecord", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DnsDomainRecord resources.
type dnsDomainRecordState struct {
	// The account ID of this resource
	AccountId *string `pulumi:"accountId"`
	// Timestamp when this resource was created
	CreatedAt *string `pulumi:"createdAt"`
	// ID from domain name
	DomainId *string `pulumi:"domainId"`
	// The portion before the domain name (e.g. www) or an @ for the apex/root domain (you cannot use an A record with an amex/root domain)
	Name *string `pulumi:"name"`
	// Useful for MX records only, the priority mail should be attempted it (defaults to 10)
	Priority *int `pulumi:"priority"`
	// How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified is 600)
	Ttl *int `pulumi:"ttl"`
	// The choice of RR type from a, cname, mx or txt
	Type *string `pulumi:"type"`
	// Timestamp when this resource was updated
	UpdatedAt *string `pulumi:"updatedAt"`
	// The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record
	Value *string `pulumi:"value"`
}

type DnsDomainRecordState struct {
	// The account ID of this resource
	AccountId pulumi.StringPtrInput
	// Timestamp when this resource was created
	CreatedAt pulumi.StringPtrInput
	// ID from domain name
	DomainId pulumi.StringPtrInput
	// The portion before the domain name (e.g. www) or an @ for the apex/root domain (you cannot use an A record with an amex/root domain)
	Name pulumi.StringPtrInput
	// Useful for MX records only, the priority mail should be attempted it (defaults to 10)
	Priority pulumi.IntPtrInput
	// How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified is 600)
	Ttl pulumi.IntPtrInput
	// The choice of RR type from a, cname, mx or txt
	Type pulumi.StringPtrInput
	// Timestamp when this resource was updated
	UpdatedAt pulumi.StringPtrInput
	// The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record
	Value pulumi.StringPtrInput
}

func (DnsDomainRecordState) ElementType() reflect.Type {
	return reflect.TypeOf((*dnsDomainRecordState)(nil)).Elem()
}

type dnsDomainRecordArgs struct {
	// ID from domain name
	DomainId string `pulumi:"domainId"`
	// The portion before the domain name (e.g. www) or an @ for the apex/root domain (you cannot use an A record with an amex/root domain)
	Name *string `pulumi:"name"`
	// Useful for MX records only, the priority mail should be attempted it (defaults to 10)
	Priority *int `pulumi:"priority"`
	// How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified is 600)
	Ttl int `pulumi:"ttl"`
	// The choice of RR type from a, cname, mx or txt
	Type string `pulumi:"type"`
	// The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record
	Value string `pulumi:"value"`
}

// The set of arguments for constructing a DnsDomainRecord resource.
type DnsDomainRecordArgs struct {
	// ID from domain name
	DomainId pulumi.StringInput
	// The portion before the domain name (e.g. www) or an @ for the apex/root domain (you cannot use an A record with an amex/root domain)
	Name pulumi.StringPtrInput
	// Useful for MX records only, the priority mail should be attempted it (defaults to 10)
	Priority pulumi.IntPtrInput
	// How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified is 600)
	Ttl pulumi.IntInput
	// The choice of RR type from a, cname, mx or txt
	Type pulumi.StringInput
	// The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record
	Value pulumi.StringInput
}

func (DnsDomainRecordArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*dnsDomainRecordArgs)(nil)).Elem()
}

type DnsDomainRecordInput interface {
	pulumi.Input

	ToDnsDomainRecordOutput() DnsDomainRecordOutput
	ToDnsDomainRecordOutputWithContext(ctx context.Context) DnsDomainRecordOutput
}

func (*DnsDomainRecord) ElementType() reflect.Type {
	return reflect.TypeOf((**DnsDomainRecord)(nil)).Elem()
}

func (i *DnsDomainRecord) ToDnsDomainRecordOutput() DnsDomainRecordOutput {
	return i.ToDnsDomainRecordOutputWithContext(context.Background())
}

func (i *DnsDomainRecord) ToDnsDomainRecordOutputWithContext(ctx context.Context) DnsDomainRecordOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DnsDomainRecordOutput)
}

// DnsDomainRecordArrayInput is an input type that accepts DnsDomainRecordArray and DnsDomainRecordArrayOutput values.
// You can construct a concrete instance of `DnsDomainRecordArrayInput` via:
//
//          DnsDomainRecordArray{ DnsDomainRecordArgs{...} }
type DnsDomainRecordArrayInput interface {
	pulumi.Input

	ToDnsDomainRecordArrayOutput() DnsDomainRecordArrayOutput
	ToDnsDomainRecordArrayOutputWithContext(context.Context) DnsDomainRecordArrayOutput
}

type DnsDomainRecordArray []DnsDomainRecordInput

func (DnsDomainRecordArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*DnsDomainRecord)(nil)).Elem()
}

func (i DnsDomainRecordArray) ToDnsDomainRecordArrayOutput() DnsDomainRecordArrayOutput {
	return i.ToDnsDomainRecordArrayOutputWithContext(context.Background())
}

func (i DnsDomainRecordArray) ToDnsDomainRecordArrayOutputWithContext(ctx context.Context) DnsDomainRecordArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DnsDomainRecordArrayOutput)
}

// DnsDomainRecordMapInput is an input type that accepts DnsDomainRecordMap and DnsDomainRecordMapOutput values.
// You can construct a concrete instance of `DnsDomainRecordMapInput` via:
//
//          DnsDomainRecordMap{ "key": DnsDomainRecordArgs{...} }
type DnsDomainRecordMapInput interface {
	pulumi.Input

	ToDnsDomainRecordMapOutput() DnsDomainRecordMapOutput
	ToDnsDomainRecordMapOutputWithContext(context.Context) DnsDomainRecordMapOutput
}

type DnsDomainRecordMap map[string]DnsDomainRecordInput

func (DnsDomainRecordMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*DnsDomainRecord)(nil)).Elem()
}

func (i DnsDomainRecordMap) ToDnsDomainRecordMapOutput() DnsDomainRecordMapOutput {
	return i.ToDnsDomainRecordMapOutputWithContext(context.Background())
}

func (i DnsDomainRecordMap) ToDnsDomainRecordMapOutputWithContext(ctx context.Context) DnsDomainRecordMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DnsDomainRecordMapOutput)
}

type DnsDomainRecordOutput struct{ *pulumi.OutputState }

func (DnsDomainRecordOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DnsDomainRecord)(nil)).Elem()
}

func (o DnsDomainRecordOutput) ToDnsDomainRecordOutput() DnsDomainRecordOutput {
	return o
}

func (o DnsDomainRecordOutput) ToDnsDomainRecordOutputWithContext(ctx context.Context) DnsDomainRecordOutput {
	return o
}

// The account ID of this resource
func (o DnsDomainRecordOutput) AccountId() pulumi.StringOutput {
	return o.ApplyT(func(v *DnsDomainRecord) pulumi.StringOutput { return v.AccountId }).(pulumi.StringOutput)
}

// Timestamp when this resource was created
func (o DnsDomainRecordOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *DnsDomainRecord) pulumi.StringOutput { return v.CreatedAt }).(pulumi.StringOutput)
}

// ID from domain name
func (o DnsDomainRecordOutput) DomainId() pulumi.StringOutput {
	return o.ApplyT(func(v *DnsDomainRecord) pulumi.StringOutput { return v.DomainId }).(pulumi.StringOutput)
}

// The portion before the domain name (e.g. www) or an @ for the apex/root domain (you cannot use an A record with an amex/root domain)
func (o DnsDomainRecordOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *DnsDomainRecord) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Useful for MX records only, the priority mail should be attempted it (defaults to 10)
func (o DnsDomainRecordOutput) Priority() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *DnsDomainRecord) pulumi.IntPtrOutput { return v.Priority }).(pulumi.IntPtrOutput)
}

// How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified is 600)
func (o DnsDomainRecordOutput) Ttl() pulumi.IntOutput {
	return o.ApplyT(func(v *DnsDomainRecord) pulumi.IntOutput { return v.Ttl }).(pulumi.IntOutput)
}

// The choice of RR type from a, cname, mx or txt
func (o DnsDomainRecordOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v *DnsDomainRecord) pulumi.StringOutput { return v.Type }).(pulumi.StringOutput)
}

// Timestamp when this resource was updated
func (o DnsDomainRecordOutput) UpdatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *DnsDomainRecord) pulumi.StringOutput { return v.UpdatedAt }).(pulumi.StringOutput)
}

// The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record
func (o DnsDomainRecordOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v *DnsDomainRecord) pulumi.StringOutput { return v.Value }).(pulumi.StringOutput)
}

type DnsDomainRecordArrayOutput struct{ *pulumi.OutputState }

func (DnsDomainRecordArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*DnsDomainRecord)(nil)).Elem()
}

func (o DnsDomainRecordArrayOutput) ToDnsDomainRecordArrayOutput() DnsDomainRecordArrayOutput {
	return o
}

func (o DnsDomainRecordArrayOutput) ToDnsDomainRecordArrayOutputWithContext(ctx context.Context) DnsDomainRecordArrayOutput {
	return o
}

func (o DnsDomainRecordArrayOutput) Index(i pulumi.IntInput) DnsDomainRecordOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *DnsDomainRecord {
		return vs[0].([]*DnsDomainRecord)[vs[1].(int)]
	}).(DnsDomainRecordOutput)
}

type DnsDomainRecordMapOutput struct{ *pulumi.OutputState }

func (DnsDomainRecordMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*DnsDomainRecord)(nil)).Elem()
}

func (o DnsDomainRecordMapOutput) ToDnsDomainRecordMapOutput() DnsDomainRecordMapOutput {
	return o
}

func (o DnsDomainRecordMapOutput) ToDnsDomainRecordMapOutputWithContext(ctx context.Context) DnsDomainRecordMapOutput {
	return o
}

func (o DnsDomainRecordMapOutput) MapIndex(k pulumi.StringInput) DnsDomainRecordOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *DnsDomainRecord {
		return vs[0].(map[string]*DnsDomainRecord)[vs[1].(string)]
	}).(DnsDomainRecordOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DnsDomainRecordInput)(nil)).Elem(), &DnsDomainRecord{})
	pulumi.RegisterInputType(reflect.TypeOf((*DnsDomainRecordArrayInput)(nil)).Elem(), DnsDomainRecordArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*DnsDomainRecordMapInput)(nil)).Elem(), DnsDomainRecordMap{})
	pulumi.RegisterOutputType(DnsDomainRecordOutput{})
	pulumi.RegisterOutputType(DnsDomainRecordArrayOutput{})
	pulumi.RegisterOutputType(DnsDomainRecordMapOutput{})
}

// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-civo/sdk/v2/go/civo/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Get information on a DNS record. This data source provides the name, TTL, and zone file as configured on your Civo account.
//
// An error will be raised if the provided domain name or record are not in your Civo account.
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
//			domain, err := civo.LookupDnsDomainName(ctx, &civo.LookupDnsDomainNameArgs{
//				Name: pulumi.StringRef("domain.com"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			www, err := civo.LookupDnsDomainRecord(ctx, &civo.LookupDnsDomainRecordArgs{
//				DomainId: domain.Id,
//				Name:     "www",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			ctx.Export("recordType", www.Type)
//			ctx.Export("recordTtl", www.Ttl)
//			return nil
//		})
//	}
//
// ```
func LookupDnsDomainRecord(ctx *pulumi.Context, args *LookupDnsDomainRecordArgs, opts ...pulumi.InvokeOption) (*LookupDnsDomainRecordResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupDnsDomainRecordResult
	err := ctx.Invoke("civo:index/getDnsDomainRecord:getDnsDomainRecord", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getDnsDomainRecord.
type LookupDnsDomainRecordArgs struct {
	// The ID of the domain
	DomainId string `pulumi:"domainId"`
	// The name of the record
	Name string `pulumi:"name"`
}

// A collection of values returned by getDnsDomainRecord.
type LookupDnsDomainRecordResult struct {
	// The ID account of the domain
	AccountId string `pulumi:"accountId"`
	// The date when it was created in UTC format
	CreatedAt string `pulumi:"createdAt"`
	// The ID of the domain
	DomainId string `pulumi:"domainId"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The name of the record
	Name string `pulumi:"name"`
	// The priority of the record
	Priority int `pulumi:"priority"`
	// How long caching DNS servers should cache this record
	Ttl int `pulumi:"ttl"`
	// The choice of record type from A, CNAME, MX, SRV or TXT
	Type string `pulumi:"type"`
	// The date when it was updated in UTC format
	UpdatedAt string `pulumi:"updatedAt"`
	// The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record
	Value string `pulumi:"value"`
}

func LookupDnsDomainRecordOutput(ctx *pulumi.Context, args LookupDnsDomainRecordOutputArgs, opts ...pulumi.InvokeOption) LookupDnsDomainRecordResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupDnsDomainRecordResultOutput, error) {
			args := v.(LookupDnsDomainRecordArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("civo:index/getDnsDomainRecord:getDnsDomainRecord", args, LookupDnsDomainRecordResultOutput{}, options).(LookupDnsDomainRecordResultOutput), nil
		}).(LookupDnsDomainRecordResultOutput)
}

// A collection of arguments for invoking getDnsDomainRecord.
type LookupDnsDomainRecordOutputArgs struct {
	// The ID of the domain
	DomainId pulumi.StringInput `pulumi:"domainId"`
	// The name of the record
	Name pulumi.StringInput `pulumi:"name"`
}

func (LookupDnsDomainRecordOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDnsDomainRecordArgs)(nil)).Elem()
}

// A collection of values returned by getDnsDomainRecord.
type LookupDnsDomainRecordResultOutput struct{ *pulumi.OutputState }

func (LookupDnsDomainRecordResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDnsDomainRecordResult)(nil)).Elem()
}

func (o LookupDnsDomainRecordResultOutput) ToLookupDnsDomainRecordResultOutput() LookupDnsDomainRecordResultOutput {
	return o
}

func (o LookupDnsDomainRecordResultOutput) ToLookupDnsDomainRecordResultOutputWithContext(ctx context.Context) LookupDnsDomainRecordResultOutput {
	return o
}

// The ID account of the domain
func (o LookupDnsDomainRecordResultOutput) AccountId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDnsDomainRecordResult) string { return v.AccountId }).(pulumi.StringOutput)
}

// The date when it was created in UTC format
func (o LookupDnsDomainRecordResultOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDnsDomainRecordResult) string { return v.CreatedAt }).(pulumi.StringOutput)
}

// The ID of the domain
func (o LookupDnsDomainRecordResultOutput) DomainId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDnsDomainRecordResult) string { return v.DomainId }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupDnsDomainRecordResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDnsDomainRecordResult) string { return v.Id }).(pulumi.StringOutput)
}

// The name of the record
func (o LookupDnsDomainRecordResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDnsDomainRecordResult) string { return v.Name }).(pulumi.StringOutput)
}

// The priority of the record
func (o LookupDnsDomainRecordResultOutput) Priority() pulumi.IntOutput {
	return o.ApplyT(func(v LookupDnsDomainRecordResult) int { return v.Priority }).(pulumi.IntOutput)
}

// How long caching DNS servers should cache this record
func (o LookupDnsDomainRecordResultOutput) Ttl() pulumi.IntOutput {
	return o.ApplyT(func(v LookupDnsDomainRecordResult) int { return v.Ttl }).(pulumi.IntOutput)
}

// The choice of record type from A, CNAME, MX, SRV or TXT
func (o LookupDnsDomainRecordResultOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDnsDomainRecordResult) string { return v.Type }).(pulumi.StringOutput)
}

// The date when it was updated in UTC format
func (o LookupDnsDomainRecordResultOutput) UpdatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDnsDomainRecordResult) string { return v.UpdatedAt }).(pulumi.StringOutput)
}

// The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record
func (o LookupDnsDomainRecordResultOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDnsDomainRecordResult) string { return v.Value }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDnsDomainRecordResultOutput{})
}

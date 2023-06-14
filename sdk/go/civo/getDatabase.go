// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Get information of an Database for use in other resources. This data source provides all of the Database's properties as configured on your Civo account.
//
// Note: This data source returns a single Database. When specifying a name, an error will be raised if more than one Databases with the same name found.
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
//			_, err := civo.LookupDatabase(ctx, &civo.LookupDatabaseArgs{
//				Name:   pulumi.StringRef("test-database"),
//				Region: pulumi.StringRef("LON1"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupDatabase(ctx *pulumi.Context, args *LookupDatabaseArgs, opts ...pulumi.InvokeOption) (*LookupDatabaseResult, error) {
	var rv LookupDatabaseResult
	err := ctx.Invoke("civo:index/getDatabase:getDatabase", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getDatabase.
type LookupDatabaseArgs struct {
	// The ID of the Database
	Id *string `pulumi:"id"`
	// The name of the Database
	Name *string `pulumi:"name"`
	// The region of an existing Database
	Region *string `pulumi:"region"`
}

// A collection of values returned by getDatabase.
type LookupDatabaseResult struct {
	// The engine of the database
	Engine string `pulumi:"engine"`
	// The firewall id of the Database
	FirewallId string `pulumi:"firewallId"`
	// The ID of the Database
	Id *string `pulumi:"id"`
	// The name of the Database
	Name *string `pulumi:"name"`
	// The network id of the Database
	NetworkId string `pulumi:"networkId"`
	// Count of nodes
	Nodes int `pulumi:"nodes"`
	// The password of the database
	Password string `pulumi:"password"`
	// The region of an existing Database
	Region string `pulumi:"region"`
	// Size of the database
	Size string `pulumi:"size"`
	// The status of the database
	Status string `pulumi:"status"`
	// The username of the database
	Username string `pulumi:"username"`
	// The version of the database
	Version string `pulumi:"version"`
}

func LookupDatabaseOutput(ctx *pulumi.Context, args LookupDatabaseOutputArgs, opts ...pulumi.InvokeOption) LookupDatabaseResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDatabaseResult, error) {
			args := v.(LookupDatabaseArgs)
			r, err := LookupDatabase(ctx, &args, opts...)
			var s LookupDatabaseResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDatabaseResultOutput)
}

// A collection of arguments for invoking getDatabase.
type LookupDatabaseOutputArgs struct {
	// The ID of the Database
	Id pulumi.StringPtrInput `pulumi:"id"`
	// The name of the Database
	Name pulumi.StringPtrInput `pulumi:"name"`
	// The region of an existing Database
	Region pulumi.StringPtrInput `pulumi:"region"`
}

func (LookupDatabaseOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDatabaseArgs)(nil)).Elem()
}

// A collection of values returned by getDatabase.
type LookupDatabaseResultOutput struct{ *pulumi.OutputState }

func (LookupDatabaseResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDatabaseResult)(nil)).Elem()
}

func (o LookupDatabaseResultOutput) ToLookupDatabaseResultOutput() LookupDatabaseResultOutput {
	return o
}

func (o LookupDatabaseResultOutput) ToLookupDatabaseResultOutputWithContext(ctx context.Context) LookupDatabaseResultOutput {
	return o
}

// The engine of the database
func (o LookupDatabaseResultOutput) Engine() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDatabaseResult) string { return v.Engine }).(pulumi.StringOutput)
}

// The firewall id of the Database
func (o LookupDatabaseResultOutput) FirewallId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDatabaseResult) string { return v.FirewallId }).(pulumi.StringOutput)
}

// The ID of the Database
func (o LookupDatabaseResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDatabaseResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// The name of the Database
func (o LookupDatabaseResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDatabaseResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

// The network id of the Database
func (o LookupDatabaseResultOutput) NetworkId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDatabaseResult) string { return v.NetworkId }).(pulumi.StringOutput)
}

// Count of nodes
func (o LookupDatabaseResultOutput) Nodes() pulumi.IntOutput {
	return o.ApplyT(func(v LookupDatabaseResult) int { return v.Nodes }).(pulumi.IntOutput)
}

// The password of the database
func (o LookupDatabaseResultOutput) Password() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDatabaseResult) string { return v.Password }).(pulumi.StringOutput)
}

// The region of an existing Database
func (o LookupDatabaseResultOutput) Region() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDatabaseResult) string { return v.Region }).(pulumi.StringOutput)
}

// Size of the database
func (o LookupDatabaseResultOutput) Size() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDatabaseResult) string { return v.Size }).(pulumi.StringOutput)
}

// The status of the database
func (o LookupDatabaseResultOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDatabaseResult) string { return v.Status }).(pulumi.StringOutput)
}

// The username of the database
func (o LookupDatabaseResultOutput) Username() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDatabaseResult) string { return v.Username }).(pulumi.StringOutput)
}

// The version of the database
func (o LookupDatabaseResultOutput) Version() pulumi.StringOutput {
	return o.ApplyT(func(v LookupDatabaseResult) string { return v.Version }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDatabaseResultOutput{})
}

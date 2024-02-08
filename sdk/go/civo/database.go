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

// ## Import
//
// using ID
//
// ```sh
// $ pulumi import civo:index/database:Database mydb 29fcd1c4-fb61-44c7-b49c-dc7b98e9927e
// ```
type Database struct {
	pulumi.CustomResourceState

	// The DNS endpoint of the database
	DnsEndpoint pulumi.StringOutput `pulumi:"dnsEndpoint"`
	// The endpoint of the database
	Endpoint pulumi.StringOutput `pulumi:"endpoint"`
	// The engine of the database
	Engine pulumi.StringOutput `pulumi:"engine"`
	// The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all)
	FirewallId pulumi.StringOutput `pulumi:"firewallId"`
	// Name of the database
	Name pulumi.StringOutput `pulumi:"name"`
	// The id of the associated network
	NetworkId pulumi.StringOutput `pulumi:"networkId"`
	// Count of nodes
	Nodes pulumi.IntOutput `pulumi:"nodes"`
	// The password of the database
	Password pulumi.StringOutput `pulumi:"password"`
	// The port of the database
	Port pulumi.IntOutput `pulumi:"port"`
	// The region where the database will be created.
	Region pulumi.StringOutput `pulumi:"region"`
	// Size of the database
	Size pulumi.StringOutput `pulumi:"size"`
	// The status of the database
	Status pulumi.StringOutput `pulumi:"status"`
	// The username of the database
	Username pulumi.StringOutput `pulumi:"username"`
	// The version of the database
	Version pulumi.StringOutput `pulumi:"version"`
}

// NewDatabase registers a new resource with the given unique name, arguments, and options.
func NewDatabase(ctx *pulumi.Context,
	name string, args *DatabaseArgs, opts ...pulumi.ResourceOption) (*Database, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Engine == nil {
		return nil, errors.New("invalid value for required argument 'Engine'")
	}
	if args.Nodes == nil {
		return nil, errors.New("invalid value for required argument 'Nodes'")
	}
	if args.Size == nil {
		return nil, errors.New("invalid value for required argument 'Size'")
	}
	if args.Version == nil {
		return nil, errors.New("invalid value for required argument 'Version'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Database
	err := ctx.RegisterResource("civo:index/database:Database", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDatabase gets an existing Database resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDatabase(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DatabaseState, opts ...pulumi.ResourceOption) (*Database, error) {
	var resource Database
	err := ctx.ReadResource("civo:index/database:Database", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Database resources.
type databaseState struct {
	// The DNS endpoint of the database
	DnsEndpoint *string `pulumi:"dnsEndpoint"`
	// The endpoint of the database
	Endpoint *string `pulumi:"endpoint"`
	// The engine of the database
	Engine *string `pulumi:"engine"`
	// The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all)
	FirewallId *string `pulumi:"firewallId"`
	// Name of the database
	Name *string `pulumi:"name"`
	// The id of the associated network
	NetworkId *string `pulumi:"networkId"`
	// Count of nodes
	Nodes *int `pulumi:"nodes"`
	// The password of the database
	Password *string `pulumi:"password"`
	// The port of the database
	Port *int `pulumi:"port"`
	// The region where the database will be created.
	Region *string `pulumi:"region"`
	// Size of the database
	Size *string `pulumi:"size"`
	// The status of the database
	Status *string `pulumi:"status"`
	// The username of the database
	Username *string `pulumi:"username"`
	// The version of the database
	Version *string `pulumi:"version"`
}

type DatabaseState struct {
	// The DNS endpoint of the database
	DnsEndpoint pulumi.StringPtrInput
	// The endpoint of the database
	Endpoint pulumi.StringPtrInput
	// The engine of the database
	Engine pulumi.StringPtrInput
	// The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all)
	FirewallId pulumi.StringPtrInput
	// Name of the database
	Name pulumi.StringPtrInput
	// The id of the associated network
	NetworkId pulumi.StringPtrInput
	// Count of nodes
	Nodes pulumi.IntPtrInput
	// The password of the database
	Password pulumi.StringPtrInput
	// The port of the database
	Port pulumi.IntPtrInput
	// The region where the database will be created.
	Region pulumi.StringPtrInput
	// Size of the database
	Size pulumi.StringPtrInput
	// The status of the database
	Status pulumi.StringPtrInput
	// The username of the database
	Username pulumi.StringPtrInput
	// The version of the database
	Version pulumi.StringPtrInput
}

func (DatabaseState) ElementType() reflect.Type {
	return reflect.TypeOf((*databaseState)(nil)).Elem()
}

type databaseArgs struct {
	// The engine of the database
	Engine string `pulumi:"engine"`
	// The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all)
	FirewallId *string `pulumi:"firewallId"`
	// Name of the database
	Name *string `pulumi:"name"`
	// The id of the associated network
	NetworkId *string `pulumi:"networkId"`
	// Count of nodes
	Nodes int `pulumi:"nodes"`
	// The region where the database will be created.
	Region *string `pulumi:"region"`
	// Size of the database
	Size string `pulumi:"size"`
	// The version of the database
	Version string `pulumi:"version"`
}

// The set of arguments for constructing a Database resource.
type DatabaseArgs struct {
	// The engine of the database
	Engine pulumi.StringInput
	// The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all)
	FirewallId pulumi.StringPtrInput
	// Name of the database
	Name pulumi.StringPtrInput
	// The id of the associated network
	NetworkId pulumi.StringPtrInput
	// Count of nodes
	Nodes pulumi.IntInput
	// The region where the database will be created.
	Region pulumi.StringPtrInput
	// Size of the database
	Size pulumi.StringInput
	// The version of the database
	Version pulumi.StringInput
}

func (DatabaseArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*databaseArgs)(nil)).Elem()
}

type DatabaseInput interface {
	pulumi.Input

	ToDatabaseOutput() DatabaseOutput
	ToDatabaseOutputWithContext(ctx context.Context) DatabaseOutput
}

func (*Database) ElementType() reflect.Type {
	return reflect.TypeOf((**Database)(nil)).Elem()
}

func (i *Database) ToDatabaseOutput() DatabaseOutput {
	return i.ToDatabaseOutputWithContext(context.Background())
}

func (i *Database) ToDatabaseOutputWithContext(ctx context.Context) DatabaseOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DatabaseOutput)
}

// DatabaseArrayInput is an input type that accepts DatabaseArray and DatabaseArrayOutput values.
// You can construct a concrete instance of `DatabaseArrayInput` via:
//
//	DatabaseArray{ DatabaseArgs{...} }
type DatabaseArrayInput interface {
	pulumi.Input

	ToDatabaseArrayOutput() DatabaseArrayOutput
	ToDatabaseArrayOutputWithContext(context.Context) DatabaseArrayOutput
}

type DatabaseArray []DatabaseInput

func (DatabaseArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Database)(nil)).Elem()
}

func (i DatabaseArray) ToDatabaseArrayOutput() DatabaseArrayOutput {
	return i.ToDatabaseArrayOutputWithContext(context.Background())
}

func (i DatabaseArray) ToDatabaseArrayOutputWithContext(ctx context.Context) DatabaseArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DatabaseArrayOutput)
}

// DatabaseMapInput is an input type that accepts DatabaseMap and DatabaseMapOutput values.
// You can construct a concrete instance of `DatabaseMapInput` via:
//
//	DatabaseMap{ "key": DatabaseArgs{...} }
type DatabaseMapInput interface {
	pulumi.Input

	ToDatabaseMapOutput() DatabaseMapOutput
	ToDatabaseMapOutputWithContext(context.Context) DatabaseMapOutput
}

type DatabaseMap map[string]DatabaseInput

func (DatabaseMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Database)(nil)).Elem()
}

func (i DatabaseMap) ToDatabaseMapOutput() DatabaseMapOutput {
	return i.ToDatabaseMapOutputWithContext(context.Background())
}

func (i DatabaseMap) ToDatabaseMapOutputWithContext(ctx context.Context) DatabaseMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DatabaseMapOutput)
}

type DatabaseOutput struct{ *pulumi.OutputState }

func (DatabaseOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Database)(nil)).Elem()
}

func (o DatabaseOutput) ToDatabaseOutput() DatabaseOutput {
	return o
}

func (o DatabaseOutput) ToDatabaseOutputWithContext(ctx context.Context) DatabaseOutput {
	return o
}

// The DNS endpoint of the database
func (o DatabaseOutput) DnsEndpoint() pulumi.StringOutput {
	return o.ApplyT(func(v *Database) pulumi.StringOutput { return v.DnsEndpoint }).(pulumi.StringOutput)
}

// The endpoint of the database
func (o DatabaseOutput) Endpoint() pulumi.StringOutput {
	return o.ApplyT(func(v *Database) pulumi.StringOutput { return v.Endpoint }).(pulumi.StringOutput)
}

// The engine of the database
func (o DatabaseOutput) Engine() pulumi.StringOutput {
	return o.ApplyT(func(v *Database) pulumi.StringOutput { return v.Engine }).(pulumi.StringOutput)
}

// The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all)
func (o DatabaseOutput) FirewallId() pulumi.StringOutput {
	return o.ApplyT(func(v *Database) pulumi.StringOutput { return v.FirewallId }).(pulumi.StringOutput)
}

// Name of the database
func (o DatabaseOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Database) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The id of the associated network
func (o DatabaseOutput) NetworkId() pulumi.StringOutput {
	return o.ApplyT(func(v *Database) pulumi.StringOutput { return v.NetworkId }).(pulumi.StringOutput)
}

// Count of nodes
func (o DatabaseOutput) Nodes() pulumi.IntOutput {
	return o.ApplyT(func(v *Database) pulumi.IntOutput { return v.Nodes }).(pulumi.IntOutput)
}

// The password of the database
func (o DatabaseOutput) Password() pulumi.StringOutput {
	return o.ApplyT(func(v *Database) pulumi.StringOutput { return v.Password }).(pulumi.StringOutput)
}

// The port of the database
func (o DatabaseOutput) Port() pulumi.IntOutput {
	return o.ApplyT(func(v *Database) pulumi.IntOutput { return v.Port }).(pulumi.IntOutput)
}

// The region where the database will be created.
func (o DatabaseOutput) Region() pulumi.StringOutput {
	return o.ApplyT(func(v *Database) pulumi.StringOutput { return v.Region }).(pulumi.StringOutput)
}

// Size of the database
func (o DatabaseOutput) Size() pulumi.StringOutput {
	return o.ApplyT(func(v *Database) pulumi.StringOutput { return v.Size }).(pulumi.StringOutput)
}

// The status of the database
func (o DatabaseOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v *Database) pulumi.StringOutput { return v.Status }).(pulumi.StringOutput)
}

// The username of the database
func (o DatabaseOutput) Username() pulumi.StringOutput {
	return o.ApplyT(func(v *Database) pulumi.StringOutput { return v.Username }).(pulumi.StringOutput)
}

// The version of the database
func (o DatabaseOutput) Version() pulumi.StringOutput {
	return o.ApplyT(func(v *Database) pulumi.StringOutput { return v.Version }).(pulumi.StringOutput)
}

type DatabaseArrayOutput struct{ *pulumi.OutputState }

func (DatabaseArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Database)(nil)).Elem()
}

func (o DatabaseArrayOutput) ToDatabaseArrayOutput() DatabaseArrayOutput {
	return o
}

func (o DatabaseArrayOutput) ToDatabaseArrayOutputWithContext(ctx context.Context) DatabaseArrayOutput {
	return o
}

func (o DatabaseArrayOutput) Index(i pulumi.IntInput) DatabaseOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Database {
		return vs[0].([]*Database)[vs[1].(int)]
	}).(DatabaseOutput)
}

type DatabaseMapOutput struct{ *pulumi.OutputState }

func (DatabaseMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Database)(nil)).Elem()
}

func (o DatabaseMapOutput) ToDatabaseMapOutput() DatabaseMapOutput {
	return o
}

func (o DatabaseMapOutput) ToDatabaseMapOutputWithContext(ctx context.Context) DatabaseMapOutput {
	return o
}

func (o DatabaseMapOutput) MapIndex(k pulumi.StringInput) DatabaseOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Database {
		return vs[0].(map[string]*Database)[vs[1].(string)]
	}).(DatabaseOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DatabaseInput)(nil)).Elem(), &Database{})
	pulumi.RegisterInputType(reflect.TypeOf((*DatabaseArrayInput)(nil)).Elem(), DatabaseArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*DatabaseMapInput)(nil)).Elem(), DatabaseMap{})
	pulumi.RegisterOutputType(DatabaseOutput{})
	pulumi.RegisterOutputType(DatabaseArrayOutput{})
	pulumi.RegisterOutputType(DatabaseMapOutput{})
}

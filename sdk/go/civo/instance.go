// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides a Civo instance resource. This can be used to create, modify, and delete instances.
//
// ## Import
//
// # using ID
//
// ```sh
//  $ pulumi import civo:index/instance:Instance myintance 18bd98ad-1b6e-4f87-b48f-e690b4fd7413
// ```
type Instance struct {
	pulumi.CustomResourceState

	// Instance's CPU cores
	CpuCores pulumi.IntOutput `pulumi:"cpuCores"`
	// Timestamp when the instance was created
	CreatedAt pulumi.StringOutput `pulumi:"createdAt"`
	// Instance's disk (GB)
	DiskGb pulumi.IntOutput `pulumi:"diskGb"`
	// The ID for the disk image to use to build the instance
	DiskImage pulumi.StringOutput `pulumi:"diskImage"`
	// The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all)
	FirewallId pulumi.StringOutput `pulumi:"firewallId"`
	// A fully qualified domain name that should be set as the instance's hostname
	Hostname pulumi.StringOutput `pulumi:"hostname"`
	// Initial password for login
	InitialPassword pulumi.StringOutput `pulumi:"initialPassword"`
	// The name of the initial user created on the server (optional; this will default to the template's defaultUsername and fallback to civo)
	InitialUser pulumi.StringPtrOutput `pulumi:"initialUser"`
	// This must be the ID of the network from the network listing (optional; default network used when not specified)
	NetworkId pulumi.StringOutput `pulumi:"networkId"`
	// Add some notes to the instance
	Notes pulumi.StringPtrOutput `pulumi:"notes"`
	// Instance's private IP address
	PrivateIp pulumi.StringOutput `pulumi:"privateIp"`
	// Instance's public IP address
	PublicIp pulumi.StringOutput `pulumi:"publicIp"`
	// This should be either 'none' or 'create' (default: 'create')
	PublicIpRequired pulumi.StringPtrOutput `pulumi:"publicIpRequired"`
	// Instance's RAM (MB)
	RamMb pulumi.IntOutput `pulumi:"ramMb"`
	// The region for the instance, if not declare we use the region in declared in the provider
	Region pulumi.StringPtrOutput `pulumi:"region"`
	// A fully qualified domain name that should be used as the instance's IP's reverse DNS (optional, uses the hostname if unspecified)
	ReverseDns pulumi.StringPtrOutput `pulumi:"reverseDns"`
	// The contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance, read/write/executable only by root and then will be executed at the end of the cloud initialization
	Script pulumi.StringPtrOutput `pulumi:"script"`
	// The name of the size, from the current list, e.g. g3.xsmall
	Size pulumi.StringPtrOutput `pulumi:"size"`
	// Instance's source ID
	SourceId pulumi.StringOutput `pulumi:"sourceId"`
	// Instance's source type
	SourceType pulumi.StringOutput `pulumi:"sourceType"`
	// The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn't provided a random password will be set and returned in the initialPassword field)
	SshkeyId pulumi.StringPtrOutput `pulumi:"sshkeyId"`
	// Instance's status
	Status pulumi.StringOutput `pulumi:"status"`
	// An optional list of tags, represented as a key, value pair
	Tags pulumi.StringArrayOutput `pulumi:"tags"`
	// The ID for the template to use to build the instance
	//
	// Deprecated: "template" attribute is deprecated. Moving forward, please use "disk_image" attribute.
	Template pulumi.StringOutput `pulumi:"template"`
}

// NewInstance registers a new resource with the given unique name, arguments, and options.
func NewInstance(ctx *pulumi.Context,
	name string, args *InstanceArgs, opts ...pulumi.ResourceOption) (*Instance, error) {
	if args == nil {
		args = &InstanceArgs{}
	}

	var resource Instance
	err := ctx.RegisterResource("civo:index/instance:Instance", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetInstance gets an existing Instance resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetInstance(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *InstanceState, opts ...pulumi.ResourceOption) (*Instance, error) {
	var resource Instance
	err := ctx.ReadResource("civo:index/instance:Instance", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Instance resources.
type instanceState struct {
	// Instance's CPU cores
	CpuCores *int `pulumi:"cpuCores"`
	// Timestamp when the instance was created
	CreatedAt *string `pulumi:"createdAt"`
	// Instance's disk (GB)
	DiskGb *int `pulumi:"diskGb"`
	// The ID for the disk image to use to build the instance
	DiskImage *string `pulumi:"diskImage"`
	// The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all)
	FirewallId *string `pulumi:"firewallId"`
	// A fully qualified domain name that should be set as the instance's hostname
	Hostname *string `pulumi:"hostname"`
	// Initial password for login
	InitialPassword *string `pulumi:"initialPassword"`
	// The name of the initial user created on the server (optional; this will default to the template's defaultUsername and fallback to civo)
	InitialUser *string `pulumi:"initialUser"`
	// This must be the ID of the network from the network listing (optional; default network used when not specified)
	NetworkId *string `pulumi:"networkId"`
	// Add some notes to the instance
	Notes *string `pulumi:"notes"`
	// Instance's private IP address
	PrivateIp *string `pulumi:"privateIp"`
	// Instance's public IP address
	PublicIp *string `pulumi:"publicIp"`
	// This should be either 'none' or 'create' (default: 'create')
	PublicIpRequired *string `pulumi:"publicIpRequired"`
	// Instance's RAM (MB)
	RamMb *int `pulumi:"ramMb"`
	// The region for the instance, if not declare we use the region in declared in the provider
	Region *string `pulumi:"region"`
	// A fully qualified domain name that should be used as the instance's IP's reverse DNS (optional, uses the hostname if unspecified)
	ReverseDns *string `pulumi:"reverseDns"`
	// The contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance, read/write/executable only by root and then will be executed at the end of the cloud initialization
	Script *string `pulumi:"script"`
	// The name of the size, from the current list, e.g. g3.xsmall
	Size *string `pulumi:"size"`
	// Instance's source ID
	SourceId *string `pulumi:"sourceId"`
	// Instance's source type
	SourceType *string `pulumi:"sourceType"`
	// The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn't provided a random password will be set and returned in the initialPassword field)
	SshkeyId *string `pulumi:"sshkeyId"`
	// Instance's status
	Status *string `pulumi:"status"`
	// An optional list of tags, represented as a key, value pair
	Tags []string `pulumi:"tags"`
	// The ID for the template to use to build the instance
	//
	// Deprecated: "template" attribute is deprecated. Moving forward, please use "disk_image" attribute.
	Template *string `pulumi:"template"`
}

type InstanceState struct {
	// Instance's CPU cores
	CpuCores pulumi.IntPtrInput
	// Timestamp when the instance was created
	CreatedAt pulumi.StringPtrInput
	// Instance's disk (GB)
	DiskGb pulumi.IntPtrInput
	// The ID for the disk image to use to build the instance
	DiskImage pulumi.StringPtrInput
	// The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all)
	FirewallId pulumi.StringPtrInput
	// A fully qualified domain name that should be set as the instance's hostname
	Hostname pulumi.StringPtrInput
	// Initial password for login
	InitialPassword pulumi.StringPtrInput
	// The name of the initial user created on the server (optional; this will default to the template's defaultUsername and fallback to civo)
	InitialUser pulumi.StringPtrInput
	// This must be the ID of the network from the network listing (optional; default network used when not specified)
	NetworkId pulumi.StringPtrInput
	// Add some notes to the instance
	Notes pulumi.StringPtrInput
	// Instance's private IP address
	PrivateIp pulumi.StringPtrInput
	// Instance's public IP address
	PublicIp pulumi.StringPtrInput
	// This should be either 'none' or 'create' (default: 'create')
	PublicIpRequired pulumi.StringPtrInput
	// Instance's RAM (MB)
	RamMb pulumi.IntPtrInput
	// The region for the instance, if not declare we use the region in declared in the provider
	Region pulumi.StringPtrInput
	// A fully qualified domain name that should be used as the instance's IP's reverse DNS (optional, uses the hostname if unspecified)
	ReverseDns pulumi.StringPtrInput
	// The contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance, read/write/executable only by root and then will be executed at the end of the cloud initialization
	Script pulumi.StringPtrInput
	// The name of the size, from the current list, e.g. g3.xsmall
	Size pulumi.StringPtrInput
	// Instance's source ID
	SourceId pulumi.StringPtrInput
	// Instance's source type
	SourceType pulumi.StringPtrInput
	// The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn't provided a random password will be set and returned in the initialPassword field)
	SshkeyId pulumi.StringPtrInput
	// Instance's status
	Status pulumi.StringPtrInput
	// An optional list of tags, represented as a key, value pair
	Tags pulumi.StringArrayInput
	// The ID for the template to use to build the instance
	//
	// Deprecated: "template" attribute is deprecated. Moving forward, please use "disk_image" attribute.
	Template pulumi.StringPtrInput
}

func (InstanceState) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceState)(nil)).Elem()
}

type instanceArgs struct {
	// The ID for the disk image to use to build the instance
	DiskImage *string `pulumi:"diskImage"`
	// The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all)
	FirewallId *string `pulumi:"firewallId"`
	// A fully qualified domain name that should be set as the instance's hostname
	Hostname *string `pulumi:"hostname"`
	// The name of the initial user created on the server (optional; this will default to the template's defaultUsername and fallback to civo)
	InitialUser *string `pulumi:"initialUser"`
	// This must be the ID of the network from the network listing (optional; default network used when not specified)
	NetworkId *string `pulumi:"networkId"`
	// Add some notes to the instance
	Notes *string `pulumi:"notes"`
	// This should be either 'none' or 'create' (default: 'create')
	PublicIpRequired *string `pulumi:"publicIpRequired"`
	// The region for the instance, if not declare we use the region in declared in the provider
	Region *string `pulumi:"region"`
	// A fully qualified domain name that should be used as the instance's IP's reverse DNS (optional, uses the hostname if unspecified)
	ReverseDns *string `pulumi:"reverseDns"`
	// The contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance, read/write/executable only by root and then will be executed at the end of the cloud initialization
	Script *string `pulumi:"script"`
	// The name of the size, from the current list, e.g. g3.xsmall
	Size *string `pulumi:"size"`
	// The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn't provided a random password will be set and returned in the initialPassword field)
	SshkeyId *string `pulumi:"sshkeyId"`
	// An optional list of tags, represented as a key, value pair
	Tags []string `pulumi:"tags"`
	// The ID for the template to use to build the instance
	//
	// Deprecated: "template" attribute is deprecated. Moving forward, please use "disk_image" attribute.
	Template *string `pulumi:"template"`
}

// The set of arguments for constructing a Instance resource.
type InstanceArgs struct {
	// The ID for the disk image to use to build the instance
	DiskImage pulumi.StringPtrInput
	// The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all)
	FirewallId pulumi.StringPtrInput
	// A fully qualified domain name that should be set as the instance's hostname
	Hostname pulumi.StringPtrInput
	// The name of the initial user created on the server (optional; this will default to the template's defaultUsername and fallback to civo)
	InitialUser pulumi.StringPtrInput
	// This must be the ID of the network from the network listing (optional; default network used when not specified)
	NetworkId pulumi.StringPtrInput
	// Add some notes to the instance
	Notes pulumi.StringPtrInput
	// This should be either 'none' or 'create' (default: 'create')
	PublicIpRequired pulumi.StringPtrInput
	// The region for the instance, if not declare we use the region in declared in the provider
	Region pulumi.StringPtrInput
	// A fully qualified domain name that should be used as the instance's IP's reverse DNS (optional, uses the hostname if unspecified)
	ReverseDns pulumi.StringPtrInput
	// The contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance, read/write/executable only by root and then will be executed at the end of the cloud initialization
	Script pulumi.StringPtrInput
	// The name of the size, from the current list, e.g. g3.xsmall
	Size pulumi.StringPtrInput
	// The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn't provided a random password will be set and returned in the initialPassword field)
	SshkeyId pulumi.StringPtrInput
	// An optional list of tags, represented as a key, value pair
	Tags pulumi.StringArrayInput
	// The ID for the template to use to build the instance
	//
	// Deprecated: "template" attribute is deprecated. Moving forward, please use "disk_image" attribute.
	Template pulumi.StringPtrInput
}

func (InstanceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceArgs)(nil)).Elem()
}

type InstanceInput interface {
	pulumi.Input

	ToInstanceOutput() InstanceOutput
	ToInstanceOutputWithContext(ctx context.Context) InstanceOutput
}

func (*Instance) ElementType() reflect.Type {
	return reflect.TypeOf((**Instance)(nil)).Elem()
}

func (i *Instance) ToInstanceOutput() InstanceOutput {
	return i.ToInstanceOutputWithContext(context.Background())
}

func (i *Instance) ToInstanceOutputWithContext(ctx context.Context) InstanceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceOutput)
}

// InstanceArrayInput is an input type that accepts InstanceArray and InstanceArrayOutput values.
// You can construct a concrete instance of `InstanceArrayInput` via:
//
//          InstanceArray{ InstanceArgs{...} }
type InstanceArrayInput interface {
	pulumi.Input

	ToInstanceArrayOutput() InstanceArrayOutput
	ToInstanceArrayOutputWithContext(context.Context) InstanceArrayOutput
}

type InstanceArray []InstanceInput

func (InstanceArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Instance)(nil)).Elem()
}

func (i InstanceArray) ToInstanceArrayOutput() InstanceArrayOutput {
	return i.ToInstanceArrayOutputWithContext(context.Background())
}

func (i InstanceArray) ToInstanceArrayOutputWithContext(ctx context.Context) InstanceArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceArrayOutput)
}

// InstanceMapInput is an input type that accepts InstanceMap and InstanceMapOutput values.
// You can construct a concrete instance of `InstanceMapInput` via:
//
//          InstanceMap{ "key": InstanceArgs{...} }
type InstanceMapInput interface {
	pulumi.Input

	ToInstanceMapOutput() InstanceMapOutput
	ToInstanceMapOutputWithContext(context.Context) InstanceMapOutput
}

type InstanceMap map[string]InstanceInput

func (InstanceMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Instance)(nil)).Elem()
}

func (i InstanceMap) ToInstanceMapOutput() InstanceMapOutput {
	return i.ToInstanceMapOutputWithContext(context.Background())
}

func (i InstanceMap) ToInstanceMapOutputWithContext(ctx context.Context) InstanceMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceMapOutput)
}

type InstanceOutput struct{ *pulumi.OutputState }

func (InstanceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Instance)(nil)).Elem()
}

func (o InstanceOutput) ToInstanceOutput() InstanceOutput {
	return o
}

func (o InstanceOutput) ToInstanceOutputWithContext(ctx context.Context) InstanceOutput {
	return o
}

type InstanceArrayOutput struct{ *pulumi.OutputState }

func (InstanceArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Instance)(nil)).Elem()
}

func (o InstanceArrayOutput) ToInstanceArrayOutput() InstanceArrayOutput {
	return o
}

func (o InstanceArrayOutput) ToInstanceArrayOutputWithContext(ctx context.Context) InstanceArrayOutput {
	return o
}

func (o InstanceArrayOutput) Index(i pulumi.IntInput) InstanceOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Instance {
		return vs[0].([]*Instance)[vs[1].(int)]
	}).(InstanceOutput)
}

type InstanceMapOutput struct{ *pulumi.OutputState }

func (InstanceMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Instance)(nil)).Elem()
}

func (o InstanceMapOutput) ToInstanceMapOutput() InstanceMapOutput {
	return o
}

func (o InstanceMapOutput) ToInstanceMapOutputWithContext(ctx context.Context) InstanceMapOutput {
	return o
}

func (o InstanceMapOutput) MapIndex(k pulumi.StringInput) InstanceOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Instance {
		return vs[0].(map[string]*Instance)[vs[1].(string)]
	}).(InstanceOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*InstanceInput)(nil)).Elem(), &Instance{})
	pulumi.RegisterInputType(reflect.TypeOf((*InstanceArrayInput)(nil)).Elem(), InstanceArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*InstanceMapInput)(nil)).Elem(), InstanceMap{})
	pulumi.RegisterOutputType(InstanceOutput{})
	pulumi.RegisterOutputType(InstanceArrayOutput{})
	pulumi.RegisterOutputType(InstanceMapOutput{})
}

// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-civo/sdk/v2/go/civo/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides an Object Store Credential resource. This can be used to create, modify, and delete object stores credential.
//
// ## Example Usage
//
// <!--Start PulumiCodeChooser -->
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
//			// Create a simple credential for the object store
//			_, err := civo.LookupObjectStoreCredential(ctx, &civo.LookupObjectStoreCredentialArgs{
//				Name: pulumi.StringRef("backup-server"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			// Create a credential for the object store with a specific access key and secret key
//			backupObjectStoreCredential, err := civo.NewObjectStoreCredential(ctx, "backup", &civo.ObjectStoreCredentialArgs{
//				Name:            pulumi.String("backup-server"),
//				AccessKeyId:     pulumi.String("my-access-key"),
//				SecretAccessKey: pulumi.String("my-secret-key"),
//			})
//			if err != nil {
//				return err
//			}
//			// Use the credential to create a bucket
//			_, err = civo.NewObjectStore(ctx, "backup", &civo.ObjectStoreArgs{
//				Name:        pulumi.String("backup-server"),
//				MaxSizeGb:   pulumi.Int(500),
//				Region:      pulumi.String("LON1"),
//				AccessKeyId: backupObjectStoreCredential.AccessKeyId,
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
// <!--End PulumiCodeChooser -->
//
// ## Import
//
// using ID
//
// ```sh
// $ pulumi import civo:index/objectStoreCredential:ObjectStoreCredential custom_object b8ecd2ab-2267-4a5e-8692-cbf1d32583e3
// ```
type ObjectStoreCredential struct {
	pulumi.CustomResourceState

	// The access key id of the Object Store Credential. It is generated by the provider.
	AccessKeyId pulumi.StringOutput `pulumi:"accessKeyId"`
	// The name of the Object Store Credential. Must be unique.
	Name pulumi.StringOutput `pulumi:"name"`
	// The region where the Object Store Credential will be created.
	Region pulumi.StringPtrOutput `pulumi:"region"`
	// The secret access key of the Object Store Credential. It is generated by the provider.
	SecretAccessKey pulumi.StringOutput `pulumi:"secretAccessKey"`
	// The status of the Object Store Credential.
	Status pulumi.StringOutput `pulumi:"status"`
}

// NewObjectStoreCredential registers a new resource with the given unique name, arguments, and options.
func NewObjectStoreCredential(ctx *pulumi.Context,
	name string, args *ObjectStoreCredentialArgs, opts ...pulumi.ResourceOption) (*ObjectStoreCredential, error) {
	if args == nil {
		args = &ObjectStoreCredentialArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ObjectStoreCredential
	err := ctx.RegisterResource("civo:index/objectStoreCredential:ObjectStoreCredential", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetObjectStoreCredential gets an existing ObjectStoreCredential resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetObjectStoreCredential(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ObjectStoreCredentialState, opts ...pulumi.ResourceOption) (*ObjectStoreCredential, error) {
	var resource ObjectStoreCredential
	err := ctx.ReadResource("civo:index/objectStoreCredential:ObjectStoreCredential", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ObjectStoreCredential resources.
type objectStoreCredentialState struct {
	// The access key id of the Object Store Credential. It is generated by the provider.
	AccessKeyId *string `pulumi:"accessKeyId"`
	// The name of the Object Store Credential. Must be unique.
	Name *string `pulumi:"name"`
	// The region where the Object Store Credential will be created.
	Region *string `pulumi:"region"`
	// The secret access key of the Object Store Credential. It is generated by the provider.
	SecretAccessKey *string `pulumi:"secretAccessKey"`
	// The status of the Object Store Credential.
	Status *string `pulumi:"status"`
}

type ObjectStoreCredentialState struct {
	// The access key id of the Object Store Credential. It is generated by the provider.
	AccessKeyId pulumi.StringPtrInput
	// The name of the Object Store Credential. Must be unique.
	Name pulumi.StringPtrInput
	// The region where the Object Store Credential will be created.
	Region pulumi.StringPtrInput
	// The secret access key of the Object Store Credential. It is generated by the provider.
	SecretAccessKey pulumi.StringPtrInput
	// The status of the Object Store Credential.
	Status pulumi.StringPtrInput
}

func (ObjectStoreCredentialState) ElementType() reflect.Type {
	return reflect.TypeOf((*objectStoreCredentialState)(nil)).Elem()
}

type objectStoreCredentialArgs struct {
	// The access key id of the Object Store Credential. It is generated by the provider.
	AccessKeyId *string `pulumi:"accessKeyId"`
	// The name of the Object Store Credential. Must be unique.
	Name *string `pulumi:"name"`
	// The region where the Object Store Credential will be created.
	Region *string `pulumi:"region"`
	// The secret access key of the Object Store Credential. It is generated by the provider.
	SecretAccessKey *string `pulumi:"secretAccessKey"`
}

// The set of arguments for constructing a ObjectStoreCredential resource.
type ObjectStoreCredentialArgs struct {
	// The access key id of the Object Store Credential. It is generated by the provider.
	AccessKeyId pulumi.StringPtrInput
	// The name of the Object Store Credential. Must be unique.
	Name pulumi.StringPtrInput
	// The region where the Object Store Credential will be created.
	Region pulumi.StringPtrInput
	// The secret access key of the Object Store Credential. It is generated by the provider.
	SecretAccessKey pulumi.StringPtrInput
}

func (ObjectStoreCredentialArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*objectStoreCredentialArgs)(nil)).Elem()
}

type ObjectStoreCredentialInput interface {
	pulumi.Input

	ToObjectStoreCredentialOutput() ObjectStoreCredentialOutput
	ToObjectStoreCredentialOutputWithContext(ctx context.Context) ObjectStoreCredentialOutput
}

func (*ObjectStoreCredential) ElementType() reflect.Type {
	return reflect.TypeOf((**ObjectStoreCredential)(nil)).Elem()
}

func (i *ObjectStoreCredential) ToObjectStoreCredentialOutput() ObjectStoreCredentialOutput {
	return i.ToObjectStoreCredentialOutputWithContext(context.Background())
}

func (i *ObjectStoreCredential) ToObjectStoreCredentialOutputWithContext(ctx context.Context) ObjectStoreCredentialOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ObjectStoreCredentialOutput)
}

// ObjectStoreCredentialArrayInput is an input type that accepts ObjectStoreCredentialArray and ObjectStoreCredentialArrayOutput values.
// You can construct a concrete instance of `ObjectStoreCredentialArrayInput` via:
//
//	ObjectStoreCredentialArray{ ObjectStoreCredentialArgs{...} }
type ObjectStoreCredentialArrayInput interface {
	pulumi.Input

	ToObjectStoreCredentialArrayOutput() ObjectStoreCredentialArrayOutput
	ToObjectStoreCredentialArrayOutputWithContext(context.Context) ObjectStoreCredentialArrayOutput
}

type ObjectStoreCredentialArray []ObjectStoreCredentialInput

func (ObjectStoreCredentialArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ObjectStoreCredential)(nil)).Elem()
}

func (i ObjectStoreCredentialArray) ToObjectStoreCredentialArrayOutput() ObjectStoreCredentialArrayOutput {
	return i.ToObjectStoreCredentialArrayOutputWithContext(context.Background())
}

func (i ObjectStoreCredentialArray) ToObjectStoreCredentialArrayOutputWithContext(ctx context.Context) ObjectStoreCredentialArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ObjectStoreCredentialArrayOutput)
}

// ObjectStoreCredentialMapInput is an input type that accepts ObjectStoreCredentialMap and ObjectStoreCredentialMapOutput values.
// You can construct a concrete instance of `ObjectStoreCredentialMapInput` via:
//
//	ObjectStoreCredentialMap{ "key": ObjectStoreCredentialArgs{...} }
type ObjectStoreCredentialMapInput interface {
	pulumi.Input

	ToObjectStoreCredentialMapOutput() ObjectStoreCredentialMapOutput
	ToObjectStoreCredentialMapOutputWithContext(context.Context) ObjectStoreCredentialMapOutput
}

type ObjectStoreCredentialMap map[string]ObjectStoreCredentialInput

func (ObjectStoreCredentialMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ObjectStoreCredential)(nil)).Elem()
}

func (i ObjectStoreCredentialMap) ToObjectStoreCredentialMapOutput() ObjectStoreCredentialMapOutput {
	return i.ToObjectStoreCredentialMapOutputWithContext(context.Background())
}

func (i ObjectStoreCredentialMap) ToObjectStoreCredentialMapOutputWithContext(ctx context.Context) ObjectStoreCredentialMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ObjectStoreCredentialMapOutput)
}

type ObjectStoreCredentialOutput struct{ *pulumi.OutputState }

func (ObjectStoreCredentialOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ObjectStoreCredential)(nil)).Elem()
}

func (o ObjectStoreCredentialOutput) ToObjectStoreCredentialOutput() ObjectStoreCredentialOutput {
	return o
}

func (o ObjectStoreCredentialOutput) ToObjectStoreCredentialOutputWithContext(ctx context.Context) ObjectStoreCredentialOutput {
	return o
}

// The access key id of the Object Store Credential. It is generated by the provider.
func (o ObjectStoreCredentialOutput) AccessKeyId() pulumi.StringOutput {
	return o.ApplyT(func(v *ObjectStoreCredential) pulumi.StringOutput { return v.AccessKeyId }).(pulumi.StringOutput)
}

// The name of the Object Store Credential. Must be unique.
func (o ObjectStoreCredentialOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *ObjectStoreCredential) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The region where the Object Store Credential will be created.
func (o ObjectStoreCredentialOutput) Region() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ObjectStoreCredential) pulumi.StringPtrOutput { return v.Region }).(pulumi.StringPtrOutput)
}

// The secret access key of the Object Store Credential. It is generated by the provider.
func (o ObjectStoreCredentialOutput) SecretAccessKey() pulumi.StringOutput {
	return o.ApplyT(func(v *ObjectStoreCredential) pulumi.StringOutput { return v.SecretAccessKey }).(pulumi.StringOutput)
}

// The status of the Object Store Credential.
func (o ObjectStoreCredentialOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v *ObjectStoreCredential) pulumi.StringOutput { return v.Status }).(pulumi.StringOutput)
}

type ObjectStoreCredentialArrayOutput struct{ *pulumi.OutputState }

func (ObjectStoreCredentialArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ObjectStoreCredential)(nil)).Elem()
}

func (o ObjectStoreCredentialArrayOutput) ToObjectStoreCredentialArrayOutput() ObjectStoreCredentialArrayOutput {
	return o
}

func (o ObjectStoreCredentialArrayOutput) ToObjectStoreCredentialArrayOutputWithContext(ctx context.Context) ObjectStoreCredentialArrayOutput {
	return o
}

func (o ObjectStoreCredentialArrayOutput) Index(i pulumi.IntInput) ObjectStoreCredentialOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *ObjectStoreCredential {
		return vs[0].([]*ObjectStoreCredential)[vs[1].(int)]
	}).(ObjectStoreCredentialOutput)
}

type ObjectStoreCredentialMapOutput struct{ *pulumi.OutputState }

func (ObjectStoreCredentialMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ObjectStoreCredential)(nil)).Elem()
}

func (o ObjectStoreCredentialMapOutput) ToObjectStoreCredentialMapOutput() ObjectStoreCredentialMapOutput {
	return o
}

func (o ObjectStoreCredentialMapOutput) ToObjectStoreCredentialMapOutputWithContext(ctx context.Context) ObjectStoreCredentialMapOutput {
	return o
}

func (o ObjectStoreCredentialMapOutput) MapIndex(k pulumi.StringInput) ObjectStoreCredentialOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *ObjectStoreCredential {
		return vs[0].(map[string]*ObjectStoreCredential)[vs[1].(string)]
	}).(ObjectStoreCredentialOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ObjectStoreCredentialInput)(nil)).Elem(), &ObjectStoreCredential{})
	pulumi.RegisterInputType(reflect.TypeOf((*ObjectStoreCredentialArrayInput)(nil)).Elem(), ObjectStoreCredentialArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ObjectStoreCredentialMapInput)(nil)).Elem(), ObjectStoreCredentialMap{})
	pulumi.RegisterOutputType(ObjectStoreCredentialOutput{})
	pulumi.RegisterOutputType(ObjectStoreCredentialArrayOutput{})
	pulumi.RegisterOutputType(ObjectStoreCredentialMapOutput{})
}

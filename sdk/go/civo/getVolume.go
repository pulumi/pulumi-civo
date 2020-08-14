// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func LookupVolume(ctx *pulumi.Context, args *LookupVolumeArgs, opts ...pulumi.InvokeOption) (*LookupVolumeResult, error) {
	var rv LookupVolumeResult
	err := ctx.Invoke("civo:index/getVolume:getVolume", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getVolume.
type LookupVolumeArgs struct {
	// The unique identifier for the volume.
	Id *string `pulumi:"id"`
	// The name of the volume.
	Name *string `pulumi:"name"`
}

// A collection of values returned by getVolume.
type LookupVolumeResult struct {
	// if is bootable or not.
	Bootable bool `pulumi:"bootable"`
	// The date of the creation of the volume.
	CreatedAt string `pulumi:"createdAt"`
	// The unique identifier for the volume.
	Id *string `pulumi:"id"`
	// The mount point of the volume.
	MountPoint string `pulumi:"mountPoint"`
	// Name of the volume.
	Name *string `pulumi:"name"`
	// The size of the volume.
	SizeGb int `pulumi:"sizeGb"`
}
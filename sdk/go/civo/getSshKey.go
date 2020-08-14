// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func LookupSshKey(ctx *pulumi.Context, args *LookupSshKeyArgs, opts ...pulumi.InvokeOption) (*LookupSshKeyResult, error) {
	var rv LookupSshKeyResult
	err := ctx.Invoke("civo:index/getSshKey:getSshKey", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getSshKey.
type LookupSshKeyArgs struct {
	// The ID of the ssh key.
	Id *string `pulumi:"id"`
	// The name of the ssh key.
	Name *string `pulumi:"name"`
}

// A collection of values returned by getSshKey.
type LookupSshKeyResult struct {
	Fingerprint string  `pulumi:"fingerprint"`
	Id          *string `pulumi:"id"`
	Name        *string `pulumi:"name"`
}
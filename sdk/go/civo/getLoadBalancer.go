// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Get information on a load balancer for use in other resources. This data source provides all of the load balancers properties as configured on your Civo account.
//
// An error will be raised if the provided load balancer name does not exist in your Civo account.
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
//			my_lb, err := civo.GetLoadBalancer(ctx, &GetLoadBalancerArgs{
//				Name:   pulumi.StringRef("lb-name"),
//				Region: pulumi.StringRef("LON1"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			ctx.Export("civoLoadbalancerOutput", my_lb.PublicIp)
//			return nil
//		})
//	}
//
// ```
func GetLoadBalancer(ctx *pulumi.Context, args *GetLoadBalancerArgs, opts ...pulumi.InvokeOption) (*GetLoadBalancerResult, error) {
	var rv GetLoadBalancerResult
	err := ctx.Invoke("civo:index/getLoadBalancer:getLoadBalancer", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getLoadBalancer.
type GetLoadBalancerArgs struct {
	// The id of the load balancer to retrieve (You can find this id from service annotations 'kubernetes.civo.com/loadbalancer-id')
	Id *string `pulumi:"id"`
	// The name of the load balancer (You can find this name from service annotations 'kubernetes.civo.com/loadbalancer-name')
	Name *string `pulumi:"name"`
	// The region of the load balancer, if you delcare this field, the datasource will use this value instead of the one defined in the provider
	Region *string `pulumi:"region"`
}

// A collection of values returned by getLoadBalancer.
type GetLoadBalancerResult struct {
	// The algorithm used by the load balancer
	Algorithm string                   `pulumi:"algorithm"`
	Backends  []GetLoadBalancerBackend `pulumi:"backends"`
	// The cluster id of the load balancer
	ClusterId string `pulumi:"clusterId"`
	// The enabled proxy protocol of the load balancer
	EnableProxyProtocol string `pulumi:"enableProxyProtocol"`
	// The external traffic policy of the load balancer
	ExternalTrafficPolicy string `pulumi:"externalTrafficPolicy"`
	// The firewall id of the load balancer
	FirewallId string `pulumi:"firewallId"`
	// The id of the load balancer to retrieve (You can find this id from service annotations 'kubernetes.civo.com/loadbalancer-id')
	Id *string `pulumi:"id"`
	// The name of the load balancer (You can find this name from service annotations 'kubernetes.civo.com/loadbalancer-name')
	Name *string `pulumi:"name"`
	// The private ip of the load balancer
	PrivateIp string `pulumi:"privateIp"`
	// The public ip of the load balancer
	PublicIp string `pulumi:"publicIp"`
	// The region of the load balancer, if you delcare this field, the datasource will use this value instead of the one defined in the provider
	Region *string `pulumi:"region"`
	// The session affinity of the load balancer
	SessionAffinity string `pulumi:"sessionAffinity"`
	// The session affinity config timeout of the load balancer
	SessionAffinityConfigTimeout int `pulumi:"sessionAffinityConfigTimeout"`
	// The state of the load balancer
	State string `pulumi:"state"`
}

func GetLoadBalancerOutput(ctx *pulumi.Context, args GetLoadBalancerOutputArgs, opts ...pulumi.InvokeOption) GetLoadBalancerResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetLoadBalancerResult, error) {
			args := v.(GetLoadBalancerArgs)
			r, err := GetLoadBalancer(ctx, &args, opts...)
			var s GetLoadBalancerResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetLoadBalancerResultOutput)
}

// A collection of arguments for invoking getLoadBalancer.
type GetLoadBalancerOutputArgs struct {
	// The id of the load balancer to retrieve (You can find this id from service annotations 'kubernetes.civo.com/loadbalancer-id')
	Id pulumi.StringPtrInput `pulumi:"id"`
	// The name of the load balancer (You can find this name from service annotations 'kubernetes.civo.com/loadbalancer-name')
	Name pulumi.StringPtrInput `pulumi:"name"`
	// The region of the load balancer, if you delcare this field, the datasource will use this value instead of the one defined in the provider
	Region pulumi.StringPtrInput `pulumi:"region"`
}

func (GetLoadBalancerOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetLoadBalancerArgs)(nil)).Elem()
}

// A collection of values returned by getLoadBalancer.
type GetLoadBalancerResultOutput struct{ *pulumi.OutputState }

func (GetLoadBalancerResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetLoadBalancerResult)(nil)).Elem()
}

func (o GetLoadBalancerResultOutput) ToGetLoadBalancerResultOutput() GetLoadBalancerResultOutput {
	return o
}

func (o GetLoadBalancerResultOutput) ToGetLoadBalancerResultOutputWithContext(ctx context.Context) GetLoadBalancerResultOutput {
	return o
}

// The algorithm used by the load balancer
func (o GetLoadBalancerResultOutput) Algorithm() pulumi.StringOutput {
	return o.ApplyT(func(v GetLoadBalancerResult) string { return v.Algorithm }).(pulumi.StringOutput)
}

func (o GetLoadBalancerResultOutput) Backends() GetLoadBalancerBackendArrayOutput {
	return o.ApplyT(func(v GetLoadBalancerResult) []GetLoadBalancerBackend { return v.Backends }).(GetLoadBalancerBackendArrayOutput)
}

// The cluster id of the load balancer
func (o GetLoadBalancerResultOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v GetLoadBalancerResult) string { return v.ClusterId }).(pulumi.StringOutput)
}

// The enabled proxy protocol of the load balancer
func (o GetLoadBalancerResultOutput) EnableProxyProtocol() pulumi.StringOutput {
	return o.ApplyT(func(v GetLoadBalancerResult) string { return v.EnableProxyProtocol }).(pulumi.StringOutput)
}

// The external traffic policy of the load balancer
func (o GetLoadBalancerResultOutput) ExternalTrafficPolicy() pulumi.StringOutput {
	return o.ApplyT(func(v GetLoadBalancerResult) string { return v.ExternalTrafficPolicy }).(pulumi.StringOutput)
}

// The firewall id of the load balancer
func (o GetLoadBalancerResultOutput) FirewallId() pulumi.StringOutput {
	return o.ApplyT(func(v GetLoadBalancerResult) string { return v.FirewallId }).(pulumi.StringOutput)
}

// The id of the load balancer to retrieve (You can find this id from service annotations 'kubernetes.civo.com/loadbalancer-id')
func (o GetLoadBalancerResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetLoadBalancerResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// The name of the load balancer (You can find this name from service annotations 'kubernetes.civo.com/loadbalancer-name')
func (o GetLoadBalancerResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetLoadBalancerResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

// The private ip of the load balancer
func (o GetLoadBalancerResultOutput) PrivateIp() pulumi.StringOutput {
	return o.ApplyT(func(v GetLoadBalancerResult) string { return v.PrivateIp }).(pulumi.StringOutput)
}

// The public ip of the load balancer
func (o GetLoadBalancerResultOutput) PublicIp() pulumi.StringOutput {
	return o.ApplyT(func(v GetLoadBalancerResult) string { return v.PublicIp }).(pulumi.StringOutput)
}

// The region of the load balancer, if you delcare this field, the datasource will use this value instead of the one defined in the provider
func (o GetLoadBalancerResultOutput) Region() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetLoadBalancerResult) *string { return v.Region }).(pulumi.StringPtrOutput)
}

// The session affinity of the load balancer
func (o GetLoadBalancerResultOutput) SessionAffinity() pulumi.StringOutput {
	return o.ApplyT(func(v GetLoadBalancerResult) string { return v.SessionAffinity }).(pulumi.StringOutput)
}

// The session affinity config timeout of the load balancer
func (o GetLoadBalancerResultOutput) SessionAffinityConfigTimeout() pulumi.IntOutput {
	return o.ApplyT(func(v GetLoadBalancerResult) int { return v.SessionAffinityConfigTimeout }).(pulumi.IntOutput)
}

// The state of the load balancer
func (o GetLoadBalancerResultOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v GetLoadBalancerResult) string { return v.State }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetLoadBalancerResultOutput{})
}

// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Get information on a load balancer for use in other resources. This data source provides all of the load balancers properties as configured on your Civo account.
 *
 * An error will be raised if the provided load balancer name does not exist in your Civo account.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as civo from "@pulumi/civo";
 *
 * // TODO
 * const my-lb = civo.getLoadBalancer({
 *     name: "lb-name",
 *     region: "LON1",
 * });
 * export const civoLoadbalancerOutput = my_lb.then(my_lb => my_lb.publicIp);
 * ```
 */
export function getLoadBalancer(args?: GetLoadBalancerArgs, opts?: pulumi.InvokeOptions): Promise<GetLoadBalancerResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("civo:index/getLoadBalancer:getLoadBalancer", {
        "id": args.id,
        "name": args.name,
        "region": args.region,
    }, opts);
}

/**
 * A collection of arguments for invoking getLoadBalancer.
 */
export interface GetLoadBalancerArgs {
    /**
     * The id of the load balancer to retrieve (You can find this id from service annotations 'kubernetes.civo.com/loadbalancer-id')
     */
    id?: string;
    /**
     * The name of the load balancer (You can find this name from service annotations 'kubernetes.civo.com/loadbalancer-name')
     */
    name?: string;
    /**
     * The region of the load balancer, if you declare this field, the datasource will use this value instead of the one defined in the provider
     */
    region?: string;
}

/**
 * A collection of values returned by getLoadBalancer.
 */
export interface GetLoadBalancerResult {
    /**
     * The algorithm used by the load balancer
     */
    readonly algorithm: string;
    readonly backends: outputs.GetLoadBalancerBackend[];
    /**
     * The cluster id of the load balancer
     */
    readonly clusterId: string;
    /**
     * The enabled proxy protocol of the load balancer
     */
    readonly enableProxyProtocol: string;
    /**
     * The external traffic policy of the load balancer
     */
    readonly externalTrafficPolicy: string;
    /**
     * The firewall id of the load balancer
     */
    readonly firewallId: string;
    /**
     * The id of the load balancer to retrieve (You can find this id from service annotations 'kubernetes.civo.com/loadbalancer-id')
     */
    readonly id?: string;
    /**
     * The name of the load balancer (You can find this name from service annotations 'kubernetes.civo.com/loadbalancer-name')
     */
    readonly name?: string;
    /**
     * The private ip of the load balancer
     */
    readonly privateIp: string;
    /**
     * The public ip of the load balancer
     */
    readonly publicIp: string;
    /**
     * The region of the load balancer, if you declare this field, the datasource will use this value instead of the one defined in the provider
     */
    readonly region?: string;
    /**
     * The session affinity of the load balancer
     */
    readonly sessionAffinity: string;
    /**
     * The session affinity config timeout of the load balancer
     */
    readonly sessionAffinityConfigTimeout: number;
    /**
     * The state of the load balancer
     */
    readonly state: string;
}
/**
 * Get information on a load balancer for use in other resources. This data source provides all of the load balancers properties as configured on your Civo account.
 *
 * An error will be raised if the provided load balancer name does not exist in your Civo account.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as civo from "@pulumi/civo";
 *
 * // TODO
 * const my-lb = civo.getLoadBalancer({
 *     name: "lb-name",
 *     region: "LON1",
 * });
 * export const civoLoadbalancerOutput = my_lb.then(my_lb => my_lb.publicIp);
 * ```
 */
export function getLoadBalancerOutput(args?: GetLoadBalancerOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetLoadBalancerResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("civo:index/getLoadBalancer:getLoadBalancer", {
        "id": args.id,
        "name": args.name,
        "region": args.region,
    }, opts);
}

/**
 * A collection of arguments for invoking getLoadBalancer.
 */
export interface GetLoadBalancerOutputArgs {
    /**
     * The id of the load balancer to retrieve (You can find this id from service annotations 'kubernetes.civo.com/loadbalancer-id')
     */
    id?: pulumi.Input<string>;
    /**
     * The name of the load balancer (You can find this name from service annotations 'kubernetes.civo.com/loadbalancer-name')
     */
    name?: pulumi.Input<string>;
    /**
     * The region of the load balancer, if you declare this field, the datasource will use this value instead of the one defined in the provider
     */
    region?: pulumi.Input<string>;
}

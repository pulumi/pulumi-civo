// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export function getReservedIp(args?: GetReservedIpArgs, opts?: pulumi.InvokeOptions): Promise<GetReservedIpResult> {
    args = args || {};

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("civo:index/getReservedIp:getReservedIp", {
        "id": args.id,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getReservedIp.
 */
export interface GetReservedIpArgs {
    /**
     * ID for the ip address
     */
    id?: string;
    /**
     * Name for the ip address
     */
    name?: string;
}

/**
 * A collection of values returned by getReservedIp.
 */
export interface GetReservedIpResult {
    /**
     * ID for the ip address
     */
    readonly id?: string;
    /**
     * The ID of the instance the IP is attached to
     */
    readonly instanceId: string;
    /**
     * The name of the instance the IP is attached to
     */
    readonly instanceName: string;
    /**
     * The IP Address requested
     */
    readonly ip: string;
    /**
     * Name for the ip address
     */
    readonly name?: string;
    /**
     * The region the ip address is in
     */
    readonly region: string;
}
export function getReservedIpOutput(args?: GetReservedIpOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetReservedIpResult> {
    return pulumi.output(args).apply((a: any) => getReservedIp(a, opts))
}

/**
 * A collection of arguments for invoking getReservedIp.
 */
export interface GetReservedIpOutputArgs {
    /**
     * ID for the ip address
     */
    id?: pulumi.Input<string>;
    /**
     * Name for the ip address
     */
    name?: pulumi.Input<string>;
}

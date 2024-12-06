// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Get information on an instance for use in other resources. This data source provides all of the instance's properties as configured on your Civo account.
 *
 * Note: This data source returns a single instance. When specifying a hostname, an error will be raised if more than one instances found.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as civo from "@pulumi/civo";
 *
 * const myhostaname = civo.getInstance({
 *     hostname: "myhostname.com",
 * });
 * export const instanceOutput = myhostaname.then(myhostaname => myhostaname.publicIp);
 * ```
 */
export function getInstance(args?: GetInstanceArgs, opts?: pulumi.InvokeOptions): Promise<GetInstanceResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("civo:index/getInstance:getInstance", {
        "hostname": args.hostname,
        "id": args.id,
        "region": args.region,
    }, opts);
}

/**
 * A collection of arguments for invoking getInstance.
 */
export interface GetInstanceArgs {
    /**
     * The hostname of the Instance
     */
    hostname?: string;
    /**
     * The ID of this resource.
     */
    id?: string;
    /**
     * The region of an existing Instance
     */
    region?: string;
}

/**
 * A collection of values returned by getInstance.
 */
export interface GetInstanceResult {
    /**
     * Total cpu of the instance
     */
    readonly cpuCores: number;
    /**
     * The date of creation of the instance
     */
    readonly createdAt: string;
    /**
     * The size of the disk
     */
    readonly diskGb: number;
    /**
     * The ID of the firewall used
     */
    readonly firewallId: string;
    /**
     * The hostname of the Instance
     */
    readonly hostname?: string;
    /**
     * The ID of this resource.
     */
    readonly id?: string;
    /**
     * Instance initial password
     */
    readonly initialPassword: string;
    /**
     * The name of the initial user created on the server
     */
    readonly initialUser: string;
    /**
     * his will be the ID of the network
     */
    readonly networkId: string;
    /**
     * The notes of the instance
     */
    readonly notes: string;
    /**
     * The private IP
     */
    readonly privateIp: string;
    /**
     * Is the ip that is used to route the public ip from the internet to the instance using NAT
     */
    readonly pseudoIp: string;
    /**
     * The public IP
     */
    readonly publicIp: string;
    /**
     * Total ram of the instance
     */
    readonly ramMb: number;
    /**
     * The region of an existing Instance
     */
    readonly region?: string;
    /**
     * A fully qualified domain name
     */
    readonly reverseDns: string;
    /**
     * The contents of a script uploaded
     */
    readonly script: string;
    /**
     * The name of the size
     */
    readonly size: string;
    /**
     * The ID SSH key
     */
    readonly sshkeyId: string;
    /**
     * The status of the instance
     */
    readonly status: string;
    /**
     * An optional list of tags
     */
    readonly tags: string[];
    /**
     * The ID for the disk image/template to used to build the instance
     */
    readonly template: string;
}
/**
 * Get information on an instance for use in other resources. This data source provides all of the instance's properties as configured on your Civo account.
 *
 * Note: This data source returns a single instance. When specifying a hostname, an error will be raised if more than one instances found.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as civo from "@pulumi/civo";
 *
 * const myhostaname = civo.getInstance({
 *     hostname: "myhostname.com",
 * });
 * export const instanceOutput = myhostaname.then(myhostaname => myhostaname.publicIp);
 * ```
 */
export function getInstanceOutput(args?: GetInstanceOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetInstanceResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("civo:index/getInstance:getInstance", {
        "hostname": args.hostname,
        "id": args.id,
        "region": args.region,
    }, opts);
}

/**
 * A collection of arguments for invoking getInstance.
 */
export interface GetInstanceOutputArgs {
    /**
     * The hostname of the Instance
     */
    hostname?: pulumi.Input<string>;
    /**
     * The ID of this resource.
     */
    id?: pulumi.Input<string>;
    /**
     * The region of an existing Instance
     */
    region?: pulumi.Input<string>;
}

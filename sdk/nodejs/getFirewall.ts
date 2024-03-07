// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Retrieve information about a firewall for use in other resources.
 *
 * This data source provides all of the firewall's properties as configured on your Civo account.
 *
 * Firewalls may be looked up by id or name, and you can optionally pass region if you want to make a lookup for a specific firewall inside that region.
 *
 * ## Example Usage
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as civo from "@pulumi/civo";
 *
 * const test = civo.getFirewall({
 *     name: "test-firewall",
 *     region: "LON1",
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 */
export function getFirewall(args?: GetFirewallArgs, opts?: pulumi.InvokeOptions): Promise<GetFirewallResult> {
    args = args || {};

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("civo:index/getFirewall:getFirewall", {
        "id": args.id,
        "name": args.name,
        "region": args.region,
    }, opts);
}

/**
 * A collection of arguments for invoking getFirewall.
 */
export interface GetFirewallArgs {
    /**
     * The ID of this resource.
     */
    id?: string;
    /**
     * The name of the firewall
     */
    name?: string;
    /**
     * The region where the firewall is
     */
    region?: string;
}

/**
 * A collection of values returned by getFirewall.
 */
export interface GetFirewallResult {
    /**
     * The ID of this resource.
     */
    readonly id?: string;
    /**
     * The name of the firewall
     */
    readonly name?: string;
    /**
     * The id of the associated network
     */
    readonly networkId: string;
    /**
     * The region where the firewall is
     */
    readonly region?: string;
}
/**
 * Retrieve information about a firewall for use in other resources.
 *
 * This data source provides all of the firewall's properties as configured on your Civo account.
 *
 * Firewalls may be looked up by id or name, and you can optionally pass region if you want to make a lookup for a specific firewall inside that region.
 *
 * ## Example Usage
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as civo from "@pulumi/civo";
 *
 * const test = civo.getFirewall({
 *     name: "test-firewall",
 *     region: "LON1",
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 */
export function getFirewallOutput(args?: GetFirewallOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetFirewallResult> {
    return pulumi.output(args).apply((a: any) => getFirewall(a, opts))
}

/**
 * A collection of arguments for invoking getFirewall.
 */
export interface GetFirewallOutputArgs {
    /**
     * The ID of this resource.
     */
    id?: pulumi.Input<string>;
    /**
     * The name of the firewall
     */
    name?: pulumi.Input<string>;
    /**
     * The region where the firewall is
     */
    region?: pulumi.Input<string>;
}

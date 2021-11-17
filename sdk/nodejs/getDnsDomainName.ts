// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Get information on a domain. This data source provides the name and the id.
 *
 * An error will be raised if the provided domain name is not in your Civo account.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as civo from "@pulumi/civo";
 *
 * const domain = civo.getDnsDomainName({
 *     name: "domain.com",
 * });
 * export const domainOutput = domain.then(domain => domain.name);
 * export const domainIdOutput = domain.then(domain => domain.id);
 * ```
 */
export function getDnsDomainName(args?: GetDnsDomainNameArgs, opts?: pulumi.InvokeOptions): Promise<GetDnsDomainNameResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("civo:index/getDnsDomainName:getDnsDomainName", {
        "id": args.id,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getDnsDomainName.
 */
export interface GetDnsDomainNameArgs {
    /**
     * The ID of this resource.
     */
    id?: string;
    /**
     * The name of the domain
     */
    name?: string;
}

/**
 * A collection of values returned by getDnsDomainName.
 */
export interface GetDnsDomainNameResult {
    /**
     * The ID of this resource.
     */
    readonly id?: string;
    /**
     * The name of the domain
     */
    readonly name?: string;
}

export function getDnsDomainNameOutput(args?: GetDnsDomainNameOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDnsDomainNameResult> {
    return pulumi.output(args).apply(a => getDnsDomainName(a, opts))
}

/**
 * A collection of arguments for invoking getDnsDomainName.
 */
export interface GetDnsDomainNameOutputArgs {
    /**
     * The ID of this resource.
     */
    id?: pulumi.Input<string>;
    /**
     * The name of the domain
     */
    name?: pulumi.Input<string>;
}

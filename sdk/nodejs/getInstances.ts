// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export function getInstances(args?: GetInstancesArgs, opts?: pulumi.InvokeOptions): Promise<GetInstancesResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("civo:index/getInstances:getInstances", {
        "filters": args.filters,
        "sorts": args.sorts,
    }, opts);
}

/**
 * A collection of arguments for invoking getInstances.
 */
export interface GetInstancesArgs {
    /**
     * Filter the results.
     * The `filter` block is documented below.
     */
    readonly filters?: inputs.GetInstancesFilter[];
    /**
     * Sort the results.
     * The `sort` block is documented below.
     */
    readonly sorts?: inputs.GetInstancesSort[];
}

/**
 * A collection of values returned by getInstances.
 */
export interface GetInstancesResult {
    readonly filters?: outputs.GetInstancesFilter[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * A list of Instances satisfying any `filter` and `sort` criteria. Each instance has the following attributes:
     */
    readonly instances: outputs.GetInstancesInstance[];
    readonly sorts?: outputs.GetInstancesSort[];
}

// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * Retrieves information about the instance sizes that Civo supports, with the ability to filter the results.
 */
export function getInstancesSize(args?: GetInstancesSizeArgs, opts?: pulumi.InvokeOptions): Promise<GetInstancesSizeResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("civo:index/getInstancesSize:getInstancesSize", {
        "filters": args.filters,
        "sorts": args.sorts,
    }, opts);
}

/**
 * A collection of arguments for invoking getInstancesSize.
 */
export interface GetInstancesSizeArgs {
    /**
     * One or more key/value pairs on which to filter results
     */
    filters?: inputs.GetInstancesSizeFilter[];
    /**
     * One or more key/direction pairs on which to sort results
     */
    sorts?: inputs.GetInstancesSizeSort[];
}

/**
 * A collection of values returned by getInstancesSize.
 */
export interface GetInstancesSizeResult {
    /**
     * One or more key/value pairs on which to filter results
     */
    readonly filters?: outputs.GetInstancesSizeFilter[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly sizes: outputs.GetInstancesSizeSize[];
    /**
     * One or more key/direction pairs on which to sort results
     */
    readonly sorts?: outputs.GetInstancesSizeSort[];
}

export function getInstancesSizeOutput(args?: GetInstancesSizeOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetInstancesSizeResult> {
    return pulumi.output(args).apply(a => getInstancesSize(a, opts))
}

/**
 * A collection of arguments for invoking getInstancesSize.
 */
export interface GetInstancesSizeOutputArgs {
    /**
     * One or more key/value pairs on which to filter results
     */
    filters?: pulumi.Input<pulumi.Input<inputs.GetInstancesSizeFilterArgs>[]>;
    /**
     * One or more key/direction pairs on which to sort results
     */
    sorts?: pulumi.Input<pulumi.Input<inputs.GetInstancesSizeSortArgs>[]>;
}

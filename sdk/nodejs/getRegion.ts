// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Retrieves information about the region that Civo supports, with the ability to filter the results.
 */
export function getRegion(args?: GetRegionArgs, opts?: pulumi.InvokeOptions): Promise<GetRegionResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("civo:index/getRegion:getRegion", {
        "filters": args.filters,
        "sorts": args.sorts,
    }, opts);
}

/**
 * A collection of arguments for invoking getRegion.
 */
export interface GetRegionArgs {
    /**
     * One or more key/value pairs on which to filter results
     */
    filters?: inputs.GetRegionFilter[];
    /**
     * One or more key/direction pairs on which to sort results
     */
    sorts?: inputs.GetRegionSort[];
}

/**
 * A collection of values returned by getRegion.
 */
export interface GetRegionResult {
    /**
     * One or more key/value pairs on which to filter results
     */
    readonly filters?: outputs.GetRegionFilter[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly regions: outputs.GetRegionRegion[];
    /**
     * One or more key/direction pairs on which to sort results
     */
    readonly sorts?: outputs.GetRegionSort[];
}
/**
 * Retrieves information about the region that Civo supports, with the ability to filter the results.
 */
export function getRegionOutput(args?: GetRegionOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetRegionResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("civo:index/getRegion:getRegion", {
        "filters": args.filters,
        "sorts": args.sorts,
    }, opts);
}

/**
 * A collection of arguments for invoking getRegion.
 */
export interface GetRegionOutputArgs {
    /**
     * One or more key/value pairs on which to filter results
     */
    filters?: pulumi.Input<pulumi.Input<inputs.GetRegionFilterArgs>[]>;
    /**
     * One or more key/direction pairs on which to sort results
     */
    sorts?: pulumi.Input<pulumi.Input<inputs.GetRegionSortArgs>[]>;
}

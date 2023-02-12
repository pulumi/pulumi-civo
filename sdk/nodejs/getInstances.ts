// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Get information on instances for use in other resources, with the ability to filter and sort the results. If no filters are specified, all instances will be returned.
 *
 * Note: You can use the `civo.Instance` data source to obtain metadata about a single instance if you already know the id, unique hostname, or unique tag to retrieve.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as civo from "@pulumi/civo";
 *
 * const small-size = civo.getInstances({
 *     region: "LON1",
 *     filters: [{
 *         key: "size",
 *         values: [g3.small],
 *     }],
 * });
 * ```
 */
export function getInstances(args?: GetInstancesArgs, opts?: pulumi.InvokeOptions): Promise<GetInstancesResult> {
    args = args || {};

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("civo:index/getInstances:getInstances", {
        "filters": args.filters,
        "region": args.region,
        "sorts": args.sorts,
    }, opts);
}

/**
 * A collection of arguments for invoking getInstances.
 */
export interface GetInstancesArgs {
    /**
     * One or more key/value pairs on which to filter results
     */
    filters?: inputs.GetInstancesFilter[];
    /**
     * If used, all instances will be from the provided region
     */
    region?: string;
    /**
     * One or more key/direction pairs on which to sort results
     */
    sorts?: inputs.GetInstancesSort[];
}

/**
 * A collection of values returned by getInstances.
 */
export interface GetInstancesResult {
    /**
     * One or more key/value pairs on which to filter results
     */
    readonly filters?: outputs.GetInstancesFilter[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly instances: outputs.GetInstancesInstance[];
    /**
     * If used, all instances will be from the provided region
     */
    readonly region?: string;
    /**
     * One or more key/direction pairs on which to sort results
     */
    readonly sorts?: outputs.GetInstancesSort[];
}
/**
 * Get information on instances for use in other resources, with the ability to filter and sort the results. If no filters are specified, all instances will be returned.
 *
 * Note: You can use the `civo.Instance` data source to obtain metadata about a single instance if you already know the id, unique hostname, or unique tag to retrieve.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as civo from "@pulumi/civo";
 *
 * const small-size = civo.getInstances({
 *     region: "LON1",
 *     filters: [{
 *         key: "size",
 *         values: [g3.small],
 *     }],
 * });
 * ```
 */
export function getInstancesOutput(args?: GetInstancesOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetInstancesResult> {
    return pulumi.output(args).apply((a: any) => getInstances(a, opts))
}

/**
 * A collection of arguments for invoking getInstances.
 */
export interface GetInstancesOutputArgs {
    /**
     * One or more key/value pairs on which to filter results
     */
    filters?: pulumi.Input<pulumi.Input<inputs.GetInstancesFilterArgs>[]>;
    /**
     * If used, all instances will be from the provided region
     */
    region?: pulumi.Input<string>;
    /**
     * One or more key/direction pairs on which to sort results
     */
    sorts?: pulumi.Input<pulumi.Input<inputs.GetInstancesSortArgs>[]>;
}

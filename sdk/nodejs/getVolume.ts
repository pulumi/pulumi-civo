// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Get information on a volume for use in other resources. This data source provides all of the volumes properties as configured on your Civo account.
 *
 * An error will be raised if the provided volume name does not exist in your Civo account.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as civo from "@pulumi/civo";
 *
 * const myvolume = civo.getVolume({
 *     name: "test-volume-name",
 * });
 * export const volumeOutput = myvolume;
 * ```
 */
export function getVolume(args?: GetVolumeArgs, opts?: pulumi.InvokeOptions): Promise<GetVolumeResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("civo:index/getVolume:getVolume", {
        "id": args.id,
        "name": args.name,
        "region": args.region,
    }, opts);
}

/**
 * A collection of arguments for invoking getVolume.
 */
export interface GetVolumeArgs {
    /**
     * The ID of this resource.
     */
    id?: string;
    /**
     * The name of the volume
     */
    name?: string;
    /**
     * The region where volume is running
     */
    region?: string;
}

/**
 * A collection of values returned by getVolume.
 */
export interface GetVolumeResult {
    /**
     * The date of the creation of the volume
     */
    readonly createdAt: string;
    /**
     * The ID of this resource.
     */
    readonly id?: string;
    /**
     * The mount point of the volume
     */
    readonly mountPoint: string;
    /**
     * The name of the volume
     */
    readonly name?: string;
    /**
     * The region where volume is running
     */
    readonly region?: string;
    /**
     * The size of the volume (in GB)
     */
    readonly sizeGb: number;
}
/**
 * Get information on a volume for use in other resources. This data source provides all of the volumes properties as configured on your Civo account.
 *
 * An error will be raised if the provided volume name does not exist in your Civo account.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as civo from "@pulumi/civo";
 *
 * const myvolume = civo.getVolume({
 *     name: "test-volume-name",
 * });
 * export const volumeOutput = myvolume;
 * ```
 */
export function getVolumeOutput(args?: GetVolumeOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetVolumeResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("civo:index/getVolume:getVolume", {
        "id": args.id,
        "name": args.name,
        "region": args.region,
    }, opts);
}

/**
 * A collection of arguments for invoking getVolume.
 */
export interface GetVolumeOutputArgs {
    /**
     * The ID of this resource.
     */
    id?: pulumi.Input<string>;
    /**
     * The name of the volume
     */
    name?: pulumi.Input<string>;
    /**
     * The region where volume is running
     */
    region?: pulumi.Input<string>;
}

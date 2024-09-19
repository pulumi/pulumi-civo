// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Get information of an Object Store for use in other resources. This data source provides all of the Object Store's properties as configured on your Civo account.
 *
 * Note: This data source returns a single Object Store. When specifying a name, an error will be raised if more than one Object Stores with the same name found.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as civo from "@pulumi/civo";
 *
 * const backup = civo.getObjectStore({
 *     name: "backup-server",
 * });
 * ```
 */
export function getObjectStore(args?: GetObjectStoreArgs, opts?: pulumi.InvokeOptions): Promise<GetObjectStoreResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("civo:index/getObjectStore:getObjectStore", {
        "id": args.id,
        "name": args.name,
        "region": args.region,
    }, opts);
}

/**
 * A collection of arguments for invoking getObjectStore.
 */
export interface GetObjectStoreArgs {
    /**
     * The ID of the Object Store
     */
    id?: string;
    /**
     * The name of the Object Store
     */
    name?: string;
    /**
     * The region of an existing Object Store
     */
    region?: string;
}

/**
 * A collection of values returned by getObjectStore.
 */
export interface GetObjectStoreResult {
    /**
     * The access key ID from the Object Store credential. If this is not set, a new credential will be created.
     */
    readonly accessKeyId: string;
    /**
     * The endpoint of the Object Store
     */
    readonly bucketUrl: string;
    /**
     * The ID of the Object Store
     */
    readonly id?: string;
    /**
     * The maximum size of the Object Store
     */
    readonly maxSizeGb: number;
    /**
     * The name of the Object Store
     */
    readonly name?: string;
    /**
     * The region of an existing Object Store
     */
    readonly region?: string;
    /**
     * The status of the Object Store
     */
    readonly status: string;
}
/**
 * Get information of an Object Store for use in other resources. This data source provides all of the Object Store's properties as configured on your Civo account.
 *
 * Note: This data source returns a single Object Store. When specifying a name, an error will be raised if more than one Object Stores with the same name found.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as civo from "@pulumi/civo";
 *
 * const backup = civo.getObjectStore({
 *     name: "backup-server",
 * });
 * ```
 */
export function getObjectStoreOutput(args?: GetObjectStoreOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetObjectStoreResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("civo:index/getObjectStore:getObjectStore", {
        "id": args.id,
        "name": args.name,
        "region": args.region,
    }, opts);
}

/**
 * A collection of arguments for invoking getObjectStore.
 */
export interface GetObjectStoreOutputArgs {
    /**
     * The ID of the Object Store
     */
    id?: pulumi.Input<string>;
    /**
     * The name of the Object Store
     */
    name?: pulumi.Input<string>;
    /**
     * The region of an existing Object Store
     */
    region?: pulumi.Input<string>;
}

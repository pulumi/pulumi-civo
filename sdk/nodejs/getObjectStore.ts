// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Get information of an Object Store for use in other resources. This data source provides all of the Object Store's properties as configured on your Civo account.
 *
 * Note: This data source returns a single Object Store. When specifying a name, an error will be raised if more than one Object Stores with the same name found.
 */
export function getObjectStore(args?: GetObjectStoreArgs, opts?: pulumi.InvokeOptions): Promise<GetObjectStoreResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("civo:index/getObjectStore:getObjectStore", {
        "id": args.id,
        "maxSizeGb": args.maxSizeGb,
        "name": args.name,
        "region": args.region,
    }, opts);
}

/**
 * A collection of arguments for invoking getObjectStore.
 */
export interface GetObjectStoreArgs {
    id?: string;
    maxSizeGb?: number;
    name?: string;
    region?: string;
}

/**
 * A collection of values returned by getObjectStore.
 */
export interface GetObjectStoreResult {
    readonly accessKeyId: string;
    readonly endpoint: string;
    readonly generatedName: string;
    readonly id?: string;
    readonly maxSizeGb?: number;
    readonly name?: string;
    readonly region?: string;
    readonly secretAccessKey: string;
    readonly status: string;
}

export function getObjectStoreOutput(args?: GetObjectStoreOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetObjectStoreResult> {
    return pulumi.output(args).apply(a => getObjectStore(a, opts))
}

/**
 * A collection of arguments for invoking getObjectStore.
 */
export interface GetObjectStoreOutputArgs {
    id?: pulumi.Input<string>;
    maxSizeGb?: pulumi.Input<number>;
    name?: pulumi.Input<string>;
    region?: pulumi.Input<string>;
}

// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Get information of an Object Store Credential for use in other resources. This data source provides all of the Object Store Credential's properties as configured on your Civo account.
 *
 * Note: This data source returns a single Object Store Credential. When specifying a name, an error will be raised if more than one Object Store Credentials with the same name found.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as civo from "@pulumi/civo";
 *
 * // Read a credential for the object store
 * const backup = civo.getObjectStoreCredential({
 *     name: "backup-server",
 * });
 * // Use the credential to create a bucket
 * const backupObjectStore = new civo.ObjectStore("backup", {
 *     name: "backup-server",
 *     maxSizeGb: 500,
 *     region: "LON1",
 *     accessKeyId: backup.then(backup => backup.accessKeyId),
 * });
 * ```
 */
export function getObjectStoreCredential(args?: GetObjectStoreCredentialArgs, opts?: pulumi.InvokeOptions): Promise<GetObjectStoreCredentialResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("civo:index/getObjectStoreCredential:getObjectStoreCredential", {
        "id": args.id,
        "name": args.name,
        "region": args.region,
    }, opts);
}

/**
 * A collection of arguments for invoking getObjectStoreCredential.
 */
export interface GetObjectStoreCredentialArgs {
    /**
     * The ID of the Object Store Credential
     */
    id?: string;
    /**
     * The name of the Object Store Credential
     */
    name?: string;
    /**
     * The region of an existing Object Store
     */
    region?: string;
}

/**
 * A collection of values returned by getObjectStoreCredential.
 */
export interface GetObjectStoreCredentialResult {
    /**
     * The access key id of the Object Store Credential
     */
    readonly accessKeyId: string;
    /**
     * The ID of the Object Store Credential
     */
    readonly id?: string;
    /**
     * The name of the Object Store Credential
     */
    readonly name?: string;
    /**
     * The region of an existing Object Store
     */
    readonly region?: string;
    /**
     * The secret access key of the Object Store Credential
     */
    readonly secretAccessKey: string;
    /**
     * The status of the Object Store Credential
     */
    readonly status: string;
}
/**
 * Get information of an Object Store Credential for use in other resources. This data source provides all of the Object Store Credential's properties as configured on your Civo account.
 *
 * Note: This data source returns a single Object Store Credential. When specifying a name, an error will be raised if more than one Object Store Credentials with the same name found.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as civo from "@pulumi/civo";
 *
 * // Read a credential for the object store
 * const backup = civo.getObjectStoreCredential({
 *     name: "backup-server",
 * });
 * // Use the credential to create a bucket
 * const backupObjectStore = new civo.ObjectStore("backup", {
 *     name: "backup-server",
 *     maxSizeGb: 500,
 *     region: "LON1",
 *     accessKeyId: backup.then(backup => backup.accessKeyId),
 * });
 * ```
 */
export function getObjectStoreCredentialOutput(args?: GetObjectStoreCredentialOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetObjectStoreCredentialResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("civo:index/getObjectStoreCredential:getObjectStoreCredential", {
        "id": args.id,
        "name": args.name,
        "region": args.region,
    }, opts);
}

/**
 * A collection of arguments for invoking getObjectStoreCredential.
 */
export interface GetObjectStoreCredentialOutputArgs {
    /**
     * The ID of the Object Store Credential
     */
    id?: pulumi.Input<string>;
    /**
     * The name of the Object Store Credential
     */
    name?: pulumi.Input<string>;
    /**
     * The region of an existing Object Store
     */
    region?: pulumi.Input<string>;
}

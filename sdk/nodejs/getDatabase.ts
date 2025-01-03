// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Get information of an Database for use in other resources. This data source provides all of the Database's properties as configured on your Civo account.
 *
 * Note: This data source returns a single Database. When specifying a name, an error will be raised if more than one Databases with the same name found.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as civo from "@pulumi/civo";
 *
 * const test = civo.getDatabase({
 *     name: "test-database",
 *     region: "LON1",
 * });
 * ```
 */
export function getDatabase(args?: GetDatabaseArgs, opts?: pulumi.InvokeOptions): Promise<GetDatabaseResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("civo:index/getDatabase:getDatabase", {
        "id": args.id,
        "name": args.name,
        "region": args.region,
    }, opts);
}

/**
 * A collection of arguments for invoking getDatabase.
 */
export interface GetDatabaseArgs {
    /**
     * The ID of the Database
     */
    id?: string;
    /**
     * The name of the Database
     */
    name?: string;
    /**
     * The region of an existing Database
     */
    region?: string;
}

/**
 * A collection of values returned by getDatabase.
 */
export interface GetDatabaseResult {
    /**
     * The DNS endpoint of the database
     */
    readonly dnsEndpoint: string;
    /**
     * The endpoint of the database
     */
    readonly endpoint: string;
    /**
     * The engine of the database
     */
    readonly engine: string;
    /**
     * The firewall id of the Database
     */
    readonly firewallId: string;
    /**
     * The ID of the Database
     */
    readonly id?: string;
    /**
     * The name of the Database
     */
    readonly name?: string;
    /**
     * The network id of the Database
     */
    readonly networkId: string;
    /**
     * Count of nodes
     */
    readonly nodes: number;
    /**
     * The password of the database
     */
    readonly password: string;
    /**
     * The port of the database
     */
    readonly port: number;
    /**
     * The region of an existing Database
     */
    readonly region: string;
    /**
     * Size of the database
     */
    readonly size: string;
    /**
     * The status of the database
     */
    readonly status: string;
    /**
     * The username of the database
     */
    readonly username: string;
    /**
     * The version of the database
     */
    readonly version: string;
}
/**
 * Get information of an Database for use in other resources. This data source provides all of the Database's properties as configured on your Civo account.
 *
 * Note: This data source returns a single Database. When specifying a name, an error will be raised if more than one Databases with the same name found.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as civo from "@pulumi/civo";
 *
 * const test = civo.getDatabase({
 *     name: "test-database",
 *     region: "LON1",
 * });
 * ```
 */
export function getDatabaseOutput(args?: GetDatabaseOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetDatabaseResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("civo:index/getDatabase:getDatabase", {
        "id": args.id,
        "name": args.name,
        "region": args.region,
    }, opts);
}

/**
 * A collection of arguments for invoking getDatabase.
 */
export interface GetDatabaseOutputArgs {
    /**
     * The ID of the Database
     */
    id?: pulumi.Input<string>;
    /**
     * The name of the Database
     */
    name?: pulumi.Input<string>;
    /**
     * The region of an existing Database
     */
    region?: pulumi.Input<string>;
}

// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * Provides access to the available Civo Kubernetes versions, with the ability to filter the results.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as civo from "@pulumi/civo";
 *
 * const stable = pulumi.output(civo.getKubernetesVersion({
 *     filters: [{
 *         key: "type",
 *         values: ["stable"],
 *     }],
 * }, { async: true }));
 * ```
 *
 * <!-- schema generated by tfplugindocs -->
 * ## Schema
 *
 * ### Optional
 *
 * - **filter** (Block Set) One or more key/value pairs on which to filter results (see below for nested schema)
 * - **id** (String) The ID of this resource.
 * - **sort** (Block List) One or more key/direction pairs on which to sort results (see below for nested schema)
 *
 * ### Read-Only
 *
 * - **versions** (List of Object) (see below for nested schema)
 *
 * <a id="nestedblock--filter"></a>
 * ### Nested Schema for `filter`
 *
 * Required:
 *
 * - **key** (String) Filter versions by this key. This may be one of `default`, `label`, `type`, `version`.
 * - **values** (List of String) Only retrieves `versions` which keys has value that matches one of the values provided here
 *
 * Optional:
 *
 * - **all** (Boolean) Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
 * - **match_by** (String) One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
 *
 * <a id="nestedblock--sort"></a>
 * ### Nested Schema for `sort`
 *
 * Required:
 *
 * - **key** (String) Sort versions by this key. This may be one of `default`, `label`, `type`, `version`.
 *
 * Optional:
 *
 * - **direction** (String) The sort direction. This may be either `asc` or `desc`.
 *
 * <a id="nestedatt--versions"></a>
 * ### Nested Schema for `versions`
 *
 * Read-Only:
 *
 * - **default** (Boolean)
 * - **label** (String)
 * - **type** (String)
 * - **version** (String)
 */
export function getKubernetesVersion(args?: GetKubernetesVersionArgs, opts?: pulumi.InvokeOptions): Promise<GetKubernetesVersionResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("civo:index/getKubernetesVersion:getKubernetesVersion", {
        "filters": args.filters,
        "sorts": args.sorts,
    }, opts);
}

/**
 * A collection of arguments for invoking getKubernetesVersion.
 */
export interface GetKubernetesVersionArgs {
    readonly filters?: inputs.GetKubernetesVersionFilter[];
    readonly sorts?: inputs.GetKubernetesVersionSort[];
}

/**
 * A collection of values returned by getKubernetesVersion.
 */
export interface GetKubernetesVersionResult {
    readonly filters?: outputs.GetKubernetesVersionFilter[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly sorts?: outputs.GetKubernetesVersionSort[];
    readonly versions: outputs.GetKubernetesVersionVersion[];
}

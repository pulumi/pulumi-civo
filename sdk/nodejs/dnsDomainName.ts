// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a Civo DNS domain name resource.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as civo from "@pulumi/civo";
 *
 * // Create a new domain name
 * const main = new civo.DnsDomainName("main", {});
 * ```
 *
 * ## Import
 *
 * # using domain name
 *
 * ```sh
 *  $ pulumi import civo:index/dnsDomainName:DnsDomainName main mydomain.com
 * ```
 */
export class DnsDomainName extends pulumi.CustomResource {
    /**
     * Get an existing DnsDomainName resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DnsDomainNameState, opts?: pulumi.CustomResourceOptions): DnsDomainName {
        return new DnsDomainName(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'civo:index/dnsDomainName:DnsDomainName';

    /**
     * Returns true if the given object is an instance of DnsDomainName.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DnsDomainName {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DnsDomainName.__pulumiType;
    }

    /**
     * The account ID of the domain
     */
    public /*out*/ readonly accountId!: pulumi.Output<string>;
    /**
     * The name of the domain
     */
    public readonly name!: pulumi.Output<string>;

    /**
     * Create a DnsDomainName resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: DnsDomainNameArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DnsDomainNameArgs | DnsDomainNameState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as DnsDomainNameState | undefined;
            resourceInputs["accountId"] = state ? state.accountId : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
        } else {
            const args = argsOrState as DnsDomainNameArgs | undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["accountId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(DnsDomainName.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DnsDomainName resources.
 */
export interface DnsDomainNameState {
    /**
     * The account ID of the domain
     */
    accountId?: pulumi.Input<string>;
    /**
     * The name of the domain
     */
    name?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a DnsDomainName resource.
 */
export interface DnsDomainNameArgs {
    /**
     * The name of the domain
     */
    name?: pulumi.Input<string>;
}

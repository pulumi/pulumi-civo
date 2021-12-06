// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a Civo DNS domain record resource.
 *
 * ## Import
 *
 * # using domain_id:domain_record_id
 *
 * ```sh
 *  $ pulumi import civo:index/dnsDomainRecord:DnsDomainRecord www a3cd6832-9577-4017-afd7-17d239fc0bf0:c9a39d14-ee1b-4870-8fb0-a2d4f465e822
 * ```
 */
export class DnsDomainRecord extends pulumi.CustomResource {
    /**
     * Get an existing DnsDomainRecord resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DnsDomainRecordState, opts?: pulumi.CustomResourceOptions): DnsDomainRecord {
        return new DnsDomainRecord(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'civo:index/dnsDomainRecord:DnsDomainRecord';

    /**
     * Returns true if the given object is an instance of DnsDomainRecord.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DnsDomainRecord {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DnsDomainRecord.__pulumiType;
    }

    /**
     * The account ID of this resource
     */
    public /*out*/ readonly accountId!: pulumi.Output<string>;
    /**
     * Timestamp when this resource was created
     */
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    /**
     * ID from domain name
     */
    public readonly domainId!: pulumi.Output<string>;
    /**
     * The portion before the domain name (e.g. www) or an @ for the apex/root domain (you cannot use an A record with an amex/root domain)
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Useful for MX records only, the priority mail should be attempted it (defaults to 10)
     */
    public readonly priority!: pulumi.Output<number | undefined>;
    /**
     * How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified is 600)
     */
    public readonly ttl!: pulumi.Output<number>;
    /**
     * The choice of RR type from a, cname, mx or txt
     */
    public readonly type!: pulumi.Output<string>;
    /**
     * Timestamp when this resource was updated
     */
    public /*out*/ readonly updatedAt!: pulumi.Output<string>;
    /**
     * The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record
     */
    public readonly value!: pulumi.Output<string>;

    /**
     * Create a DnsDomainRecord resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DnsDomainRecordArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DnsDomainRecordArgs | DnsDomainRecordState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as DnsDomainRecordState | undefined;
            resourceInputs["accountId"] = state ? state.accountId : undefined;
            resourceInputs["createdAt"] = state ? state.createdAt : undefined;
            resourceInputs["domainId"] = state ? state.domainId : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["priority"] = state ? state.priority : undefined;
            resourceInputs["ttl"] = state ? state.ttl : undefined;
            resourceInputs["type"] = state ? state.type : undefined;
            resourceInputs["updatedAt"] = state ? state.updatedAt : undefined;
            resourceInputs["value"] = state ? state.value : undefined;
        } else {
            const args = argsOrState as DnsDomainRecordArgs | undefined;
            if ((!args || args.domainId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'domainId'");
            }
            if ((!args || args.ttl === undefined) && !opts.urn) {
                throw new Error("Missing required property 'ttl'");
            }
            if ((!args || args.type === undefined) && !opts.urn) {
                throw new Error("Missing required property 'type'");
            }
            if ((!args || args.value === undefined) && !opts.urn) {
                throw new Error("Missing required property 'value'");
            }
            resourceInputs["domainId"] = args ? args.domainId : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["priority"] = args ? args.priority : undefined;
            resourceInputs["ttl"] = args ? args.ttl : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
            resourceInputs["value"] = args ? args.value : undefined;
            resourceInputs["accountId"] = undefined /*out*/;
            resourceInputs["createdAt"] = undefined /*out*/;
            resourceInputs["updatedAt"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(DnsDomainRecord.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DnsDomainRecord resources.
 */
export interface DnsDomainRecordState {
    /**
     * The account ID of this resource
     */
    accountId?: pulumi.Input<string>;
    /**
     * Timestamp when this resource was created
     */
    createdAt?: pulumi.Input<string>;
    /**
     * ID from domain name
     */
    domainId?: pulumi.Input<string>;
    /**
     * The portion before the domain name (e.g. www) or an @ for the apex/root domain (you cannot use an A record with an amex/root domain)
     */
    name?: pulumi.Input<string>;
    /**
     * Useful for MX records only, the priority mail should be attempted it (defaults to 10)
     */
    priority?: pulumi.Input<number>;
    /**
     * How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified is 600)
     */
    ttl?: pulumi.Input<number>;
    /**
     * The choice of RR type from a, cname, mx or txt
     */
    type?: pulumi.Input<string>;
    /**
     * Timestamp when this resource was updated
     */
    updatedAt?: pulumi.Input<string>;
    /**
     * The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record
     */
    value?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a DnsDomainRecord resource.
 */
export interface DnsDomainRecordArgs {
    /**
     * ID from domain name
     */
    domainId: pulumi.Input<string>;
    /**
     * The portion before the domain name (e.g. www) or an @ for the apex/root domain (you cannot use an A record with an amex/root domain)
     */
    name?: pulumi.Input<string>;
    /**
     * Useful for MX records only, the priority mail should be attempted it (defaults to 10)
     */
    priority?: pulumi.Input<number>;
    /**
     * How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified is 600)
     */
    ttl: pulumi.Input<number>;
    /**
     * The choice of RR type from a, cname, mx or txt
     */
    type: pulumi.Input<string>;
    /**
     * The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record
     */
    value: pulumi.Input<string>;
}

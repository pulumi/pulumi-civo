// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a Civo network resource. This can be used to create, modify, and delete networks.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as civo from "@pulumi/civo";
 *
 * const customNet = new civo.Network("custom_net", {
 *     label: "test_network",
 * });
 * ```
 *
 * <!-- schema generated by tfplugindocs -->
 * ## Schema
 *
 * ### Required
 *
 * - **label** (String) Name for the network
 *
 * ### Optional
 *
 * - **id** (String) The ID of this resource.
 * - **region** (String) The region of the network
 *
 * ### Read-Only
 *
 * - **default** (Boolean) If the network is default, this will be `true`
 * - **name** (String) The name of the network
 *
 * ## Import
 *
 * Import is supported using the following syntax# using ID
 *
 * ```sh
 *  $ pulumi import civo:index/network:Network custom_net b8ecd2ab-2267-4a5e-8692-cbf1d32583e3
 * ```
 */
export class Network extends pulumi.CustomResource {
    /**
     * Get an existing Network resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NetworkState, opts?: pulumi.CustomResourceOptions): Network {
        return new Network(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'civo:index/network:Network';

    /**
     * Returns true if the given object is an instance of Network.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Network {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Network.__pulumiType;
    }

    /**
     * If the network is default, this will be `true`
     */
    public /*out*/ readonly default!: pulumi.Output<boolean>;
    /**
     * Name for the network
     */
    public readonly label!: pulumi.Output<string>;
    /**
     * The name of the network
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * The region of the network
     */
    public readonly region!: pulumi.Output<string | undefined>;

    /**
     * Create a Network resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: NetworkArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: NetworkArgs | NetworkState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as NetworkState | undefined;
            inputs["default"] = state ? state.default : undefined;
            inputs["label"] = state ? state.label : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["region"] = state ? state.region : undefined;
        } else {
            const args = argsOrState as NetworkArgs | undefined;
            if ((!args || args.label === undefined) && !opts.urn) {
                throw new Error("Missing required property 'label'");
            }
            inputs["label"] = args ? args.label : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["default"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Network.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Network resources.
 */
export interface NetworkState {
    /**
     * If the network is default, this will be `true`
     */
    readonly default?: pulumi.Input<boolean>;
    /**
     * Name for the network
     */
    readonly label?: pulumi.Input<string>;
    /**
     * The name of the network
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The region of the network
     */
    readonly region?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Network resource.
 */
export interface NetworkArgs {
    /**
     * Name for the network
     */
    readonly label: pulumi.Input<string>;
    /**
     * The region of the network
     */
    readonly region?: pulumi.Input<string>;
}

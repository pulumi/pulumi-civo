// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a Civo network resource. This can be used to create, modify, and delete networks.
 *
 * ## Example Usage
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as civo from "@pulumi/civo";
 *
 * const customNet = new civo.Network("customNet", {label: "test_network"});
 * ```
 * <!--End PulumiCodeChooser -->
 *
 * ## Import
 *
 * using ID
 *
 * ```sh
 * $ pulumi import civo:index/network:Network custom_net b8ecd2ab-2267-4a5e-8692-cbf1d32583e3
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
    public readonly region!: pulumi.Output<string>;

    /**
     * Create a Network resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: NetworkArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: NetworkArgs | NetworkState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as NetworkState | undefined;
            resourceInputs["default"] = state ? state.default : undefined;
            resourceInputs["label"] = state ? state.label : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["region"] = state ? state.region : undefined;
        } else {
            const args = argsOrState as NetworkArgs | undefined;
            if ((!args || args.label === undefined) && !opts.urn) {
                throw new Error("Missing required property 'label'");
            }
            resourceInputs["label"] = args ? args.label : undefined;
            resourceInputs["region"] = args ? args.region : undefined;
            resourceInputs["default"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Network.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Network resources.
 */
export interface NetworkState {
    /**
     * If the network is default, this will be `true`
     */
    default?: pulumi.Input<boolean>;
    /**
     * Name for the network
     */
    label?: pulumi.Input<string>;
    /**
     * The name of the network
     */
    name?: pulumi.Input<string>;
    /**
     * The region of the network
     */
    region?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Network resource.
 */
export interface NetworkArgs {
    /**
     * Name for the network
     */
    label: pulumi.Input<string>;
    /**
     * The region of the network
     */
    region?: pulumi.Input<string>;
}

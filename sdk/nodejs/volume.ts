// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a Civo volume which can be attached to an instance in order to provide expanded storage.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as civo from "@pulumi/civo";
 *
 * const defaultNetwork = civo.getNetwork({
 *     label: "Default",
 * });
 * // Create volume
 * const db = new civo.Volume("db", {
 *     sizeGb: 5,
 *     networkId: defaultNetwork.then(defaultNetwork => defaultNetwork.id),
 * }, {
 *     dependsOn: [defaultNetwork],
 * });
 * ```
 *
 * ## Import
 *
 * # using ID
 *
 * ```sh
 *  $ pulumi import civo:index/volume:Volume db 506f78a4-e098-11e5-ad9f-000f53306ae1
 * ```
 */
export class Volume extends pulumi.CustomResource {
    /**
     * Get an existing Volume resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VolumeState, opts?: pulumi.CustomResourceOptions): Volume {
        return new Volume(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'civo:index/volume:Volume';

    /**
     * Returns true if the given object is an instance of Volume.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Volume {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Volume.__pulumiType;
    }

    /**
     * The mount point of the volume (from instance's perspective)
     */
    public /*out*/ readonly mountPoint!: pulumi.Output<string>;
    /**
     * A name that you wish to use to refer to this volume
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The network that the volume belongs to
     */
    public readonly networkId!: pulumi.Output<string>;
    /**
     * The region for the volume, if not declare we use the region in declared in the provider.
     */
    public readonly region!: pulumi.Output<string | undefined>;
    /**
     * A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes
     */
    public readonly sizeGb!: pulumi.Output<number>;

    /**
     * Create a Volume resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VolumeArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: VolumeArgs | VolumeState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as VolumeState | undefined;
            resourceInputs["mountPoint"] = state ? state.mountPoint : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["networkId"] = state ? state.networkId : undefined;
            resourceInputs["region"] = state ? state.region : undefined;
            resourceInputs["sizeGb"] = state ? state.sizeGb : undefined;
        } else {
            const args = argsOrState as VolumeArgs | undefined;
            if ((!args || args.networkId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'networkId'");
            }
            if ((!args || args.sizeGb === undefined) && !opts.urn) {
                throw new Error("Missing required property 'sizeGb'");
            }
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["networkId"] = args ? args.networkId : undefined;
            resourceInputs["region"] = args ? args.region : undefined;
            resourceInputs["sizeGb"] = args ? args.sizeGb : undefined;
            resourceInputs["mountPoint"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Volume.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Volume resources.
 */
export interface VolumeState {
    /**
     * The mount point of the volume (from instance's perspective)
     */
    mountPoint?: pulumi.Input<string>;
    /**
     * A name that you wish to use to refer to this volume
     */
    name?: pulumi.Input<string>;
    /**
     * The network that the volume belongs to
     */
    networkId?: pulumi.Input<string>;
    /**
     * The region for the volume, if not declare we use the region in declared in the provider.
     */
    region?: pulumi.Input<string>;
    /**
     * A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes
     */
    sizeGb?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a Volume resource.
 */
export interface VolumeArgs {
    /**
     * A name that you wish to use to refer to this volume
     */
    name?: pulumi.Input<string>;
    /**
     * The network that the volume belongs to
     */
    networkId: pulumi.Input<string>;
    /**
     * The region for the volume, if not declare we use the region in declared in the provider.
     */
    region?: pulumi.Input<string>;
    /**
     * A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes
     */
    sizeGb: pulumi.Input<number>;
}

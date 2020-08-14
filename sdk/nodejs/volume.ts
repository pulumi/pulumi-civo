// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a Civo volume which can be attached to a Instance in order to provide expanded storage.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as civo from "@pulumi/civo";
 *
 * const db = new civo.Volume("db", {
 *     bootable: false,
 *     sizeGb: 60,
 * });
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
     * Mark the volume as bootable.
     */
    public readonly bootable!: pulumi.Output<boolean>;
    /**
     * The date of the creation of the volume.
     */
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    /**
     * The mount point of the volume.
     */
    public /*out*/ readonly mountPoint!: pulumi.Output<string>;
    /**
     * A name that you wish to use to refer to this volume .
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes .
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
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as VolumeState | undefined;
            inputs["bootable"] = state ? state.bootable : undefined;
            inputs["createdAt"] = state ? state.createdAt : undefined;
            inputs["mountPoint"] = state ? state.mountPoint : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["sizeGb"] = state ? state.sizeGb : undefined;
        } else {
            const args = argsOrState as VolumeArgs | undefined;
            if (!args || args.bootable === undefined) {
                throw new Error("Missing required property 'bootable'");
            }
            if (!args || args.sizeGb === undefined) {
                throw new Error("Missing required property 'sizeGb'");
            }
            inputs["bootable"] = args ? args.bootable : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["sizeGb"] = args ? args.sizeGb : undefined;
            inputs["createdAt"] = undefined /*out*/;
            inputs["mountPoint"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Volume.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Volume resources.
 */
export interface VolumeState {
    /**
     * Mark the volume as bootable.
     */
    readonly bootable?: pulumi.Input<boolean>;
    /**
     * The date of the creation of the volume.
     */
    readonly createdAt?: pulumi.Input<string>;
    /**
     * The mount point of the volume.
     */
    readonly mountPoint?: pulumi.Input<string>;
    /**
     * A name that you wish to use to refer to this volume .
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes .
     */
    readonly sizeGb?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a Volume resource.
 */
export interface VolumeArgs {
    /**
     * Mark the volume as bootable.
     */
    readonly bootable: pulumi.Input<boolean>;
    /**
     * A name that you wish to use to refer to this volume .
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes .
     */
    readonly sizeGb: pulumi.Input<number>;
}
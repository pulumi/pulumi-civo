// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class Snapshot extends pulumi.CustomResource {
    /**
     * Get an existing Snapshot resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SnapshotState, opts?: pulumi.CustomResourceOptions): Snapshot {
        return new Snapshot(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'civo:index/snapshot:Snapshot';

    /**
     * Returns true if the given object is an instance of Snapshot.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Snapshot {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Snapshot.__pulumiType;
    }

    public /*out*/ readonly completedAt!: pulumi.Output<string>;
    /**
     * If a valid cron string is passed, the snapshot will be saved as an automated snapshot,continuing to automatically update
     * based on the schedule of the cron sequence provided.The default is nil meaning the snapshot will be saved as a one-off
     * snapshot.
     */
    public readonly cronTiming!: pulumi.Output<string | undefined>;
    public /*out*/ readonly hostname!: pulumi.Output<string>;
    /**
     * The ID of the instance to snapshot
     */
    public readonly instanceId!: pulumi.Output<string>;
    /**
     * This is a unqiue, alphanumerical, short, human readable code for the snapshot
     */
    public readonly name!: pulumi.Output<string>;
    public /*out*/ readonly nextExecution!: pulumi.Output<string>;
    public /*out*/ readonly region!: pulumi.Output<string>;
    public /*out*/ readonly requestedAt!: pulumi.Output<string>;
    /**
     * If true the instance will be shut down during the snapshot to ensure all filesare in a consistent state (e.g. database
     * tables aren't in the middle of being optimisedand hence risking corruption). The default is false so you experience no
     * interruptionof service, but a small risk of corruption.
     */
    public readonly safe!: pulumi.Output<boolean | undefined>;
    public /*out*/ readonly sizeGb!: pulumi.Output<number>;
    public /*out*/ readonly state!: pulumi.Output<string>;
    public /*out*/ readonly templateId!: pulumi.Output<string>;

    /**
     * Create a Snapshot resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SnapshotArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SnapshotArgs | SnapshotState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as SnapshotState | undefined;
            inputs["completedAt"] = state ? state.completedAt : undefined;
            inputs["cronTiming"] = state ? state.cronTiming : undefined;
            inputs["hostname"] = state ? state.hostname : undefined;
            inputs["instanceId"] = state ? state.instanceId : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["nextExecution"] = state ? state.nextExecution : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["requestedAt"] = state ? state.requestedAt : undefined;
            inputs["safe"] = state ? state.safe : undefined;
            inputs["sizeGb"] = state ? state.sizeGb : undefined;
            inputs["state"] = state ? state.state : undefined;
            inputs["templateId"] = state ? state.templateId : undefined;
        } else {
            const args = argsOrState as SnapshotArgs | undefined;
            if (!args || args.instanceId === undefined) {
                throw new Error("Missing required property 'instanceId'");
            }
            inputs["cronTiming"] = args ? args.cronTiming : undefined;
            inputs["instanceId"] = args ? args.instanceId : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["safe"] = args ? args.safe : undefined;
            inputs["completedAt"] = undefined /*out*/;
            inputs["hostname"] = undefined /*out*/;
            inputs["nextExecution"] = undefined /*out*/;
            inputs["region"] = undefined /*out*/;
            inputs["requestedAt"] = undefined /*out*/;
            inputs["sizeGb"] = undefined /*out*/;
            inputs["state"] = undefined /*out*/;
            inputs["templateId"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Snapshot.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Snapshot resources.
 */
export interface SnapshotState {
    readonly completedAt?: pulumi.Input<string>;
    /**
     * If a valid cron string is passed, the snapshot will be saved as an automated snapshot,continuing to automatically update
     * based on the schedule of the cron sequence provided.The default is nil meaning the snapshot will be saved as a one-off
     * snapshot.
     */
    readonly cronTiming?: pulumi.Input<string>;
    readonly hostname?: pulumi.Input<string>;
    /**
     * The ID of the instance to snapshot
     */
    readonly instanceId?: pulumi.Input<string>;
    /**
     * This is a unqiue, alphanumerical, short, human readable code for the snapshot
     */
    readonly name?: pulumi.Input<string>;
    readonly nextExecution?: pulumi.Input<string>;
    readonly region?: pulumi.Input<string>;
    readonly requestedAt?: pulumi.Input<string>;
    /**
     * If true the instance will be shut down during the snapshot to ensure all filesare in a consistent state (e.g. database
     * tables aren't in the middle of being optimisedand hence risking corruption). The default is false so you experience no
     * interruptionof service, but a small risk of corruption.
     */
    readonly safe?: pulumi.Input<boolean>;
    readonly sizeGb?: pulumi.Input<number>;
    readonly state?: pulumi.Input<string>;
    readonly templateId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Snapshot resource.
 */
export interface SnapshotArgs {
    /**
     * If a valid cron string is passed, the snapshot will be saved as an automated snapshot,continuing to automatically update
     * based on the schedule of the cron sequence provided.The default is nil meaning the snapshot will be saved as a one-off
     * snapshot.
     */
    readonly cronTiming?: pulumi.Input<string>;
    /**
     * The ID of the instance to snapshot
     */
    readonly instanceId: pulumi.Input<string>;
    /**
     * This is a unqiue, alphanumerical, short, human readable code for the snapshot
     */
    readonly name?: pulumi.Input<string>;
    /**
     * If true the instance will be shut down during the snapshot to ensure all filesare in a consistent state (e.g. database
     * tables aren't in the middle of being optimisedand hence risking corruption). The default is false so you experience no
     * interruptionof service, but a small risk of corruption.
     */
    readonly safe?: pulumi.Input<boolean>;
}

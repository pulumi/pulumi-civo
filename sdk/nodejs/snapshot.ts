// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a resource which can be used to create a snapshot from an existing Civo Instance.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as civo from "@pulumi/civo";
 *
 * const myinstance_backup = new civo.Snapshot("myinstance-backup", {instanceId: civo_instance.myinstance.id});
 * ```
 */
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

    /**
     * The date where the snapshot was completed.
     */
    public /*out*/ readonly completedAt!: pulumi.Output<string>;
    /**
     * If a valid cron string is passed, the snapshot will be saved as an automated snapshot 
     * continuing to automatically update based on the schedule of the cron sequence provided
     * The default is nil meaning the snapshot will be saved as a one-off snapshot.
     */
    public readonly cronTiming!: pulumi.Output<string | undefined>;
    /**
     * The hostname of the instance.
     */
    public /*out*/ readonly hostname!: pulumi.Output<string>;
    /**
     * The ID of the Instance from which the snapshot will be taken.
     */
    public readonly instanceId!: pulumi.Output<string>;
    /**
     * A name for the instance snapshot.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * if cron was define this date will be the next execution date.
     */
    public /*out*/ readonly nextExecution!: pulumi.Output<string>;
    /**
     * The region where the snapshot was take.
     */
    public /*out*/ readonly region!: pulumi.Output<string>;
    /**
     * The date where the snapshot was requested.
     */
    public /*out*/ readonly requestedAt!: pulumi.Output<string>;
    /**
     * If `true` the instance will be shut down during the snapshot to ensure all files 
     * are in a consistent state (e.g. database tables aren't in the middle of being optimised
     * and hence risking corruption). The default is `false` so you experience no interruption
     * of service, but a small risk of corruption.
     */
    public readonly safe!: pulumi.Output<boolean | undefined>;
    /**
     * The size of the snapshot in GB.
     */
    public /*out*/ readonly sizeGb!: pulumi.Output<number>;
    /**
     * The status of the snapshot.
     */
    public /*out*/ readonly state!: pulumi.Output<string>;
    /**
     * The template id.
     */
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
    /**
     * The date where the snapshot was completed.
     */
    readonly completedAt?: pulumi.Input<string>;
    /**
     * If a valid cron string is passed, the snapshot will be saved as an automated snapshot 
     * continuing to automatically update based on the schedule of the cron sequence provided
     * The default is nil meaning the snapshot will be saved as a one-off snapshot.
     */
    readonly cronTiming?: pulumi.Input<string>;
    /**
     * The hostname of the instance.
     */
    readonly hostname?: pulumi.Input<string>;
    /**
     * The ID of the Instance from which the snapshot will be taken.
     */
    readonly instanceId?: pulumi.Input<string>;
    /**
     * A name for the instance snapshot.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * if cron was define this date will be the next execution date.
     */
    readonly nextExecution?: pulumi.Input<string>;
    /**
     * The region where the snapshot was take.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The date where the snapshot was requested.
     */
    readonly requestedAt?: pulumi.Input<string>;
    /**
     * If `true` the instance will be shut down during the snapshot to ensure all files 
     * are in a consistent state (e.g. database tables aren't in the middle of being optimised
     * and hence risking corruption). The default is `false` so you experience no interruption
     * of service, but a small risk of corruption.
     */
    readonly safe?: pulumi.Input<boolean>;
    /**
     * The size of the snapshot in GB.
     */
    readonly sizeGb?: pulumi.Input<number>;
    /**
     * The status of the snapshot.
     */
    readonly state?: pulumi.Input<string>;
    /**
     * The template id.
     */
    readonly templateId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Snapshot resource.
 */
export interface SnapshotArgs {
    /**
     * If a valid cron string is passed, the snapshot will be saved as an automated snapshot 
     * continuing to automatically update based on the schedule of the cron sequence provided
     * The default is nil meaning the snapshot will be saved as a one-off snapshot.
     */
    readonly cronTiming?: pulumi.Input<string>;
    /**
     * The ID of the Instance from which the snapshot will be taken.
     */
    readonly instanceId: pulumi.Input<string>;
    /**
     * A name for the instance snapshot.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * If `true` the instance will be shut down during the snapshot to ensure all files 
     * are in a consistent state (e.g. database tables aren't in the middle of being optimised
     * and hence risking corruption). The default is `false` so you experience no interruption
     * of service, but a small risk of corruption.
     */
    readonly safe?: pulumi.Input<boolean>;
}

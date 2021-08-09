// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a Civo Kubernetes node pool resource. While the default node pool must be defined in the civo.KubernetesCluster resource, this resource can be used to add additional ones to a cluster.
 *
 * ## Import
 *
 * Then the Kubernetes cluster node pool can be imported using the cluster's and pool id `cluster_id:node_pool_id`, e.g.
 *
 * ```sh
 *  $ pulumi import civo:index/kubernetesNodePool:KubernetesNodePool my-pool 1b8b2100-0e9f-4e8f-ad78-9eb578c2a0af:502c1130-cb9b-4a88-b6d2-307bd96d946a
 * ```
 */
export class KubernetesNodePool extends pulumi.CustomResource {
    /**
     * Get an existing KubernetesNodePool resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: KubernetesNodePoolState, opts?: pulumi.CustomResourceOptions): KubernetesNodePool {
        return new KubernetesNodePool(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'civo:index/kubernetesNodePool:KubernetesNodePool';

    /**
     * Returns true if the given object is an instance of KubernetesNodePool.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is KubernetesNodePool {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === KubernetesNodePool.__pulumiType;
    }

    /**
     * The ID of the Kubernetes cluster to which the node pool is associated.
     */
    public readonly clusterId!: pulumi.Output<string>;
    /**
     * The number of instances to create (The default at the time of writing is 3).
     */
    public readonly numTargetNodes!: pulumi.Output<number>;
    /**
     * The region of the node pool, has to match that of the cluster.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * The size of each node.
     */
    public readonly targetNodesSize!: pulumi.Output<string>;

    /**
     * Create a KubernetesNodePool resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: KubernetesNodePoolArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: KubernetesNodePoolArgs | KubernetesNodePoolState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as KubernetesNodePoolState | undefined;
            inputs["clusterId"] = state ? state.clusterId : undefined;
            inputs["numTargetNodes"] = state ? state.numTargetNodes : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["targetNodesSize"] = state ? state.targetNodesSize : undefined;
        } else {
            const args = argsOrState as KubernetesNodePoolArgs | undefined;
            if ((!args || args.clusterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'clusterId'");
            }
            if ((!args || args.region === undefined) && !opts.urn) {
                throw new Error("Missing required property 'region'");
            }
            inputs["clusterId"] = args ? args.clusterId : undefined;
            inputs["numTargetNodes"] = args ? args.numTargetNodes : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["targetNodesSize"] = args ? args.targetNodesSize : undefined;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(KubernetesNodePool.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering KubernetesNodePool resources.
 */
export interface KubernetesNodePoolState {
    /**
     * The ID of the Kubernetes cluster to which the node pool is associated.
     */
    readonly clusterId?: pulumi.Input<string>;
    /**
     * The number of instances to create (The default at the time of writing is 3).
     */
    readonly numTargetNodes?: pulumi.Input<number>;
    /**
     * The region of the node pool, has to match that of the cluster.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The size of each node.
     */
    readonly targetNodesSize?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a KubernetesNodePool resource.
 */
export interface KubernetesNodePoolArgs {
    /**
     * The ID of the Kubernetes cluster to which the node pool is associated.
     */
    readonly clusterId: pulumi.Input<string>;
    /**
     * The number of instances to create (The default at the time of writing is 3).
     */
    readonly numTargetNodes?: pulumi.Input<number>;
    /**
     * The region of the node pool, has to match that of the cluster.
     */
    readonly region: pulumi.Input<string>;
    /**
     * The size of each node.
     */
    readonly targetNodesSize?: pulumi.Input<string>;
}

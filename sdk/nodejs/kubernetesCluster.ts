// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export class KubernetesCluster extends pulumi.CustomResource {
    /**
     * Get an existing KubernetesCluster resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: KubernetesClusterState, opts?: pulumi.CustomResourceOptions): KubernetesCluster {
        return new KubernetesCluster(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'civo:index/kubernetesCluster:KubernetesCluster';

    /**
     * Returns true if the given object is an instance of KubernetesCluster.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is KubernetesCluster {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === KubernetesCluster.__pulumiType;
    }

    /**
     * The base URL of the API server on the Kubernetes master node.
     */
    public /*out*/ readonly apiEndpoint!: pulumi.Output<string>;
    /**
     * A comma separated list of applications to install. Spaces within application names are fine, but shouldn't be either side of the comma. If you want to remove a default installed application, prefix it with a '-', e.g. -traefik
     */
    public readonly applications!: pulumi.Output<string | undefined>;
    /**
     * The date where the Kubernetes cluster was build.
     */
    public /*out*/ readonly builtAt!: pulumi.Output<string>;
    /**
     * The date where the Kubernetes cluster was create.
     */
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    /**
     * The unique dns entry for the cluster in this case point to the master.
     */
    public /*out*/ readonly dnsEntry!: pulumi.Output<string>;
    /**
     * A unique ID that can be used to identify and reference a Kubernetes cluster.
     */
    public /*out*/ readonly installedApplications!: pulumi.Output<outputs.KubernetesClusterInstalledApplication[]>;
    /**
     * In addition to the arguments provided, these additional attributes about the cluster's default node instance are exported.
     */
    public /*out*/ readonly instances!: pulumi.Output<outputs.KubernetesClusterInstance[]>;
    /**
     * A representation of the Kubernetes cluster's kubeconfig in yaml format.
     */
    public /*out*/ readonly kubeconfig!: pulumi.Output<string>;
    /**
     * The version of k3s to install (optional, the default is currently the latest available).
     */
    public readonly kubernetesVersion!: pulumi.Output<string>;
    /**
     * The Ip of the Kubernetes master node.
     */
    public /*out*/ readonly masterIp!: pulumi.Output<string>;
    /**
     * A name for the Kubernetes cluster.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The number of instances to create (optional, the default at the time of writing is 3).
     */
    public readonly numTargetNodes!: pulumi.Output<number | undefined>;
    public /*out*/ readonly ready!: pulumi.Output<boolean>;
    /**
     * The status of Kubernetes cluster.
     * * `ready` -If the Kubernetes cluster is ready.
     */
    public /*out*/ readonly status!: pulumi.Output<string>;
    /**
     * A space separated list of tags, to be used freely as required.
     */
    public readonly tags!: pulumi.Output<string | undefined>;
    /**
     * The size of each node (optional, the default is currently g2.small)
     */
    public readonly targetNodesSize!: pulumi.Output<string | undefined>;

    /**
     * Create a KubernetesCluster resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: KubernetesClusterArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: KubernetesClusterArgs | KubernetesClusterState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as KubernetesClusterState | undefined;
            inputs["apiEndpoint"] = state ? state.apiEndpoint : undefined;
            inputs["applications"] = state ? state.applications : undefined;
            inputs["builtAt"] = state ? state.builtAt : undefined;
            inputs["createdAt"] = state ? state.createdAt : undefined;
            inputs["dnsEntry"] = state ? state.dnsEntry : undefined;
            inputs["installedApplications"] = state ? state.installedApplications : undefined;
            inputs["instances"] = state ? state.instances : undefined;
            inputs["kubeconfig"] = state ? state.kubeconfig : undefined;
            inputs["kubernetesVersion"] = state ? state.kubernetesVersion : undefined;
            inputs["masterIp"] = state ? state.masterIp : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["numTargetNodes"] = state ? state.numTargetNodes : undefined;
            inputs["ready"] = state ? state.ready : undefined;
            inputs["status"] = state ? state.status : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["targetNodesSize"] = state ? state.targetNodesSize : undefined;
        } else {
            const args = argsOrState as KubernetesClusterArgs | undefined;
            inputs["applications"] = args ? args.applications : undefined;
            inputs["kubernetesVersion"] = args ? args.kubernetesVersion : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["numTargetNodes"] = args ? args.numTargetNodes : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["targetNodesSize"] = args ? args.targetNodesSize : undefined;
            inputs["apiEndpoint"] = undefined /*out*/;
            inputs["builtAt"] = undefined /*out*/;
            inputs["createdAt"] = undefined /*out*/;
            inputs["dnsEntry"] = undefined /*out*/;
            inputs["installedApplications"] = undefined /*out*/;
            inputs["instances"] = undefined /*out*/;
            inputs["kubeconfig"] = undefined /*out*/;
            inputs["masterIp"] = undefined /*out*/;
            inputs["ready"] = undefined /*out*/;
            inputs["status"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(KubernetesCluster.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering KubernetesCluster resources.
 */
export interface KubernetesClusterState {
    /**
     * The base URL of the API server on the Kubernetes master node.
     */
    readonly apiEndpoint?: pulumi.Input<string>;
    /**
     * A comma separated list of applications to install. Spaces within application names are fine, but shouldn't be either side of the comma. If you want to remove a default installed application, prefix it with a '-', e.g. -traefik
     */
    readonly applications?: pulumi.Input<string>;
    /**
     * The date where the Kubernetes cluster was build.
     */
    readonly builtAt?: pulumi.Input<string>;
    /**
     * The date where the Kubernetes cluster was create.
     */
    readonly createdAt?: pulumi.Input<string>;
    /**
     * The unique dns entry for the cluster in this case point to the master.
     */
    readonly dnsEntry?: pulumi.Input<string>;
    /**
     * A unique ID that can be used to identify and reference a Kubernetes cluster.
     */
    readonly installedApplications?: pulumi.Input<pulumi.Input<inputs.KubernetesClusterInstalledApplication>[]>;
    /**
     * In addition to the arguments provided, these additional attributes about the cluster's default node instance are exported.
     */
    readonly instances?: pulumi.Input<pulumi.Input<inputs.KubernetesClusterInstance>[]>;
    /**
     * A representation of the Kubernetes cluster's kubeconfig in yaml format.
     */
    readonly kubeconfig?: pulumi.Input<string>;
    /**
     * The version of k3s to install (optional, the default is currently the latest available).
     */
    readonly kubernetesVersion?: pulumi.Input<string>;
    /**
     * The Ip of the Kubernetes master node.
     */
    readonly masterIp?: pulumi.Input<string>;
    /**
     * A name for the Kubernetes cluster.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The number of instances to create (optional, the default at the time of writing is 3).
     */
    readonly numTargetNodes?: pulumi.Input<number>;
    readonly ready?: pulumi.Input<boolean>;
    /**
     * The status of Kubernetes cluster.
     * * `ready` -If the Kubernetes cluster is ready.
     */
    readonly status?: pulumi.Input<string>;
    /**
     * A space separated list of tags, to be used freely as required.
     */
    readonly tags?: pulumi.Input<string>;
    /**
     * The size of each node (optional, the default is currently g2.small)
     */
    readonly targetNodesSize?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a KubernetesCluster resource.
 */
export interface KubernetesClusterArgs {
    /**
     * A comma separated list of applications to install. Spaces within application names are fine, but shouldn't be either side of the comma. If you want to remove a default installed application, prefix it with a '-', e.g. -traefik
     */
    readonly applications?: pulumi.Input<string>;
    /**
     * The version of k3s to install (optional, the default is currently the latest available).
     */
    readonly kubernetesVersion?: pulumi.Input<string>;
    /**
     * A name for the Kubernetes cluster.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The number of instances to create (optional, the default at the time of writing is 3).
     */
    readonly numTargetNodes?: pulumi.Input<number>;
    /**
     * A space separated list of tags, to be used freely as required.
     */
    readonly tags?: pulumi.Input<string>;
    /**
     * The size of each node (optional, the default is currently g2.small)
     */
    readonly targetNodesSize?: pulumi.Input<string>;
}

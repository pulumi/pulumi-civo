// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * Provides a Civo Kubernetes cluster data source.
 *
 * Note: This data source returns a single Kubernetes cluster. When specifying a name, an error will be raised if more than one Kubernetes cluster found.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as civo from "@pulumi/civo";
 *
 * const my-cluster = civo.getKubernetesCluster({
 *     name: "my-super-cluster",
 * });
 * export const kubernetesClusterOutput = my_cluster.then(my_cluster => my_cluster.masterIp);
 * ```
 */
export function getKubernetesCluster(args?: GetKubernetesClusterArgs, opts?: pulumi.InvokeOptions): Promise<GetKubernetesClusterResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("civo:index/getKubernetesCluster:getKubernetesCluster", {
        "id": args.id,
        "name": args.name,
        "region": args.region,
    }, opts);
}

/**
 * A collection of arguments for invoking getKubernetesCluster.
 */
export interface GetKubernetesClusterArgs {
    /**
     * The ID of this resource.
     */
    id?: string;
    /**
     * The name of the Kubernetes Cluster
     */
    name?: string;
    /**
     * The region where cluster is running
     */
    region?: string;
}

/**
 * A collection of values returned by getKubernetesCluster.
 */
export interface GetKubernetesClusterResult {
    /**
     * The base URL of the API server on the Kubernetes master node
     */
    readonly apiEndpoint: string;
    /**
     * A list of application installed
     */
    readonly applications: string;
    /**
     * The date where the Kubernetes cluster was create
     */
    readonly createdAt: string;
    /**
     * The unique dns entry for the cluster in this case point to the master
     */
    readonly dnsEntry: string;
    /**
     * The ID of this resource.
     */
    readonly id?: string;
    readonly installedApplications: outputs.GetKubernetesClusterInstalledApplication[];
    readonly instances: outputs.GetKubernetesClusterInstance[];
    /**
     * A representation of the Kubernetes cluster's kubeconfig in yaml format
     */
    readonly kubeconfig: string;
    /**
     * The version of Kubernetes
     */
    readonly kubernetesVersion: string;
    /**
     * The IP of the Kubernetes master node
     */
    readonly masterIp: string;
    /**
     * The name of the Kubernetes Cluster
     */
    readonly name?: string;
    /**
     * The size of the Kubernetes cluster
     */
    readonly numTargetNodes: number;
    readonly pools: outputs.GetKubernetesClusterPool[];
    /**
     * If the Kubernetes cluster is ready
     */
    readonly ready: boolean;
    /**
     * The region where cluster is running
     */
    readonly region?: string;
    /**
     * The status of Kubernetes cluster
     */
    readonly status: string;
    /**
     * A list of tags
     */
    readonly tags: string;
    /**
     * The size of each node
     */
    readonly targetNodesSize: string;
}

export function getKubernetesClusterOutput(args?: GetKubernetesClusterOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetKubernetesClusterResult> {
    return pulumi.output(args).apply(a => getKubernetesCluster(a, opts))
}

/**
 * A collection of arguments for invoking getKubernetesCluster.
 */
export interface GetKubernetesClusterOutputArgs {
    /**
     * The ID of this resource.
     */
    id?: pulumi.Input<string>;
    /**
     * The name of the Kubernetes Cluster
     */
    name?: pulumi.Input<string>;
    /**
     * The region where cluster is running
     */
    region?: pulumi.Input<string>;
}

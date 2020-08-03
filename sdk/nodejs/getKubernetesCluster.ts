// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Provides a Civo Kubernetes cluster data source.
 *
 * **Note:** This data source returns a single kubernetes cluster. When specifying a `name`, an
 * error is triggered if more than one kubernetes Cluster is found.
 *
 * ## Example Usage
 *
 * Get the Kubernetes Cluster by name:
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
 *
 * Get the Kubernetes Cluster by id:
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as civo from "@pulumi/civo";
 *
 * const my_cluster = pulumi.output(civo.getKubernetesCluster({
 *     name: "40ac97ee-b82b-4231-9b60-079c7e2e5d79",
 * }, { async: true }));
 * ```
 */
export function getKubernetesCluster(args?: GetKubernetesClusterArgs, opts?: pulumi.InvokeOptions): Promise<GetKubernetesClusterResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("civo:index/getKubernetesCluster:getKubernetesCluster", {
        "id": args.id,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getKubernetesCluster.
 */
export interface GetKubernetesClusterArgs {
    /**
     * The ID of the kubernetes Cluster
     */
    readonly id?: string;
    /**
     * The name of the kubernetes Cluster.
     */
    readonly name?: string;
}

/**
 * A collection of values returned by getKubernetesCluster.
 */
export interface GetKubernetesClusterResult {
    /**
     * The base URL of the API server on the Kubernetes master node.
     */
    readonly apiEndpoint: string;
    /**
     * A list of application installed.
     */
    readonly applications: string;
    /**
     * The date where the Kubernetes cluster was build.
     */
    readonly builtAt: string;
    /**
     * The date where the Kubernetes cluster was create.
     */
    readonly createdAt: string;
    /**
     * The unique dns entry for the cluster in this case point to the master.
     */
    readonly dnsEntry: string;
    /**
     * A unique ID that can be used to identify and reference a Kubernetes cluster.
     */
    readonly id?: string;
    /**
     * A unique ID that can be used to identify and reference a Kubernetes cluster.
     */
    readonly installedApplications: outputs.GetKubernetesClusterInstalledApplication[];
    /**
     * In addition to the arguments provided, these additional attributes about the cluster's default node instance are exported.
     */
    readonly instances: outputs.GetKubernetesClusterInstance[];
    /**
     * A representation of the Kubernetes cluster's kubeconfig in yaml format.
     */
    readonly kubeconfig: string;
    /**
     * The version of Kubernetes.
     */
    readonly kubernetesVersion: string;
    /**
     * The Ip of the Kubernetes master node.
     */
    readonly masterIp: string;
    /**
     * The name of your cluster,.
     */
    readonly name?: string;
    /**
     * The size of the Kubernetes cluster.
     */
    readonly numTargetNodes: number;
    readonly ready: boolean;
    /**
     * The status of Kubernetes cluster.
     * * `ready` -If the Kubernetes cluster is ready.
     */
    readonly status: string;
    /**
     * The tag of the instances
     */
    readonly tags: string;
    /**
     * The size of each node.
     */
    readonly targetNodesSize: string;
}

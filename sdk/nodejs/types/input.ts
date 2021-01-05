// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";

export interface GetInstancesFilter {
    /**
     * Filter the Instances by this key. This may be one of '`id`, `hostname`, `publicIp`, `privateIp`,
     * `pseudoIp`, `size`, `cpuCores`, `ramMb`, `diskGb`, `template` or `createdAt`.
     */
    key: string;
    /**
     * A list of values to match against the `key` field. Only retrieves Instances
     * where the `key` field takes on one or more of the values provided here.
     */
    values: string[];
}

export interface GetInstancesSizeFilter {
    key: string;
    values: string[];
}

export interface GetInstancesSizeSort {
    direction?: string;
    key: string;
}

export interface GetInstancesSort {
    /**
     * The sort direction. This may be either `asc` or `desc`.
     */
    direction?: string;
    /**
     * Sort the Instance by this key. This may be one of `id`, `hostname`, `publicIp`, `privateIp`,
     * `pseudoIp`, `size`, `cpuCores`, `ramMb`, `diskGb`, `template` or `createdAt`.
     */
    key: string;
}

export interface GetKubernetesVersionFilter {
    /**
     * Filter the sizes by this key. This may be one of `version`,
     * `label`, `type`, `default`.
     */
    key: string;
    /**
     * Only retrieves the version which keys has value that matches
     * one of the values provided here.
     */
    values: string[];
}

export interface GetKubernetesVersionSort {
    /**
     * The sort direction. This may be either `asc` or `desc`.
     */
    direction?: string;
    /**
     * Sort the sizes by this key. This may be one of `version`.
     */
    key: string;
}

export interface GetTemplateFilter {
    /**
     * Filter the sizes by this key. This may be one of `code`,
     * `name`.
     */
    key: string;
    /**
     * Only retrieves the template which keys has value that matches
     * one of the values provided here.
     */
    values: string[];
}

export interface GetTemplateSort {
    /**
     * The sort direction. This may be either `asc` or `desc`.
     */
    direction?: string;
    /**
     * Sort the sizes by this key. This may be one of `code`, 
     * `name`.
     */
    key: string;
}

export interface KubernetesClusterInstalledApplication {
    /**
     * The name of the application
     */
    application?: pulumi.Input<string>;
    /**
     * The category of the application
     */
    category?: pulumi.Input<string>;
    /**
     * if installed or not
     */
    installed?: pulumi.Input<boolean>;
    /**
     * The version of the application
     */
    version?: pulumi.Input<string>;
}

export interface KubernetesClusterInstance {
    /**
     * Total cpu of the inatance.
     */
    cpuCores?: pulumi.Input<number>;
    /**
     * The date where the Kubernetes cluster was create.
     */
    createdAt?: pulumi.Input<string>;
    /**
     * The size of the disk.
     */
    diskGb?: pulumi.Input<number>;
    /**
     * The firewall id assigned to the instance
     */
    firewallId?: pulumi.Input<string>;
    /**
     * The hostname of the instance.
     */
    hostname?: pulumi.Input<string>;
    /**
     * The public ip of the instances, only available if the instances is the master
     */
    publicIp?: pulumi.Input<string>;
    /**
     * Total ram of the instance.
     */
    ramMb?: pulumi.Input<number>;
    /**
     * The region where instance are.
     */
    region?: pulumi.Input<string>;
    /**
     * The size of the instance.
     */
    size?: pulumi.Input<string>;
    /**
     * The status of Kubernetes cluster.
     * * `ready` -If the Kubernetes cluster is ready.
     */
    status?: pulumi.Input<string>;
    /**
     * A space separated list of tags, to be used freely as required.
     */
    tags?: pulumi.Input<pulumi.Input<string>[]>;
}

export interface LoadBalancerBackend {
    instanceId: pulumi.Input<string>;
    port: pulumi.Input<number>;
    protocol: pulumi.Input<string>;
}

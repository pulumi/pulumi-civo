// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";

export interface FirewallEgressRule {
    action: pulumi.Input<string>;
    cidrs: pulumi.Input<pulumi.Input<string>[]>;
    id?: pulumi.Input<string>;
    label?: pulumi.Input<string>;
    portRange?: pulumi.Input<string>;
    protocol?: pulumi.Input<string>;
}

export interface FirewallIngressRule {
    action: pulumi.Input<string>;
    cidrs: pulumi.Input<pulumi.Input<string>[]>;
    id?: pulumi.Input<string>;
    label?: pulumi.Input<string>;
    portRange?: pulumi.Input<string>;
    protocol?: pulumi.Input<string>;
}

export interface GetDiskImageFilter {
    all?: boolean;
    key: string;
    matchBy?: string;
    values: string[];
}

export interface GetDiskImageFilterArgs {
    all?: pulumi.Input<boolean>;
    key: pulumi.Input<string>;
    matchBy?: pulumi.Input<string>;
    values: pulumi.Input<pulumi.Input<string>[]>;
}

export interface GetDiskImageSort {
    direction?: string;
    key: string;
}

export interface GetDiskImageSortArgs {
    direction?: pulumi.Input<string>;
    key: pulumi.Input<string>;
}

export interface GetInstancesFilter {
    all?: boolean;
    key: string;
    matchBy?: string;
    values: string[];
}

export interface GetInstancesFilterArgs {
    all?: pulumi.Input<boolean>;
    key: pulumi.Input<string>;
    matchBy?: pulumi.Input<string>;
    values: pulumi.Input<pulumi.Input<string>[]>;
}

export interface GetInstancesSizeFilter {
    all?: boolean;
    key: string;
    matchBy?: string;
    values: string[];
}

export interface GetInstancesSizeFilterArgs {
    all?: pulumi.Input<boolean>;
    key: pulumi.Input<string>;
    matchBy?: pulumi.Input<string>;
    values: pulumi.Input<pulumi.Input<string>[]>;
}

export interface GetInstancesSizeSort {
    direction?: string;
    key: string;
}

export interface GetInstancesSizeSortArgs {
    direction?: pulumi.Input<string>;
    key: pulumi.Input<string>;
}

export interface GetInstancesSort {
    direction?: string;
    key: string;
}

export interface GetInstancesSortArgs {
    direction?: pulumi.Input<string>;
    key: pulumi.Input<string>;
}

export interface GetKubernetesVersionFilter {
    all?: boolean;
    key: string;
    matchBy?: string;
    values: string[];
}

export interface GetKubernetesVersionFilterArgs {
    all?: pulumi.Input<boolean>;
    key: pulumi.Input<string>;
    matchBy?: pulumi.Input<string>;
    values: pulumi.Input<pulumi.Input<string>[]>;
}

export interface GetKubernetesVersionSort {
    direction?: string;
    key: string;
}

export interface GetKubernetesVersionSortArgs {
    direction?: pulumi.Input<string>;
    key: pulumi.Input<string>;
}

export interface GetRegionFilter {
    all?: boolean;
    key: string;
    matchBy?: string;
    values: string[];
}

export interface GetRegionFilterArgs {
    all?: pulumi.Input<boolean>;
    key: pulumi.Input<string>;
    matchBy?: pulumi.Input<string>;
    values: pulumi.Input<pulumi.Input<string>[]>;
}

export interface GetRegionSort {
    direction?: string;
    key: string;
}

export interface GetRegionSortArgs {
    direction?: pulumi.Input<string>;
    key: pulumi.Input<string>;
}

export interface GetSizeFilter {
    all?: boolean;
    key: string;
    matchBy?: string;
    values: string[];
}

export interface GetSizeFilterArgs {
    all?: pulumi.Input<boolean>;
    key: pulumi.Input<string>;
    matchBy?: pulumi.Input<string>;
    values: pulumi.Input<pulumi.Input<string>[]>;
}

export interface GetSizeSort {
    direction?: string;
    key: string;
}

export interface GetSizeSortArgs {
    direction?: pulumi.Input<string>;
    key: pulumi.Input<string>;
}

export interface KubernetesClusterInstalledApplication {
    application?: pulumi.Input<string>;
    category?: pulumi.Input<string>;
    installed?: pulumi.Input<boolean>;
    version?: pulumi.Input<string>;
}

export interface KubernetesClusterPools {
    instanceNames?: pulumi.Input<pulumi.Input<string>[]>;
    label?: pulumi.Input<string>;
    nodeCount: pulumi.Input<number>;
    size: pulumi.Input<string>;
}

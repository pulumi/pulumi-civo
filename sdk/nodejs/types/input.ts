// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export interface GetInstancesFilter {
    key: string;
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
    direction?: string;
    key: string;
}

export interface GetKubernetesVersionFilter {
    key: string;
    values: string[];
}

export interface GetKubernetesVersionSort {
    direction?: string;
    key: string;
}

export interface GetTemplateFilter {
    key: string;
    values: string[];
}

export interface GetTemplateSort {
    direction?: string;
    key: string;
}

export interface KubernetesClusterInstalledApplication {
    application?: pulumi.Input<string>;
    category?: pulumi.Input<string>;
    installed?: pulumi.Input<boolean>;
    version?: pulumi.Input<string>;
}

export interface KubernetesClusterInstance {
    cpuCores?: pulumi.Input<number>;
    createdAt?: pulumi.Input<string>;
    diskGb?: pulumi.Input<number>;
    firewallId?: pulumi.Input<string>;
    hostname?: pulumi.Input<string>;
    publicIp?: pulumi.Input<string>;
    ramMb?: pulumi.Input<number>;
    region?: pulumi.Input<string>;
    size?: pulumi.Input<string>;
    status?: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<string>[]>;
}

export interface LoadBalancerBackend {
    instanceId: pulumi.Input<string>;
    port: pulumi.Input<number>;
    protocol: pulumi.Input<string>;
}

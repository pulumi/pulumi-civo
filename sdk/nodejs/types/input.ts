// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export interface FirewallEgressRule {
    /**
     * The action of the rule can be allow or deny. When we set the `action = 'allow'`, this is going to add a rule to allow traffic. Similarly, setting `action = 'deny'` will deny the traffic.
     */
    action: pulumi.Input<string>;
    /**
     * The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32 to open just for a specific IP address)
     */
    cidrs: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The ID of this resource.
     */
    id?: pulumi.Input<string>;
    /**
     * A string that will be the displayed name/reference for this rule
     */
    label?: pulumi.Input<string>;
    /**
     * The port or port range to open, can be a single port or a range separated by a dash (`-`), e.g. `80` or `80-443`
     */
    portRange?: pulumi.Input<string>;
    /**
     * The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
     */
    protocol?: pulumi.Input<string>;
}

export interface FirewallIngressRule {
    /**
     * The action of the rule can be allow or deny. When we set the `action = 'allow'`, this is going to add a rule to allow traffic. Similarly, setting `action = 'deny'` will deny the traffic.
     */
    action: pulumi.Input<string>;
    /**
     * The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32 to open just for a specific IP address)
     */
    cidrs: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The ID of this resource.
     */
    id?: pulumi.Input<string>;
    /**
     * A string that will be the displayed name/reference for this rule
     */
    label?: pulumi.Input<string>;
    /**
     * The port or port range to open, can be a single port or a range separated by a dash (`-`), e.g. `80` or `80-443`
     */
    portRange?: pulumi.Input<string>;
    /**
     * The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
     */
    protocol?: pulumi.Input<string>;
}

export interface GetDatabaseVersionFilter {
    /**
     * Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
     */
    all?: boolean;
    /**
     * Filter versions by this key. This may be one of `default`, `engine`, `version`.
     */
    key: string;
    /**
     * One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
     */
    matchBy?: string;
    /**
     * Only retrieves `versions` which keys has value that matches one of the values provided here
     */
    values: string[];
}

export interface GetDatabaseVersionFilterArgs {
    /**
     * Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
     */
    all?: pulumi.Input<boolean>;
    /**
     * Filter versions by this key. This may be one of `default`, `engine`, `version`.
     */
    key: pulumi.Input<string>;
    /**
     * One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
     */
    matchBy?: pulumi.Input<string>;
    /**
     * Only retrieves `versions` which keys has value that matches one of the values provided here
     */
    values: pulumi.Input<pulumi.Input<string>[]>;
}

export interface GetDatabaseVersionSort {
    /**
     * The sort direction. This may be either `asc` or `desc`.
     */
    direction?: string;
    /**
     * Sort versions by this key. This may be one of `default`, `engine`, `version`.
     */
    key: string;
}

export interface GetDatabaseVersionSortArgs {
    /**
     * The sort direction. This may be either `asc` or `desc`.
     */
    direction?: pulumi.Input<string>;
    /**
     * Sort versions by this key. This may be one of `default`, `engine`, `version`.
     */
    key: pulumi.Input<string>;
}

export interface GetDiskImageFilter {
    /**
     * Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
     */
    all?: boolean;
    /**
     * Filter diskimages by this key. This may be one of `id`, `label`, `name`, `version`.
     */
    key: string;
    /**
     * One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
     */
    matchBy?: string;
    /**
     * Only retrieves `diskimages` which keys has value that matches one of the values provided here
     */
    values: string[];
}

export interface GetDiskImageFilterArgs {
    /**
     * Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
     */
    all?: pulumi.Input<boolean>;
    /**
     * Filter diskimages by this key. This may be one of `id`, `label`, `name`, `version`.
     */
    key: pulumi.Input<string>;
    /**
     * One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
     */
    matchBy?: pulumi.Input<string>;
    /**
     * Only retrieves `diskimages` which keys has value that matches one of the values provided here
     */
    values: pulumi.Input<pulumi.Input<string>[]>;
}

export interface GetDiskImageSort {
    /**
     * The sort direction. This may be either `asc` or `desc`.
     */
    direction?: string;
    /**
     * Sort diskimages by this key. This may be one of `id`, `label`, `name`, `version`.
     */
    key: string;
}

export interface GetDiskImageSortArgs {
    /**
     * The sort direction. This may be either `asc` or `desc`.
     */
    direction?: pulumi.Input<string>;
    /**
     * Sort diskimages by this key. This may be one of `id`, `label`, `name`, `version`.
     */
    key: pulumi.Input<string>;
}

export interface GetInstancesFilter {
    /**
     * Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
     */
    all?: boolean;
    /**
     * Filter instances by this key. This may be one of `cpuCores`, `createdAt`, `diskGb`, `firewallId`, `hostname`, `id`, `initialPassword`, `initialUser`, `networkId`, `notes`, `privateIp`, `pseudoIp`, `publicIp`, `ramMb`, `region`, `reverseDns`, `script`, `size`, `sshkeyId`, `status`, `tags`, `template`.
     */
    key: string;
    /**
     * One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
     */
    matchBy?: string;
    /**
     * Only retrieves `instances` which keys has value that matches one of the values provided here
     */
    values: string[];
}

export interface GetInstancesFilterArgs {
    /**
     * Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
     */
    all?: pulumi.Input<boolean>;
    /**
     * Filter instances by this key. This may be one of `cpuCores`, `createdAt`, `diskGb`, `firewallId`, `hostname`, `id`, `initialPassword`, `initialUser`, `networkId`, `notes`, `privateIp`, `pseudoIp`, `publicIp`, `ramMb`, `region`, `reverseDns`, `script`, `size`, `sshkeyId`, `status`, `tags`, `template`.
     */
    key: pulumi.Input<string>;
    /**
     * One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
     */
    matchBy?: pulumi.Input<string>;
    /**
     * Only retrieves `instances` which keys has value that matches one of the values provided here
     */
    values: pulumi.Input<pulumi.Input<string>[]>;
}

export interface GetInstancesSort {
    /**
     * The sort direction. This may be either `asc` or `desc`.
     */
    direction?: string;
    /**
     * Sort instances by this key. This may be one of `cpuCores`, `createdAt`, `diskGb`, `firewallId`, `hostname`, `id`, `initialPassword`, `initialUser`, `networkId`, `notes`, `privateIp`, `pseudoIp`, `publicIp`, `ramMb`, `region`, `reverseDns`, `script`, `size`, `sshkeyId`, `status`, `template`.
     */
    key: string;
}

export interface GetInstancesSortArgs {
    /**
     * The sort direction. This may be either `asc` or `desc`.
     */
    direction?: pulumi.Input<string>;
    /**
     * Sort instances by this key. This may be one of `cpuCores`, `createdAt`, `diskGb`, `firewallId`, `hostname`, `id`, `initialPassword`, `initialUser`, `networkId`, `notes`, `privateIp`, `pseudoIp`, `publicIp`, `ramMb`, `region`, `reverseDns`, `script`, `size`, `sshkeyId`, `status`, `template`.
     */
    key: pulumi.Input<string>;
}

export interface GetKubernetesVersionFilter {
    /**
     * Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
     */
    all?: boolean;
    /**
     * Filter versions by this key. This may be one of `default`, `label`, `type`, `version`.
     */
    key: string;
    /**
     * One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
     */
    matchBy?: string;
    /**
     * Only retrieves `versions` which keys has value that matches one of the values provided here
     */
    values: string[];
}

export interface GetKubernetesVersionFilterArgs {
    /**
     * Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
     */
    all?: pulumi.Input<boolean>;
    /**
     * Filter versions by this key. This may be one of `default`, `label`, `type`, `version`.
     */
    key: pulumi.Input<string>;
    /**
     * One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
     */
    matchBy?: pulumi.Input<string>;
    /**
     * Only retrieves `versions` which keys has value that matches one of the values provided here
     */
    values: pulumi.Input<pulumi.Input<string>[]>;
}

export interface GetKubernetesVersionSort {
    /**
     * The sort direction. This may be either `asc` or `desc`.
     */
    direction?: string;
    /**
     * Sort versions by this key. This may be one of `default`, `label`, `type`, `version`.
     */
    key: string;
}

export interface GetKubernetesVersionSortArgs {
    /**
     * The sort direction. This may be either `asc` or `desc`.
     */
    direction?: pulumi.Input<string>;
    /**
     * Sort versions by this key. This may be one of `default`, `label`, `type`, `version`.
     */
    key: pulumi.Input<string>;
}

export interface GetRegionFilter {
    /**
     * Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
     */
    all?: boolean;
    /**
     * Filter regions by this key. This may be one of `code`, `country`, `default`, `name`.
     */
    key: string;
    /**
     * One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
     */
    matchBy?: string;
    /**
     * Only retrieves `regions` which keys has value that matches one of the values provided here
     */
    values: string[];
}

export interface GetRegionFilterArgs {
    /**
     * Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
     */
    all?: pulumi.Input<boolean>;
    /**
     * Filter regions by this key. This may be one of `code`, `country`, `default`, `name`.
     */
    key: pulumi.Input<string>;
    /**
     * One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
     */
    matchBy?: pulumi.Input<string>;
    /**
     * Only retrieves `regions` which keys has value that matches one of the values provided here
     */
    values: pulumi.Input<pulumi.Input<string>[]>;
}

export interface GetRegionSort {
    /**
     * The sort direction. This may be either `asc` or `desc`.
     */
    direction?: string;
    /**
     * Sort regions by this key. This may be one of `code`, `country`, `default`, `name`.
     */
    key: string;
}

export interface GetRegionSortArgs {
    /**
     * The sort direction. This may be either `asc` or `desc`.
     */
    direction?: pulumi.Input<string>;
    /**
     * Sort regions by this key. This may be one of `code`, `country`, `default`, `name`.
     */
    key: pulumi.Input<string>;
}

export interface GetSizeFilter {
    /**
     * Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
     */
    all?: boolean;
    /**
     * Filter sizes by this key. This may be one of `cpu`, `description`, `disk`, `name`, `ram`, `selectable`, `type`.
     */
    key: string;
    /**
     * One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
     */
    matchBy?: string;
    /**
     * Only retrieves `sizes` which keys has value that matches one of the values provided here
     */
    values: string[];
}

export interface GetSizeFilterArgs {
    /**
     * Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
     */
    all?: pulumi.Input<boolean>;
    /**
     * Filter sizes by this key. This may be one of `cpu`, `description`, `disk`, `name`, `ram`, `selectable`, `type`.
     */
    key: pulumi.Input<string>;
    /**
     * One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
     */
    matchBy?: pulumi.Input<string>;
    /**
     * Only retrieves `sizes` which keys has value that matches one of the values provided here
     */
    values: pulumi.Input<pulumi.Input<string>[]>;
}

export interface GetSizeSort {
    /**
     * The sort direction. This may be either `asc` or `desc`.
     */
    direction?: string;
    /**
     * Sort sizes by this key. This may be one of `cpu`, `description`, `disk`, `name`, `ram`, `selectable`, `type`.
     */
    key: string;
}

export interface GetSizeSortArgs {
    /**
     * The sort direction. This may be either `asc` or `desc`.
     */
    direction?: pulumi.Input<string>;
    /**
     * Sort sizes by this key. This may be one of `cpu`, `description`, `disk`, `name`, `ram`, `selectable`, `type`.
     */
    key: pulumi.Input<string>;
}

export interface KubernetesClusterInstalledApplication {
    application?: pulumi.Input<string>;
    category?: pulumi.Input<string>;
    installed?: pulumi.Input<boolean>;
    version?: pulumi.Input<string>;
}

export interface KubernetesClusterPools {
    /**
     * Instance names in the nodepool
     */
    instanceNames?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Node pool label, if you don't provide one, we will generate one for you
     */
    label?: pulumi.Input<string>;
    /**
     * Number of nodes in the nodepool
     */
    nodeCount: pulumi.Input<number>;
    /**
     * Node pool belongs to the public ip node pool
     */
    publicIpNodePool?: pulumi.Input<boolean>;
    /**
     * Size of the nodes in the nodepool
     */
    size: pulumi.Input<string>;
}

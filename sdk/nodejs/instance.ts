// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a Civo instance resource. This can be used to create, modify, and delete instances.
 *
 * ## Import
 *
 * using ID
 *
 * ```sh
 * $ pulumi import civo:index/instance:Instance myintance 18bd98ad-1b6e-4f87-b48f-e690b4fd7413
 * ```
 */
export class Instance extends pulumi.CustomResource {
    /**
     * Get an existing Instance resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InstanceState, opts?: pulumi.CustomResourceOptions): Instance {
        return new Instance(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'civo:index/instance:Instance';

    /**
     * Returns true if the given object is an instance of Instance.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Instance {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Instance.__pulumiType;
    }

    /**
     * Instance's CPU cores
     */
    public /*out*/ readonly cpuCores!: pulumi.Output<number>;
    /**
     * Timestamp when the instance was created
     */
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    /**
     * Instance's disk (GB)
     */
    public /*out*/ readonly diskGb!: pulumi.Output<number>;
    /**
     * The ID for the disk image to use to build the instance
     */
    public readonly diskImage!: pulumi.Output<string>;
    /**
     * The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all)
     */
    public readonly firewallId!: pulumi.Output<string>;
    /**
     * A fully qualified domain name that should be set as the instance's hostname
     */
    public readonly hostname!: pulumi.Output<string>;
    /**
     * Initial password for login
     */
    public /*out*/ readonly initialPassword!: pulumi.Output<string>;
    /**
     * The name of the initial user created on the server (optional; this will default to the template's defaultUsername and fallback to civo)
     */
    public readonly initialUser!: pulumi.Output<string | undefined>;
    /**
     * This must be the ID of the network from the network listing (optional; default network used when not specified)
     */
    public readonly networkId!: pulumi.Output<string>;
    /**
     * Add some notes to the instance
     */
    public readonly notes!: pulumi.Output<string | undefined>;
    /**
     * Instance's private IP address
     */
    public /*out*/ readonly privateIp!: pulumi.Output<string>;
    /**
     * Instance's public IP address
     */
    public /*out*/ readonly publicIp!: pulumi.Output<string>;
    /**
     * This should be either 'none' or 'create' (default: 'create')
     */
    public readonly publicIpRequired!: pulumi.Output<string | undefined>;
    /**
     * Instance's RAM (MB)
     */
    public /*out*/ readonly ramMb!: pulumi.Output<number>;
    /**
     * The region for the instance, if not declare we use the region in declared in the provider
     */
    public readonly region!: pulumi.Output<string | undefined>;
    /**
     * A fully qualified domain name that should be used as the instance's IP's reverse DNS (optional, uses the hostname if unspecified)
     */
    public readonly reverseDns!: pulumi.Output<string | undefined>;
    /**
     * The contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance, read/write/executable only by root and then will be executed at the end of the cloud initialization
     */
    public readonly script!: pulumi.Output<string | undefined>;
    /**
     * The name of the size, from the current list, e.g. g3.xsmall
     */
    public readonly size!: pulumi.Output<string | undefined>;
    /**
     * Instance's source ID
     */
    public /*out*/ readonly sourceId!: pulumi.Output<string>;
    /**
     * Instance's source type
     */
    public /*out*/ readonly sourceType!: pulumi.Output<string>;
    /**
     * The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn't provided a random password will be set and returned in the initialPassword field)
     */
    public readonly sshkeyId!: pulumi.Output<string | undefined>;
    /**
     * Instance's status
     */
    public /*out*/ readonly status!: pulumi.Output<string>;
    /**
     * An optional list of tags, represented as a key, value pair
     */
    public readonly tags!: pulumi.Output<string[] | undefined>;
    /**
     * The ID for the template to use to build the instance
     *
     * @deprecated "template" attribute is deprecated. Moving forward, please use "disk_image" attribute.
     */
    public readonly template!: pulumi.Output<string>;

    /**
     * Create a Instance resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: InstanceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: InstanceArgs | InstanceState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as InstanceState | undefined;
            resourceInputs["cpuCores"] = state ? state.cpuCores : undefined;
            resourceInputs["createdAt"] = state ? state.createdAt : undefined;
            resourceInputs["diskGb"] = state ? state.diskGb : undefined;
            resourceInputs["diskImage"] = state ? state.diskImage : undefined;
            resourceInputs["firewallId"] = state ? state.firewallId : undefined;
            resourceInputs["hostname"] = state ? state.hostname : undefined;
            resourceInputs["initialPassword"] = state ? state.initialPassword : undefined;
            resourceInputs["initialUser"] = state ? state.initialUser : undefined;
            resourceInputs["networkId"] = state ? state.networkId : undefined;
            resourceInputs["notes"] = state ? state.notes : undefined;
            resourceInputs["privateIp"] = state ? state.privateIp : undefined;
            resourceInputs["publicIp"] = state ? state.publicIp : undefined;
            resourceInputs["publicIpRequired"] = state ? state.publicIpRequired : undefined;
            resourceInputs["ramMb"] = state ? state.ramMb : undefined;
            resourceInputs["region"] = state ? state.region : undefined;
            resourceInputs["reverseDns"] = state ? state.reverseDns : undefined;
            resourceInputs["script"] = state ? state.script : undefined;
            resourceInputs["size"] = state ? state.size : undefined;
            resourceInputs["sourceId"] = state ? state.sourceId : undefined;
            resourceInputs["sourceType"] = state ? state.sourceType : undefined;
            resourceInputs["sshkeyId"] = state ? state.sshkeyId : undefined;
            resourceInputs["status"] = state ? state.status : undefined;
            resourceInputs["tags"] = state ? state.tags : undefined;
            resourceInputs["template"] = state ? state.template : undefined;
        } else {
            const args = argsOrState as InstanceArgs | undefined;
            resourceInputs["diskImage"] = args ? args.diskImage : undefined;
            resourceInputs["firewallId"] = args ? args.firewallId : undefined;
            resourceInputs["hostname"] = args ? args.hostname : undefined;
            resourceInputs["initialUser"] = args ? args.initialUser : undefined;
            resourceInputs["networkId"] = args ? args.networkId : undefined;
            resourceInputs["notes"] = args ? args.notes : undefined;
            resourceInputs["publicIpRequired"] = args ? args.publicIpRequired : undefined;
            resourceInputs["region"] = args ? args.region : undefined;
            resourceInputs["reverseDns"] = args ? args.reverseDns : undefined;
            resourceInputs["script"] = args ? args.script : undefined;
            resourceInputs["size"] = args ? args.size : undefined;
            resourceInputs["sshkeyId"] = args ? args.sshkeyId : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["template"] = args ? args.template : undefined;
            resourceInputs["cpuCores"] = undefined /*out*/;
            resourceInputs["createdAt"] = undefined /*out*/;
            resourceInputs["diskGb"] = undefined /*out*/;
            resourceInputs["initialPassword"] = undefined /*out*/;
            resourceInputs["privateIp"] = undefined /*out*/;
            resourceInputs["publicIp"] = undefined /*out*/;
            resourceInputs["ramMb"] = undefined /*out*/;
            resourceInputs["sourceId"] = undefined /*out*/;
            resourceInputs["sourceType"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["initialPassword"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(Instance.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Instance resources.
 */
export interface InstanceState {
    /**
     * Instance's CPU cores
     */
    cpuCores?: pulumi.Input<number>;
    /**
     * Timestamp when the instance was created
     */
    createdAt?: pulumi.Input<string>;
    /**
     * Instance's disk (GB)
     */
    diskGb?: pulumi.Input<number>;
    /**
     * The ID for the disk image to use to build the instance
     */
    diskImage?: pulumi.Input<string>;
    /**
     * The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all)
     */
    firewallId?: pulumi.Input<string>;
    /**
     * A fully qualified domain name that should be set as the instance's hostname
     */
    hostname?: pulumi.Input<string>;
    /**
     * Initial password for login
     */
    initialPassword?: pulumi.Input<string>;
    /**
     * The name of the initial user created on the server (optional; this will default to the template's defaultUsername and fallback to civo)
     */
    initialUser?: pulumi.Input<string>;
    /**
     * This must be the ID of the network from the network listing (optional; default network used when not specified)
     */
    networkId?: pulumi.Input<string>;
    /**
     * Add some notes to the instance
     */
    notes?: pulumi.Input<string>;
    /**
     * Instance's private IP address
     */
    privateIp?: pulumi.Input<string>;
    /**
     * Instance's public IP address
     */
    publicIp?: pulumi.Input<string>;
    /**
     * This should be either 'none' or 'create' (default: 'create')
     */
    publicIpRequired?: pulumi.Input<string>;
    /**
     * Instance's RAM (MB)
     */
    ramMb?: pulumi.Input<number>;
    /**
     * The region for the instance, if not declare we use the region in declared in the provider
     */
    region?: pulumi.Input<string>;
    /**
     * A fully qualified domain name that should be used as the instance's IP's reverse DNS (optional, uses the hostname if unspecified)
     */
    reverseDns?: pulumi.Input<string>;
    /**
     * The contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance, read/write/executable only by root and then will be executed at the end of the cloud initialization
     */
    script?: pulumi.Input<string>;
    /**
     * The name of the size, from the current list, e.g. g3.xsmall
     */
    size?: pulumi.Input<string>;
    /**
     * Instance's source ID
     */
    sourceId?: pulumi.Input<string>;
    /**
     * Instance's source type
     */
    sourceType?: pulumi.Input<string>;
    /**
     * The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn't provided a random password will be set and returned in the initialPassword field)
     */
    sshkeyId?: pulumi.Input<string>;
    /**
     * Instance's status
     */
    status?: pulumi.Input<string>;
    /**
     * An optional list of tags, represented as a key, value pair
     */
    tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The ID for the template to use to build the instance
     *
     * @deprecated "template" attribute is deprecated. Moving forward, please use "disk_image" attribute.
     */
    template?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Instance resource.
 */
export interface InstanceArgs {
    /**
     * The ID for the disk image to use to build the instance
     */
    diskImage?: pulumi.Input<string>;
    /**
     * The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all)
     */
    firewallId?: pulumi.Input<string>;
    /**
     * A fully qualified domain name that should be set as the instance's hostname
     */
    hostname?: pulumi.Input<string>;
    /**
     * The name of the initial user created on the server (optional; this will default to the template's defaultUsername and fallback to civo)
     */
    initialUser?: pulumi.Input<string>;
    /**
     * This must be the ID of the network from the network listing (optional; default network used when not specified)
     */
    networkId?: pulumi.Input<string>;
    /**
     * Add some notes to the instance
     */
    notes?: pulumi.Input<string>;
    /**
     * This should be either 'none' or 'create' (default: 'create')
     */
    publicIpRequired?: pulumi.Input<string>;
    /**
     * The region for the instance, if not declare we use the region in declared in the provider
     */
    region?: pulumi.Input<string>;
    /**
     * A fully qualified domain name that should be used as the instance's IP's reverse DNS (optional, uses the hostname if unspecified)
     */
    reverseDns?: pulumi.Input<string>;
    /**
     * The contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance, read/write/executable only by root and then will be executed at the end of the cloud initialization
     */
    script?: pulumi.Input<string>;
    /**
     * The name of the size, from the current list, e.g. g3.xsmall
     */
    size?: pulumi.Input<string>;
    /**
     * The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn't provided a random password will be set and returned in the initialPassword field)
     */
    sshkeyId?: pulumi.Input<string>;
    /**
     * An optional list of tags, represented as a key, value pair
     */
    tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The ID for the template to use to build the instance
     *
     * @deprecated "template" attribute is deprecated. Moving forward, please use "disk_image" attribute.
     */
    template?: pulumi.Input<string>;
}

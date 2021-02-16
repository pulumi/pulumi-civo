// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a Civo Instance resource. This can be used to create,
 * modify, and delete Instances.
 *
 * ## Import
 *
 * Instances can be imported using the instance `id`, e.g.
 *
 * ```sh
 *  $ pulumi import civo:index/instance:Instance myintance 18bd98ad-1b6e-4f87-b48f-e690b4fd7413
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
     * Total cpu of the inatance.
     */
    public /*out*/ readonly cpuCores!: pulumi.Output<number>;
    /**
     * The date of creation of the instance
     */
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    /**
     * The size of the disk.
     */
    public /*out*/ readonly diskGb!: pulumi.Output<number>;
    /**
     * The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all).
     */
    public readonly firewallId!: pulumi.Output<string | undefined>;
    /**
     * The Instance hostname.
     */
    public readonly hostname!: pulumi.Output<string>;
    /**
     * Instance initial password
     */
    public /*out*/ readonly initialPassword!: pulumi.Output<string>;
    /**
     * The name of the initial user created on the server (optional; this will default to the template's defaultUsername and fallback to civo).
     */
    public readonly initialUser!: pulumi.Output<string | undefined>;
    /**
     * This must be the ID of the network from the network listing (optional; default network used when not specified).
     */
    public readonly networkId!: pulumi.Output<string | undefined>;
    /**
     * Add some notes to the instance.
     */
    public readonly notes!: pulumi.Output<string | undefined>;
    /**
     * The private ip.
     */
    public /*out*/ readonly privateIp!: pulumi.Output<string>;
    /**
     * Is the ip that is used to route the public ip from the internet to the instance using NAT
     */
    public /*out*/ readonly pseudoIp!: pulumi.Output<string>;
    /**
     * The public ip.
     */
    public /*out*/ readonly publicIp!: pulumi.Output<string>;
    /**
     * This should be either false, true or `move_ip_from:intances_id`.
     */
    public readonly publicIpRequired!: pulumi.Output<string | undefined>;
    /**
     * Total ram of the instance.
     */
    public /*out*/ readonly ramMb!: pulumi.Output<number>;
    /**
     * A fully qualified domain name that should be used as the instance's IP's reverse DNS (optional, uses the hostname if unspecified).
     */
    public readonly reverseDns!: pulumi.Output<string | undefined>;
    /**
     * the contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance, read/write/executable only by root and then will be executed at the end of the cloud initialization
     */
    public readonly script!: pulumi.Output<string | undefined>;
    /**
     * The name of the size, from the current list, e.g. g2.small (required).
     */
    public readonly size!: pulumi.Output<string | undefined>;
    /**
     * The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn't provided a random password will be set and returned in the initialPassword field).
     */
    public readonly sshkeyId!: pulumi.Output<string | undefined>;
    /**
     * The status of the instance
     */
    public /*out*/ readonly status!: pulumi.Output<string>;
    /**
     * An optional list of tags, represented as a key, value pair.
     */
    public readonly tags!: pulumi.Output<string[] | undefined>;
    /**
     * The ID for the template to use to build the instance.
     */
    public readonly template!: pulumi.Output<string | undefined>;

    /**
     * Create a Instance resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: InstanceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: InstanceArgs | InstanceState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as InstanceState | undefined;
            inputs["cpuCores"] = state ? state.cpuCores : undefined;
            inputs["createdAt"] = state ? state.createdAt : undefined;
            inputs["diskGb"] = state ? state.diskGb : undefined;
            inputs["firewallId"] = state ? state.firewallId : undefined;
            inputs["hostname"] = state ? state.hostname : undefined;
            inputs["initialPassword"] = state ? state.initialPassword : undefined;
            inputs["initialUser"] = state ? state.initialUser : undefined;
            inputs["networkId"] = state ? state.networkId : undefined;
            inputs["notes"] = state ? state.notes : undefined;
            inputs["privateIp"] = state ? state.privateIp : undefined;
            inputs["pseudoIp"] = state ? state.pseudoIp : undefined;
            inputs["publicIp"] = state ? state.publicIp : undefined;
            inputs["publicIpRequired"] = state ? state.publicIpRequired : undefined;
            inputs["ramMb"] = state ? state.ramMb : undefined;
            inputs["reverseDns"] = state ? state.reverseDns : undefined;
            inputs["script"] = state ? state.script : undefined;
            inputs["size"] = state ? state.size : undefined;
            inputs["sshkeyId"] = state ? state.sshkeyId : undefined;
            inputs["status"] = state ? state.status : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["template"] = state ? state.template : undefined;
        } else {
            const args = argsOrState as InstanceArgs | undefined;
            if ((!args || args.hostname === undefined) && !opts.urn) {
                throw new Error("Missing required property 'hostname'");
            }
            inputs["firewallId"] = args ? args.firewallId : undefined;
            inputs["hostname"] = args ? args.hostname : undefined;
            inputs["initialUser"] = args ? args.initialUser : undefined;
            inputs["networkId"] = args ? args.networkId : undefined;
            inputs["notes"] = args ? args.notes : undefined;
            inputs["publicIpRequired"] = args ? args.publicIpRequired : undefined;
            inputs["reverseDns"] = args ? args.reverseDns : undefined;
            inputs["script"] = args ? args.script : undefined;
            inputs["size"] = args ? args.size : undefined;
            inputs["sshkeyId"] = args ? args.sshkeyId : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["template"] = args ? args.template : undefined;
            inputs["cpuCores"] = undefined /*out*/;
            inputs["createdAt"] = undefined /*out*/;
            inputs["diskGb"] = undefined /*out*/;
            inputs["initialPassword"] = undefined /*out*/;
            inputs["privateIp"] = undefined /*out*/;
            inputs["pseudoIp"] = undefined /*out*/;
            inputs["publicIp"] = undefined /*out*/;
            inputs["ramMb"] = undefined /*out*/;
            inputs["status"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Instance.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Instance resources.
 */
export interface InstanceState {
    /**
     * Total cpu of the inatance.
     */
    readonly cpuCores?: pulumi.Input<number>;
    /**
     * The date of creation of the instance
     */
    readonly createdAt?: pulumi.Input<string>;
    /**
     * The size of the disk.
     */
    readonly diskGb?: pulumi.Input<number>;
    /**
     * The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all).
     */
    readonly firewallId?: pulumi.Input<string>;
    /**
     * The Instance hostname.
     */
    readonly hostname?: pulumi.Input<string>;
    /**
     * Instance initial password
     */
    readonly initialPassword?: pulumi.Input<string>;
    /**
     * The name of the initial user created on the server (optional; this will default to the template's defaultUsername and fallback to civo).
     */
    readonly initialUser?: pulumi.Input<string>;
    /**
     * This must be the ID of the network from the network listing (optional; default network used when not specified).
     */
    readonly networkId?: pulumi.Input<string>;
    /**
     * Add some notes to the instance.
     */
    readonly notes?: pulumi.Input<string>;
    /**
     * The private ip.
     */
    readonly privateIp?: pulumi.Input<string>;
    /**
     * Is the ip that is used to route the public ip from the internet to the instance using NAT
     */
    readonly pseudoIp?: pulumi.Input<string>;
    /**
     * The public ip.
     */
    readonly publicIp?: pulumi.Input<string>;
    /**
     * This should be either false, true or `move_ip_from:intances_id`.
     */
    readonly publicIpRequired?: pulumi.Input<string>;
    /**
     * Total ram of the instance.
     */
    readonly ramMb?: pulumi.Input<number>;
    /**
     * A fully qualified domain name that should be used as the instance's IP's reverse DNS (optional, uses the hostname if unspecified).
     */
    readonly reverseDns?: pulumi.Input<string>;
    /**
     * the contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance, read/write/executable only by root and then will be executed at the end of the cloud initialization
     */
    readonly script?: pulumi.Input<string>;
    /**
     * The name of the size, from the current list, e.g. g2.small (required).
     */
    readonly size?: pulumi.Input<string>;
    /**
     * The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn't provided a random password will be set and returned in the initialPassword field).
     */
    readonly sshkeyId?: pulumi.Input<string>;
    /**
     * The status of the instance
     */
    readonly status?: pulumi.Input<string>;
    /**
     * An optional list of tags, represented as a key, value pair.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The ID for the template to use to build the instance.
     */
    readonly template?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Instance resource.
 */
export interface InstanceArgs {
    /**
     * The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all).
     */
    readonly firewallId?: pulumi.Input<string>;
    /**
     * The Instance hostname.
     */
    readonly hostname: pulumi.Input<string>;
    /**
     * The name of the initial user created on the server (optional; this will default to the template's defaultUsername and fallback to civo).
     */
    readonly initialUser?: pulumi.Input<string>;
    /**
     * This must be the ID of the network from the network listing (optional; default network used when not specified).
     */
    readonly networkId?: pulumi.Input<string>;
    /**
     * Add some notes to the instance.
     */
    readonly notes?: pulumi.Input<string>;
    /**
     * This should be either false, true or `move_ip_from:intances_id`.
     */
    readonly publicIpRequired?: pulumi.Input<string>;
    /**
     * A fully qualified domain name that should be used as the instance's IP's reverse DNS (optional, uses the hostname if unspecified).
     */
    readonly reverseDns?: pulumi.Input<string>;
    /**
     * the contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance, read/write/executable only by root and then will be executed at the end of the cloud initialization
     */
    readonly script?: pulumi.Input<string>;
    /**
     * The name of the size, from the current list, e.g. g2.small (required).
     */
    readonly size?: pulumi.Input<string>;
    /**
     * The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn't provided a random password will be set and returned in the initialPassword field).
     */
    readonly sshkeyId?: pulumi.Input<string>;
    /**
     * An optional list of tags, represented as a key, value pair.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The ID for the template to use to build the instance.
     */
    readonly template?: pulumi.Input<string>;
}

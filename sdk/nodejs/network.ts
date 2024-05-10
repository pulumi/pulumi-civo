// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a Civo network resource. This can be used to create, modify, and delete networks.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as civo from "@pulumi/civo";
 *
 * const customNet = new civo.Network("custom_net", {label: "test_network"});
 * ```
 *
 * ## Import
 *
 * using ID
 *
 * ```sh
 * $ pulumi import civo:index/network:Network custom_net b8ecd2ab-2267-4a5e-8692-cbf1d32583e3
 * ```
 */
export class Network extends pulumi.CustomResource {
    /**
     * Get an existing Network resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NetworkState, opts?: pulumi.CustomResourceOptions): Network {
        return new Network(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'civo:index/network:Network';

    /**
     * Returns true if the given object is an instance of Network.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Network {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Network.__pulumiType;
    }

    /**
     * The CIDR block for the network
     */
    public readonly cidrV4!: pulumi.Output<string | undefined>;
    /**
     * If the network is default, this will be `true`
     */
    public /*out*/ readonly default!: pulumi.Output<boolean>;
    /**
     * Name for the network
     */
    public readonly label!: pulumi.Output<string>;
    /**
     * The name of the network
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * List of nameservers for the network
     */
    public readonly nameserversV4s!: pulumi.Output<string[] | undefined>;
    /**
     * The region of the network
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * End of the IPv4 allocation pool for VLAN
     */
    public readonly vlanAllocationPoolV4End!: pulumi.Output<string | undefined>;
    /**
     * Start of the IPv4 allocation pool for VLAN
     */
    public readonly vlanAllocationPoolV4Start!: pulumi.Output<string | undefined>;
    /**
     * CIDR for VLAN IPv4
     */
    public readonly vlanCidrV4!: pulumi.Output<string | undefined>;
    /**
     * Gateway IP for VLAN IPv4
     */
    public readonly vlanGatewayIpV4!: pulumi.Output<string | undefined>;
    /**
     * Hardware address for VLAN
     */
    public readonly vlanHardwareAddr!: pulumi.Output<string | undefined>;
    /**
     * VLAN ID for the network
     */
    public readonly vlanId!: pulumi.Output<number | undefined>;

    /**
     * Create a Network resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: NetworkArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: NetworkArgs | NetworkState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as NetworkState | undefined;
            resourceInputs["cidrV4"] = state ? state.cidrV4 : undefined;
            resourceInputs["default"] = state ? state.default : undefined;
            resourceInputs["label"] = state ? state.label : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["nameserversV4s"] = state ? state.nameserversV4s : undefined;
            resourceInputs["region"] = state ? state.region : undefined;
            resourceInputs["vlanAllocationPoolV4End"] = state ? state.vlanAllocationPoolV4End : undefined;
            resourceInputs["vlanAllocationPoolV4Start"] = state ? state.vlanAllocationPoolV4Start : undefined;
            resourceInputs["vlanCidrV4"] = state ? state.vlanCidrV4 : undefined;
            resourceInputs["vlanGatewayIpV4"] = state ? state.vlanGatewayIpV4 : undefined;
            resourceInputs["vlanHardwareAddr"] = state ? state.vlanHardwareAddr : undefined;
            resourceInputs["vlanId"] = state ? state.vlanId : undefined;
        } else {
            const args = argsOrState as NetworkArgs | undefined;
            if ((!args || args.label === undefined) && !opts.urn) {
                throw new Error("Missing required property 'label'");
            }
            resourceInputs["cidrV4"] = args ? args.cidrV4 : undefined;
            resourceInputs["label"] = args ? args.label : undefined;
            resourceInputs["nameserversV4s"] = args ? args.nameserversV4s : undefined;
            resourceInputs["region"] = args ? args.region : undefined;
            resourceInputs["vlanAllocationPoolV4End"] = args ? args.vlanAllocationPoolV4End : undefined;
            resourceInputs["vlanAllocationPoolV4Start"] = args ? args.vlanAllocationPoolV4Start : undefined;
            resourceInputs["vlanCidrV4"] = args ? args.vlanCidrV4 : undefined;
            resourceInputs["vlanGatewayIpV4"] = args ? args.vlanGatewayIpV4 : undefined;
            resourceInputs["vlanHardwareAddr"] = args ? args.vlanHardwareAddr : undefined;
            resourceInputs["vlanId"] = args ? args.vlanId : undefined;
            resourceInputs["default"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Network.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Network resources.
 */
export interface NetworkState {
    /**
     * The CIDR block for the network
     */
    cidrV4?: pulumi.Input<string>;
    /**
     * If the network is default, this will be `true`
     */
    default?: pulumi.Input<boolean>;
    /**
     * Name for the network
     */
    label?: pulumi.Input<string>;
    /**
     * The name of the network
     */
    name?: pulumi.Input<string>;
    /**
     * List of nameservers for the network
     */
    nameserversV4s?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The region of the network
     */
    region?: pulumi.Input<string>;
    /**
     * End of the IPv4 allocation pool for VLAN
     */
    vlanAllocationPoolV4End?: pulumi.Input<string>;
    /**
     * Start of the IPv4 allocation pool for VLAN
     */
    vlanAllocationPoolV4Start?: pulumi.Input<string>;
    /**
     * CIDR for VLAN IPv4
     */
    vlanCidrV4?: pulumi.Input<string>;
    /**
     * Gateway IP for VLAN IPv4
     */
    vlanGatewayIpV4?: pulumi.Input<string>;
    /**
     * Hardware address for VLAN
     */
    vlanHardwareAddr?: pulumi.Input<string>;
    /**
     * VLAN ID for the network
     */
    vlanId?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a Network resource.
 */
export interface NetworkArgs {
    /**
     * The CIDR block for the network
     */
    cidrV4?: pulumi.Input<string>;
    /**
     * Name for the network
     */
    label: pulumi.Input<string>;
    /**
     * List of nameservers for the network
     */
    nameserversV4s?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The region of the network
     */
    region?: pulumi.Input<string>;
    /**
     * End of the IPv4 allocation pool for VLAN
     */
    vlanAllocationPoolV4End?: pulumi.Input<string>;
    /**
     * Start of the IPv4 allocation pool for VLAN
     */
    vlanAllocationPoolV4Start?: pulumi.Input<string>;
    /**
     * CIDR for VLAN IPv4
     */
    vlanCidrV4?: pulumi.Input<string>;
    /**
     * Gateway IP for VLAN IPv4
     */
    vlanGatewayIpV4?: pulumi.Input<string>;
    /**
     * Hardware address for VLAN
     */
    vlanHardwareAddr?: pulumi.Input<string>;
    /**
     * VLAN ID for the network
     */
    vlanId?: pulumi.Input<number>;
}

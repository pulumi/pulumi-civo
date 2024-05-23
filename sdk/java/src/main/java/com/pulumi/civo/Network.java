// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo;

import com.pulumi.civo.NetworkArgs;
import com.pulumi.civo.Utilities;
import com.pulumi.civo.inputs.NetworkState;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * Provides a Civo network resource. This can be used to create, modify, and delete networks.
 * 
 * ## Example Usage
 * 
 * &lt;!--Start PulumiCodeChooser --&gt;
 * <pre>
 * {@code
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.civo.Network;
 * import com.pulumi.civo.NetworkArgs;
 * import java.util.List;
 * import java.util.ArrayList;
 * import java.util.Map;
 * import java.io.File;
 * import java.nio.file.Files;
 * import java.nio.file.Paths;
 * 
 * public class App {
 *     public static void main(String[] args) {
 *         Pulumi.run(App::stack);
 *     }
 * 
 *     public static void stack(Context ctx) {
 *         var customNet = new Network("customNet", NetworkArgs.builder()
 *             .label("test_network")
 *             .build());
 * 
 *     }
 * }
 * }
 * </pre>
 * &lt;!--End PulumiCodeChooser --&gt;
 * 
 * ## Import
 * 
 * using ID
 * 
 * ```sh
 * $ pulumi import civo:index/network:Network custom_net b8ecd2ab-2267-4a5e-8692-cbf1d32583e3
 * ```
 * 
 */
@ResourceType(type="civo:index/network:Network")
public class Network extends com.pulumi.resources.CustomResource {
    /**
     * The CIDR block for the network
     * 
     */
    @Export(name="cidrV4", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> cidrV4;

    /**
     * @return The CIDR block for the network
     * 
     */
    public Output<Optional<String>> cidrV4() {
        return Codegen.optional(this.cidrV4);
    }
    /**
     * If the network is default, this will be `true`
     * 
     */
    @Export(name="default", refs={Boolean.class}, tree="[0]")
    private Output<Boolean> default_;

    /**
     * @return If the network is default, this will be `true`
     * 
     */
    public Output<Boolean> default_() {
        return this.default_;
    }
    /**
     * Name for the network
     * 
     */
    @Export(name="label", refs={String.class}, tree="[0]")
    private Output<String> label;

    /**
     * @return Name for the network
     * 
     */
    public Output<String> label() {
        return this.label;
    }
    /**
     * The name of the network
     * 
     */
    @Export(name="name", refs={String.class}, tree="[0]")
    private Output<String> name;

    /**
     * @return The name of the network
     * 
     */
    public Output<String> name() {
        return this.name;
    }
    /**
     * List of nameservers for the network
     * 
     */
    @Export(name="nameserversV4s", refs={List.class,String.class}, tree="[0,1]")
    private Output</* @Nullable */ List<String>> nameserversV4s;

    /**
     * @return List of nameservers for the network
     * 
     */
    public Output<Optional<List<String>>> nameserversV4s() {
        return Codegen.optional(this.nameserversV4s);
    }
    /**
     * The region of the network
     * 
     */
    @Export(name="region", refs={String.class}, tree="[0]")
    private Output<String> region;

    /**
     * @return The region of the network
     * 
     */
    public Output<String> region() {
        return this.region;
    }
    /**
     * End of the IPv4 allocation pool for VLAN
     * 
     */
    @Export(name="vlanAllocationPoolV4End", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> vlanAllocationPoolV4End;

    /**
     * @return End of the IPv4 allocation pool for VLAN
     * 
     */
    public Output<Optional<String>> vlanAllocationPoolV4End() {
        return Codegen.optional(this.vlanAllocationPoolV4End);
    }
    /**
     * Start of the IPv4 allocation pool for VLAN
     * 
     */
    @Export(name="vlanAllocationPoolV4Start", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> vlanAllocationPoolV4Start;

    /**
     * @return Start of the IPv4 allocation pool for VLAN
     * 
     */
    public Output<Optional<String>> vlanAllocationPoolV4Start() {
        return Codegen.optional(this.vlanAllocationPoolV4Start);
    }
    /**
     * CIDR for VLAN IPv4
     * 
     */
    @Export(name="vlanCidrV4", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> vlanCidrV4;

    /**
     * @return CIDR for VLAN IPv4
     * 
     */
    public Output<Optional<String>> vlanCidrV4() {
        return Codegen.optional(this.vlanCidrV4);
    }
    /**
     * Gateway IP for VLAN IPv4
     * 
     */
    @Export(name="vlanGatewayIpV4", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> vlanGatewayIpV4;

    /**
     * @return Gateway IP for VLAN IPv4
     * 
     */
    public Output<Optional<String>> vlanGatewayIpV4() {
        return Codegen.optional(this.vlanGatewayIpV4);
    }
    /**
     * Hardware address for VLAN
     * 
     */
    @Export(name="vlanHardwareAddr", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> vlanHardwareAddr;

    /**
     * @return Hardware address for VLAN
     * 
     */
    public Output<Optional<String>> vlanHardwareAddr() {
        return Codegen.optional(this.vlanHardwareAddr);
    }
    /**
     * VLAN ID for the network
     * 
     */
    @Export(name="vlanId", refs={Integer.class}, tree="[0]")
    private Output</* @Nullable */ Integer> vlanId;

    /**
     * @return VLAN ID for the network
     * 
     */
    public Output<Optional<Integer>> vlanId() {
        return Codegen.optional(this.vlanId);
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public Network(String name) {
        this(name, NetworkArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public Network(String name, NetworkArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public Network(String name, NetworkArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("civo:index/network:Network", name, args == null ? NetworkArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private Network(String name, Output<String> id, @Nullable NetworkState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("civo:index/network:Network", name, state, makeResourceOptions(options, id));
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .build();
        return com.pulumi.resources.CustomResourceOptions.merge(defaultOptions, options, id);
    }

    /**
     * Get an existing Host resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state
     * @param options Optional settings to control the behavior of the CustomResource.
     */
    public static Network get(String name, Output<String> id, @Nullable NetworkState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new Network(name, id, state, options);
    }
}

// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo;

import com.pulumi.civo.FirewallArgs;
import com.pulumi.civo.Utilities;
import com.pulumi.civo.inputs.FirewallState;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import java.lang.Boolean;
import java.lang.String;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * Provides a Civo firewall resource. This can be used to create, modify, and delete firewalls.
 * 
 * ## Example Usage
 * ```java
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.civo.Network;
 * import com.pulumi.civo.NetworkArgs;
 * import com.pulumi.civo.Firewall;
 * import com.pulumi.civo.FirewallArgs;
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
 *         var customNet = new Network(&#34;customNet&#34;, NetworkArgs.builder()        
 *             .label(&#34;my-custom-network&#34;)
 *             .build());
 * 
 *         var www = new Firewall(&#34;www&#34;, FirewallArgs.builder()        
 *             .networkId(customNet.id())
 *             .build());
 * 
 *     }
 * }
 * ```
 * 
 * ## Import
 * 
 * # using ID
 * 
 * ```sh
 *  $ pulumi import civo:index/firewall:Firewall www b8ecd2ab-2267-4a5e-8692-cbf1d32583e3
 * ```
 * 
 */
@ResourceType(type="civo:index/firewall:Firewall")
public class Firewall extends com.pulumi.resources.CustomResource {
    /**
     * The create rules flag is used to create the default firewall rules, if is not defined will be set to true
     * 
     */
    @Export(name="createDefaultRules", type=Boolean.class, parameters={})
    private Output</* @Nullable */ Boolean> createDefaultRules;

    /**
     * @return The create rules flag is used to create the default firewall rules, if is not defined will be set to true
     * 
     */
    public Output<Optional<Boolean>> createDefaultRules() {
        return Codegen.optional(this.createDefaultRules);
    }
    /**
     * The firewall name
     * 
     */
    @Export(name="name", type=String.class, parameters={})
    private Output<String> name;

    /**
     * @return The firewall name
     * 
     */
    public Output<String> name() {
        return this.name;
    }
    /**
     * The firewall network, if is not defined we use the default network
     * 
     */
    @Export(name="networkId", type=String.class, parameters={})
    private Output<String> networkId;

    /**
     * @return The firewall network, if is not defined we use the default network
     * 
     */
    public Output<String> networkId() {
        return this.networkId;
    }
    /**
     * The firewall region, if is not defined we use the global defined in the provider
     * 
     */
    @Export(name="region", type=String.class, parameters={})
    private Output</* @Nullable */ String> region;

    /**
     * @return The firewall region, if is not defined we use the global defined in the provider
     * 
     */
    public Output<Optional<String>> region() {
        return Codegen.optional(this.region);
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public Firewall(String name) {
        this(name, FirewallArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public Firewall(String name, @Nullable FirewallArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public Firewall(String name, @Nullable FirewallArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("civo:index/firewall:Firewall", name, args == null ? FirewallArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private Firewall(String name, Output<String> id, @Nullable FirewallState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("civo:index/firewall:Firewall", name, state, makeResourceOptions(options, id));
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
    public static Firewall get(String name, Output<String> id, @Nullable FirewallState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new Firewall(name, id, state, options);
    }
}

// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo;

import com.pulumi.civo.ReservedIpArgs;
import com.pulumi.civo.Utilities;
import com.pulumi.civo.inputs.ReservedIpState;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import java.lang.String;
import javax.annotation.Nullable;

/**
 * Provides a Civo reserved IP to represent a publicly-accessible static IP addresses that can be mapped to one of your Instancesor Load Balancer.
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
 * import com.pulumi.civo.ReservedIp;
 * import com.pulumi.civo.ReservedIpArgs;
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
 *         var www = new ReservedIp("www", ReservedIpArgs.builder()        
 *             .name("nginx-www")
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
 * terrafom import civo_reserved_ip.www 9f0e86fc-b2c6-46b4-82ed-2f28419f8ae3
 * 
 */
@ResourceType(type="civo:index/reservedIp:ReservedIp")
public class ReservedIp extends com.pulumi.resources.CustomResource {
    /**
     * The IP Address of the resource
     * 
     */
    @Export(name="ip", refs={String.class}, tree="[0]")
    private Output<String> ip;

    /**
     * @return The IP Address of the resource
     * 
     */
    public Output<String> ip() {
        return this.ip;
    }
    /**
     * Name for the ip address
     * 
     */
    @Export(name="name", refs={String.class}, tree="[0]")
    private Output<String> name;

    /**
     * @return Name for the ip address
     * 
     */
    public Output<String> name() {
        return this.name;
    }
    /**
     * The region of the ip
     * 
     */
    @Export(name="region", refs={String.class}, tree="[0]")
    private Output<String> region;

    /**
     * @return The region of the ip
     * 
     */
    public Output<String> region() {
        return this.region;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public ReservedIp(String name) {
        this(name, ReservedIpArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public ReservedIp(String name, @Nullable ReservedIpArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public ReservedIp(String name, @Nullable ReservedIpArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("civo:index/reservedIp:ReservedIp", name, args == null ? ReservedIpArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private ReservedIp(String name, Output<String> id, @Nullable ReservedIpState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("civo:index/reservedIp:ReservedIp", name, state, makeResourceOptions(options, id));
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
    public static ReservedIp get(String name, Output<String> id, @Nullable ReservedIpState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new ReservedIp(name, id, state, options);
    }
}

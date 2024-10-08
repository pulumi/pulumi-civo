// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo;

import com.pulumi.civo.DnsDomainNameArgs;
import com.pulumi.civo.Utilities;
import com.pulumi.civo.inputs.DnsDomainNameState;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import java.lang.String;
import javax.annotation.Nullable;

/**
 * Provides a Civo DNS domain name resource.
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
 * import com.pulumi.civo.DnsDomainName;
 * import com.pulumi.civo.DnsDomainNameArgs;
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
 *         // Create a new domain name
 *         var main = new DnsDomainName("main", DnsDomainNameArgs.builder()
 *             .name("mydomain.com")
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
 * using domain name
 * 
 * ```sh
 * $ pulumi import civo:index/dnsDomainName:DnsDomainName main mydomain.com
 * ```
 * 
 */
@ResourceType(type="civo:index/dnsDomainName:DnsDomainName")
public class DnsDomainName extends com.pulumi.resources.CustomResource {
    /**
     * The account ID of the domain
     * 
     */
    @Export(name="accountId", refs={String.class}, tree="[0]")
    private Output<String> accountId;

    /**
     * @return The account ID of the domain
     * 
     */
    public Output<String> accountId() {
        return this.accountId;
    }
    /**
     * The name of the domain
     * 
     */
    @Export(name="name", refs={String.class}, tree="[0]")
    private Output<String> name;

    /**
     * @return The name of the domain
     * 
     */
    public Output<String> name() {
        return this.name;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public DnsDomainName(java.lang.String name) {
        this(name, DnsDomainNameArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public DnsDomainName(java.lang.String name, @Nullable DnsDomainNameArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public DnsDomainName(java.lang.String name, @Nullable DnsDomainNameArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("civo:index/dnsDomainName:DnsDomainName", name, makeArgs(args, options), makeResourceOptions(options, Codegen.empty()), false);
    }

    private DnsDomainName(java.lang.String name, Output<java.lang.String> id, @Nullable DnsDomainNameState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("civo:index/dnsDomainName:DnsDomainName", name, state, makeResourceOptions(options, id), false);
    }

    private static DnsDomainNameArgs makeArgs(@Nullable DnsDomainNameArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        if (options != null && options.getUrn().isPresent()) {
            return null;
        }
        return args == null ? DnsDomainNameArgs.Empty : args;
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<java.lang.String> id) {
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
    public static DnsDomainName get(java.lang.String name, Output<java.lang.String> id, @Nullable DnsDomainNameState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new DnsDomainName(name, id, state, options);
    }
}

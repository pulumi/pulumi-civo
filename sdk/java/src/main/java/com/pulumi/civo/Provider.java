// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo;

import com.pulumi.civo.ProviderArgs;
import com.pulumi.civo.Utilities;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import java.lang.String;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * The provider type for the civo package. By default, resources use package-wide configuration
 * settings, however an explicit `Provider` instance may be created and passed during resource
 * construction to achieve fine-grained programmatic control over provider settings. See the
 * [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
 * 
 */
@ResourceType(type="pulumi:providers:civo")
public class Provider extends com.pulumi.resources.ProviderResource {
    /**
     * The Base URL to use for CIVO API.
     * 
     */
    @Export(name="apiEndpoint", type=String.class, parameters={})
    private Output</* @Nullable */ String> apiEndpoint;

    /**
     * @return The Base URL to use for CIVO API.
     * 
     */
    public Output<Optional<String>> apiEndpoint() {
        return Codegen.optional(this.apiEndpoint);
    }
    /**
     * If region is not set, then no region will be used and them you need expensify in every resource even if you expensify
     * here you can overwrite in a resource.
     * 
     */
    @Export(name="region", type=String.class, parameters={})
    private Output</* @Nullable */ String> region;

    /**
     * @return If region is not set, then no region will be used and them you need expensify in every resource even if you expensify
     * here you can overwrite in a resource.
     * 
     */
    public Output<Optional<String>> region() {
        return Codegen.optional(this.region);
    }
    /**
     * This is the Civo API token. Alternatively, this can also be specified using `CIVO_TOKEN` environment variable.
     * 
     */
    @Export(name="token", type=String.class, parameters={})
    private Output</* @Nullable */ String> token;

    /**
     * @return This is the Civo API token. Alternatively, this can also be specified using `CIVO_TOKEN` environment variable.
     * 
     */
    public Output<Optional<String>> token() {
        return Codegen.optional(this.token);
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public Provider(String name) {
        this(name, ProviderArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public Provider(String name, @Nullable ProviderArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public Provider(String name, @Nullable ProviderArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("civo", name, args == null ? ProviderArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .build();
        return com.pulumi.resources.CustomResourceOptions.merge(defaultOptions, options, id);
    }

}
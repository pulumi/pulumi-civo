// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class ProviderArgs extends com.pulumi.resources.ResourceArgs {

    public static final ProviderArgs Empty = new ProviderArgs();

    /**
     * If region is not set, then no region will be used and them you need expensify in every resource even if you expensify
     * here you can overwrite in a resource.
     * 
     */
    @Import(name="region")
    private @Nullable Output<String> region;

    /**
     * @return If region is not set, then no region will be used and them you need expensify in every resource even if you expensify
     * here you can overwrite in a resource.
     * 
     */
    public Optional<Output<String>> region() {
        return Optional.ofNullable(this.region);
    }

    /**
     * This is the Civo API token. Alternatively, this can also be specified using `CIVO_TOKEN` environment variable.
     * 
     */
    @Import(name="token")
    private @Nullable Output<String> token;

    /**
     * @return This is the Civo API token. Alternatively, this can also be specified using `CIVO_TOKEN` environment variable.
     * 
     */
    public Optional<Output<String>> token() {
        return Optional.ofNullable(this.token);
    }

    private ProviderArgs() {}

    private ProviderArgs(ProviderArgs $) {
        this.region = $.region;
        this.token = $.token;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ProviderArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ProviderArgs $;

        public Builder() {
            $ = new ProviderArgs();
        }

        public Builder(ProviderArgs defaults) {
            $ = new ProviderArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param region If region is not set, then no region will be used and them you need expensify in every resource even if you expensify
         * here you can overwrite in a resource.
         * 
         * @return builder
         * 
         */
        public Builder region(@Nullable Output<String> region) {
            $.region = region;
            return this;
        }

        /**
         * @param region If region is not set, then no region will be used and them you need expensify in every resource even if you expensify
         * here you can overwrite in a resource.
         * 
         * @return builder
         * 
         */
        public Builder region(String region) {
            return region(Output.of(region));
        }

        /**
         * @param token This is the Civo API token. Alternatively, this can also be specified using `CIVO_TOKEN` environment variable.
         * 
         * @return builder
         * 
         */
        public Builder token(@Nullable Output<String> token) {
            $.token = token;
            return this;
        }

        /**
         * @param token This is the Civo API token. Alternatively, this can also be specified using `CIVO_TOKEN` environment variable.
         * 
         * @return builder
         * 
         */
        public Builder token(String token) {
            return token(Output.of(token));
        }

        public ProviderArgs build() {
            return $;
        }
    }

}

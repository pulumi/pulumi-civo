// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.inputs;

import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetVolumePlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetVolumePlainArgs Empty = new GetVolumePlainArgs();

    /**
     * The ID of this resource.
     * 
     */
    @Import(name="id")
    private @Nullable String id;

    /**
     * @return The ID of this resource.
     * 
     */
    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }

    /**
     * The name of the volume
     * 
     */
    @Import(name="name")
    private @Nullable String name;

    /**
     * @return The name of the volume
     * 
     */
    public Optional<String> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * The region where volume is running
     * 
     */
    @Import(name="region")
    private @Nullable String region;

    /**
     * @return The region where volume is running
     * 
     */
    public Optional<String> region() {
        return Optional.ofNullable(this.region);
    }

    private GetVolumePlainArgs() {}

    private GetVolumePlainArgs(GetVolumePlainArgs $) {
        this.id = $.id;
        this.name = $.name;
        this.region = $.region;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetVolumePlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetVolumePlainArgs $;

        public Builder() {
            $ = new GetVolumePlainArgs();
        }

        public Builder(GetVolumePlainArgs defaults) {
            $ = new GetVolumePlainArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param id The ID of this resource.
         * 
         * @return builder
         * 
         */
        public Builder id(@Nullable String id) {
            $.id = id;
            return this;
        }

        /**
         * @param name The name of the volume
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable String name) {
            $.name = name;
            return this;
        }

        /**
         * @param region The region where volume is running
         * 
         * @return builder
         * 
         */
        public Builder region(@Nullable String region) {
            $.region = region;
            return this;
        }

        public GetVolumePlainArgs build() {
            return $;
        }
    }

}
// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetReservedIpArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetReservedIpArgs Empty = new GetReservedIpArgs();

    /**
     * ID for the ip address
     * 
     */
    @Import(name="id")
    private @Nullable Output<String> id;

    /**
     * @return ID for the ip address
     * 
     */
    public Optional<Output<String>> id() {
        return Optional.ofNullable(this.id);
    }

    /**
     * Name for the ip address
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return Name for the ip address
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    private GetReservedIpArgs() {}

    private GetReservedIpArgs(GetReservedIpArgs $) {
        this.id = $.id;
        this.name = $.name;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetReservedIpArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetReservedIpArgs $;

        public Builder() {
            $ = new GetReservedIpArgs();
        }

        public Builder(GetReservedIpArgs defaults) {
            $ = new GetReservedIpArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param id ID for the ip address
         * 
         * @return builder
         * 
         */
        public Builder id(@Nullable Output<String> id) {
            $.id = id;
            return this;
        }

        /**
         * @param id ID for the ip address
         * 
         * @return builder
         * 
         */
        public Builder id(String id) {
            return id(Output.of(id));
        }

        /**
         * @param name Name for the ip address
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name Name for the ip address
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        public GetReservedIpArgs build() {
            return $;
        }
    }

}
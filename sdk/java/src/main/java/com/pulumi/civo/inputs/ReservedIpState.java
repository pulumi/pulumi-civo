// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class ReservedIpState extends com.pulumi.resources.ResourceArgs {

    public static final ReservedIpState Empty = new ReservedIpState();

    /**
     * The IP Address of the resource
     * 
     */
    @Import(name="ip")
    private @Nullable Output<String> ip;

    /**
     * @return The IP Address of the resource
     * 
     */
    public Optional<Output<String>> ip() {
        return Optional.ofNullable(this.ip);
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

    /**
     * The region of the ip
     * 
     */
    @Import(name="region")
    private @Nullable Output<String> region;

    /**
     * @return The region of the ip
     * 
     */
    public Optional<Output<String>> region() {
        return Optional.ofNullable(this.region);
    }

    private ReservedIpState() {}

    private ReservedIpState(ReservedIpState $) {
        this.ip = $.ip;
        this.name = $.name;
        this.region = $.region;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ReservedIpState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ReservedIpState $;

        public Builder() {
            $ = new ReservedIpState();
        }

        public Builder(ReservedIpState defaults) {
            $ = new ReservedIpState(Objects.requireNonNull(defaults));
        }

        /**
         * @param ip The IP Address of the resource
         * 
         * @return builder
         * 
         */
        public Builder ip(@Nullable Output<String> ip) {
            $.ip = ip;
            return this;
        }

        /**
         * @param ip The IP Address of the resource
         * 
         * @return builder
         * 
         */
        public Builder ip(String ip) {
            return ip(Output.of(ip));
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

        /**
         * @param region The region of the ip
         * 
         * @return builder
         * 
         */
        public Builder region(@Nullable Output<String> region) {
            $.region = region;
            return this;
        }

        /**
         * @param region The region of the ip
         * 
         * @return builder
         * 
         */
        public Builder region(String region) {
            return region(Output.of(region));
        }

        public ReservedIpState build() {
            return $;
        }
    }

}

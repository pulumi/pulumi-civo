// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class VolumeArgs extends com.pulumi.resources.ResourceArgs {

    public static final VolumeArgs Empty = new VolumeArgs();

    /**
     * A name that you wish to use to refer to this volume
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return A name that you wish to use to refer to this volume
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * The network that the volume belongs to
     * 
     */
    @Import(name="networkId", required=true)
    private Output<String> networkId;

    /**
     * @return The network that the volume belongs to
     * 
     */
    public Output<String> networkId() {
        return this.networkId;
    }

    /**
     * The region for the volume, if not declare we use the region in declared in the provider.
     * 
     */
    @Import(name="region")
    private @Nullable Output<String> region;

    /**
     * @return The region for the volume, if not declare we use the region in declared in the provider.
     * 
     */
    public Optional<Output<String>> region() {
        return Optional.ofNullable(this.region);
    }

    /**
     * A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes
     * 
     */
    @Import(name="sizeGb", required=true)
    private Output<Integer> sizeGb;

    /**
     * @return A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes
     * 
     */
    public Output<Integer> sizeGb() {
        return this.sizeGb;
    }

    /**
     * The type of the volume
     * 
     */
    @Import(name="volumeType")
    private @Nullable Output<String> volumeType;

    /**
     * @return The type of the volume
     * 
     */
    public Optional<Output<String>> volumeType() {
        return Optional.ofNullable(this.volumeType);
    }

    private VolumeArgs() {}

    private VolumeArgs(VolumeArgs $) {
        this.name = $.name;
        this.networkId = $.networkId;
        this.region = $.region;
        this.sizeGb = $.sizeGb;
        this.volumeType = $.volumeType;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(VolumeArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private VolumeArgs $;

        public Builder() {
            $ = new VolumeArgs();
        }

        public Builder(VolumeArgs defaults) {
            $ = new VolumeArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param name A name that you wish to use to refer to this volume
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name A name that you wish to use to refer to this volume
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param networkId The network that the volume belongs to
         * 
         * @return builder
         * 
         */
        public Builder networkId(Output<String> networkId) {
            $.networkId = networkId;
            return this;
        }

        /**
         * @param networkId The network that the volume belongs to
         * 
         * @return builder
         * 
         */
        public Builder networkId(String networkId) {
            return networkId(Output.of(networkId));
        }

        /**
         * @param region The region for the volume, if not declare we use the region in declared in the provider.
         * 
         * @return builder
         * 
         */
        public Builder region(@Nullable Output<String> region) {
            $.region = region;
            return this;
        }

        /**
         * @param region The region for the volume, if not declare we use the region in declared in the provider.
         * 
         * @return builder
         * 
         */
        public Builder region(String region) {
            return region(Output.of(region));
        }

        /**
         * @param sizeGb A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes
         * 
         * @return builder
         * 
         */
        public Builder sizeGb(Output<Integer> sizeGb) {
            $.sizeGb = sizeGb;
            return this;
        }

        /**
         * @param sizeGb A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes
         * 
         * @return builder
         * 
         */
        public Builder sizeGb(Integer sizeGb) {
            return sizeGb(Output.of(sizeGb));
        }

        /**
         * @param volumeType The type of the volume
         * 
         * @return builder
         * 
         */
        public Builder volumeType(@Nullable Output<String> volumeType) {
            $.volumeType = volumeType;
            return this;
        }

        /**
         * @param volumeType The type of the volume
         * 
         * @return builder
         * 
         */
        public Builder volumeType(String volumeType) {
            return volumeType(Output.of(volumeType));
        }

        public VolumeArgs build() {
            if ($.networkId == null) {
                throw new MissingRequiredPropertyException("VolumeArgs", "networkId");
            }
            if ($.sizeGb == null) {
                throw new MissingRequiredPropertyException("VolumeArgs", "sizeGb");
            }
            return $;
        }
    }

}

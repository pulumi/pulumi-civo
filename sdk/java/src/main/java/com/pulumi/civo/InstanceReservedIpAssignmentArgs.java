// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class InstanceReservedIpAssignmentArgs extends com.pulumi.resources.ResourceArgs {

    public static final InstanceReservedIpAssignmentArgs Empty = new InstanceReservedIpAssignmentArgs();

    /**
     * The instance id
     * 
     */
    @Import(name="instanceId", required=true)
    private Output<String> instanceId;

    /**
     * @return The instance id
     * 
     */
    public Output<String> instanceId() {
        return this.instanceId;
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

    /**
     * The reserved ip id
     * 
     */
    @Import(name="reservedIpId", required=true)
    private Output<String> reservedIpId;

    /**
     * @return The reserved ip id
     * 
     */
    public Output<String> reservedIpId() {
        return this.reservedIpId;
    }

    private InstanceReservedIpAssignmentArgs() {}

    private InstanceReservedIpAssignmentArgs(InstanceReservedIpAssignmentArgs $) {
        this.instanceId = $.instanceId;
        this.region = $.region;
        this.reservedIpId = $.reservedIpId;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(InstanceReservedIpAssignmentArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private InstanceReservedIpAssignmentArgs $;

        public Builder() {
            $ = new InstanceReservedIpAssignmentArgs();
        }

        public Builder(InstanceReservedIpAssignmentArgs defaults) {
            $ = new InstanceReservedIpAssignmentArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param instanceId The instance id
         * 
         * @return builder
         * 
         */
        public Builder instanceId(Output<String> instanceId) {
            $.instanceId = instanceId;
            return this;
        }

        /**
         * @param instanceId The instance id
         * 
         * @return builder
         * 
         */
        public Builder instanceId(String instanceId) {
            return instanceId(Output.of(instanceId));
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

        /**
         * @param reservedIpId The reserved ip id
         * 
         * @return builder
         * 
         */
        public Builder reservedIpId(Output<String> reservedIpId) {
            $.reservedIpId = reservedIpId;
            return this;
        }

        /**
         * @param reservedIpId The reserved ip id
         * 
         * @return builder
         * 
         */
        public Builder reservedIpId(String reservedIpId) {
            return reservedIpId(Output.of(reservedIpId));
        }

        public InstanceReservedIpAssignmentArgs build() {
            if ($.instanceId == null) {
                throw new MissingRequiredPropertyException("InstanceReservedIpAssignmentArgs", "instanceId");
            }
            if ($.reservedIpId == null) {
                throw new MissingRequiredPropertyException("InstanceReservedIpAssignmentArgs", "reservedIpId");
            }
            return $;
        }
    }

}

// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class NetworkArgs extends com.pulumi.resources.ResourceArgs {

    public static final NetworkArgs Empty = new NetworkArgs();

    /**
     * The CIDR block for the network
     * 
     */
    @Import(name="cidrV4")
    private @Nullable Output<String> cidrV4;

    /**
     * @return The CIDR block for the network
     * 
     */
    public Optional<Output<String>> cidrV4() {
        return Optional.ofNullable(this.cidrV4);
    }

    /**
     * Name for the network
     * 
     */
    @Import(name="label", required=true)
    private Output<String> label;

    /**
     * @return Name for the network
     * 
     */
    public Output<String> label() {
        return this.label;
    }

    /**
     * List of nameservers for the network
     * 
     */
    @Import(name="nameserversV4s")
    private @Nullable Output<List<String>> nameserversV4s;

    /**
     * @return List of nameservers for the network
     * 
     */
    public Optional<Output<List<String>>> nameserversV4s() {
        return Optional.ofNullable(this.nameserversV4s);
    }

    /**
     * The region of the network
     * 
     */
    @Import(name="region")
    private @Nullable Output<String> region;

    /**
     * @return The region of the network
     * 
     */
    public Optional<Output<String>> region() {
        return Optional.ofNullable(this.region);
    }

    /**
     * End of the IPv4 allocation pool for VLAN
     * 
     */
    @Import(name="vlanAllocationPoolV4End")
    private @Nullable Output<String> vlanAllocationPoolV4End;

    /**
     * @return End of the IPv4 allocation pool for VLAN
     * 
     */
    public Optional<Output<String>> vlanAllocationPoolV4End() {
        return Optional.ofNullable(this.vlanAllocationPoolV4End);
    }

    /**
     * Start of the IPv4 allocation pool for VLAN
     * 
     */
    @Import(name="vlanAllocationPoolV4Start")
    private @Nullable Output<String> vlanAllocationPoolV4Start;

    /**
     * @return Start of the IPv4 allocation pool for VLAN
     * 
     */
    public Optional<Output<String>> vlanAllocationPoolV4Start() {
        return Optional.ofNullable(this.vlanAllocationPoolV4Start);
    }

    /**
     * CIDR for VLAN IPv4
     * 
     */
    @Import(name="vlanCidrV4")
    private @Nullable Output<String> vlanCidrV4;

    /**
     * @return CIDR for VLAN IPv4
     * 
     */
    public Optional<Output<String>> vlanCidrV4() {
        return Optional.ofNullable(this.vlanCidrV4);
    }

    /**
     * Gateway IP for VLAN IPv4
     * 
     */
    @Import(name="vlanGatewayIpV4")
    private @Nullable Output<String> vlanGatewayIpV4;

    /**
     * @return Gateway IP for VLAN IPv4
     * 
     */
    public Optional<Output<String>> vlanGatewayIpV4() {
        return Optional.ofNullable(this.vlanGatewayIpV4);
    }

    /**
     * VLAN ID for the network
     * 
     */
    @Import(name="vlanId")
    private @Nullable Output<Integer> vlanId;

    /**
     * @return VLAN ID for the network
     * 
     */
    public Optional<Output<Integer>> vlanId() {
        return Optional.ofNullable(this.vlanId);
    }

    /**
     * Physical interface for VLAN
     * 
     */
    @Import(name="vlanPhysicalInterface")
    private @Nullable Output<String> vlanPhysicalInterface;

    /**
     * @return Physical interface for VLAN
     * 
     */
    public Optional<Output<String>> vlanPhysicalInterface() {
        return Optional.ofNullable(this.vlanPhysicalInterface);
    }

    private NetworkArgs() {}

    private NetworkArgs(NetworkArgs $) {
        this.cidrV4 = $.cidrV4;
        this.label = $.label;
        this.nameserversV4s = $.nameserversV4s;
        this.region = $.region;
        this.vlanAllocationPoolV4End = $.vlanAllocationPoolV4End;
        this.vlanAllocationPoolV4Start = $.vlanAllocationPoolV4Start;
        this.vlanCidrV4 = $.vlanCidrV4;
        this.vlanGatewayIpV4 = $.vlanGatewayIpV4;
        this.vlanId = $.vlanId;
        this.vlanPhysicalInterface = $.vlanPhysicalInterface;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(NetworkArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private NetworkArgs $;

        public Builder() {
            $ = new NetworkArgs();
        }

        public Builder(NetworkArgs defaults) {
            $ = new NetworkArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param cidrV4 The CIDR block for the network
         * 
         * @return builder
         * 
         */
        public Builder cidrV4(@Nullable Output<String> cidrV4) {
            $.cidrV4 = cidrV4;
            return this;
        }

        /**
         * @param cidrV4 The CIDR block for the network
         * 
         * @return builder
         * 
         */
        public Builder cidrV4(String cidrV4) {
            return cidrV4(Output.of(cidrV4));
        }

        /**
         * @param label Name for the network
         * 
         * @return builder
         * 
         */
        public Builder label(Output<String> label) {
            $.label = label;
            return this;
        }

        /**
         * @param label Name for the network
         * 
         * @return builder
         * 
         */
        public Builder label(String label) {
            return label(Output.of(label));
        }

        /**
         * @param nameserversV4s List of nameservers for the network
         * 
         * @return builder
         * 
         */
        public Builder nameserversV4s(@Nullable Output<List<String>> nameserversV4s) {
            $.nameserversV4s = nameserversV4s;
            return this;
        }

        /**
         * @param nameserversV4s List of nameservers for the network
         * 
         * @return builder
         * 
         */
        public Builder nameserversV4s(List<String> nameserversV4s) {
            return nameserversV4s(Output.of(nameserversV4s));
        }

        /**
         * @param nameserversV4s List of nameservers for the network
         * 
         * @return builder
         * 
         */
        public Builder nameserversV4s(String... nameserversV4s) {
            return nameserversV4s(List.of(nameserversV4s));
        }

        /**
         * @param region The region of the network
         * 
         * @return builder
         * 
         */
        public Builder region(@Nullable Output<String> region) {
            $.region = region;
            return this;
        }

        /**
         * @param region The region of the network
         * 
         * @return builder
         * 
         */
        public Builder region(String region) {
            return region(Output.of(region));
        }

        /**
         * @param vlanAllocationPoolV4End End of the IPv4 allocation pool for VLAN
         * 
         * @return builder
         * 
         */
        public Builder vlanAllocationPoolV4End(@Nullable Output<String> vlanAllocationPoolV4End) {
            $.vlanAllocationPoolV4End = vlanAllocationPoolV4End;
            return this;
        }

        /**
         * @param vlanAllocationPoolV4End End of the IPv4 allocation pool for VLAN
         * 
         * @return builder
         * 
         */
        public Builder vlanAllocationPoolV4End(String vlanAllocationPoolV4End) {
            return vlanAllocationPoolV4End(Output.of(vlanAllocationPoolV4End));
        }

        /**
         * @param vlanAllocationPoolV4Start Start of the IPv4 allocation pool for VLAN
         * 
         * @return builder
         * 
         */
        public Builder vlanAllocationPoolV4Start(@Nullable Output<String> vlanAllocationPoolV4Start) {
            $.vlanAllocationPoolV4Start = vlanAllocationPoolV4Start;
            return this;
        }

        /**
         * @param vlanAllocationPoolV4Start Start of the IPv4 allocation pool for VLAN
         * 
         * @return builder
         * 
         */
        public Builder vlanAllocationPoolV4Start(String vlanAllocationPoolV4Start) {
            return vlanAllocationPoolV4Start(Output.of(vlanAllocationPoolV4Start));
        }

        /**
         * @param vlanCidrV4 CIDR for VLAN IPv4
         * 
         * @return builder
         * 
         */
        public Builder vlanCidrV4(@Nullable Output<String> vlanCidrV4) {
            $.vlanCidrV4 = vlanCidrV4;
            return this;
        }

        /**
         * @param vlanCidrV4 CIDR for VLAN IPv4
         * 
         * @return builder
         * 
         */
        public Builder vlanCidrV4(String vlanCidrV4) {
            return vlanCidrV4(Output.of(vlanCidrV4));
        }

        /**
         * @param vlanGatewayIpV4 Gateway IP for VLAN IPv4
         * 
         * @return builder
         * 
         */
        public Builder vlanGatewayIpV4(@Nullable Output<String> vlanGatewayIpV4) {
            $.vlanGatewayIpV4 = vlanGatewayIpV4;
            return this;
        }

        /**
         * @param vlanGatewayIpV4 Gateway IP for VLAN IPv4
         * 
         * @return builder
         * 
         */
        public Builder vlanGatewayIpV4(String vlanGatewayIpV4) {
            return vlanGatewayIpV4(Output.of(vlanGatewayIpV4));
        }

        /**
         * @param vlanId VLAN ID for the network
         * 
         * @return builder
         * 
         */
        public Builder vlanId(@Nullable Output<Integer> vlanId) {
            $.vlanId = vlanId;
            return this;
        }

        /**
         * @param vlanId VLAN ID for the network
         * 
         * @return builder
         * 
         */
        public Builder vlanId(Integer vlanId) {
            return vlanId(Output.of(vlanId));
        }

        /**
         * @param vlanPhysicalInterface Physical interface for VLAN
         * 
         * @return builder
         * 
         */
        public Builder vlanPhysicalInterface(@Nullable Output<String> vlanPhysicalInterface) {
            $.vlanPhysicalInterface = vlanPhysicalInterface;
            return this;
        }

        /**
         * @param vlanPhysicalInterface Physical interface for VLAN
         * 
         * @return builder
         * 
         */
        public Builder vlanPhysicalInterface(String vlanPhysicalInterface) {
            return vlanPhysicalInterface(Output.of(vlanPhysicalInterface));
        }

        public NetworkArgs build() {
            if ($.label == null) {
                throw new MissingRequiredPropertyException("NetworkArgs", "label");
            }
            return $;
        }
    }

}

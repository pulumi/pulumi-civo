// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class FirewallRuleState extends com.pulumi.resources.ResourceArgs {

    public static final FirewallRuleState Empty = new FirewallRuleState();

    /**
     * The action of the rule can be allow or deny. When we set the `action = &#39;allow&#39;`, this is going to add a rule to allow
     * traffic. Similarly, setting `action = &#39;deny&#39;` will deny the traffic.
     * 
     */
    @Import(name="action")
    private @Nullable Output<String> action;

    /**
     * @return The action of the rule can be allow or deny. When we set the `action = &#39;allow&#39;`, this is going to add a rule to allow
     * traffic. Similarly, setting `action = &#39;deny&#39;` will deny the traffic.
     * 
     */
    public Optional<Output<String>> action() {
        return Optional.ofNullable(this.action);
    }

    /**
     * The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32
     * to open just for a specific IP address)
     * 
     */
    @Import(name="cidrs")
    private @Nullable Output<List<String>> cidrs;

    /**
     * @return The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32
     * to open just for a specific IP address)
     * 
     */
    public Optional<Output<List<String>>> cidrs() {
        return Optional.ofNullable(this.cidrs);
    }

    /**
     * The direction of the rule can be ingress or egress
     * 
     */
    @Import(name="direction")
    private @Nullable Output<String> direction;

    /**
     * @return The direction of the rule can be ingress or egress
     * 
     */
    public Optional<Output<String>> direction() {
        return Optional.ofNullable(this.direction);
    }

    /**
     * The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
     * 
     */
    @Import(name="endPort")
    private @Nullable Output<String> endPort;

    /**
     * @return The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
     * 
     */
    public Optional<Output<String>> endPort() {
        return Optional.ofNullable(this.endPort);
    }

    /**
     * The Firewall ID
     * 
     */
    @Import(name="firewallId")
    private @Nullable Output<String> firewallId;

    /**
     * @return The Firewall ID
     * 
     */
    public Optional<Output<String>> firewallId() {
        return Optional.ofNullable(this.firewallId);
    }

    /**
     * A string that will be the displayed name/reference for this rule
     * 
     */
    @Import(name="label")
    private @Nullable Output<String> label;

    /**
     * @return A string that will be the displayed name/reference for this rule
     * 
     */
    public Optional<Output<String>> label() {
        return Optional.ofNullable(this.label);
    }

    /**
     * The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
     * 
     */
    @Import(name="protocol")
    private @Nullable Output<String> protocol;

    /**
     * @return The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
     * 
     */
    public Optional<Output<String>> protocol() {
        return Optional.ofNullable(this.protocol);
    }

    /**
     * The region for this rule
     * 
     */
    @Import(name="region")
    private @Nullable Output<String> region;

    /**
     * @return The region for this rule
     * 
     */
    public Optional<Output<String>> region() {
        return Optional.ofNullable(this.region);
    }

    /**
     * The start of the port range to configure for this rule (or the single port if required)
     * 
     */
    @Import(name="startPort")
    private @Nullable Output<String> startPort;

    /**
     * @return The start of the port range to configure for this rule (or the single port if required)
     * 
     */
    public Optional<Output<String>> startPort() {
        return Optional.ofNullable(this.startPort);
    }

    private FirewallRuleState() {}

    private FirewallRuleState(FirewallRuleState $) {
        this.action = $.action;
        this.cidrs = $.cidrs;
        this.direction = $.direction;
        this.endPort = $.endPort;
        this.firewallId = $.firewallId;
        this.label = $.label;
        this.protocol = $.protocol;
        this.region = $.region;
        this.startPort = $.startPort;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(FirewallRuleState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private FirewallRuleState $;

        public Builder() {
            $ = new FirewallRuleState();
        }

        public Builder(FirewallRuleState defaults) {
            $ = new FirewallRuleState(Objects.requireNonNull(defaults));
        }

        /**
         * @param action The action of the rule can be allow or deny. When we set the `action = &#39;allow&#39;`, this is going to add a rule to allow
         * traffic. Similarly, setting `action = &#39;deny&#39;` will deny the traffic.
         * 
         * @return builder
         * 
         */
        public Builder action(@Nullable Output<String> action) {
            $.action = action;
            return this;
        }

        /**
         * @param action The action of the rule can be allow or deny. When we set the `action = &#39;allow&#39;`, this is going to add a rule to allow
         * traffic. Similarly, setting `action = &#39;deny&#39;` will deny the traffic.
         * 
         * @return builder
         * 
         */
        public Builder action(String action) {
            return action(Output.of(action));
        }

        /**
         * @param cidrs The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32
         * to open just for a specific IP address)
         * 
         * @return builder
         * 
         */
        public Builder cidrs(@Nullable Output<List<String>> cidrs) {
            $.cidrs = cidrs;
            return this;
        }

        /**
         * @param cidrs The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32
         * to open just for a specific IP address)
         * 
         * @return builder
         * 
         */
        public Builder cidrs(List<String> cidrs) {
            return cidrs(Output.of(cidrs));
        }

        /**
         * @param cidrs The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32
         * to open just for a specific IP address)
         * 
         * @return builder
         * 
         */
        public Builder cidrs(String... cidrs) {
            return cidrs(List.of(cidrs));
        }

        /**
         * @param direction The direction of the rule can be ingress or egress
         * 
         * @return builder
         * 
         */
        public Builder direction(@Nullable Output<String> direction) {
            $.direction = direction;
            return this;
        }

        /**
         * @param direction The direction of the rule can be ingress or egress
         * 
         * @return builder
         * 
         */
        public Builder direction(String direction) {
            return direction(Output.of(direction));
        }

        /**
         * @param endPort The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
         * 
         * @return builder
         * 
         */
        public Builder endPort(@Nullable Output<String> endPort) {
            $.endPort = endPort;
            return this;
        }

        /**
         * @param endPort The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
         * 
         * @return builder
         * 
         */
        public Builder endPort(String endPort) {
            return endPort(Output.of(endPort));
        }

        /**
         * @param firewallId The Firewall ID
         * 
         * @return builder
         * 
         */
        public Builder firewallId(@Nullable Output<String> firewallId) {
            $.firewallId = firewallId;
            return this;
        }

        /**
         * @param firewallId The Firewall ID
         * 
         * @return builder
         * 
         */
        public Builder firewallId(String firewallId) {
            return firewallId(Output.of(firewallId));
        }

        /**
         * @param label A string that will be the displayed name/reference for this rule
         * 
         * @return builder
         * 
         */
        public Builder label(@Nullable Output<String> label) {
            $.label = label;
            return this;
        }

        /**
         * @param label A string that will be the displayed name/reference for this rule
         * 
         * @return builder
         * 
         */
        public Builder label(String label) {
            return label(Output.of(label));
        }

        /**
         * @param protocol The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
         * 
         * @return builder
         * 
         */
        public Builder protocol(@Nullable Output<String> protocol) {
            $.protocol = protocol;
            return this;
        }

        /**
         * @param protocol The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
         * 
         * @return builder
         * 
         */
        public Builder protocol(String protocol) {
            return protocol(Output.of(protocol));
        }

        /**
         * @param region The region for this rule
         * 
         * @return builder
         * 
         */
        public Builder region(@Nullable Output<String> region) {
            $.region = region;
            return this;
        }

        /**
         * @param region The region for this rule
         * 
         * @return builder
         * 
         */
        public Builder region(String region) {
            return region(Output.of(region));
        }

        /**
         * @param startPort The start of the port range to configure for this rule (or the single port if required)
         * 
         * @return builder
         * 
         */
        public Builder startPort(@Nullable Output<String> startPort) {
            $.startPort = startPort;
            return this;
        }

        /**
         * @param startPort The start of the port range to configure for this rule (or the single port if required)
         * 
         * @return builder
         * 
         */
        public Builder startPort(String startPort) {
            return startPort(Output.of(startPort));
        }

        public FirewallRuleState build() {
            return $;
        }
    }

}

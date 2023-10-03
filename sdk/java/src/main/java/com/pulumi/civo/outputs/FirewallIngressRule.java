// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class FirewallIngressRule {
    /**
     * @return The action of the rule can be allow or deny. When we set the `action = &#39;allow&#39;`, this is going to add a rule to allow traffic. Similarly, setting `action = &#39;deny&#39;` will deny the traffic.
     * 
     */
    private String action;
    /**
     * @return The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32 to open just for a specific IP address)
     * 
     */
    private List<String> cidrs;
    private @Nullable String id;
    /**
     * @return A string that will be the displayed name/reference for this rule
     * 
     */
    private @Nullable String label;
    /**
     * @return The port or port range to open, can be a single port or a range separated by a dash (`-`), e.g. `80` or `80-443`
     * 
     */
    private @Nullable String portRange;
    /**
     * @return The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
     * 
     */
    private @Nullable String protocol;

    private FirewallIngressRule() {}
    /**
     * @return The action of the rule can be allow or deny. When we set the `action = &#39;allow&#39;`, this is going to add a rule to allow traffic. Similarly, setting `action = &#39;deny&#39;` will deny the traffic.
     * 
     */
    public String action() {
        return this.action;
    }
    /**
     * @return The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32 to open just for a specific IP address)
     * 
     */
    public List<String> cidrs() {
        return this.cidrs;
    }
    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }
    /**
     * @return A string that will be the displayed name/reference for this rule
     * 
     */
    public Optional<String> label() {
        return Optional.ofNullable(this.label);
    }
    /**
     * @return The port or port range to open, can be a single port or a range separated by a dash (`-`), e.g. `80` or `80-443`
     * 
     */
    public Optional<String> portRange() {
        return Optional.ofNullable(this.portRange);
    }
    /**
     * @return The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
     * 
     */
    public Optional<String> protocol() {
        return Optional.ofNullable(this.protocol);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(FirewallIngressRule defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String action;
        private List<String> cidrs;
        private @Nullable String id;
        private @Nullable String label;
        private @Nullable String portRange;
        private @Nullable String protocol;
        public Builder() {}
        public Builder(FirewallIngressRule defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.action = defaults.action;
    	      this.cidrs = defaults.cidrs;
    	      this.id = defaults.id;
    	      this.label = defaults.label;
    	      this.portRange = defaults.portRange;
    	      this.protocol = defaults.protocol;
        }

        @CustomType.Setter
        public Builder action(String action) {
            this.action = Objects.requireNonNull(action);
            return this;
        }
        @CustomType.Setter
        public Builder cidrs(List<String> cidrs) {
            this.cidrs = Objects.requireNonNull(cidrs);
            return this;
        }
        public Builder cidrs(String... cidrs) {
            return cidrs(List.of(cidrs));
        }
        @CustomType.Setter
        public Builder id(@Nullable String id) {
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder label(@Nullable String label) {
            this.label = label;
            return this;
        }
        @CustomType.Setter
        public Builder portRange(@Nullable String portRange) {
            this.portRange = portRange;
            return this;
        }
        @CustomType.Setter
        public Builder protocol(@Nullable String protocol) {
            this.protocol = protocol;
            return this;
        }
        public FirewallIngressRule build() {
            final var o = new FirewallIngressRule();
            o.action = action;
            o.cidrs = cidrs;
            o.id = id;
            o.label = label;
            o.portRange = portRange;
            o.protocol = protocol;
            return o;
        }
    }
}

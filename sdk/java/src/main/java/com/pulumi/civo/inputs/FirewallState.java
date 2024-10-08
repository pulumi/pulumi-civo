// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.inputs;

import com.pulumi.civo.inputs.FirewallEgressRuleArgs;
import com.pulumi.civo.inputs.FirewallIngressRuleArgs;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class FirewallState extends com.pulumi.resources.ResourceArgs {

    public static final FirewallState Empty = new FirewallState();

    /**
     * The create rules flag is used to create the default firewall rules, if is not defined will be set to true, and if you
     * set to false you need to define at least one ingress or egress rule
     * 
     */
    @Import(name="createDefaultRules")
    private @Nullable Output<Boolean> createDefaultRules;

    /**
     * @return The create rules flag is used to create the default firewall rules, if is not defined will be set to true, and if you
     * set to false you need to define at least one ingress or egress rule
     * 
     */
    public Optional<Output<Boolean>> createDefaultRules() {
        return Optional.ofNullable(this.createDefaultRules);
    }

    /**
     * The egress rules, this is a list of rules that will be applied to the firewall
     * 
     */
    @Import(name="egressRules")
    private @Nullable Output<List<FirewallEgressRuleArgs>> egressRules;

    /**
     * @return The egress rules, this is a list of rules that will be applied to the firewall
     * 
     */
    public Optional<Output<List<FirewallEgressRuleArgs>>> egressRules() {
        return Optional.ofNullable(this.egressRules);
    }

    /**
     * The ingress rules, this is a list of rules that will be applied to the firewall
     * 
     */
    @Import(name="ingressRules")
    private @Nullable Output<List<FirewallIngressRuleArgs>> ingressRules;

    /**
     * @return The ingress rules, this is a list of rules that will be applied to the firewall
     * 
     */
    public Optional<Output<List<FirewallIngressRuleArgs>>> ingressRules() {
        return Optional.ofNullable(this.ingressRules);
    }

    /**
     * The firewall name
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return The firewall name
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * The firewall network, if is not defined we use the default network
     * 
     */
    @Import(name="networkId")
    private @Nullable Output<String> networkId;

    /**
     * @return The firewall network, if is not defined we use the default network
     * 
     */
    public Optional<Output<String>> networkId() {
        return Optional.ofNullable(this.networkId);
    }

    /**
     * The firewall region, if is not defined we use the global defined in the provider
     * 
     */
    @Import(name="region")
    private @Nullable Output<String> region;

    /**
     * @return The firewall region, if is not defined we use the global defined in the provider
     * 
     */
    public Optional<Output<String>> region() {
        return Optional.ofNullable(this.region);
    }

    private FirewallState() {}

    private FirewallState(FirewallState $) {
        this.createDefaultRules = $.createDefaultRules;
        this.egressRules = $.egressRules;
        this.ingressRules = $.ingressRules;
        this.name = $.name;
        this.networkId = $.networkId;
        this.region = $.region;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(FirewallState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private FirewallState $;

        public Builder() {
            $ = new FirewallState();
        }

        public Builder(FirewallState defaults) {
            $ = new FirewallState(Objects.requireNonNull(defaults));
        }

        /**
         * @param createDefaultRules The create rules flag is used to create the default firewall rules, if is not defined will be set to true, and if you
         * set to false you need to define at least one ingress or egress rule
         * 
         * @return builder
         * 
         */
        public Builder createDefaultRules(@Nullable Output<Boolean> createDefaultRules) {
            $.createDefaultRules = createDefaultRules;
            return this;
        }

        /**
         * @param createDefaultRules The create rules flag is used to create the default firewall rules, if is not defined will be set to true, and if you
         * set to false you need to define at least one ingress or egress rule
         * 
         * @return builder
         * 
         */
        public Builder createDefaultRules(Boolean createDefaultRules) {
            return createDefaultRules(Output.of(createDefaultRules));
        }

        /**
         * @param egressRules The egress rules, this is a list of rules that will be applied to the firewall
         * 
         * @return builder
         * 
         */
        public Builder egressRules(@Nullable Output<List<FirewallEgressRuleArgs>> egressRules) {
            $.egressRules = egressRules;
            return this;
        }

        /**
         * @param egressRules The egress rules, this is a list of rules that will be applied to the firewall
         * 
         * @return builder
         * 
         */
        public Builder egressRules(List<FirewallEgressRuleArgs> egressRules) {
            return egressRules(Output.of(egressRules));
        }

        /**
         * @param egressRules The egress rules, this is a list of rules that will be applied to the firewall
         * 
         * @return builder
         * 
         */
        public Builder egressRules(FirewallEgressRuleArgs... egressRules) {
            return egressRules(List.of(egressRules));
        }

        /**
         * @param ingressRules The ingress rules, this is a list of rules that will be applied to the firewall
         * 
         * @return builder
         * 
         */
        public Builder ingressRules(@Nullable Output<List<FirewallIngressRuleArgs>> ingressRules) {
            $.ingressRules = ingressRules;
            return this;
        }

        /**
         * @param ingressRules The ingress rules, this is a list of rules that will be applied to the firewall
         * 
         * @return builder
         * 
         */
        public Builder ingressRules(List<FirewallIngressRuleArgs> ingressRules) {
            return ingressRules(Output.of(ingressRules));
        }

        /**
         * @param ingressRules The ingress rules, this is a list of rules that will be applied to the firewall
         * 
         * @return builder
         * 
         */
        public Builder ingressRules(FirewallIngressRuleArgs... ingressRules) {
            return ingressRules(List.of(ingressRules));
        }

        /**
         * @param name The firewall name
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name The firewall name
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param networkId The firewall network, if is not defined we use the default network
         * 
         * @return builder
         * 
         */
        public Builder networkId(@Nullable Output<String> networkId) {
            $.networkId = networkId;
            return this;
        }

        /**
         * @param networkId The firewall network, if is not defined we use the default network
         * 
         * @return builder
         * 
         */
        public Builder networkId(String networkId) {
            return networkId(Output.of(networkId));
        }

        /**
         * @param region The firewall region, if is not defined we use the global defined in the provider
         * 
         * @return builder
         * 
         */
        public Builder region(@Nullable Output<String> region) {
            $.region = region;
            return this;
        }

        /**
         * @param region The firewall region, if is not defined we use the global defined in the provider
         * 
         * @return builder
         * 
         */
        public Builder region(String region) {
            return region(Output.of(region));
        }

        public FirewallState build() {
            return $;
        }
    }

}

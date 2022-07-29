// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo;

import com.pulumi.civo.FirewallRuleArgs;
import com.pulumi.civo.Utilities;
import com.pulumi.civo.inputs.FirewallRuleState;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import java.lang.String;
import java.util.List;
import javax.annotation.Nullable;

/**
 * Provides a Civo firewall rule resource. This can be used to create, modify, and delete firewalls rules. This resource don&#39;t have an update option because Civo backend doesn&#39;t support it at this moment. In that case, we use `ForceNew` for all object in the resource.
 * 
 * ## Import
 * 
 * # using firewall_id:firewall_rule_id
 * 
 * ```sh
 *  $ pulumi import civo:index/firewallRule:FirewallRule http b8ecd2ab-2267-4a5e-8692-cbf1d32583e3:4b0022ee-00b2-4f81-a40d-b4f8728923a7
 * ```
 * 
 */
@ResourceType(type="civo:index/firewallRule:FirewallRule")
public class FirewallRule extends com.pulumi.resources.CustomResource {
    /**
     * The action of the rule can be allow or deny. When we set the `action = &#39;allow&#39;`, this is going to add a rule to allow
     * traffic. Similarly, setting `action = &#39;deny&#39;` will deny the traffic.
     * 
     */
    @Export(name="action", type=String.class, parameters={})
    private Output<String> action;

    /**
     * @return The action of the rule can be allow or deny. When we set the `action = &#39;allow&#39;`, this is going to add a rule to allow
     * traffic. Similarly, setting `action = &#39;deny&#39;` will deny the traffic.
     * 
     */
    public Output<String> action() {
        return this.action;
    }
    /**
     * The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32
     * to open just for a specific IP address)
     * 
     */
    @Export(name="cidrs", type=List.class, parameters={String.class})
    private Output<List<String>> cidrs;

    /**
     * @return The CIDR notation of the other end to affect, or a valid network CIDR (e.g. 0.0.0.0/0 to open for everyone or 1.2.3.4/32
     * to open just for a specific IP address)
     * 
     */
    public Output<List<String>> cidrs() {
        return this.cidrs;
    }
    /**
     * The direction of the rule can be ingress or egress
     * 
     */
    @Export(name="direction", type=String.class, parameters={})
    private Output<String> direction;

    /**
     * @return The direction of the rule can be ingress or egress
     * 
     */
    public Output<String> direction() {
        return this.direction;
    }
    /**
     * The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
     * 
     */
    @Export(name="endPort", type=String.class, parameters={})
    private Output<String> endPort;

    /**
     * @return The end of the port range (this is optional, by default it will only apply to the single port listed in start_port)
     * 
     */
    public Output<String> endPort() {
        return this.endPort;
    }
    /**
     * The Firewall ID
     * 
     */
    @Export(name="firewallId", type=String.class, parameters={})
    private Output<String> firewallId;

    /**
     * @return The Firewall ID
     * 
     */
    public Output<String> firewallId() {
        return this.firewallId;
    }
    /**
     * A string that will be the displayed name/reference for this rule
     * 
     */
    @Export(name="label", type=String.class, parameters={})
    private Output<String> label;

    /**
     * @return A string that will be the displayed name/reference for this rule
     * 
     */
    public Output<String> label() {
        return this.label;
    }
    /**
     * The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
     * 
     */
    @Export(name="protocol", type=String.class, parameters={})
    private Output<String> protocol;

    /**
     * @return The protocol choice from `tcp`, `udp` or `icmp` (the default if unspecified is `tcp`)
     * 
     */
    public Output<String> protocol() {
        return this.protocol;
    }
    /**
     * The region for this rule
     * 
     */
    @Export(name="region", type=String.class, parameters={})
    private Output<String> region;

    /**
     * @return The region for this rule
     * 
     */
    public Output<String> region() {
        return this.region;
    }
    /**
     * The start of the port range to configure for this rule (or the single port if required)
     * 
     */
    @Export(name="startPort", type=String.class, parameters={})
    private Output<String> startPort;

    /**
     * @return The start of the port range to configure for this rule (or the single port if required)
     * 
     */
    public Output<String> startPort() {
        return this.startPort;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public FirewallRule(String name) {
        this(name, FirewallRuleArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public FirewallRule(String name, FirewallRuleArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public FirewallRule(String name, FirewallRuleArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("civo:index/firewallRule:FirewallRule", name, args == null ? FirewallRuleArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private FirewallRule(String name, Output<String> id, @Nullable FirewallRuleState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("civo:index/firewallRule:FirewallRule", name, state, makeResourceOptions(options, id));
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .build();
        return com.pulumi.resources.CustomResourceOptions.merge(defaultOptions, options, id);
    }

    /**
     * Get an existing Host resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state
     * @param options Optional settings to control the behavior of the CustomResource.
     */
    public static FirewallRule get(String name, Output<String> id, @Nullable FirewallRuleState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new FirewallRule(name, id, state, options);
    }
}

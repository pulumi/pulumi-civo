// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo;

import com.pulumi.civo.FirewallArgs;
import com.pulumi.civo.Utilities;
import com.pulumi.civo.inputs.FirewallState;
import com.pulumi.civo.outputs.FirewallEgressRule;
import com.pulumi.civo.outputs.FirewallIngressRule;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import java.lang.Boolean;
import java.lang.String;
import java.util.List;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * Provides a Civo firewall resource. This can be used to create, modify, and delete firewalls.
 * 
 * ## Example Usage
 * 
 * * View firewalls after creation on the [CLI](https://www.civo.com/docs/overview/civo-cli):
 * * View firewalls after creation on the [Dashboard](https://dashboard.civo.com/firewalls)
 * * View firewall rules on [CLI](https://www.civo.com/docs/overview/civo-cli):
 * 
 * ### Custom ingress and egress rules firewall
 * 
 * &lt;!--Start PulumiCodeChooser --&gt;
 * <pre>
 * {@code
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.civo.Network;
 * import com.pulumi.civo.NetworkArgs;
 * import com.pulumi.civo.Firewall;
 * import com.pulumi.civo.FirewallArgs;
 * import com.pulumi.civo.inputs.FirewallIngressRuleArgs;
 * import com.pulumi.civo.inputs.FirewallEgressRuleArgs;
 * import com.pulumi.civo.CivoFunctions;
 * import com.pulumi.civo.inputs.GetDiskImageArgs;
 * import com.pulumi.civo.Instance;
 * import com.pulumi.civo.InstanceArgs;
 * import java.util.List;
 * import java.util.ArrayList;
 * import java.util.Map;
 * import java.io.File;
 * import java.nio.file.Files;
 * import java.nio.file.Paths;
 * 
 * public class App {
 *     public static void main(String[] args) {
 *         Pulumi.run(App::stack);
 *     }
 * 
 *     public static void stack(Context ctx) {
 *         var example = new Network("example", NetworkArgs.builder()
 *             .label("example-network")
 *             .build());
 * 
 *         var exampleFirewall = new Firewall("exampleFirewall", FirewallArgs.builder()
 *             .name("example-firewall")
 *             .networkId(example.id())
 *             .createDefaultRules(false)
 *             .ingressRules(            
 *                 FirewallIngressRuleArgs.builder()
 *                     .label("http")
 *                     .protocol("tcp")
 *                     .portRange("80")
 *                     .cidrs("0.0.0.0")
 *                     .action("allow")
 *                     .build(),
 *                 FirewallIngressRuleArgs.builder()
 *                     .label("https")
 *                     .protocol("tcp")
 *                     .portRange("443")
 *                     .cidrs("0.0.0.0")
 *                     .action("allow")
 *                     .build(),
 *                 FirewallIngressRuleArgs.builder()
 *                     .label("ssh")
 *                     .protocol("tcp")
 *                     .portRange("22")
 *                     .cidrs(                    
 *                         "192.168.1.1/32",
 *                         "192.168.10.4/32",
 *                         "192.168.10.10/32")
 *                     .action("allow")
 *                     .build())
 *             .egressRules(FirewallEgressRuleArgs.builder()
 *                 .label("all")
 *                 .protocol("tcp")
 *                 .portRange("1-65535")
 *                 .cidrs("0.0.0.0/0")
 *                 .action("allow")
 *                 .build())
 *             .build());
 * 
 *         final var debian = CivoFunctions.getDiskImage(GetDiskImageArgs.builder()
 *             .filters(GetDiskImageFilterArgs.builder()
 *                 .key("name")
 *                 .values("debian-10")
 *                 .build())
 *             .build());
 * 
 *         // Create a new instance
 *         var exampleInstance = new Instance("exampleInstance", InstanceArgs.builder()
 *             .hostname("example")
 *             .notes("This is an example instance")
 *             .firewallId(exampleFirewall.id())
 *             .networkId(example.id())
 *             .size("g3.xsmall")
 *             .diskImage(debian.applyValue(getDiskImageResult -> getDiskImageResult.diskimages()[0].id()))
 *             .build());
 * 
 *     }
 * }
 * }
 * </pre>
 * &lt;!--End PulumiCodeChooser --&gt;
 * 
 * ### Simple firewall
 * 
 * This the minimum amount of code to create a firewall with default rules:
 * 
 * &lt;!--Start PulumiCodeChooser --&gt;
 * <pre>
 * {@code
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.civo.Firewall;
 * import com.pulumi.civo.FirewallArgs;
 * import java.util.List;
 * import java.util.ArrayList;
 * import java.util.Map;
 * import java.io.File;
 * import java.nio.file.Files;
 * import java.nio.file.Paths;
 * 
 * public class App {
 *     public static void main(String[] args) {
 *         Pulumi.run(App::stack);
 *     }
 * 
 *     public static void stack(Context ctx) {
 *         // ...
 *         var example = new Firewall("example", FirewallArgs.builder()
 *             .name("example-firewall")
 *             .networkId(exampleCivoNetwork.id())
 *             .build());
 * 
 *     }
 * }
 * }
 * </pre>
 * &lt;!--End PulumiCodeChooser --&gt;
 * 
 * ## Import
 * 
 * using ID
 * 
 * ```sh
 * $ pulumi import civo:index/firewall:Firewall www b8ecd2ab-2267-4a5e-8692-cbf1d32583e3
 * ```
 * 
 */
@ResourceType(type="civo:index/firewall:Firewall")
public class Firewall extends com.pulumi.resources.CustomResource {
    /**
     * The create rules flag is used to create the default firewall rules, if is not defined will be set to true, and if you
     * set to false you need to define at least one ingress or egress rule
     * 
     */
    @Export(name="createDefaultRules", refs={Boolean.class}, tree="[0]")
    private Output</* @Nullable */ Boolean> createDefaultRules;

    /**
     * @return The create rules flag is used to create the default firewall rules, if is not defined will be set to true, and if you
     * set to false you need to define at least one ingress or egress rule
     * 
     */
    public Output<Optional<Boolean>> createDefaultRules() {
        return Codegen.optional(this.createDefaultRules);
    }
    /**
     * The egress rules, this is a list of rules that will be applied to the firewall
     * 
     */
    @Export(name="egressRules", refs={List.class,FirewallEgressRule.class}, tree="[0,1]")
    private Output<List<FirewallEgressRule>> egressRules;

    /**
     * @return The egress rules, this is a list of rules that will be applied to the firewall
     * 
     */
    public Output<List<FirewallEgressRule>> egressRules() {
        return this.egressRules;
    }
    /**
     * The ingress rules, this is a list of rules that will be applied to the firewall
     * 
     */
    @Export(name="ingressRules", refs={List.class,FirewallIngressRule.class}, tree="[0,1]")
    private Output<List<FirewallIngressRule>> ingressRules;

    /**
     * @return The ingress rules, this is a list of rules that will be applied to the firewall
     * 
     */
    public Output<List<FirewallIngressRule>> ingressRules() {
        return this.ingressRules;
    }
    /**
     * The firewall name
     * 
     */
    @Export(name="name", refs={String.class}, tree="[0]")
    private Output<String> name;

    /**
     * @return The firewall name
     * 
     */
    public Output<String> name() {
        return this.name;
    }
    /**
     * The firewall network, if is not defined we use the default network
     * 
     */
    @Export(name="networkId", refs={String.class}, tree="[0]")
    private Output<String> networkId;

    /**
     * @return The firewall network, if is not defined we use the default network
     * 
     */
    public Output<String> networkId() {
        return this.networkId;
    }
    /**
     * The firewall region, if is not defined we use the global defined in the provider
     * 
     */
    @Export(name="region", refs={String.class}, tree="[0]")
    private Output<String> region;

    /**
     * @return The firewall region, if is not defined we use the global defined in the provider
     * 
     */
    public Output<String> region() {
        return this.region;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public Firewall(java.lang.String name) {
        this(name, FirewallArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public Firewall(java.lang.String name, @Nullable FirewallArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public Firewall(java.lang.String name, @Nullable FirewallArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("civo:index/firewall:Firewall", name, makeArgs(args, options), makeResourceOptions(options, Codegen.empty()), false);
    }

    private Firewall(java.lang.String name, Output<java.lang.String> id, @Nullable FirewallState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("civo:index/firewall:Firewall", name, state, makeResourceOptions(options, id), false);
    }

    private static FirewallArgs makeArgs(@Nullable FirewallArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        if (options != null && options.getUrn().isPresent()) {
            return null;
        }
        return args == null ? FirewallArgs.Empty : args;
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<java.lang.String> id) {
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
    public static Firewall get(java.lang.String name, Output<java.lang.String> id, @Nullable FirewallState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new Firewall(name, id, state, options);
    }
}

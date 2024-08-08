// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo;

import com.pulumi.civo.InstanceArgs;
import com.pulumi.civo.Utilities;
import com.pulumi.civo.inputs.InstanceState;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * Provides a Civo instance resource. This can be used to create, modify, and delete instances.
 * 
 * ## Example Usage
 * 
 * * View instances after creation on the [CLI](https://www.civo.com/docs/overview/civo-cli):
 * * View instances after creation on the [Dashboard](https://dashboard.civo.com/instances)
 * * View node sizes on [CLI](https://www.civo.com/docs/overview/civo-cli):
 * 
 * ### Simple and smallest instance with its own network
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
 *         var exampleNetwork = new Network("exampleNetwork", NetworkArgs.builder()
 *             .label("example-network")
 *             .build());
 * 
 *         var example = new Firewall("example", FirewallArgs.builder()
 *             .name("example-firewall")
 *             .createDefaultRules(true)
 *             .networkId(exampleNetwork.id())
 *             .build());
 * 
 *         // Query instance disk image
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
 *             .tags(            
 *                 "example",
 *                 "documentation")
 *             .notes("This is an example instance")
 *             .firewallId(example.id())
 *             .networkId(exampleNetwork.id())
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
 * With this configuration, an initial password for the instance gets written to the state on output `initial_password` which you can use to access the instance.
 * 
 * Alternative you can get the password with the [CLI](https://www.civo.com/docs/overview/civo-cli):
 * 
 * ### Instance with ssh login
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
 * import com.pulumi.civo.CivoFunctions;
 * import com.pulumi.civo.inputs.GetDiskImageArgs;
 * import com.pulumi.civo.SshKey;
 * import com.pulumi.civo.SshKeyArgs;
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
 *         var exampleNetwork = new Network("exampleNetwork", NetworkArgs.builder()
 *             .label("example-network")
 *             .build());
 * 
 *         var example = new Firewall("example", FirewallArgs.builder()
 *             .name("example-firewall")
 *             .createDefaultRules(true)
 *             .networkId(exampleNetwork.id())
 *             .build());
 * 
 *         // Query instance disk image
 *         final var debian = CivoFunctions.getDiskImage(GetDiskImageArgs.builder()
 *             .filters(GetDiskImageFilterArgs.builder()
 *                 .key("name")
 *                 .values("debian-10")
 *                 .build())
 *             .build());
 * 
 *         // To create the example key, run this command:
 *         // ssh-keygen -f ~/.ssh/example-tf -C "terraform-example{@literal @}localmachine"
 *         var exampleSshKey = new SshKey("exampleSshKey", SshKeyArgs.builder()
 *             .name("example")
 *             .publicKey(StdFunctions.file(FileArgs.builder()
 *                 .input("~/.ssh/example-tf.pub")
 *                 .build()).result())
 *             .build());
 * 
 *         // Create a new instance
 *         var exampleInstance = new Instance("exampleInstance", InstanceArgs.builder()
 *             .hostname("example")
 *             .tags(            
 *                 "example",
 *                 "documentation")
 *             .notes("This is an example instance")
 *             .sshkeyId(exampleSshKey.id())
 *             .firewallId(example.id())
 *             .networkId(exampleNetwork.id())
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
 * ## Import
 * 
 * using ID
 * 
 * ```sh
 * $ pulumi import civo:index/instance:Instance example 18bd98ad-1b6e-4f87-b48f-e690b4fd7413
 * ```
 * 
 */
@ResourceType(type="civo:index/instance:Instance")
public class Instance extends com.pulumi.resources.CustomResource {
    /**
     * (Number) Instance&#39;s CPU cores
     * 
     */
    @Export(name="cpuCores", refs={Integer.class}, tree="[0]")
    private Output<Integer> cpuCores;

    /**
     * @return (Number) Instance&#39;s CPU cores
     * 
     */
    public Output<Integer> cpuCores() {
        return this.cpuCores;
    }
    /**
     * (String) Timestamp when the instance was created
     * 
     */
    @Export(name="createdAt", refs={String.class}, tree="[0]")
    private Output<String> createdAt;

    /**
     * @return (String) Timestamp when the instance was created
     * 
     */
    public Output<String> createdAt() {
        return this.createdAt;
    }
    /**
     * (Number) Instance&#39;s disk (GB)
     * 
     */
    @Export(name="diskGb", refs={Integer.class}, tree="[0]")
    private Output<Integer> diskGb;

    /**
     * @return (Number) Instance&#39;s disk (GB)
     * 
     */
    public Output<Integer> diskGb() {
        return this.diskGb;
    }
    /**
     * The ID for the disk image to use to build the instance
     * 
     */
    @Export(name="diskImage", refs={String.class}, tree="[0]")
    private Output<String> diskImage;

    /**
     * @return The ID for the disk image to use to build the instance
     * 
     */
    public Output<String> diskImage() {
        return this.diskImage;
    }
    /**
     * The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open
     * to all)
     * 
     */
    @Export(name="firewallId", refs={String.class}, tree="[0]")
    private Output<String> firewallId;

    /**
     * @return The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open
     * to all)
     * 
     */
    public Output<String> firewallId() {
        return this.firewallId;
    }
    /**
     * A fully qualified domain name that should be set as the instance&#39;s hostname
     * 
     */
    @Export(name="hostname", refs={String.class}, tree="[0]")
    private Output<String> hostname;

    /**
     * @return A fully qualified domain name that should be set as the instance&#39;s hostname
     * 
     */
    public Output<String> hostname() {
        return this.hostname;
    }
    /**
     * (String, Sensitive) Initial password for login
     * 
     */
    @Export(name="initialPassword", refs={String.class}, tree="[0]")
    private Output<String> initialPassword;

    /**
     * @return (String, Sensitive) Initial password for login
     * 
     */
    public Output<String> initialPassword() {
        return this.initialPassword;
    }
    /**
     * The name of the initial user created on the server (optional; this will default to the template&#39;s default_username and
     * fallback to civo)
     * 
     */
    @Export(name="initialUser", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> initialUser;

    /**
     * @return The name of the initial user created on the server (optional; this will default to the template&#39;s default_username and
     * fallback to civo)
     * 
     */
    public Output<Optional<String>> initialUser() {
        return Codegen.optional(this.initialUser);
    }
    /**
     * This must be the ID of the network from the network listing (optional; default network used when not specified)
     * 
     */
    @Export(name="networkId", refs={String.class}, tree="[0]")
    private Output<String> networkId;

    /**
     * @return This must be the ID of the network from the network listing (optional; default network used when not specified)
     * 
     */
    public Output<String> networkId() {
        return this.networkId;
    }
    /**
     * Add some notes to the instance
     * 
     */
    @Export(name="notes", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> notes;

    /**
     * @return Add some notes to the instance
     * 
     */
    public Output<Optional<String>> notes() {
        return Codegen.optional(this.notes);
    }
    /**
     * (String) Instance&#39;s private IP address
     * 
     */
    @Export(name="privateIp", refs={String.class}, tree="[0]")
    private Output<String> privateIp;

    /**
     * @return (String) Instance&#39;s private IP address
     * 
     */
    public Output<String> privateIp() {
        return this.privateIp;
    }
    /**
     * The private IPv4 address for the instance (optional)
     * 
     */
    @Export(name="privateIpv4", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> privateIpv4;

    /**
     * @return The private IPv4 address for the instance (optional)
     * 
     */
    public Output<Optional<String>> privateIpv4() {
        return Codegen.optional(this.privateIpv4);
    }
    /**
     * (String) Instance&#39;s public IP address
     * 
     */
    @Export(name="publicIp", refs={String.class}, tree="[0]")
    private Output<String> publicIp;

    /**
     * @return (String) Instance&#39;s public IP address
     * 
     */
    public Output<String> publicIp() {
        return this.publicIp;
    }
    /**
     * This should be either &#39;none&#39; or &#39;create&#39; (default: &#39;create&#39;)
     * 
     */
    @Export(name="publicIpRequired", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> publicIpRequired;

    /**
     * @return This should be either &#39;none&#39; or &#39;create&#39; (default: &#39;create&#39;)
     * 
     */
    public Output<Optional<String>> publicIpRequired() {
        return Codegen.optional(this.publicIpRequired);
    }
    /**
     * (Number) Instance&#39;s RAM (MB)
     * 
     */
    @Export(name="ramMb", refs={Integer.class}, tree="[0]")
    private Output<Integer> ramMb;

    /**
     * @return (Number) Instance&#39;s RAM (MB)
     * 
     */
    public Output<Integer> ramMb() {
        return this.ramMb;
    }
    /**
     * The region for the instance, if not declare we use the region in declared in the provider
     * 
     */
    @Export(name="region", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> region;

    /**
     * @return The region for the instance, if not declare we use the region in declared in the provider
     * 
     */
    public Output<Optional<String>> region() {
        return Codegen.optional(this.region);
    }
    /**
     * Can be either the UUID, name, or the IP address of the reserved IP
     * 
     */
    @Export(name="reservedIpv4", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> reservedIpv4;

    /**
     * @return Can be either the UUID, name, or the IP address of the reserved IP
     * 
     */
    public Output<Optional<String>> reservedIpv4() {
        return Codegen.optional(this.reservedIpv4);
    }
    /**
     * A fully qualified domain name that should be used as the instance&#39;s IP&#39;s reverse DNS (optional, uses the hostname if
     * unspecified)
     * 
     */
    @Export(name="reverseDns", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> reverseDns;

    /**
     * @return A fully qualified domain name that should be used as the instance&#39;s IP&#39;s reverse DNS (optional, uses the hostname if
     * unspecified)
     * 
     */
    public Output<Optional<String>> reverseDns() {
        return Codegen.optional(this.reverseDns);
    }
    /**
     * The contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance,
     * read/write/executable only by root and then will be executed at the end of the cloud initialization
     * 
     */
    @Export(name="script", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> script;

    /**
     * @return The contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance,
     * read/write/executable only by root and then will be executed at the end of the cloud initialization
     * 
     */
    public Output<Optional<String>> script() {
        return Codegen.optional(this.script);
    }
    /**
     * The name of the size, from the current list, e.g. g3.xsmall
     * 
     */
    @Export(name="size", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> size;

    /**
     * @return The name of the size, from the current list, e.g. g3.xsmall
     * 
     */
    public Output<Optional<String>> size() {
        return Codegen.optional(this.size);
    }
    /**
     * (String) Instance&#39;s source ID
     * 
     */
    @Export(name="sourceId", refs={String.class}, tree="[0]")
    private Output<String> sourceId;

    /**
     * @return (String) Instance&#39;s source ID
     * 
     */
    public Output<String> sourceId() {
        return this.sourceId;
    }
    /**
     * (String) Instance&#39;s source type
     * 
     */
    @Export(name="sourceType", refs={String.class}, tree="[0]")
    private Output<String> sourceType;

    /**
     * @return (String) Instance&#39;s source type
     * 
     */
    public Output<String> sourceType() {
        return this.sourceType;
    }
    /**
     * The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn&#39;t provided a
     * random password will be set and returned in the initial_password field)
     * 
     */
    @Export(name="sshkeyId", refs={String.class}, tree="[0]")
    private Output<String> sshkeyId;

    /**
     * @return The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn&#39;t provided a
     * random password will be set and returned in the initial_password field)
     * 
     */
    public Output<String> sshkeyId() {
        return this.sshkeyId;
    }
    /**
     * (String) Instance&#39;s status
     * 
     */
    @Export(name="status", refs={String.class}, tree="[0]")
    private Output<String> status;

    /**
     * @return (String) Instance&#39;s status
     * 
     */
    public Output<String> status() {
        return this.status;
    }
    /**
     * An optional list of tags, represented as a key, value pair
     * 
     */
    @Export(name="tags", refs={List.class,String.class}, tree="[0,1]")
    private Output</* @Nullable */ List<String>> tags;

    /**
     * @return An optional list of tags, represented as a key, value pair
     * 
     */
    public Output<Optional<List<String>>> tags() {
        return Codegen.optional(this.tags);
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public Instance(String name) {
        this(name, InstanceArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public Instance(String name, InstanceArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public Instance(String name, InstanceArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("civo:index/instance:Instance", name, makeArgs(args, options), makeResourceOptions(options, Codegen.empty()));
    }

    private Instance(String name, Output<String> id, @Nullable InstanceState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("civo:index/instance:Instance", name, state, makeResourceOptions(options, id));
    }

    private static InstanceArgs makeArgs(InstanceArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        if (options != null && options.getUrn().isPresent()) {
            return null;
        }
        return args == null ? InstanceArgs.Empty : args;
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .additionalSecretOutputs(List.of(
                "initialPassword"
            ))
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
    public static Instance get(String name, Output<String> id, @Nullable InstanceState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new Instance(name, id, state, options);
    }
}

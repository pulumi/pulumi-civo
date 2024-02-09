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
 * ## Import
 * 
 * using ID
 * 
 * ```sh
 * $ pulumi import civo:index/instance:Instance myintance 18bd98ad-1b6e-4f87-b48f-e690b4fd7413
 * ```
 * 
 */
@ResourceType(type="civo:index/instance:Instance")
public class Instance extends com.pulumi.resources.CustomResource {
    /**
     * Instance&#39;s CPU cores
     * 
     */
    @Export(name="cpuCores", refs={Integer.class}, tree="[0]")
    private Output<Integer> cpuCores;

    /**
     * @return Instance&#39;s CPU cores
     * 
     */
    public Output<Integer> cpuCores() {
        return this.cpuCores;
    }
    /**
     * Timestamp when the instance was created
     * 
     */
    @Export(name="createdAt", refs={String.class}, tree="[0]")
    private Output<String> createdAt;

    /**
     * @return Timestamp when the instance was created
     * 
     */
    public Output<String> createdAt() {
        return this.createdAt;
    }
    /**
     * Instance&#39;s disk (GB)
     * 
     */
    @Export(name="diskGb", refs={Integer.class}, tree="[0]")
    private Output<Integer> diskGb;

    /**
     * @return Instance&#39;s disk (GB)
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
     * The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all)
     * 
     */
    @Export(name="firewallId", refs={String.class}, tree="[0]")
    private Output<String> firewallId;

    /**
     * @return The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all)
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
     * Initial password for login
     * 
     */
    @Export(name="initialPassword", refs={String.class}, tree="[0]")
    private Output<String> initialPassword;

    /**
     * @return Initial password for login
     * 
     */
    public Output<String> initialPassword() {
        return this.initialPassword;
    }
    /**
     * The name of the initial user created on the server (optional; this will default to the template&#39;s default_username and fallback to civo)
     * 
     */
    @Export(name="initialUser", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> initialUser;

    /**
     * @return The name of the initial user created on the server (optional; this will default to the template&#39;s default_username and fallback to civo)
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
     * Instance&#39;s private IP address
     * 
     */
    @Export(name="privateIp", refs={String.class}, tree="[0]")
    private Output<String> privateIp;

    /**
     * @return Instance&#39;s private IP address
     * 
     */
    public Output<String> privateIp() {
        return this.privateIp;
    }
    /**
     * Instance&#39;s public IP address
     * 
     */
    @Export(name="publicIp", refs={String.class}, tree="[0]")
    private Output<String> publicIp;

    /**
     * @return Instance&#39;s public IP address
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
     * Instance&#39;s RAM (MB)
     * 
     */
    @Export(name="ramMb", refs={Integer.class}, tree="[0]")
    private Output<Integer> ramMb;

    /**
     * @return Instance&#39;s RAM (MB)
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
     * A fully qualified domain name that should be used as the instance&#39;s IP&#39;s reverse DNS (optional, uses the hostname if unspecified)
     * 
     */
    @Export(name="reverseDns", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> reverseDns;

    /**
     * @return A fully qualified domain name that should be used as the instance&#39;s IP&#39;s reverse DNS (optional, uses the hostname if unspecified)
     * 
     */
    public Output<Optional<String>> reverseDns() {
        return Codegen.optional(this.reverseDns);
    }
    /**
     * The contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance, read/write/executable only by root and then will be executed at the end of the cloud initialization
     * 
     */
    @Export(name="script", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> script;

    /**
     * @return The contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance, read/write/executable only by root and then will be executed at the end of the cloud initialization
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
     * Instance&#39;s source ID
     * 
     */
    @Export(name="sourceId", refs={String.class}, tree="[0]")
    private Output<String> sourceId;

    /**
     * @return Instance&#39;s source ID
     * 
     */
    public Output<String> sourceId() {
        return this.sourceId;
    }
    /**
     * Instance&#39;s source type
     * 
     */
    @Export(name="sourceType", refs={String.class}, tree="[0]")
    private Output<String> sourceType;

    /**
     * @return Instance&#39;s source type
     * 
     */
    public Output<String> sourceType() {
        return this.sourceType;
    }
    /**
     * The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn&#39;t provided a random password will be set and returned in the initial_password field)
     * 
     */
    @Export(name="sshkeyId", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> sshkeyId;

    /**
     * @return The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn&#39;t provided a random password will be set and returned in the initial_password field)
     * 
     */
    public Output<Optional<String>> sshkeyId() {
        return Codegen.optional(this.sshkeyId);
    }
    /**
     * Instance&#39;s status
     * 
     */
    @Export(name="status", refs={String.class}, tree="[0]")
    private Output<String> status;

    /**
     * @return Instance&#39;s status
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
     * The ID for the template to use to build the instance
     * 
     * @deprecated
     * &#34;template&#34; attribute is deprecated. Moving forward, please use &#34;disk_image&#34; attribute.
     * 
     */
    @Deprecated /* ""template"" attribute is deprecated. Moving forward, please use ""disk_image"" attribute. */
    @Export(name="template", refs={String.class}, tree="[0]")
    private Output<String> template;

    /**
     * @return The ID for the template to use to build the instance
     * 
     */
    public Output<String> template() {
        return this.template;
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
    public Instance(String name, @Nullable InstanceArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public Instance(String name, @Nullable InstanceArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("civo:index/instance:Instance", name, args == null ? InstanceArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private Instance(String name, Output<String> id, @Nullable InstanceState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("civo:index/instance:Instance", name, state, makeResourceOptions(options, id));
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

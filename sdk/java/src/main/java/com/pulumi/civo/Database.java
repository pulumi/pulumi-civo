// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo;

import com.pulumi.civo.DatabaseArgs;
import com.pulumi.civo.Utilities;
import com.pulumi.civo.inputs.DatabaseState;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import java.lang.Integer;
import java.lang.String;
import javax.annotation.Nullable;

/**
 * ## Example Usage
 * 
 * ## Import
 * 
 * using ID
 * 
 * ```sh
 * $ pulumi import civo:index/database:Database mydb 29fcd1c4-fb61-44c7-b49c-dc7b98e9927e
 * ```
 * 
 */
@ResourceType(type="civo:index/database:Database")
public class Database extends com.pulumi.resources.CustomResource {
    /**
     * The DNS endpoint of the database
     * 
     */
    @Export(name="dnsEndpoint", refs={String.class}, tree="[0]")
    private Output<String> dnsEndpoint;

    /**
     * @return The DNS endpoint of the database
     * 
     */
    public Output<String> dnsEndpoint() {
        return this.dnsEndpoint;
    }
    /**
     * The endpoint of the database
     * 
     */
    @Export(name="endpoint", refs={String.class}, tree="[0]")
    private Output<String> endpoint;

    /**
     * @return The endpoint of the database
     * 
     */
    public Output<String> endpoint() {
        return this.endpoint;
    }
    /**
     * The engine of the database
     * 
     */
    @Export(name="engine", refs={String.class}, tree="[0]")
    private Output<String> engine;

    /**
     * @return The engine of the database
     * 
     */
    public Output<String> engine() {
        return this.engine;
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
     * Name of the database
     * 
     */
    @Export(name="name", refs={String.class}, tree="[0]")
    private Output<String> name;

    /**
     * @return Name of the database
     * 
     */
    public Output<String> name() {
        return this.name;
    }
    /**
     * The id of the associated network
     * 
     */
    @Export(name="networkId", refs={String.class}, tree="[0]")
    private Output<String> networkId;

    /**
     * @return The id of the associated network
     * 
     */
    public Output<String> networkId() {
        return this.networkId;
    }
    /**
     * Count of nodes
     * 
     */
    @Export(name="nodes", refs={Integer.class}, tree="[0]")
    private Output<Integer> nodes;

    /**
     * @return Count of nodes
     * 
     */
    public Output<Integer> nodes() {
        return this.nodes;
    }
    /**
     * The password of the database
     * 
     */
    @Export(name="password", refs={String.class}, tree="[0]")
    private Output<String> password;

    /**
     * @return The password of the database
     * 
     */
    public Output<String> password() {
        return this.password;
    }
    /**
     * The port of the database
     * 
     */
    @Export(name="port", refs={Integer.class}, tree="[0]")
    private Output<Integer> port;

    /**
     * @return The port of the database
     * 
     */
    public Output<Integer> port() {
        return this.port;
    }
    /**
     * The region where the database will be created.
     * 
     */
    @Export(name="region", refs={String.class}, tree="[0]")
    private Output<String> region;

    /**
     * @return The region where the database will be created.
     * 
     */
    public Output<String> region() {
        return this.region;
    }
    /**
     * Size of the database
     * 
     */
    @Export(name="size", refs={String.class}, tree="[0]")
    private Output<String> size;

    /**
     * @return Size of the database
     * 
     */
    public Output<String> size() {
        return this.size;
    }
    /**
     * The status of the database
     * 
     */
    @Export(name="status", refs={String.class}, tree="[0]")
    private Output<String> status;

    /**
     * @return The status of the database
     * 
     */
    public Output<String> status() {
        return this.status;
    }
    /**
     * The username of the database
     * 
     */
    @Export(name="username", refs={String.class}, tree="[0]")
    private Output<String> username;

    /**
     * @return The username of the database
     * 
     */
    public Output<String> username() {
        return this.username;
    }
    /**
     * The version of the database
     * 
     */
    @Export(name="version", refs={String.class}, tree="[0]")
    private Output<String> version;

    /**
     * @return The version of the database
     * 
     */
    public Output<String> version() {
        return this.version;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public Database(String name) {
        this(name, DatabaseArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public Database(String name, DatabaseArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public Database(String name, DatabaseArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("civo:index/database:Database", name, makeArgs(args, options), makeResourceOptions(options, Codegen.empty()));
    }

    private Database(String name, Output<String> id, @Nullable DatabaseState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("civo:index/database:Database", name, state, makeResourceOptions(options, id));
    }

    private static DatabaseArgs makeArgs(DatabaseArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        if (options != null && options.getUrn().isPresent()) {
            return null;
        }
        return args == null ? DatabaseArgs.Empty : args;
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
    public static Database get(String name, Output<String> id, @Nullable DatabaseState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new Database(name, id, state, options);
    }
}

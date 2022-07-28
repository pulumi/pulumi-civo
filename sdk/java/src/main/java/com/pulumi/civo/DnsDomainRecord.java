// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo;

import com.pulumi.civo.DnsDomainRecordArgs;
import com.pulumi.civo.Utilities;
import com.pulumi.civo.inputs.DnsDomainRecordState;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import java.lang.Integer;
import java.lang.String;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * Provides a Civo DNS domain record resource.
 * 
 * ## Import
 * 
 * # using domain_id:domain_record_id
 * 
 * ```sh
 *  $ pulumi import civo:index/dnsDomainRecord:DnsDomainRecord www a3cd6832-9577-4017-afd7-17d239fc0bf0:c9a39d14-ee1b-4870-8fb0-a2d4f465e822
 * ```
 * 
 */
@ResourceType(type="civo:index/dnsDomainRecord:DnsDomainRecord")
public class DnsDomainRecord extends com.pulumi.resources.CustomResource {
    /**
     * The account ID of this resource
     * 
     */
    @Export(name="accountId", type=String.class, parameters={})
    private Output<String> accountId;

    /**
     * @return The account ID of this resource
     * 
     */
    public Output<String> accountId() {
        return this.accountId;
    }
    /**
     * Timestamp when this resource was created
     * 
     */
    @Export(name="createdAt", type=String.class, parameters={})
    private Output<String> createdAt;

    /**
     * @return Timestamp when this resource was created
     * 
     */
    public Output<String> createdAt() {
        return this.createdAt;
    }
    /**
     * ID from domain name
     * 
     */
    @Export(name="domainId", type=String.class, parameters={})
    private Output<String> domainId;

    /**
     * @return ID from domain name
     * 
     */
    public Output<String> domainId() {
        return this.domainId;
    }
    /**
     * The portion before the domain name (e.g. www) or an @ for the apex/root domain (you cannot use an A record with an
     * amex/root domain)
     * 
     */
    @Export(name="name", type=String.class, parameters={})
    private Output<String> name;

    /**
     * @return The portion before the domain name (e.g. www) or an @ for the apex/root domain (you cannot use an A record with an
     * amex/root domain)
     * 
     */
    public Output<String> name() {
        return this.name;
    }
    /**
     * Useful for MX records only, the priority mail should be attempted it (defaults to 10)
     * 
     */
    @Export(name="priority", type=Integer.class, parameters={})
    private Output</* @Nullable */ Integer> priority;

    /**
     * @return Useful for MX records only, the priority mail should be attempted it (defaults to 10)
     * 
     */
    public Output<Optional<Integer>> priority() {
        return Codegen.optional(this.priority);
    }
    /**
     * How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified
     * is 600)
     * 
     */
    @Export(name="ttl", type=Integer.class, parameters={})
    private Output<Integer> ttl;

    /**
     * @return How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified
     * is 600)
     * 
     */
    public Output<Integer> ttl() {
        return this.ttl;
    }
    /**
     * The choice of RR type from a, cname, mx or txt
     * 
     */
    @Export(name="type", type=String.class, parameters={})
    private Output<String> type;

    /**
     * @return The choice of RR type from a, cname, mx or txt
     * 
     */
    public Output<String> type() {
        return this.type;
    }
    /**
     * Timestamp when this resource was updated
     * 
     */
    @Export(name="updatedAt", type=String.class, parameters={})
    private Output<String> updatedAt;

    /**
     * @return Timestamp when this resource was updated
     * 
     */
    public Output<String> updatedAt() {
        return this.updatedAt;
    }
    /**
     * The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record
     * 
     */
    @Export(name="value", type=String.class, parameters={})
    private Output<String> value;

    /**
     * @return The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record
     * 
     */
    public Output<String> value() {
        return this.value;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public DnsDomainRecord(String name) {
        this(name, DnsDomainRecordArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public DnsDomainRecord(String name, DnsDomainRecordArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public DnsDomainRecord(String name, DnsDomainRecordArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("civo:index/dnsDomainRecord:DnsDomainRecord", name, args == null ? DnsDomainRecordArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private DnsDomainRecord(String name, Output<String> id, @Nullable DnsDomainRecordState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("civo:index/dnsDomainRecord:DnsDomainRecord", name, state, makeResourceOptions(options, id));
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
    public static DnsDomainRecord get(String name, Output<String> id, @Nullable DnsDomainRecordState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new DnsDomainRecord(name, id, state, options);
    }
}

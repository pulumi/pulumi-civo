// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class DnsDomainRecordArgs extends com.pulumi.resources.ResourceArgs {

    public static final DnsDomainRecordArgs Empty = new DnsDomainRecordArgs();

    /**
     * ID from domain name
     * 
     */
    @Import(name="domainId", required=true)
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
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return The portion before the domain name (e.g. www) or an @ for the apex/root domain (you cannot use an A record with an
     * amex/root domain)
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * Useful for MX records only, the priority mail should be attempted it (defaults to 10)
     * 
     */
    @Import(name="priority")
    private @Nullable Output<Integer> priority;

    /**
     * @return Useful for MX records only, the priority mail should be attempted it (defaults to 10)
     * 
     */
    public Optional<Output<Integer>> priority() {
        return Optional.ofNullable(this.priority);
    }

    /**
     * How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified
     * is 600)
     * 
     */
    @Import(name="ttl", required=true)
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
    @Import(name="type", required=true)
    private Output<String> type;

    /**
     * @return The choice of RR type from a, cname, mx or txt
     * 
     */
    public Output<String> type() {
        return this.type;
    }

    /**
     * The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record
     * 
     */
    @Import(name="value", required=true)
    private Output<String> value;

    /**
     * @return The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record
     * 
     */
    public Output<String> value() {
        return this.value;
    }

    private DnsDomainRecordArgs() {}

    private DnsDomainRecordArgs(DnsDomainRecordArgs $) {
        this.domainId = $.domainId;
        this.name = $.name;
        this.priority = $.priority;
        this.ttl = $.ttl;
        this.type = $.type;
        this.value = $.value;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(DnsDomainRecordArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private DnsDomainRecordArgs $;

        public Builder() {
            $ = new DnsDomainRecordArgs();
        }

        public Builder(DnsDomainRecordArgs defaults) {
            $ = new DnsDomainRecordArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param domainId ID from domain name
         * 
         * @return builder
         * 
         */
        public Builder domainId(Output<String> domainId) {
            $.domainId = domainId;
            return this;
        }

        /**
         * @param domainId ID from domain name
         * 
         * @return builder
         * 
         */
        public Builder domainId(String domainId) {
            return domainId(Output.of(domainId));
        }

        /**
         * @param name The portion before the domain name (e.g. www) or an @ for the apex/root domain (you cannot use an A record with an
         * amex/root domain)
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name The portion before the domain name (e.g. www) or an @ for the apex/root domain (you cannot use an A record with an
         * amex/root domain)
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param priority Useful for MX records only, the priority mail should be attempted it (defaults to 10)
         * 
         * @return builder
         * 
         */
        public Builder priority(@Nullable Output<Integer> priority) {
            $.priority = priority;
            return this;
        }

        /**
         * @param priority Useful for MX records only, the priority mail should be attempted it (defaults to 10)
         * 
         * @return builder
         * 
         */
        public Builder priority(Integer priority) {
            return priority(Output.of(priority));
        }

        /**
         * @param ttl How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified
         * is 600)
         * 
         * @return builder
         * 
         */
        public Builder ttl(Output<Integer> ttl) {
            $.ttl = ttl;
            return this;
        }

        /**
         * @param ttl How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified
         * is 600)
         * 
         * @return builder
         * 
         */
        public Builder ttl(Integer ttl) {
            return ttl(Output.of(ttl));
        }

        /**
         * @param type The choice of RR type from a, cname, mx or txt
         * 
         * @return builder
         * 
         */
        public Builder type(Output<String> type) {
            $.type = type;
            return this;
        }

        /**
         * @param type The choice of RR type from a, cname, mx or txt
         * 
         * @return builder
         * 
         */
        public Builder type(String type) {
            return type(Output.of(type));
        }

        /**
         * @param value The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record
         * 
         * @return builder
         * 
         */
        public Builder value(Output<String> value) {
            $.value = value;
            return this;
        }

        /**
         * @param value The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record
         * 
         * @return builder
         * 
         */
        public Builder value(String value) {
            return value(Output.of(value));
        }

        public DnsDomainRecordArgs build() {
            $.domainId = Objects.requireNonNull($.domainId, "expected parameter 'domainId' to be non-null");
            $.ttl = Objects.requireNonNull($.ttl, "expected parameter 'ttl' to be non-null");
            $.type = Objects.requireNonNull($.type, "expected parameter 'type' to be non-null");
            $.value = Objects.requireNonNull($.value, "expected parameter 'value' to be non-null");
            return $;
        }
    }

}

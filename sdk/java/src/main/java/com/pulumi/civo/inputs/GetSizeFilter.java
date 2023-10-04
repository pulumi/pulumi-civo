// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.inputs;

import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetSizeFilter extends com.pulumi.resources.InvokeArgs {

    public static final GetSizeFilter Empty = new GetSizeFilter();

    /**
     * Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
     * 
     */
    @Import(name="all")
    private @Nullable Boolean all;

    /**
     * @return Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
     * 
     */
    public Optional<Boolean> all() {
        return Optional.ofNullable(this.all);
    }

    /**
     * Filter sizes by this key. This may be one of `cpu`, `description`, `disk`, `gpu_type`, `gpu`, `name`, `ram`, `selectable`, `type`.
     * 
     */
    @Import(name="key", required=true)
    private String key;

    /**
     * @return Filter sizes by this key. This may be one of `cpu`, `description`, `disk`, `gpu_type`, `gpu`, `name`, `ram`, `selectable`, `type`.
     * 
     */
    public String key() {
        return this.key;
    }

    /**
     * One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
     * 
     */
    @Import(name="matchBy")
    private @Nullable String matchBy;

    /**
     * @return One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
     * 
     */
    public Optional<String> matchBy() {
        return Optional.ofNullable(this.matchBy);
    }

    /**
     * Only retrieves `sizes` which keys has value that matches one of the values provided here
     * 
     */
    @Import(name="values", required=true)
    private List<String> values;

    /**
     * @return Only retrieves `sizes` which keys has value that matches one of the values provided here
     * 
     */
    public List<String> values() {
        return this.values;
    }

    private GetSizeFilter() {}

    private GetSizeFilter(GetSizeFilter $) {
        this.all = $.all;
        this.key = $.key;
        this.matchBy = $.matchBy;
        this.values = $.values;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetSizeFilter defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetSizeFilter $;

        public Builder() {
            $ = new GetSizeFilter();
        }

        public Builder(GetSizeFilter defaults) {
            $ = new GetSizeFilter(Objects.requireNonNull(defaults));
        }

        /**
         * @param all Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
         * 
         * @return builder
         * 
         */
        public Builder all(@Nullable Boolean all) {
            $.all = all;
            return this;
        }

        /**
         * @param key Filter sizes by this key. This may be one of `cpu`, `description`, `disk`, `gpu_type`, `gpu`, `name`, `ram`, `selectable`, `type`.
         * 
         * @return builder
         * 
         */
        public Builder key(String key) {
            $.key = key;
            return this;
        }

        /**
         * @param matchBy One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
         * 
         * @return builder
         * 
         */
        public Builder matchBy(@Nullable String matchBy) {
            $.matchBy = matchBy;
            return this;
        }

        /**
         * @param values Only retrieves `sizes` which keys has value that matches one of the values provided here
         * 
         * @return builder
         * 
         */
        public Builder values(List<String> values) {
            $.values = values;
            return this;
        }

        /**
         * @param values Only retrieves `sizes` which keys has value that matches one of the values provided here
         * 
         * @return builder
         * 
         */
        public Builder values(String... values) {
            return values(List.of(values));
        }

        public GetSizeFilter build() {
            $.key = Objects.requireNonNull($.key, "expected parameter 'key' to be non-null");
            $.values = Objects.requireNonNull($.values, "expected parameter 'values' to be non-null");
            return $;
        }
    }

}

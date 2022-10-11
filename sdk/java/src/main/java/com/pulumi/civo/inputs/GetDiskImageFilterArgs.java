// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetDiskImageFilterArgs extends com.pulumi.resources.ResourceArgs {

    public static final GetDiskImageFilterArgs Empty = new GetDiskImageFilterArgs();

    /**
     * Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
     * 
     */
    @Import(name="all")
    private @Nullable Output<Boolean> all;

    /**
     * @return Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
     * 
     */
    public Optional<Output<Boolean>> all() {
        return Optional.ofNullable(this.all);
    }

    /**
     * Filter diskimages by this key. This may be one of `id`, `label`, `name`, `version`.
     * 
     */
    @Import(name="key", required=true)
    private Output<String> key;

    /**
     * @return Filter diskimages by this key. This may be one of `id`, `label`, `name`, `version`.
     * 
     */
    public Output<String> key() {
        return this.key;
    }

    /**
     * One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
     * 
     */
    @Import(name="matchBy")
    private @Nullable Output<String> matchBy;

    /**
     * @return One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
     * 
     */
    public Optional<Output<String>> matchBy() {
        return Optional.ofNullable(this.matchBy);
    }

    /**
     * Only retrieves `diskimages` which keys has value that matches one of the values provided here
     * 
     */
    @Import(name="values", required=true)
    private Output<List<String>> values;

    /**
     * @return Only retrieves `diskimages` which keys has value that matches one of the values provided here
     * 
     */
    public Output<List<String>> values() {
        return this.values;
    }

    private GetDiskImageFilterArgs() {}

    private GetDiskImageFilterArgs(GetDiskImageFilterArgs $) {
        this.all = $.all;
        this.key = $.key;
        this.matchBy = $.matchBy;
        this.values = $.values;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetDiskImageFilterArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetDiskImageFilterArgs $;

        public Builder() {
            $ = new GetDiskImageFilterArgs();
        }

        public Builder(GetDiskImageFilterArgs defaults) {
            $ = new GetDiskImageFilterArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param all Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
         * 
         * @return builder
         * 
         */
        public Builder all(@Nullable Output<Boolean> all) {
            $.all = all;
            return this;
        }

        /**
         * @param all Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
         * 
         * @return builder
         * 
         */
        public Builder all(Boolean all) {
            return all(Output.of(all));
        }

        /**
         * @param key Filter diskimages by this key. This may be one of `id`, `label`, `name`, `version`.
         * 
         * @return builder
         * 
         */
        public Builder key(Output<String> key) {
            $.key = key;
            return this;
        }

        /**
         * @param key Filter diskimages by this key. This may be one of `id`, `label`, `name`, `version`.
         * 
         * @return builder
         * 
         */
        public Builder key(String key) {
            return key(Output.of(key));
        }

        /**
         * @param matchBy One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
         * 
         * @return builder
         * 
         */
        public Builder matchBy(@Nullable Output<String> matchBy) {
            $.matchBy = matchBy;
            return this;
        }

        /**
         * @param matchBy One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
         * 
         * @return builder
         * 
         */
        public Builder matchBy(String matchBy) {
            return matchBy(Output.of(matchBy));
        }

        /**
         * @param values Only retrieves `diskimages` which keys has value that matches one of the values provided here
         * 
         * @return builder
         * 
         */
        public Builder values(Output<List<String>> values) {
            $.values = values;
            return this;
        }

        /**
         * @param values Only retrieves `diskimages` which keys has value that matches one of the values provided here
         * 
         * @return builder
         * 
         */
        public Builder values(List<String> values) {
            return values(Output.of(values));
        }

        /**
         * @param values Only retrieves `diskimages` which keys has value that matches one of the values provided here
         * 
         * @return builder
         * 
         */
        public Builder values(String... values) {
            return values(List.of(values));
        }

        public GetDiskImageFilterArgs build() {
            $.key = Objects.requireNonNull($.key, "expected parameter 'key' to be non-null");
            $.values = Objects.requireNonNull($.values, "expected parameter 'values' to be non-null");
            return $;
        }
    }

}
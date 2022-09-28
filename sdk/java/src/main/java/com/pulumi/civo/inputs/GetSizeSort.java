// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.inputs;

import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetSizeSort extends com.pulumi.resources.InvokeArgs {

    public static final GetSizeSort Empty = new GetSizeSort();

    /**
     * The sort direction. This may be either `asc` or `desc`.
     * 
     */
    @Import(name="direction")
    private @Nullable String direction;

    /**
     * @return The sort direction. This may be either `asc` or `desc`.
     * 
     */
    public Optional<String> direction() {
        return Optional.ofNullable(this.direction);
    }

    /**
     * Sort sizes by this key. This may be one of `cpu`, `description`, `disk`, `name`, `ram`, `selectable`, `type`.
     * 
     */
    @Import(name="key", required=true)
    private String key;

    /**
     * @return Sort sizes by this key. This may be one of `cpu`, `description`, `disk`, `name`, `ram`, `selectable`, `type`.
     * 
     */
    public String key() {
        return this.key;
    }

    private GetSizeSort() {}

    private GetSizeSort(GetSizeSort $) {
        this.direction = $.direction;
        this.key = $.key;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetSizeSort defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetSizeSort $;

        public Builder() {
            $ = new GetSizeSort();
        }

        public Builder(GetSizeSort defaults) {
            $ = new GetSizeSort(Objects.requireNonNull(defaults));
        }

        /**
         * @param direction The sort direction. This may be either `asc` or `desc`.
         * 
         * @return builder
         * 
         */
        public Builder direction(@Nullable String direction) {
            $.direction = direction;
            return this;
        }

        /**
         * @param key Sort sizes by this key. This may be one of `cpu`, `description`, `disk`, `name`, `ram`, `selectable`, `type`.
         * 
         * @return builder
         * 
         */
        public Builder key(String key) {
            $.key = key;
            return this;
        }

        public GetSizeSort build() {
            $.key = Objects.requireNonNull($.key, "expected parameter 'key' to be non-null");
            return $;
        }
    }

}

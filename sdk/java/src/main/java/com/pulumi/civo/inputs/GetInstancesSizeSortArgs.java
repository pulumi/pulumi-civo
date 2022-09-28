// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetInstancesSizeSortArgs extends com.pulumi.resources.ResourceArgs {

    public static final GetInstancesSizeSortArgs Empty = new GetInstancesSizeSortArgs();

    /**
     * The sort direction. This may be either `asc` or `desc`.
     * 
     */
    @Import(name="direction")
    private @Nullable Output<String> direction;

    /**
     * @return The sort direction. This may be either `asc` or `desc`.
     * 
     */
    public Optional<Output<String>> direction() {
        return Optional.ofNullable(this.direction);
    }

    /**
     * Sort sizes by this key. This may be one of `cpu`, `description`, `disk`, `name`, `ram`, `selectable`, `type`.
     * 
     */
    @Import(name="key", required=true)
    private Output<String> key;

    /**
     * @return Sort sizes by this key. This may be one of `cpu`, `description`, `disk`, `name`, `ram`, `selectable`, `type`.
     * 
     */
    public Output<String> key() {
        return this.key;
    }

    private GetInstancesSizeSortArgs() {}

    private GetInstancesSizeSortArgs(GetInstancesSizeSortArgs $) {
        this.direction = $.direction;
        this.key = $.key;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetInstancesSizeSortArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetInstancesSizeSortArgs $;

        public Builder() {
            $ = new GetInstancesSizeSortArgs();
        }

        public Builder(GetInstancesSizeSortArgs defaults) {
            $ = new GetInstancesSizeSortArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param direction The sort direction. This may be either `asc` or `desc`.
         * 
         * @return builder
         * 
         */
        public Builder direction(@Nullable Output<String> direction) {
            $.direction = direction;
            return this;
        }

        /**
         * @param direction The sort direction. This may be either `asc` or `desc`.
         * 
         * @return builder
         * 
         */
        public Builder direction(String direction) {
            return direction(Output.of(direction));
        }

        /**
         * @param key Sort sizes by this key. This may be one of `cpu`, `description`, `disk`, `name`, `ram`, `selectable`, `type`.
         * 
         * @return builder
         * 
         */
        public Builder key(Output<String> key) {
            $.key = key;
            return this;
        }

        /**
         * @param key Sort sizes by this key. This may be one of `cpu`, `description`, `disk`, `name`, `ram`, `selectable`, `type`.
         * 
         * @return builder
         * 
         */
        public Builder key(String key) {
            return key(Output.of(key));
        }

        public GetInstancesSizeSortArgs build() {
            $.key = Objects.requireNonNull($.key, "expected parameter 'key' to be non-null");
            return $;
        }
    }

}

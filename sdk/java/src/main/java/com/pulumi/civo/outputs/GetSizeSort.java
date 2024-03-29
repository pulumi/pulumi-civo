// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetSizeSort {
    /**
     * @return The sort direction. This may be either `asc` or `desc`.
     * 
     */
    private @Nullable String direction;
    /**
     * @return Sort sizes by this key. This may be one of `cpu`, `description`, `disk`, `gpu_type`, `gpu`, `name`, `ram`, `selectable`, `type`.
     * 
     */
    private String key;

    private GetSizeSort() {}
    /**
     * @return The sort direction. This may be either `asc` or `desc`.
     * 
     */
    public Optional<String> direction() {
        return Optional.ofNullable(this.direction);
    }
    /**
     * @return Sort sizes by this key. This may be one of `cpu`, `description`, `disk`, `gpu_type`, `gpu`, `name`, `ram`, `selectable`, `type`.
     * 
     */
    public String key() {
        return this.key;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetSizeSort defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable String direction;
        private String key;
        public Builder() {}
        public Builder(GetSizeSort defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.direction = defaults.direction;
    	      this.key = defaults.key;
        }

        @CustomType.Setter
        public Builder direction(@Nullable String direction) {

            this.direction = direction;
            return this;
        }
        @CustomType.Setter
        public Builder key(String key) {
            if (key == null) {
              throw new MissingRequiredPropertyException("GetSizeSort", "key");
            }
            this.key = key;
            return this;
        }
        public GetSizeSort build() {
            final var _resultValue = new GetSizeSort();
            _resultValue.direction = direction;
            _resultValue.key = key;
            return _resultValue;
        }
    }
}

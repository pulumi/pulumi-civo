// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetSizeSort {
    private @Nullable String direction;
    private String key;

    private GetSizeSort() {}
    public Optional<String> direction() {
        return Optional.ofNullable(this.direction);
    }
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
            this.key = Objects.requireNonNull(key);
            return this;
        }
        public GetSizeSort build() {
            final var o = new GetSizeSort();
            o.direction = direction;
            o.key = key;
            return o;
        }
    }
}

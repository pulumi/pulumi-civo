// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.Boolean;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetKubernetesVersionFilter {
    private final @Nullable Boolean all;
    private final String key;
    private final @Nullable String matchBy;
    private final List<String> values;

    @CustomType.Constructor
    private GetKubernetesVersionFilter(
        @CustomType.Parameter("all") @Nullable Boolean all,
        @CustomType.Parameter("key") String key,
        @CustomType.Parameter("matchBy") @Nullable String matchBy,
        @CustomType.Parameter("values") List<String> values) {
        this.all = all;
        this.key = key;
        this.matchBy = matchBy;
        this.values = values;
    }

    public Optional<Boolean> all() {
        return Optional.ofNullable(this.all);
    }
    public String key() {
        return this.key;
    }
    public Optional<String> matchBy() {
        return Optional.ofNullable(this.matchBy);
    }
    public List<String> values() {
        return this.values;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetKubernetesVersionFilter defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private @Nullable Boolean all;
        private String key;
        private @Nullable String matchBy;
        private List<String> values;

        public Builder() {
    	      // Empty
        }

        public Builder(GetKubernetesVersionFilter defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.all = defaults.all;
    	      this.key = defaults.key;
    	      this.matchBy = defaults.matchBy;
    	      this.values = defaults.values;
        }

        public Builder all(@Nullable Boolean all) {
            this.all = all;
            return this;
        }
        public Builder key(String key) {
            this.key = Objects.requireNonNull(key);
            return this;
        }
        public Builder matchBy(@Nullable String matchBy) {
            this.matchBy = matchBy;
            return this;
        }
        public Builder values(List<String> values) {
            this.values = Objects.requireNonNull(values);
            return this;
        }
        public Builder values(String... values) {
            return values(List.of(values));
        }        public GetKubernetesVersionFilter build() {
            return new GetKubernetesVersionFilter(all, key, matchBy, values);
        }
    }
}

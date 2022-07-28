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


public final class GetKubernetesVersionFilter extends com.pulumi.resources.InvokeArgs {

    public static final GetKubernetesVersionFilter Empty = new GetKubernetesVersionFilter();

    @Import(name="all")
    private @Nullable Boolean all;

    public Optional<Boolean> all() {
        return Optional.ofNullable(this.all);
    }

    @Import(name="key", required=true)
    private String key;

    public String key() {
        return this.key;
    }

    @Import(name="matchBy")
    private @Nullable String matchBy;

    public Optional<String> matchBy() {
        return Optional.ofNullable(this.matchBy);
    }

    @Import(name="values", required=true)
    private List<String> values;

    public List<String> values() {
        return this.values;
    }

    private GetKubernetesVersionFilter() {}

    private GetKubernetesVersionFilter(GetKubernetesVersionFilter $) {
        this.all = $.all;
        this.key = $.key;
        this.matchBy = $.matchBy;
        this.values = $.values;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetKubernetesVersionFilter defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetKubernetesVersionFilter $;

        public Builder() {
            $ = new GetKubernetesVersionFilter();
        }

        public Builder(GetKubernetesVersionFilter defaults) {
            $ = new GetKubernetesVersionFilter(Objects.requireNonNull(defaults));
        }

        public Builder all(@Nullable Boolean all) {
            $.all = all;
            return this;
        }

        public Builder key(String key) {
            $.key = key;
            return this;
        }

        public Builder matchBy(@Nullable String matchBy) {
            $.matchBy = matchBy;
            return this;
        }

        public Builder values(List<String> values) {
            $.values = values;
            return this;
        }

        public Builder values(String... values) {
            return values(List.of(values));
        }

        public GetKubernetesVersionFilter build() {
            $.key = Objects.requireNonNull($.key, "expected parameter 'key' to be non-null");
            $.values = Objects.requireNonNull($.values, "expected parameter 'values' to be non-null");
            return $;
        }
    }

}

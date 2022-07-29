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


public final class GetRegionFilterArgs extends com.pulumi.resources.ResourceArgs {

    public static final GetRegionFilterArgs Empty = new GetRegionFilterArgs();

    @Import(name="all")
    private @Nullable Output<Boolean> all;

    public Optional<Output<Boolean>> all() {
        return Optional.ofNullable(this.all);
    }

    @Import(name="key", required=true)
    private Output<String> key;

    public Output<String> key() {
        return this.key;
    }

    @Import(name="matchBy")
    private @Nullable Output<String> matchBy;

    public Optional<Output<String>> matchBy() {
        return Optional.ofNullable(this.matchBy);
    }

    @Import(name="values", required=true)
    private Output<List<String>> values;

    public Output<List<String>> values() {
        return this.values;
    }

    private GetRegionFilterArgs() {}

    private GetRegionFilterArgs(GetRegionFilterArgs $) {
        this.all = $.all;
        this.key = $.key;
        this.matchBy = $.matchBy;
        this.values = $.values;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetRegionFilterArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetRegionFilterArgs $;

        public Builder() {
            $ = new GetRegionFilterArgs();
        }

        public Builder(GetRegionFilterArgs defaults) {
            $ = new GetRegionFilterArgs(Objects.requireNonNull(defaults));
        }

        public Builder all(@Nullable Output<Boolean> all) {
            $.all = all;
            return this;
        }

        public Builder all(Boolean all) {
            return all(Output.of(all));
        }

        public Builder key(Output<String> key) {
            $.key = key;
            return this;
        }

        public Builder key(String key) {
            return key(Output.of(key));
        }

        public Builder matchBy(@Nullable Output<String> matchBy) {
            $.matchBy = matchBy;
            return this;
        }

        public Builder matchBy(String matchBy) {
            return matchBy(Output.of(matchBy));
        }

        public Builder values(Output<List<String>> values) {
            $.values = values;
            return this;
        }

        public Builder values(List<String> values) {
            return values(Output.of(values));
        }

        public Builder values(String... values) {
            return values(List.of(values));
        }

        public GetRegionFilterArgs build() {
            $.key = Objects.requireNonNull($.key, "expected parameter 'key' to be non-null");
            $.values = Objects.requireNonNull($.values, "expected parameter 'values' to be non-null");
            return $;
        }
    }

}

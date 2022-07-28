// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.inputs;

import com.pulumi.civo.inputs.GetInstancesFilter;
import com.pulumi.civo.inputs.GetInstancesSort;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetInstancesPlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetInstancesPlainArgs Empty = new GetInstancesPlainArgs();

    @Import(name="filters")
    private @Nullable List<GetInstancesFilter> filters;

    public Optional<List<GetInstancesFilter>> filters() {
        return Optional.ofNullable(this.filters);
    }

    @Import(name="region")
    private @Nullable String region;

    public Optional<String> region() {
        return Optional.ofNullable(this.region);
    }

    @Import(name="sorts")
    private @Nullable List<GetInstancesSort> sorts;

    public Optional<List<GetInstancesSort>> sorts() {
        return Optional.ofNullable(this.sorts);
    }

    private GetInstancesPlainArgs() {}

    private GetInstancesPlainArgs(GetInstancesPlainArgs $) {
        this.filters = $.filters;
        this.region = $.region;
        this.sorts = $.sorts;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetInstancesPlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetInstancesPlainArgs $;

        public Builder() {
            $ = new GetInstancesPlainArgs();
        }

        public Builder(GetInstancesPlainArgs defaults) {
            $ = new GetInstancesPlainArgs(Objects.requireNonNull(defaults));
        }

        public Builder filters(@Nullable List<GetInstancesFilter> filters) {
            $.filters = filters;
            return this;
        }

        public Builder filters(GetInstancesFilter... filters) {
            return filters(List.of(filters));
        }

        public Builder region(@Nullable String region) {
            $.region = region;
            return this;
        }

        public Builder sorts(@Nullable List<GetInstancesSort> sorts) {
            $.sorts = sorts;
            return this;
        }

        public Builder sorts(GetInstancesSort... sorts) {
            return sorts(List.of(sorts));
        }

        public GetInstancesPlainArgs build() {
            return $;
        }
    }

}

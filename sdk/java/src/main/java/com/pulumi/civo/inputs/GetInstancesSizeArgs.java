// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.inputs;

import com.pulumi.civo.inputs.GetInstancesSizeFilterArgs;
import com.pulumi.civo.inputs.GetInstancesSizeSortArgs;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetInstancesSizeArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetInstancesSizeArgs Empty = new GetInstancesSizeArgs();

    @Import(name="filters")
    private @Nullable Output<List<GetInstancesSizeFilterArgs>> filters;

    public Optional<Output<List<GetInstancesSizeFilterArgs>>> filters() {
        return Optional.ofNullable(this.filters);
    }

    @Import(name="sorts")
    private @Nullable Output<List<GetInstancesSizeSortArgs>> sorts;

    public Optional<Output<List<GetInstancesSizeSortArgs>>> sorts() {
        return Optional.ofNullable(this.sorts);
    }

    private GetInstancesSizeArgs() {}

    private GetInstancesSizeArgs(GetInstancesSizeArgs $) {
        this.filters = $.filters;
        this.sorts = $.sorts;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetInstancesSizeArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetInstancesSizeArgs $;

        public Builder() {
            $ = new GetInstancesSizeArgs();
        }

        public Builder(GetInstancesSizeArgs defaults) {
            $ = new GetInstancesSizeArgs(Objects.requireNonNull(defaults));
        }

        public Builder filters(@Nullable Output<List<GetInstancesSizeFilterArgs>> filters) {
            $.filters = filters;
            return this;
        }

        public Builder filters(List<GetInstancesSizeFilterArgs> filters) {
            return filters(Output.of(filters));
        }

        public Builder filters(GetInstancesSizeFilterArgs... filters) {
            return filters(List.of(filters));
        }

        public Builder sorts(@Nullable Output<List<GetInstancesSizeSortArgs>> sorts) {
            $.sorts = sorts;
            return this;
        }

        public Builder sorts(List<GetInstancesSizeSortArgs> sorts) {
            return sorts(Output.of(sorts));
        }

        public Builder sorts(GetInstancesSizeSortArgs... sorts) {
            return sorts(List.of(sorts));
        }

        public GetInstancesSizeArgs build() {
            return $;
        }
    }

}

// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.inputs;

import com.pulumi.civo.inputs.GetInstancesFilterArgs;
import com.pulumi.civo.inputs.GetInstancesSortArgs;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetInstancesArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetInstancesArgs Empty = new GetInstancesArgs();

    /**
     * One or more key/value pairs on which to filter results
     * 
     */
    @Import(name="filters")
    private @Nullable Output<List<GetInstancesFilterArgs>> filters;

    /**
     * @return One or more key/value pairs on which to filter results
     * 
     */
    public Optional<Output<List<GetInstancesFilterArgs>>> filters() {
        return Optional.ofNullable(this.filters);
    }

    /**
     * If used, all instances will be from the provided region
     * 
     */
    @Import(name="region")
    private @Nullable Output<String> region;

    /**
     * @return If used, all instances will be from the provided region
     * 
     */
    public Optional<Output<String>> region() {
        return Optional.ofNullable(this.region);
    }

    /**
     * One or more key/direction pairs on which to sort results
     * 
     */
    @Import(name="sorts")
    private @Nullable Output<List<GetInstancesSortArgs>> sorts;

    /**
     * @return One or more key/direction pairs on which to sort results
     * 
     */
    public Optional<Output<List<GetInstancesSortArgs>>> sorts() {
        return Optional.ofNullable(this.sorts);
    }

    private GetInstancesArgs() {}

    private GetInstancesArgs(GetInstancesArgs $) {
        this.filters = $.filters;
        this.region = $.region;
        this.sorts = $.sorts;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetInstancesArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetInstancesArgs $;

        public Builder() {
            $ = new GetInstancesArgs();
        }

        public Builder(GetInstancesArgs defaults) {
            $ = new GetInstancesArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param filters One or more key/value pairs on which to filter results
         * 
         * @return builder
         * 
         */
        public Builder filters(@Nullable Output<List<GetInstancesFilterArgs>> filters) {
            $.filters = filters;
            return this;
        }

        /**
         * @param filters One or more key/value pairs on which to filter results
         * 
         * @return builder
         * 
         */
        public Builder filters(List<GetInstancesFilterArgs> filters) {
            return filters(Output.of(filters));
        }

        /**
         * @param filters One or more key/value pairs on which to filter results
         * 
         * @return builder
         * 
         */
        public Builder filters(GetInstancesFilterArgs... filters) {
            return filters(List.of(filters));
        }

        /**
         * @param region If used, all instances will be from the provided region
         * 
         * @return builder
         * 
         */
        public Builder region(@Nullable Output<String> region) {
            $.region = region;
            return this;
        }

        /**
         * @param region If used, all instances will be from the provided region
         * 
         * @return builder
         * 
         */
        public Builder region(String region) {
            return region(Output.of(region));
        }

        /**
         * @param sorts One or more key/direction pairs on which to sort results
         * 
         * @return builder
         * 
         */
        public Builder sorts(@Nullable Output<List<GetInstancesSortArgs>> sorts) {
            $.sorts = sorts;
            return this;
        }

        /**
         * @param sorts One or more key/direction pairs on which to sort results
         * 
         * @return builder
         * 
         */
        public Builder sorts(List<GetInstancesSortArgs> sorts) {
            return sorts(Output.of(sorts));
        }

        /**
         * @param sorts One or more key/direction pairs on which to sort results
         * 
         * @return builder
         * 
         */
        public Builder sorts(GetInstancesSortArgs... sorts) {
            return sorts(List.of(sorts));
        }

        public GetInstancesArgs build() {
            return $;
        }
    }

}
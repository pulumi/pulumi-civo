// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.inputs;

import com.pulumi.civo.inputs.GetDiskImageFilter;
import com.pulumi.civo.inputs.GetDiskImageSort;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetDiskImagePlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetDiskImagePlainArgs Empty = new GetDiskImagePlainArgs();

    /**
     * One or more key/value pairs on which to filter results
     * 
     */
    @Import(name="filters")
    private @Nullable List<GetDiskImageFilter> filters;

    /**
     * @return One or more key/value pairs on which to filter results
     * 
     */
    public Optional<List<GetDiskImageFilter>> filters() {
        return Optional.ofNullable(this.filters);
    }

    /**
     * If is used, all disk image will be from this region. Required if no region is set in provider.
     * 
     */
    @Import(name="region")
    private @Nullable String region;

    /**
     * @return If is used, all disk image will be from this region. Required if no region is set in provider.
     * 
     */
    public Optional<String> region() {
        return Optional.ofNullable(this.region);
    }

    /**
     * One or more key/direction pairs on which to sort results
     * 
     */
    @Import(name="sorts")
    private @Nullable List<GetDiskImageSort> sorts;

    /**
     * @return One or more key/direction pairs on which to sort results
     * 
     */
    public Optional<List<GetDiskImageSort>> sorts() {
        return Optional.ofNullable(this.sorts);
    }

    private GetDiskImagePlainArgs() {}

    private GetDiskImagePlainArgs(GetDiskImagePlainArgs $) {
        this.filters = $.filters;
        this.region = $.region;
        this.sorts = $.sorts;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetDiskImagePlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetDiskImagePlainArgs $;

        public Builder() {
            $ = new GetDiskImagePlainArgs();
        }

        public Builder(GetDiskImagePlainArgs defaults) {
            $ = new GetDiskImagePlainArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param filters One or more key/value pairs on which to filter results
         * 
         * @return builder
         * 
         */
        public Builder filters(@Nullable List<GetDiskImageFilter> filters) {
            $.filters = filters;
            return this;
        }

        /**
         * @param filters One or more key/value pairs on which to filter results
         * 
         * @return builder
         * 
         */
        public Builder filters(GetDiskImageFilter... filters) {
            return filters(List.of(filters));
        }

        /**
         * @param region If is used, all disk image will be from this region. Required if no region is set in provider.
         * 
         * @return builder
         * 
         */
        public Builder region(@Nullable String region) {
            $.region = region;
            return this;
        }

        /**
         * @param sorts One or more key/direction pairs on which to sort results
         * 
         * @return builder
         * 
         */
        public Builder sorts(@Nullable List<GetDiskImageSort> sorts) {
            $.sorts = sorts;
            return this;
        }

        /**
         * @param sorts One or more key/direction pairs on which to sort results
         * 
         * @return builder
         * 
         */
        public Builder sorts(GetDiskImageSort... sorts) {
            return sorts(List.of(sorts));
        }

        public GetDiskImagePlainArgs build() {
            return $;
        }
    }

}

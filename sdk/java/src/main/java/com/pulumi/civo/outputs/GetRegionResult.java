// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.outputs;

import com.pulumi.civo.outputs.GetRegionFilter;
import com.pulumi.civo.outputs.GetRegionRegion;
import com.pulumi.civo.outputs.GetRegionSort;
import com.pulumi.core.annotations.CustomType;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import javax.annotation.Nullable;

@CustomType
public final class GetRegionResult {
    /**
     * @return One or more key/value pairs on which to filter results
     * 
     */
    private @Nullable List<GetRegionFilter> filters;
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    private String id;
    private List<GetRegionRegion> regions;
    /**
     * @return One or more key/direction pairs on which to sort results
     * 
     */
    private @Nullable List<GetRegionSort> sorts;

    private GetRegionResult() {}
    /**
     * @return One or more key/value pairs on which to filter results
     * 
     */
    public List<GetRegionFilter> filters() {
        return this.filters == null ? List.of() : this.filters;
    }
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    public String id() {
        return this.id;
    }
    public List<GetRegionRegion> regions() {
        return this.regions;
    }
    /**
     * @return One or more key/direction pairs on which to sort results
     * 
     */
    public List<GetRegionSort> sorts() {
        return this.sorts == null ? List.of() : this.sorts;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetRegionResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable List<GetRegionFilter> filters;
        private String id;
        private List<GetRegionRegion> regions;
        private @Nullable List<GetRegionSort> sorts;
        public Builder() {}
        public Builder(GetRegionResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.filters = defaults.filters;
    	      this.id = defaults.id;
    	      this.regions = defaults.regions;
    	      this.sorts = defaults.sorts;
        }

        @CustomType.Setter
        public Builder filters(@Nullable List<GetRegionFilter> filters) {
            this.filters = filters;
            return this;
        }
        public Builder filters(GetRegionFilter... filters) {
            return filters(List.of(filters));
        }
        @CustomType.Setter
        public Builder id(String id) {
            this.id = Objects.requireNonNull(id);
            return this;
        }
        @CustomType.Setter
        public Builder regions(List<GetRegionRegion> regions) {
            this.regions = Objects.requireNonNull(regions);
            return this;
        }
        public Builder regions(GetRegionRegion... regions) {
            return regions(List.of(regions));
        }
        @CustomType.Setter
        public Builder sorts(@Nullable List<GetRegionSort> sorts) {
            this.sorts = sorts;
            return this;
        }
        public Builder sorts(GetRegionSort... sorts) {
            return sorts(List.of(sorts));
        }
        public GetRegionResult build() {
            final var o = new GetRegionResult();
            o.filters = filters;
            o.id = id;
            o.regions = regions;
            o.sorts = sorts;
            return o;
        }
    }
}

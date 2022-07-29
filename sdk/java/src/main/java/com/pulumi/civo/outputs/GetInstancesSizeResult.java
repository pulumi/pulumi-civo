// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.outputs;

import com.pulumi.civo.outputs.GetInstancesSizeFilter;
import com.pulumi.civo.outputs.GetInstancesSizeSize;
import com.pulumi.civo.outputs.GetInstancesSizeSort;
import com.pulumi.core.annotations.CustomType;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import javax.annotation.Nullable;

@CustomType
public final class GetInstancesSizeResult {
    private final @Nullable List<GetInstancesSizeFilter> filters;
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    private final String id;
    private final List<GetInstancesSizeSize> sizes;
    private final @Nullable List<GetInstancesSizeSort> sorts;

    @CustomType.Constructor
    private GetInstancesSizeResult(
        @CustomType.Parameter("filters") @Nullable List<GetInstancesSizeFilter> filters,
        @CustomType.Parameter("id") String id,
        @CustomType.Parameter("sizes") List<GetInstancesSizeSize> sizes,
        @CustomType.Parameter("sorts") @Nullable List<GetInstancesSizeSort> sorts) {
        this.filters = filters;
        this.id = id;
        this.sizes = sizes;
        this.sorts = sorts;
    }

    public List<GetInstancesSizeFilter> filters() {
        return this.filters == null ? List.of() : this.filters;
    }
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    public String id() {
        return this.id;
    }
    public List<GetInstancesSizeSize> sizes() {
        return this.sizes;
    }
    public List<GetInstancesSizeSort> sorts() {
        return this.sorts == null ? List.of() : this.sorts;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetInstancesSizeResult defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private @Nullable List<GetInstancesSizeFilter> filters;
        private String id;
        private List<GetInstancesSizeSize> sizes;
        private @Nullable List<GetInstancesSizeSort> sorts;

        public Builder() {
    	      // Empty
        }

        public Builder(GetInstancesSizeResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.filters = defaults.filters;
    	      this.id = defaults.id;
    	      this.sizes = defaults.sizes;
    	      this.sorts = defaults.sorts;
        }

        public Builder filters(@Nullable List<GetInstancesSizeFilter> filters) {
            this.filters = filters;
            return this;
        }
        public Builder filters(GetInstancesSizeFilter... filters) {
            return filters(List.of(filters));
        }
        public Builder id(String id) {
            this.id = Objects.requireNonNull(id);
            return this;
        }
        public Builder sizes(List<GetInstancesSizeSize> sizes) {
            this.sizes = Objects.requireNonNull(sizes);
            return this;
        }
        public Builder sizes(GetInstancesSizeSize... sizes) {
            return sizes(List.of(sizes));
        }
        public Builder sorts(@Nullable List<GetInstancesSizeSort> sorts) {
            this.sorts = sorts;
            return this;
        }
        public Builder sorts(GetInstancesSizeSort... sorts) {
            return sorts(List.of(sorts));
        }        public GetInstancesSizeResult build() {
            return new GetInstancesSizeResult(filters, id, sizes, sorts);
        }
    }
}

// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.outputs;

import com.pulumi.civo.outputs.GetDiskImageDiskimage;
import com.pulumi.civo.outputs.GetDiskImageFilter;
import com.pulumi.civo.outputs.GetDiskImageSort;
import com.pulumi.core.annotations.CustomType;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetDiskImageResult {
    private List<GetDiskImageDiskimage> diskimages;
    private @Nullable List<GetDiskImageFilter> filters;
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    private String id;
    private @Nullable String region;
    private @Nullable List<GetDiskImageSort> sorts;

    private GetDiskImageResult() {}
    public List<GetDiskImageDiskimage> diskimages() {
        return this.diskimages;
    }
    public List<GetDiskImageFilter> filters() {
        return this.filters == null ? List.of() : this.filters;
    }
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    public String id() {
        return this.id;
    }
    public Optional<String> region() {
        return Optional.ofNullable(this.region);
    }
    public List<GetDiskImageSort> sorts() {
        return this.sorts == null ? List.of() : this.sorts;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetDiskImageResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private List<GetDiskImageDiskimage> diskimages;
        private @Nullable List<GetDiskImageFilter> filters;
        private String id;
        private @Nullable String region;
        private @Nullable List<GetDiskImageSort> sorts;
        public Builder() {}
        public Builder(GetDiskImageResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.diskimages = defaults.diskimages;
    	      this.filters = defaults.filters;
    	      this.id = defaults.id;
    	      this.region = defaults.region;
    	      this.sorts = defaults.sorts;
        }

        @CustomType.Setter
        public Builder diskimages(List<GetDiskImageDiskimage> diskimages) {
            this.diskimages = Objects.requireNonNull(diskimages);
            return this;
        }
        public Builder diskimages(GetDiskImageDiskimage... diskimages) {
            return diskimages(List.of(diskimages));
        }
        @CustomType.Setter
        public Builder filters(@Nullable List<GetDiskImageFilter> filters) {
            this.filters = filters;
            return this;
        }
        public Builder filters(GetDiskImageFilter... filters) {
            return filters(List.of(filters));
        }
        @CustomType.Setter
        public Builder id(String id) {
            this.id = Objects.requireNonNull(id);
            return this;
        }
        @CustomType.Setter
        public Builder region(@Nullable String region) {
            this.region = region;
            return this;
        }
        @CustomType.Setter
        public Builder sorts(@Nullable List<GetDiskImageSort> sorts) {
            this.sorts = sorts;
            return this;
        }
        public Builder sorts(GetDiskImageSort... sorts) {
            return sorts(List.of(sorts));
        }
        public GetDiskImageResult build() {
            final var o = new GetDiskImageResult();
            o.diskimages = diskimages;
            o.filters = filters;
            o.id = id;
            o.region = region;
            o.sorts = sorts;
            return o;
        }
    }
}

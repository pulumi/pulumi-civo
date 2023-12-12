// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.outputs;

import com.pulumi.civo.outputs.GetKubernetesVersionFilter;
import com.pulumi.civo.outputs.GetKubernetesVersionSort;
import com.pulumi.civo.outputs.GetKubernetesVersionVersion;
import com.pulumi.core.annotations.CustomType;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import javax.annotation.Nullable;

@CustomType
public final class GetKubernetesVersionResult {
    /**
     * @return One or more key/value pairs on which to filter results
     * 
     */
    private @Nullable List<GetKubernetesVersionFilter> filters;
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    private String id;
    /**
     * @return One or more key/direction pairs on which to sort results
     * 
     */
    private @Nullable List<GetKubernetesVersionSort> sorts;
    private List<GetKubernetesVersionVersion> versions;

    private GetKubernetesVersionResult() {}
    /**
     * @return One or more key/value pairs on which to filter results
     * 
     */
    public List<GetKubernetesVersionFilter> filters() {
        return this.filters == null ? List.of() : this.filters;
    }
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return One or more key/direction pairs on which to sort results
     * 
     */
    public List<GetKubernetesVersionSort> sorts() {
        return this.sorts == null ? List.of() : this.sorts;
    }
    public List<GetKubernetesVersionVersion> versions() {
        return this.versions;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetKubernetesVersionResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable List<GetKubernetesVersionFilter> filters;
        private String id;
        private @Nullable List<GetKubernetesVersionSort> sorts;
        private List<GetKubernetesVersionVersion> versions;
        public Builder() {}
        public Builder(GetKubernetesVersionResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.filters = defaults.filters;
    	      this.id = defaults.id;
    	      this.sorts = defaults.sorts;
    	      this.versions = defaults.versions;
        }

        @CustomType.Setter
        public Builder filters(@Nullable List<GetKubernetesVersionFilter> filters) {
            this.filters = filters;
            return this;
        }
        public Builder filters(GetKubernetesVersionFilter... filters) {
            return filters(List.of(filters));
        }
        @CustomType.Setter
        public Builder id(String id) {
            this.id = Objects.requireNonNull(id);
            return this;
        }
        @CustomType.Setter
        public Builder sorts(@Nullable List<GetKubernetesVersionSort> sorts) {
            this.sorts = sorts;
            return this;
        }
        public Builder sorts(GetKubernetesVersionSort... sorts) {
            return sorts(List.of(sorts));
        }
        @CustomType.Setter
        public Builder versions(List<GetKubernetesVersionVersion> versions) {
            this.versions = Objects.requireNonNull(versions);
            return this;
        }
        public Builder versions(GetKubernetesVersionVersion... versions) {
            return versions(List.of(versions));
        }
        public GetKubernetesVersionResult build() {
            final var _resultValue = new GetKubernetesVersionResult();
            _resultValue.filters = filters;
            _resultValue.id = id;
            _resultValue.sorts = sorts;
            _resultValue.versions = versions;
            return _resultValue;
        }
    }
}

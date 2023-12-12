// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;

@CustomType
public final class GetKubernetesClusterPool {
    private List<String> instanceNames;
    private String label;
    private Integer nodeCount;
    private Boolean publicIpNodePool;
    private String size;

    private GetKubernetesClusterPool() {}
    public List<String> instanceNames() {
        return this.instanceNames;
    }
    public String label() {
        return this.label;
    }
    public Integer nodeCount() {
        return this.nodeCount;
    }
    public Boolean publicIpNodePool() {
        return this.publicIpNodePool;
    }
    public String size() {
        return this.size;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetKubernetesClusterPool defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private List<String> instanceNames;
        private String label;
        private Integer nodeCount;
        private Boolean publicIpNodePool;
        private String size;
        public Builder() {}
        public Builder(GetKubernetesClusterPool defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.instanceNames = defaults.instanceNames;
    	      this.label = defaults.label;
    	      this.nodeCount = defaults.nodeCount;
    	      this.publicIpNodePool = defaults.publicIpNodePool;
    	      this.size = defaults.size;
        }

        @CustomType.Setter
        public Builder instanceNames(List<String> instanceNames) {
            this.instanceNames = Objects.requireNonNull(instanceNames);
            return this;
        }
        public Builder instanceNames(String... instanceNames) {
            return instanceNames(List.of(instanceNames));
        }
        @CustomType.Setter
        public Builder label(String label) {
            this.label = Objects.requireNonNull(label);
            return this;
        }
        @CustomType.Setter
        public Builder nodeCount(Integer nodeCount) {
            this.nodeCount = Objects.requireNonNull(nodeCount);
            return this;
        }
        @CustomType.Setter
        public Builder publicIpNodePool(Boolean publicIpNodePool) {
            this.publicIpNodePool = Objects.requireNonNull(publicIpNodePool);
            return this;
        }
        @CustomType.Setter
        public Builder size(String size) {
            this.size = Objects.requireNonNull(size);
            return this;
        }
        public GetKubernetesClusterPool build() {
            final var _resultValue = new GetKubernetesClusterPool();
            _resultValue.instanceNames = instanceNames;
            _resultValue.label = label;
            _resultValue.nodeCount = nodeCount;
            _resultValue.publicIpNodePool = publicIpNodePool;
            _resultValue.size = size;
            return _resultValue;
        }
    }
}

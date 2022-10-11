// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class KubernetesClusterPools {
    /**
     * @return Instance names in the nodepool
     * 
     */
    private @Nullable List<String> instanceNames;
    /**
     * @return Node pool label, if you don&#39;t provide one, we will generate one for you
     * 
     */
    private @Nullable String label;
    /**
     * @return Number of nodes in the nodepool
     * 
     */
    private Integer nodeCount;
    /**
     * @return Size of the nodes in the nodepool
     * 
     */
    private String size;

    private KubernetesClusterPools() {}
    /**
     * @return Instance names in the nodepool
     * 
     */
    public List<String> instanceNames() {
        return this.instanceNames == null ? List.of() : this.instanceNames;
    }
    /**
     * @return Node pool label, if you don&#39;t provide one, we will generate one for you
     * 
     */
    public Optional<String> label() {
        return Optional.ofNullable(this.label);
    }
    /**
     * @return Number of nodes in the nodepool
     * 
     */
    public Integer nodeCount() {
        return this.nodeCount;
    }
    /**
     * @return Size of the nodes in the nodepool
     * 
     */
    public String size() {
        return this.size;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(KubernetesClusterPools defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable List<String> instanceNames;
        private @Nullable String label;
        private Integer nodeCount;
        private String size;
        public Builder() {}
        public Builder(KubernetesClusterPools defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.instanceNames = defaults.instanceNames;
    	      this.label = defaults.label;
    	      this.nodeCount = defaults.nodeCount;
    	      this.size = defaults.size;
        }

        @CustomType.Setter
        public Builder instanceNames(@Nullable List<String> instanceNames) {
            this.instanceNames = instanceNames;
            return this;
        }
        public Builder instanceNames(String... instanceNames) {
            return instanceNames(List.of(instanceNames));
        }
        @CustomType.Setter
        public Builder label(@Nullable String label) {
            this.label = label;
            return this;
        }
        @CustomType.Setter
        public Builder nodeCount(Integer nodeCount) {
            this.nodeCount = Objects.requireNonNull(nodeCount);
            return this;
        }
        @CustomType.Setter
        public Builder size(String size) {
            this.size = Objects.requireNonNull(size);
            return this;
        }
        public KubernetesClusterPools build() {
            final var o = new KubernetesClusterPools();
            o.instanceNames = instanceNames;
            o.label = label;
            o.nodeCount = nodeCount;
            o.size = size;
            return o;
        }
    }
}
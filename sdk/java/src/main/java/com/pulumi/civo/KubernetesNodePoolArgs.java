// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo;

import com.pulumi.civo.inputs.KubernetesNodePoolTaintArgs;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class KubernetesNodePoolArgs extends com.pulumi.resources.ResourceArgs {

    public static final KubernetesNodePoolArgs Empty = new KubernetesNodePoolArgs();

    /**
     * The ID of your cluster
     * 
     */
    @Import(name="clusterId", required=true)
    private Output<String> clusterId;

    /**
     * @return The ID of your cluster
     * 
     */
    public Output<String> clusterId() {
        return this.clusterId;
    }

    /**
     * Node pool label, if you don&#39;t provide one, we will generate one for you
     * 
     */
    @Import(name="label")
    private @Nullable Output<String> label;

    /**
     * @return Node pool label, if you don&#39;t provide one, we will generate one for you
     * 
     */
    public Optional<Output<String>> label() {
        return Optional.ofNullable(this.label);
    }

    @Import(name="labels")
    private @Nullable Output<Map<String,String>> labels;

    public Optional<Output<Map<String,String>>> labels() {
        return Optional.ofNullable(this.labels);
    }

    /**
     * the number of instances to create (optional, the default at the time of writing is 3)
     * 
     */
    @Import(name="nodeCount")
    private @Nullable Output<Integer> nodeCount;

    /**
     * @return the number of instances to create (optional, the default at the time of writing is 3)
     * 
     */
    public Optional<Output<Integer>> nodeCount() {
        return Optional.ofNullable(this.nodeCount);
    }

    /**
     * Node pool belongs to the public ip node pool
     * 
     */
    @Import(name="publicIpNodePool")
    private @Nullable Output<Boolean> publicIpNodePool;

    /**
     * @return Node pool belongs to the public ip node pool
     * 
     */
    public Optional<Output<Boolean>> publicIpNodePool() {
        return Optional.ofNullable(this.publicIpNodePool);
    }

    /**
     * The region of the node pool, has to match that of the cluster
     * 
     */
    @Import(name="region", required=true)
    private Output<String> region;

    /**
     * @return The region of the node pool, has to match that of the cluster
     * 
     */
    public Output<String> region() {
        return this.region;
    }

    /**
     * the size of each node (optional, the default is currently g4s.kube.medium)
     * 
     */
    @Import(name="size")
    private @Nullable Output<String> size;

    /**
     * @return the size of each node (optional, the default is currently g4s.kube.medium)
     * 
     */
    public Optional<Output<String>> size() {
        return Optional.ofNullable(this.size);
    }

    @Import(name="taints")
    private @Nullable Output<List<KubernetesNodePoolTaintArgs>> taints;

    public Optional<Output<List<KubernetesNodePoolTaintArgs>>> taints() {
        return Optional.ofNullable(this.taints);
    }

    private KubernetesNodePoolArgs() {}

    private KubernetesNodePoolArgs(KubernetesNodePoolArgs $) {
        this.clusterId = $.clusterId;
        this.label = $.label;
        this.labels = $.labels;
        this.nodeCount = $.nodeCount;
        this.publicIpNodePool = $.publicIpNodePool;
        this.region = $.region;
        this.size = $.size;
        this.taints = $.taints;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(KubernetesNodePoolArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private KubernetesNodePoolArgs $;

        public Builder() {
            $ = new KubernetesNodePoolArgs();
        }

        public Builder(KubernetesNodePoolArgs defaults) {
            $ = new KubernetesNodePoolArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param clusterId The ID of your cluster
         * 
         * @return builder
         * 
         */
        public Builder clusterId(Output<String> clusterId) {
            $.clusterId = clusterId;
            return this;
        }

        /**
         * @param clusterId The ID of your cluster
         * 
         * @return builder
         * 
         */
        public Builder clusterId(String clusterId) {
            return clusterId(Output.of(clusterId));
        }

        /**
         * @param label Node pool label, if you don&#39;t provide one, we will generate one for you
         * 
         * @return builder
         * 
         */
        public Builder label(@Nullable Output<String> label) {
            $.label = label;
            return this;
        }

        /**
         * @param label Node pool label, if you don&#39;t provide one, we will generate one for you
         * 
         * @return builder
         * 
         */
        public Builder label(String label) {
            return label(Output.of(label));
        }

        public Builder labels(@Nullable Output<Map<String,String>> labels) {
            $.labels = labels;
            return this;
        }

        public Builder labels(Map<String,String> labels) {
            return labels(Output.of(labels));
        }

        /**
         * @param nodeCount the number of instances to create (optional, the default at the time of writing is 3)
         * 
         * @return builder
         * 
         */
        public Builder nodeCount(@Nullable Output<Integer> nodeCount) {
            $.nodeCount = nodeCount;
            return this;
        }

        /**
         * @param nodeCount the number of instances to create (optional, the default at the time of writing is 3)
         * 
         * @return builder
         * 
         */
        public Builder nodeCount(Integer nodeCount) {
            return nodeCount(Output.of(nodeCount));
        }

        /**
         * @param publicIpNodePool Node pool belongs to the public ip node pool
         * 
         * @return builder
         * 
         */
        public Builder publicIpNodePool(@Nullable Output<Boolean> publicIpNodePool) {
            $.publicIpNodePool = publicIpNodePool;
            return this;
        }

        /**
         * @param publicIpNodePool Node pool belongs to the public ip node pool
         * 
         * @return builder
         * 
         */
        public Builder publicIpNodePool(Boolean publicIpNodePool) {
            return publicIpNodePool(Output.of(publicIpNodePool));
        }

        /**
         * @param region The region of the node pool, has to match that of the cluster
         * 
         * @return builder
         * 
         */
        public Builder region(Output<String> region) {
            $.region = region;
            return this;
        }

        /**
         * @param region The region of the node pool, has to match that of the cluster
         * 
         * @return builder
         * 
         */
        public Builder region(String region) {
            return region(Output.of(region));
        }

        /**
         * @param size the size of each node (optional, the default is currently g4s.kube.medium)
         * 
         * @return builder
         * 
         */
        public Builder size(@Nullable Output<String> size) {
            $.size = size;
            return this;
        }

        /**
         * @param size the size of each node (optional, the default is currently g4s.kube.medium)
         * 
         * @return builder
         * 
         */
        public Builder size(String size) {
            return size(Output.of(size));
        }

        public Builder taints(@Nullable Output<List<KubernetesNodePoolTaintArgs>> taints) {
            $.taints = taints;
            return this;
        }

        public Builder taints(List<KubernetesNodePoolTaintArgs> taints) {
            return taints(Output.of(taints));
        }

        public Builder taints(KubernetesNodePoolTaintArgs... taints) {
            return taints(List.of(taints));
        }

        public KubernetesNodePoolArgs build() {
            if ($.clusterId == null) {
                throw new MissingRequiredPropertyException("KubernetesNodePoolArgs", "clusterId");
            }
            if ($.region == null) {
                throw new MissingRequiredPropertyException("KubernetesNodePoolArgs", "region");
            }
            return $;
        }
    }

}

// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Integer;
import java.lang.String;
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
     * the number of instances to create (optional, the default at the time of writing is 3)
     * 
     * @deprecated
     * This field is deprecated, please use `node_count` instead
     * 
     */
    @Deprecated /* This field is deprecated, please use `node_count` instead */
    @Import(name="numTargetNodes")
    private @Nullable Output<Integer> numTargetNodes;

    /**
     * @return the number of instances to create (optional, the default at the time of writing is 3)
     * 
     * @deprecated
     * This field is deprecated, please use `node_count` instead
     * 
     */
    @Deprecated /* This field is deprecated, please use `node_count` instead */
    public Optional<Output<Integer>> numTargetNodes() {
        return Optional.ofNullable(this.numTargetNodes);
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

    /**
     * the size of each node (optional, the default is currently g4s.kube.medium)
     * 
     * @deprecated
     * This field is deprecated, please use `size` instead
     * 
     */
    @Deprecated /* This field is deprecated, please use `size` instead */
    @Import(name="targetNodesSize")
    private @Nullable Output<String> targetNodesSize;

    /**
     * @return the size of each node (optional, the default is currently g4s.kube.medium)
     * 
     * @deprecated
     * This field is deprecated, please use `size` instead
     * 
     */
    @Deprecated /* This field is deprecated, please use `size` instead */
    public Optional<Output<String>> targetNodesSize() {
        return Optional.ofNullable(this.targetNodesSize);
    }

    private KubernetesNodePoolArgs() {}

    private KubernetesNodePoolArgs(KubernetesNodePoolArgs $) {
        this.clusterId = $.clusterId;
        this.label = $.label;
        this.nodeCount = $.nodeCount;
        this.numTargetNodes = $.numTargetNodes;
        this.region = $.region;
        this.size = $.size;
        this.targetNodesSize = $.targetNodesSize;
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
         * @param numTargetNodes the number of instances to create (optional, the default at the time of writing is 3)
         * 
         * @return builder
         * 
         * @deprecated
         * This field is deprecated, please use `node_count` instead
         * 
         */
        @Deprecated /* This field is deprecated, please use `node_count` instead */
        public Builder numTargetNodes(@Nullable Output<Integer> numTargetNodes) {
            $.numTargetNodes = numTargetNodes;
            return this;
        }

        /**
         * @param numTargetNodes the number of instances to create (optional, the default at the time of writing is 3)
         * 
         * @return builder
         * 
         * @deprecated
         * This field is deprecated, please use `node_count` instead
         * 
         */
        @Deprecated /* This field is deprecated, please use `node_count` instead */
        public Builder numTargetNodes(Integer numTargetNodes) {
            return numTargetNodes(Output.of(numTargetNodes));
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

        /**
         * @param targetNodesSize the size of each node (optional, the default is currently g4s.kube.medium)
         * 
         * @return builder
         * 
         * @deprecated
         * This field is deprecated, please use `size` instead
         * 
         */
        @Deprecated /* This field is deprecated, please use `size` instead */
        public Builder targetNodesSize(@Nullable Output<String> targetNodesSize) {
            $.targetNodesSize = targetNodesSize;
            return this;
        }

        /**
         * @param targetNodesSize the size of each node (optional, the default is currently g4s.kube.medium)
         * 
         * @return builder
         * 
         * @deprecated
         * This field is deprecated, please use `size` instead
         * 
         */
        @Deprecated /* This field is deprecated, please use `size` instead */
        public Builder targetNodesSize(String targetNodesSize) {
            return targetNodesSize(Output.of(targetNodesSize));
        }

        public KubernetesNodePoolArgs build() {
            $.clusterId = Objects.requireNonNull($.clusterId, "expected parameter 'clusterId' to be non-null");
            $.region = Objects.requireNonNull($.region, "expected parameter 'region' to be non-null");
            return $;
        }
    }

}

// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.inputs;

import com.pulumi.civo.inputs.KubernetesNodePoolTaintArgs;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class KubernetesNodePoolState extends com.pulumi.resources.ResourceArgs {

    public static final KubernetesNodePoolState Empty = new KubernetesNodePoolState();

    /**
     * The ID of your cluster
     * 
     */
    @Import(name="clusterId")
    private @Nullable Output<String> clusterId;

    /**
     * @return The ID of your cluster
     * 
     */
    public Optional<Output<String>> clusterId() {
        return Optional.ofNullable(this.clusterId);
    }

    /**
     * Instance names in the nodepool
     * 
     */
    @Import(name="instanceNames")
    private @Nullable Output<List<String>> instanceNames;

    /**
     * @return Instance names in the nodepool
     * 
     */
    public Optional<Output<List<String>>> instanceNames() {
        return Optional.ofNullable(this.instanceNames);
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
     * Number of nodes in the nodepool
     * 
     */
    @Import(name="nodeCount")
    private @Nullable Output<Integer> nodeCount;

    /**
     * @return Number of nodes in the nodepool
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
     * Size of the nodes in the nodepool
     * 
     */
    @Import(name="size")
    private @Nullable Output<String> size;

    /**
     * @return Size of the nodes in the nodepool
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

    private KubernetesNodePoolState() {}

    private KubernetesNodePoolState(KubernetesNodePoolState $) {
        this.clusterId = $.clusterId;
        this.instanceNames = $.instanceNames;
        this.label = $.label;
        this.labels = $.labels;
        this.nodeCount = $.nodeCount;
        this.publicIpNodePool = $.publicIpNodePool;
        this.size = $.size;
        this.taints = $.taints;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(KubernetesNodePoolState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private KubernetesNodePoolState $;

        public Builder() {
            $ = new KubernetesNodePoolState();
        }

        public Builder(KubernetesNodePoolState defaults) {
            $ = new KubernetesNodePoolState(Objects.requireNonNull(defaults));
        }

        /**
         * @param clusterId The ID of your cluster
         * 
         * @return builder
         * 
         */
        public Builder clusterId(@Nullable Output<String> clusterId) {
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
         * @param instanceNames Instance names in the nodepool
         * 
         * @return builder
         * 
         */
        public Builder instanceNames(@Nullable Output<List<String>> instanceNames) {
            $.instanceNames = instanceNames;
            return this;
        }

        /**
         * @param instanceNames Instance names in the nodepool
         * 
         * @return builder
         * 
         */
        public Builder instanceNames(List<String> instanceNames) {
            return instanceNames(Output.of(instanceNames));
        }

        /**
         * @param instanceNames Instance names in the nodepool
         * 
         * @return builder
         * 
         */
        public Builder instanceNames(String... instanceNames) {
            return instanceNames(List.of(instanceNames));
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
         * @param nodeCount Number of nodes in the nodepool
         * 
         * @return builder
         * 
         */
        public Builder nodeCount(@Nullable Output<Integer> nodeCount) {
            $.nodeCount = nodeCount;
            return this;
        }

        /**
         * @param nodeCount Number of nodes in the nodepool
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
         * @param size Size of the nodes in the nodepool
         * 
         * @return builder
         * 
         */
        public Builder size(@Nullable Output<String> size) {
            $.size = size;
            return this;
        }

        /**
         * @param size Size of the nodes in the nodepool
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

        public KubernetesNodePoolState build() {
            return $;
        }
    }

}
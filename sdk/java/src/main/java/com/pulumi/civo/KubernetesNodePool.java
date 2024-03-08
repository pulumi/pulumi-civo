// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo;

import com.pulumi.civo.KubernetesNodePoolArgs;
import com.pulumi.civo.Utilities;
import com.pulumi.civo.inputs.KubernetesNodePoolState;
import com.pulumi.civo.outputs.KubernetesNodePoolTaint;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * ## Import
 * 
 * ```sh
 * $ pulumi import civo:index/kubernetesNodePool:KubernetesNodePool my-pool 1b8b2100-0e9f-4e8f-ad78-9eb578c2a0af:502c1130-cb9b-4a88-b6d2-307bd96d946a
 * ```
 * 
 */
@ResourceType(type="civo:index/kubernetesNodePool:KubernetesNodePool")
public class KubernetesNodePool extends com.pulumi.resources.CustomResource {
    /**
     * The ID of your cluster
     * 
     */
    @Export(name="clusterId", refs={String.class}, tree="[0]")
    private Output<String> clusterId;

    /**
     * @return The ID of your cluster
     * 
     */
    public Output<String> clusterId() {
        return this.clusterId;
    }
    /**
     * Instance names in the nodepool
     * 
     */
    @Export(name="instanceNames", refs={List.class,String.class}, tree="[0,1]")
    private Output<List<String>> instanceNames;

    /**
     * @return Instance names in the nodepool
     * 
     */
    public Output<List<String>> instanceNames() {
        return this.instanceNames;
    }
    /**
     * Node pool label, if you don&#39;t provide one, we will generate one for you
     * 
     */
    @Export(name="label", refs={String.class}, tree="[0]")
    private Output<String> label;

    /**
     * @return Node pool label, if you don&#39;t provide one, we will generate one for you
     * 
     */
    public Output<String> label() {
        return this.label;
    }
    @Export(name="labels", refs={Map.class,String.class}, tree="[0,1,1]")
    private Output</* @Nullable */ Map<String,String>> labels;

    public Output<Optional<Map<String,String>>> labels() {
        return Codegen.optional(this.labels);
    }
    /**
     * the number of instances to create (optional, the default at the time of writing is 3)
     * 
     */
    @Export(name="nodeCount", refs={Integer.class}, tree="[0]")
    private Output<Integer> nodeCount;

    /**
     * @return the number of instances to create (optional, the default at the time of writing is 3)
     * 
     */
    public Output<Integer> nodeCount() {
        return this.nodeCount;
    }
    /**
     * Node pool belongs to the public ip node pool
     * 
     */
    @Export(name="publicIpNodePool", refs={Boolean.class}, tree="[0]")
    private Output<Boolean> publicIpNodePool;

    /**
     * @return Node pool belongs to the public ip node pool
     * 
     */
    public Output<Boolean> publicIpNodePool() {
        return this.publicIpNodePool;
    }
    /**
     * The region of the node pool, has to match that of the cluster
     * 
     */
    @Export(name="region", refs={String.class}, tree="[0]")
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
    @Export(name="size", refs={String.class}, tree="[0]")
    private Output<String> size;

    /**
     * @return the size of each node (optional, the default is currently g4s.kube.medium)
     * 
     */
    public Output<String> size() {
        return this.size;
    }
    @Export(name="taints", refs={List.class,KubernetesNodePoolTaint.class}, tree="[0,1]")
    private Output</* @Nullable */ List<KubernetesNodePoolTaint>> taints;

    public Output<Optional<List<KubernetesNodePoolTaint>>> taints() {
        return Codegen.optional(this.taints);
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public KubernetesNodePool(String name) {
        this(name, KubernetesNodePoolArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public KubernetesNodePool(String name, KubernetesNodePoolArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public KubernetesNodePool(String name, KubernetesNodePoolArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("civo:index/kubernetesNodePool:KubernetesNodePool", name, args == null ? KubernetesNodePoolArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private KubernetesNodePool(String name, Output<String> id, @Nullable KubernetesNodePoolState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("civo:index/kubernetesNodePool:KubernetesNodePool", name, state, makeResourceOptions(options, id));
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .build();
        return com.pulumi.resources.CustomResourceOptions.merge(defaultOptions, options, id);
    }

    /**
     * Get an existing Host resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state
     * @param options Optional settings to control the behavior of the CustomResource.
     */
    public static KubernetesNodePool get(String name, Output<String> id, @Nullable KubernetesNodePoolState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new KubernetesNodePool(name, id, state, options);
    }
}

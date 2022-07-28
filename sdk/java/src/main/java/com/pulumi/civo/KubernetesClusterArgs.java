// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo;

import com.pulumi.civo.inputs.KubernetesClusterPoolsArgs;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class KubernetesClusterArgs extends com.pulumi.resources.ResourceArgs {

    public static final KubernetesClusterArgs Empty = new KubernetesClusterArgs();

    /**
     * Comma separated list of applications to install. Spaces within application names are fine, but shouldn&#39;t be either side
     * of the comma. Application names are case-sensitive; the available applications can be listed with the Civo CLI: &#39;civo
     * kubernetes applications ls&#39;. If you want to remove a default installed application, prefix it with a &#39;-&#39;, e.g. -Traefik.
     * For application that supports plans, you can use &#39;app_name:app_plan&#39; format e.g. &#39;Linkerd:Linkerd &amp; Jaeger&#39; or
     * &#39;MariaDB:5GB&#39;.
     * 
     */
    @Import(name="applications")
    private @Nullable Output<String> applications;

    /**
     * @return Comma separated list of applications to install. Spaces within application names are fine, but shouldn&#39;t be either side
     * of the comma. Application names are case-sensitive; the available applications can be listed with the Civo CLI: &#39;civo
     * kubernetes applications ls&#39;. If you want to remove a default installed application, prefix it with a &#39;-&#39;, e.g. -Traefik.
     * For application that supports plans, you can use &#39;app_name:app_plan&#39; format e.g. &#39;Linkerd:Linkerd &amp; Jaeger&#39; or
     * &#39;MariaDB:5GB&#39;.
     * 
     */
    public Optional<Output<String>> applications() {
        return Optional.ofNullable(this.applications);
    }

    /**
     * The cni for the k3s to install (the default is `flannel`) valid options are `cilium` or `flannel`
     * 
     */
    @Import(name="cni")
    private @Nullable Output<String> cni;

    /**
     * @return The cni for the k3s to install (the default is `flannel`) valid options are `cilium` or `flannel`
     * 
     */
    public Optional<Output<String>> cni() {
        return Optional.ofNullable(this.cni);
    }

    /**
     * The existing firewall ID to use for this cluster
     * 
     */
    @Import(name="firewallId", required=true)
    private Output<String> firewallId;

    /**
     * @return The existing firewall ID to use for this cluster
     * 
     */
    public Output<String> firewallId() {
        return this.firewallId;
    }

    /**
     * The version of k3s to install (optional, the default is currently the latest available)
     * 
     */
    @Import(name="kubernetesVersion")
    private @Nullable Output<String> kubernetesVersion;

    /**
     * @return The version of k3s to install (optional, the default is currently the latest available)
     * 
     */
    public Optional<Output<String>> kubernetesVersion() {
        return Optional.ofNullable(this.kubernetesVersion);
    }

    /**
     * Name for your cluster, must be unique within your account
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return Name for your cluster, must be unique within your account
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * The network for the cluster, if not declare we use the default one
     * 
     */
    @Import(name="networkId")
    private @Nullable Output<String> networkId;

    /**
     * @return The network for the cluster, if not declare we use the default one
     * 
     */
    public Optional<Output<String>> networkId() {
        return Optional.ofNullable(this.networkId);
    }

    /**
     * The number of instances to create (optional, the default at the time of writing is 3)
     * 
     * @deprecated
     * This field will be deprecated in the next major release, please use the &#39;pools&#39; field instead
     * 
     */
    @Deprecated /* This field will be deprecated in the next major release, please use the 'pools' field instead */
    @Import(name="numTargetNodes")
    private @Nullable Output<Integer> numTargetNodes;

    /**
     * @return The number of instances to create (optional, the default at the time of writing is 3)
     * 
     * @deprecated
     * This field will be deprecated in the next major release, please use the &#39;pools&#39; field instead
     * 
     */
    @Deprecated /* This field will be deprecated in the next major release, please use the 'pools' field instead */
    public Optional<Output<Integer>> numTargetNodes() {
        return Optional.ofNullable(this.numTargetNodes);
    }

    @Import(name="pools", required=true)
    private Output<KubernetesClusterPoolsArgs> pools;

    public Output<KubernetesClusterPoolsArgs> pools() {
        return this.pools;
    }

    /**
     * The region for the cluster, if not declare we use the region in declared in the provider
     * 
     */
    @Import(name="region")
    private @Nullable Output<String> region;

    /**
     * @return The region for the cluster, if not declare we use the region in declared in the provider
     * 
     */
    public Optional<Output<String>> region() {
        return Optional.ofNullable(this.region);
    }

    /**
     * Space separated list of tags, to be used freely as required
     * 
     */
    @Import(name="tags")
    private @Nullable Output<String> tags;

    /**
     * @return Space separated list of tags, to be used freely as required
     * 
     */
    public Optional<Output<String>> tags() {
        return Optional.ofNullable(this.tags);
    }

    /**
     * The size of each node (optional, the default is currently g4s.kube.medium)
     * 
     * @deprecated
     * This field will be deprecated in the next major release, please use the &#39;pools&#39; field instead
     * 
     */
    @Deprecated /* This field will be deprecated in the next major release, please use the 'pools' field instead */
    @Import(name="targetNodesSize")
    private @Nullable Output<String> targetNodesSize;

    /**
     * @return The size of each node (optional, the default is currently g4s.kube.medium)
     * 
     * @deprecated
     * This field will be deprecated in the next major release, please use the &#39;pools&#39; field instead
     * 
     */
    @Deprecated /* This field will be deprecated in the next major release, please use the 'pools' field instead */
    public Optional<Output<String>> targetNodesSize() {
        return Optional.ofNullable(this.targetNodesSize);
    }

    private KubernetesClusterArgs() {}

    private KubernetesClusterArgs(KubernetesClusterArgs $) {
        this.applications = $.applications;
        this.cni = $.cni;
        this.firewallId = $.firewallId;
        this.kubernetesVersion = $.kubernetesVersion;
        this.name = $.name;
        this.networkId = $.networkId;
        this.numTargetNodes = $.numTargetNodes;
        this.pools = $.pools;
        this.region = $.region;
        this.tags = $.tags;
        this.targetNodesSize = $.targetNodesSize;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(KubernetesClusterArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private KubernetesClusterArgs $;

        public Builder() {
            $ = new KubernetesClusterArgs();
        }

        public Builder(KubernetesClusterArgs defaults) {
            $ = new KubernetesClusterArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param applications Comma separated list of applications to install. Spaces within application names are fine, but shouldn&#39;t be either side
         * of the comma. Application names are case-sensitive; the available applications can be listed with the Civo CLI: &#39;civo
         * kubernetes applications ls&#39;. If you want to remove a default installed application, prefix it with a &#39;-&#39;, e.g. -Traefik.
         * For application that supports plans, you can use &#39;app_name:app_plan&#39; format e.g. &#39;Linkerd:Linkerd &amp; Jaeger&#39; or
         * &#39;MariaDB:5GB&#39;.
         * 
         * @return builder
         * 
         */
        public Builder applications(@Nullable Output<String> applications) {
            $.applications = applications;
            return this;
        }

        /**
         * @param applications Comma separated list of applications to install. Spaces within application names are fine, but shouldn&#39;t be either side
         * of the comma. Application names are case-sensitive; the available applications can be listed with the Civo CLI: &#39;civo
         * kubernetes applications ls&#39;. If you want to remove a default installed application, prefix it with a &#39;-&#39;, e.g. -Traefik.
         * For application that supports plans, you can use &#39;app_name:app_plan&#39; format e.g. &#39;Linkerd:Linkerd &amp; Jaeger&#39; or
         * &#39;MariaDB:5GB&#39;.
         * 
         * @return builder
         * 
         */
        public Builder applications(String applications) {
            return applications(Output.of(applications));
        }

        /**
         * @param cni The cni for the k3s to install (the default is `flannel`) valid options are `cilium` or `flannel`
         * 
         * @return builder
         * 
         */
        public Builder cni(@Nullable Output<String> cni) {
            $.cni = cni;
            return this;
        }

        /**
         * @param cni The cni for the k3s to install (the default is `flannel`) valid options are `cilium` or `flannel`
         * 
         * @return builder
         * 
         */
        public Builder cni(String cni) {
            return cni(Output.of(cni));
        }

        /**
         * @param firewallId The existing firewall ID to use for this cluster
         * 
         * @return builder
         * 
         */
        public Builder firewallId(Output<String> firewallId) {
            $.firewallId = firewallId;
            return this;
        }

        /**
         * @param firewallId The existing firewall ID to use for this cluster
         * 
         * @return builder
         * 
         */
        public Builder firewallId(String firewallId) {
            return firewallId(Output.of(firewallId));
        }

        /**
         * @param kubernetesVersion The version of k3s to install (optional, the default is currently the latest available)
         * 
         * @return builder
         * 
         */
        public Builder kubernetesVersion(@Nullable Output<String> kubernetesVersion) {
            $.kubernetesVersion = kubernetesVersion;
            return this;
        }

        /**
         * @param kubernetesVersion The version of k3s to install (optional, the default is currently the latest available)
         * 
         * @return builder
         * 
         */
        public Builder kubernetesVersion(String kubernetesVersion) {
            return kubernetesVersion(Output.of(kubernetesVersion));
        }

        /**
         * @param name Name for your cluster, must be unique within your account
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name Name for your cluster, must be unique within your account
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param networkId The network for the cluster, if not declare we use the default one
         * 
         * @return builder
         * 
         */
        public Builder networkId(@Nullable Output<String> networkId) {
            $.networkId = networkId;
            return this;
        }

        /**
         * @param networkId The network for the cluster, if not declare we use the default one
         * 
         * @return builder
         * 
         */
        public Builder networkId(String networkId) {
            return networkId(Output.of(networkId));
        }

        /**
         * @param numTargetNodes The number of instances to create (optional, the default at the time of writing is 3)
         * 
         * @return builder
         * 
         * @deprecated
         * This field will be deprecated in the next major release, please use the &#39;pools&#39; field instead
         * 
         */
        @Deprecated /* This field will be deprecated in the next major release, please use the 'pools' field instead */
        public Builder numTargetNodes(@Nullable Output<Integer> numTargetNodes) {
            $.numTargetNodes = numTargetNodes;
            return this;
        }

        /**
         * @param numTargetNodes The number of instances to create (optional, the default at the time of writing is 3)
         * 
         * @return builder
         * 
         * @deprecated
         * This field will be deprecated in the next major release, please use the &#39;pools&#39; field instead
         * 
         */
        @Deprecated /* This field will be deprecated in the next major release, please use the 'pools' field instead */
        public Builder numTargetNodes(Integer numTargetNodes) {
            return numTargetNodes(Output.of(numTargetNodes));
        }

        public Builder pools(Output<KubernetesClusterPoolsArgs> pools) {
            $.pools = pools;
            return this;
        }

        public Builder pools(KubernetesClusterPoolsArgs pools) {
            return pools(Output.of(pools));
        }

        /**
         * @param region The region for the cluster, if not declare we use the region in declared in the provider
         * 
         * @return builder
         * 
         */
        public Builder region(@Nullable Output<String> region) {
            $.region = region;
            return this;
        }

        /**
         * @param region The region for the cluster, if not declare we use the region in declared in the provider
         * 
         * @return builder
         * 
         */
        public Builder region(String region) {
            return region(Output.of(region));
        }

        /**
         * @param tags Space separated list of tags, to be used freely as required
         * 
         * @return builder
         * 
         */
        public Builder tags(@Nullable Output<String> tags) {
            $.tags = tags;
            return this;
        }

        /**
         * @param tags Space separated list of tags, to be used freely as required
         * 
         * @return builder
         * 
         */
        public Builder tags(String tags) {
            return tags(Output.of(tags));
        }

        /**
         * @param targetNodesSize The size of each node (optional, the default is currently g4s.kube.medium)
         * 
         * @return builder
         * 
         * @deprecated
         * This field will be deprecated in the next major release, please use the &#39;pools&#39; field instead
         * 
         */
        @Deprecated /* This field will be deprecated in the next major release, please use the 'pools' field instead */
        public Builder targetNodesSize(@Nullable Output<String> targetNodesSize) {
            $.targetNodesSize = targetNodesSize;
            return this;
        }

        /**
         * @param targetNodesSize The size of each node (optional, the default is currently g4s.kube.medium)
         * 
         * @return builder
         * 
         * @deprecated
         * This field will be deprecated in the next major release, please use the &#39;pools&#39; field instead
         * 
         */
        @Deprecated /* This field will be deprecated in the next major release, please use the 'pools' field instead */
        public Builder targetNodesSize(String targetNodesSize) {
            return targetNodesSize(Output.of(targetNodesSize));
        }

        public KubernetesClusterArgs build() {
            $.firewallId = Objects.requireNonNull($.firewallId, "expected parameter 'firewallId' to be non-null");
            $.pools = Objects.requireNonNull($.pools, "expected parameter 'pools' to be non-null");
            return $;
        }
    }

}

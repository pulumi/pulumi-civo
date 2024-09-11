// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.outputs;

import com.pulumi.civo.outputs.GetKubernetesClusterInstalledApplication;
import com.pulumi.civo.outputs.GetKubernetesClusterPool;
import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetKubernetesClusterResult {
    /**
     * @return The base URL of the API server on the Kubernetes master node
     * 
     */
    private String apiEndpoint;
    /**
     * @return A list of application installed
     * 
     */
    private String applications;
    /**
     * @return The cni for the k3s to install (the default is `flannel`) valid options are `cilium` or `flannel`
     * 
     */
    private String cni;
    /**
     * @return The date where the Kubernetes cluster was create
     * 
     */
    private String createdAt;
    /**
     * @return The unique dns entry for the cluster in this case point to the master
     * 
     */
    private String dnsEntry;
    /**
     * @return The ID of this resource.
     * 
     */
    private @Nullable String id;
    private List<GetKubernetesClusterInstalledApplication> installedApplications;
    /**
     * @return A representation of the Kubernetes cluster&#39;s kubeconfig in yaml format
     * 
     */
    private String kubeconfig;
    /**
     * @return The version of Kubernetes
     * 
     */
    private String kubernetesVersion;
    /**
     * @return The IP of the Kubernetes master node
     * 
     */
    private String masterIp;
    /**
     * @return The name of the Kubernetes Cluster
     * 
     */
    private @Nullable String name;
    /**
     * @return The size of the Kubernetes cluster
     * 
     * @deprecated
     * This field is deprecated and will be removed in a future version of the provider
     * 
     */
    @Deprecated /* This field is deprecated and will be removed in a future version of the provider */
    private Integer numTargetNodes;
    private List<GetKubernetesClusterPool> pools;
    /**
     * @return If the Kubernetes cluster is ready
     * 
     */
    private Boolean ready;
    /**
     * @return The region where cluster is running
     * 
     */
    private @Nullable String region;
    /**
     * @return The status of Kubernetes cluster
     * 
     */
    private String status;
    /**
     * @return A list of tags
     * 
     */
    private List<String> tags;
    /**
     * @return The size of each node
     * 
     * @deprecated
     * This field is deprecated and will be removed in a future version of the provider
     * 
     */
    @Deprecated /* This field is deprecated and will be removed in a future version of the provider */
    private String targetNodesSize;

    private GetKubernetesClusterResult() {}
    /**
     * @return The base URL of the API server on the Kubernetes master node
     * 
     */
    public String apiEndpoint() {
        return this.apiEndpoint;
    }
    /**
     * @return A list of application installed
     * 
     */
    public String applications() {
        return this.applications;
    }
    /**
     * @return The cni for the k3s to install (the default is `flannel`) valid options are `cilium` or `flannel`
     * 
     */
    public String cni() {
        return this.cni;
    }
    /**
     * @return The date where the Kubernetes cluster was create
     * 
     */
    public String createdAt() {
        return this.createdAt;
    }
    /**
     * @return The unique dns entry for the cluster in this case point to the master
     * 
     */
    public String dnsEntry() {
        return this.dnsEntry;
    }
    /**
     * @return The ID of this resource.
     * 
     */
    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }
    public List<GetKubernetesClusterInstalledApplication> installedApplications() {
        return this.installedApplications;
    }
    /**
     * @return A representation of the Kubernetes cluster&#39;s kubeconfig in yaml format
     * 
     */
    public String kubeconfig() {
        return this.kubeconfig;
    }
    /**
     * @return The version of Kubernetes
     * 
     */
    public String kubernetesVersion() {
        return this.kubernetesVersion;
    }
    /**
     * @return The IP of the Kubernetes master node
     * 
     */
    public String masterIp() {
        return this.masterIp;
    }
    /**
     * @return The name of the Kubernetes Cluster
     * 
     */
    public Optional<String> name() {
        return Optional.ofNullable(this.name);
    }
    /**
     * @return The size of the Kubernetes cluster
     * 
     * @deprecated
     * This field is deprecated and will be removed in a future version of the provider
     * 
     */
    @Deprecated /* This field is deprecated and will be removed in a future version of the provider */
    public Integer numTargetNodes() {
        return this.numTargetNodes;
    }
    public List<GetKubernetesClusterPool> pools() {
        return this.pools;
    }
    /**
     * @return If the Kubernetes cluster is ready
     * 
     */
    public Boolean ready() {
        return this.ready;
    }
    /**
     * @return The region where cluster is running
     * 
     */
    public Optional<String> region() {
        return Optional.ofNullable(this.region);
    }
    /**
     * @return The status of Kubernetes cluster
     * 
     */
    public String status() {
        return this.status;
    }
    /**
     * @return A list of tags
     * 
     */
    public List<String> tags() {
        return this.tags;
    }
    /**
     * @return The size of each node
     * 
     * @deprecated
     * This field is deprecated and will be removed in a future version of the provider
     * 
     */
    @Deprecated /* This field is deprecated and will be removed in a future version of the provider */
    public String targetNodesSize() {
        return this.targetNodesSize;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetKubernetesClusterResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String apiEndpoint;
        private String applications;
        private String cni;
        private String createdAt;
        private String dnsEntry;
        private @Nullable String id;
        private List<GetKubernetesClusterInstalledApplication> installedApplications;
        private String kubeconfig;
        private String kubernetesVersion;
        private String masterIp;
        private @Nullable String name;
        private Integer numTargetNodes;
        private List<GetKubernetesClusterPool> pools;
        private Boolean ready;
        private @Nullable String region;
        private String status;
        private List<String> tags;
        private String targetNodesSize;
        public Builder() {}
        public Builder(GetKubernetesClusterResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.apiEndpoint = defaults.apiEndpoint;
    	      this.applications = defaults.applications;
    	      this.cni = defaults.cni;
    	      this.createdAt = defaults.createdAt;
    	      this.dnsEntry = defaults.dnsEntry;
    	      this.id = defaults.id;
    	      this.installedApplications = defaults.installedApplications;
    	      this.kubeconfig = defaults.kubeconfig;
    	      this.kubernetesVersion = defaults.kubernetesVersion;
    	      this.masterIp = defaults.masterIp;
    	      this.name = defaults.name;
    	      this.numTargetNodes = defaults.numTargetNodes;
    	      this.pools = defaults.pools;
    	      this.ready = defaults.ready;
    	      this.region = defaults.region;
    	      this.status = defaults.status;
    	      this.tags = defaults.tags;
    	      this.targetNodesSize = defaults.targetNodesSize;
        }

        @CustomType.Setter
        public Builder apiEndpoint(String apiEndpoint) {
            if (apiEndpoint == null) {
              throw new MissingRequiredPropertyException("GetKubernetesClusterResult", "apiEndpoint");
            }
            this.apiEndpoint = apiEndpoint;
            return this;
        }
        @CustomType.Setter
        public Builder applications(String applications) {
            if (applications == null) {
              throw new MissingRequiredPropertyException("GetKubernetesClusterResult", "applications");
            }
            this.applications = applications;
            return this;
        }
        @CustomType.Setter
        public Builder cni(String cni) {
            if (cni == null) {
              throw new MissingRequiredPropertyException("GetKubernetesClusterResult", "cni");
            }
            this.cni = cni;
            return this;
        }
        @CustomType.Setter
        public Builder createdAt(String createdAt) {
            if (createdAt == null) {
              throw new MissingRequiredPropertyException("GetKubernetesClusterResult", "createdAt");
            }
            this.createdAt = createdAt;
            return this;
        }
        @CustomType.Setter
        public Builder dnsEntry(String dnsEntry) {
            if (dnsEntry == null) {
              throw new MissingRequiredPropertyException("GetKubernetesClusterResult", "dnsEntry");
            }
            this.dnsEntry = dnsEntry;
            return this;
        }
        @CustomType.Setter
        public Builder id(@Nullable String id) {

            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder installedApplications(List<GetKubernetesClusterInstalledApplication> installedApplications) {
            if (installedApplications == null) {
              throw new MissingRequiredPropertyException("GetKubernetesClusterResult", "installedApplications");
            }
            this.installedApplications = installedApplications;
            return this;
        }
        public Builder installedApplications(GetKubernetesClusterInstalledApplication... installedApplications) {
            return installedApplications(List.of(installedApplications));
        }
        @CustomType.Setter
        public Builder kubeconfig(String kubeconfig) {
            if (kubeconfig == null) {
              throw new MissingRequiredPropertyException("GetKubernetesClusterResult", "kubeconfig");
            }
            this.kubeconfig = kubeconfig;
            return this;
        }
        @CustomType.Setter
        public Builder kubernetesVersion(String kubernetesVersion) {
            if (kubernetesVersion == null) {
              throw new MissingRequiredPropertyException("GetKubernetesClusterResult", "kubernetesVersion");
            }
            this.kubernetesVersion = kubernetesVersion;
            return this;
        }
        @CustomType.Setter
        public Builder masterIp(String masterIp) {
            if (masterIp == null) {
              throw new MissingRequiredPropertyException("GetKubernetesClusterResult", "masterIp");
            }
            this.masterIp = masterIp;
            return this;
        }
        @CustomType.Setter
        public Builder name(@Nullable String name) {

            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder numTargetNodes(Integer numTargetNodes) {
            if (numTargetNodes == null) {
              throw new MissingRequiredPropertyException("GetKubernetesClusterResult", "numTargetNodes");
            }
            this.numTargetNodes = numTargetNodes;
            return this;
        }
        @CustomType.Setter
        public Builder pools(List<GetKubernetesClusterPool> pools) {
            if (pools == null) {
              throw new MissingRequiredPropertyException("GetKubernetesClusterResult", "pools");
            }
            this.pools = pools;
            return this;
        }
        public Builder pools(GetKubernetesClusterPool... pools) {
            return pools(List.of(pools));
        }
        @CustomType.Setter
        public Builder ready(Boolean ready) {
            if (ready == null) {
              throw new MissingRequiredPropertyException("GetKubernetesClusterResult", "ready");
            }
            this.ready = ready;
            return this;
        }
        @CustomType.Setter
        public Builder region(@Nullable String region) {

            this.region = region;
            return this;
        }
        @CustomType.Setter
        public Builder status(String status) {
            if (status == null) {
              throw new MissingRequiredPropertyException("GetKubernetesClusterResult", "status");
            }
            this.status = status;
            return this;
        }
        @CustomType.Setter
        public Builder tags(List<String> tags) {
            if (tags == null) {
              throw new MissingRequiredPropertyException("GetKubernetesClusterResult", "tags");
            }
            this.tags = tags;
            return this;
        }
        public Builder tags(String... tags) {
            return tags(List.of(tags));
        }
        @CustomType.Setter
        public Builder targetNodesSize(String targetNodesSize) {
            if (targetNodesSize == null) {
              throw new MissingRequiredPropertyException("GetKubernetesClusterResult", "targetNodesSize");
            }
            this.targetNodesSize = targetNodesSize;
            return this;
        }
        public GetKubernetesClusterResult build() {
            final var _resultValue = new GetKubernetesClusterResult();
            _resultValue.apiEndpoint = apiEndpoint;
            _resultValue.applications = applications;
            _resultValue.cni = cni;
            _resultValue.createdAt = createdAt;
            _resultValue.dnsEntry = dnsEntry;
            _resultValue.id = id;
            _resultValue.installedApplications = installedApplications;
            _resultValue.kubeconfig = kubeconfig;
            _resultValue.kubernetesVersion = kubernetesVersion;
            _resultValue.masterIp = masterIp;
            _resultValue.name = name;
            _resultValue.numTargetNodes = numTargetNodes;
            _resultValue.pools = pools;
            _resultValue.ready = ready;
            _resultValue.region = region;
            _resultValue.status = status;
            _resultValue.tags = tags;
            _resultValue.targetNodesSize = targetNodesSize;
            return _resultValue;
        }
    }
}
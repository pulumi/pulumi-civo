// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.outputs;

import com.pulumi.civo.outputs.GetLoadBalancerBackend;
import com.pulumi.core.annotations.CustomType;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetLoadBalancerResult {
    /**
     * @return The algorithm used by the load balancer
     * 
     */
    private String algorithm;
    private List<GetLoadBalancerBackend> backends;
    /**
     * @return The cluster id of the load balancer
     * 
     */
    private String clusterId;
    /**
     * @return The enabled proxy protocol of the load balancer
     * 
     */
    private String enableProxyProtocol;
    /**
     * @return The external traffic policy of the load balancer
     * 
     */
    private String externalTrafficPolicy;
    /**
     * @return The firewall id of the load balancer
     * 
     */
    private String firewallId;
    /**
     * @return The id of the load balancer to retrieve (You can find this id from service annotations &#39;kubernetes.civo.com/loadbalancer-id&#39;)
     * 
     */
    private @Nullable String id;
    /**
     * @return The name of the load balancer (You can find this name from service annotations &#39;kubernetes.civo.com/loadbalancer-name&#39;)
     * 
     */
    private @Nullable String name;
    /**
     * @return The private ip of the load balancer
     * 
     */
    private String privateIp;
    /**
     * @return The public ip of the load balancer
     * 
     */
    private String publicIp;
    /**
     * @return The region of the load balancer, if you delcare this field, the datasource will use this value instead of the one defined in the provider
     * 
     */
    private @Nullable String region;
    /**
     * @return The session affinity of the load balancer
     * 
     */
    private String sessionAffinity;
    /**
     * @return The session affinity config timeout of the load balancer
     * 
     */
    private Integer sessionAffinityConfigTimeout;
    /**
     * @return The state of the load balancer
     * 
     */
    private String state;

    private GetLoadBalancerResult() {}
    /**
     * @return The algorithm used by the load balancer
     * 
     */
    public String algorithm() {
        return this.algorithm;
    }
    public List<GetLoadBalancerBackend> backends() {
        return this.backends;
    }
    /**
     * @return The cluster id of the load balancer
     * 
     */
    public String clusterId() {
        return this.clusterId;
    }
    /**
     * @return The enabled proxy protocol of the load balancer
     * 
     */
    public String enableProxyProtocol() {
        return this.enableProxyProtocol;
    }
    /**
     * @return The external traffic policy of the load balancer
     * 
     */
    public String externalTrafficPolicy() {
        return this.externalTrafficPolicy;
    }
    /**
     * @return The firewall id of the load balancer
     * 
     */
    public String firewallId() {
        return this.firewallId;
    }
    /**
     * @return The id of the load balancer to retrieve (You can find this id from service annotations &#39;kubernetes.civo.com/loadbalancer-id&#39;)
     * 
     */
    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }
    /**
     * @return The name of the load balancer (You can find this name from service annotations &#39;kubernetes.civo.com/loadbalancer-name&#39;)
     * 
     */
    public Optional<String> name() {
        return Optional.ofNullable(this.name);
    }
    /**
     * @return The private ip of the load balancer
     * 
     */
    public String privateIp() {
        return this.privateIp;
    }
    /**
     * @return The public ip of the load balancer
     * 
     */
    public String publicIp() {
        return this.publicIp;
    }
    /**
     * @return The region of the load balancer, if you delcare this field, the datasource will use this value instead of the one defined in the provider
     * 
     */
    public Optional<String> region() {
        return Optional.ofNullable(this.region);
    }
    /**
     * @return The session affinity of the load balancer
     * 
     */
    public String sessionAffinity() {
        return this.sessionAffinity;
    }
    /**
     * @return The session affinity config timeout of the load balancer
     * 
     */
    public Integer sessionAffinityConfigTimeout() {
        return this.sessionAffinityConfigTimeout;
    }
    /**
     * @return The state of the load balancer
     * 
     */
    public String state() {
        return this.state;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetLoadBalancerResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String algorithm;
        private List<GetLoadBalancerBackend> backends;
        private String clusterId;
        private String enableProxyProtocol;
        private String externalTrafficPolicy;
        private String firewallId;
        private @Nullable String id;
        private @Nullable String name;
        private String privateIp;
        private String publicIp;
        private @Nullable String region;
        private String sessionAffinity;
        private Integer sessionAffinityConfigTimeout;
        private String state;
        public Builder() {}
        public Builder(GetLoadBalancerResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.algorithm = defaults.algorithm;
    	      this.backends = defaults.backends;
    	      this.clusterId = defaults.clusterId;
    	      this.enableProxyProtocol = defaults.enableProxyProtocol;
    	      this.externalTrafficPolicy = defaults.externalTrafficPolicy;
    	      this.firewallId = defaults.firewallId;
    	      this.id = defaults.id;
    	      this.name = defaults.name;
    	      this.privateIp = defaults.privateIp;
    	      this.publicIp = defaults.publicIp;
    	      this.region = defaults.region;
    	      this.sessionAffinity = defaults.sessionAffinity;
    	      this.sessionAffinityConfigTimeout = defaults.sessionAffinityConfigTimeout;
    	      this.state = defaults.state;
        }

        @CustomType.Setter
        public Builder algorithm(String algorithm) {
            this.algorithm = Objects.requireNonNull(algorithm);
            return this;
        }
        @CustomType.Setter
        public Builder backends(List<GetLoadBalancerBackend> backends) {
            this.backends = Objects.requireNonNull(backends);
            return this;
        }
        public Builder backends(GetLoadBalancerBackend... backends) {
            return backends(List.of(backends));
        }
        @CustomType.Setter
        public Builder clusterId(String clusterId) {
            this.clusterId = Objects.requireNonNull(clusterId);
            return this;
        }
        @CustomType.Setter
        public Builder enableProxyProtocol(String enableProxyProtocol) {
            this.enableProxyProtocol = Objects.requireNonNull(enableProxyProtocol);
            return this;
        }
        @CustomType.Setter
        public Builder externalTrafficPolicy(String externalTrafficPolicy) {
            this.externalTrafficPolicy = Objects.requireNonNull(externalTrafficPolicy);
            return this;
        }
        @CustomType.Setter
        public Builder firewallId(String firewallId) {
            this.firewallId = Objects.requireNonNull(firewallId);
            return this;
        }
        @CustomType.Setter
        public Builder id(@Nullable String id) {
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder name(@Nullable String name) {
            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder privateIp(String privateIp) {
            this.privateIp = Objects.requireNonNull(privateIp);
            return this;
        }
        @CustomType.Setter
        public Builder publicIp(String publicIp) {
            this.publicIp = Objects.requireNonNull(publicIp);
            return this;
        }
        @CustomType.Setter
        public Builder region(@Nullable String region) {
            this.region = region;
            return this;
        }
        @CustomType.Setter
        public Builder sessionAffinity(String sessionAffinity) {
            this.sessionAffinity = Objects.requireNonNull(sessionAffinity);
            return this;
        }
        @CustomType.Setter
        public Builder sessionAffinityConfigTimeout(Integer sessionAffinityConfigTimeout) {
            this.sessionAffinityConfigTimeout = Objects.requireNonNull(sessionAffinityConfigTimeout);
            return this;
        }
        @CustomType.Setter
        public Builder state(String state) {
            this.state = Objects.requireNonNull(state);
            return this;
        }
        public GetLoadBalancerResult build() {
            final var o = new GetLoadBalancerResult();
            o.algorithm = algorithm;
            o.backends = backends;
            o.clusterId = clusterId;
            o.enableProxyProtocol = enableProxyProtocol;
            o.externalTrafficPolicy = externalTrafficPolicy;
            o.firewallId = firewallId;
            o.id = id;
            o.name = name;
            o.privateIp = privateIp;
            o.publicIp = publicIp;
            o.region = region;
            o.sessionAffinity = sessionAffinity;
            o.sessionAffinityConfigTimeout = sessionAffinityConfigTimeout;
            o.state = state;
            return o;
        }
    }
}

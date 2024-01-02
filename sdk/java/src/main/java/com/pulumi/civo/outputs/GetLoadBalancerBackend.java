// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetLoadBalancerBackend {
    private Integer healthCheckPort;
    private String ip;
    private String protocol;
    private Integer sourcePort;
    private Integer targetPort;

    private GetLoadBalancerBackend() {}
    public Integer healthCheckPort() {
        return this.healthCheckPort;
    }
    public String ip() {
        return this.ip;
    }
    public String protocol() {
        return this.protocol;
    }
    public Integer sourcePort() {
        return this.sourcePort;
    }
    public Integer targetPort() {
        return this.targetPort;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetLoadBalancerBackend defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private Integer healthCheckPort;
        private String ip;
        private String protocol;
        private Integer sourcePort;
        private Integer targetPort;
        public Builder() {}
        public Builder(GetLoadBalancerBackend defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.healthCheckPort = defaults.healthCheckPort;
    	      this.ip = defaults.ip;
    	      this.protocol = defaults.protocol;
    	      this.sourcePort = defaults.sourcePort;
    	      this.targetPort = defaults.targetPort;
        }

        @CustomType.Setter
        public Builder healthCheckPort(Integer healthCheckPort) {
            if (healthCheckPort == null) {
              throw new MissingRequiredPropertyException("GetLoadBalancerBackend", "healthCheckPort");
            }
            this.healthCheckPort = healthCheckPort;
            return this;
        }
        @CustomType.Setter
        public Builder ip(String ip) {
            if (ip == null) {
              throw new MissingRequiredPropertyException("GetLoadBalancerBackend", "ip");
            }
            this.ip = ip;
            return this;
        }
        @CustomType.Setter
        public Builder protocol(String protocol) {
            if (protocol == null) {
              throw new MissingRequiredPropertyException("GetLoadBalancerBackend", "protocol");
            }
            this.protocol = protocol;
            return this;
        }
        @CustomType.Setter
        public Builder sourcePort(Integer sourcePort) {
            if (sourcePort == null) {
              throw new MissingRequiredPropertyException("GetLoadBalancerBackend", "sourcePort");
            }
            this.sourcePort = sourcePort;
            return this;
        }
        @CustomType.Setter
        public Builder targetPort(Integer targetPort) {
            if (targetPort == null) {
              throw new MissingRequiredPropertyException("GetLoadBalancerBackend", "targetPort");
            }
            this.targetPort = targetPort;
            return this;
        }
        public GetLoadBalancerBackend build() {
            final var _resultValue = new GetLoadBalancerBackend();
            _resultValue.healthCheckPort = healthCheckPort;
            _resultValue.ip = ip;
            _resultValue.protocol = protocol;
            _resultValue.sourcePort = sourcePort;
            _resultValue.targetPort = targetPort;
            return _resultValue;
        }
    }
}

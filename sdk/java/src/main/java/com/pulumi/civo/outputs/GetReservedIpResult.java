// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetReservedIpResult {
    /**
     * @return ID for the ip address
     * 
     */
    private @Nullable String id;
    /**
     * @return The ID of the instance the IP is attached to
     * 
     */
    private String instanceId;
    /**
     * @return The name of the instance the IP is attached to
     * 
     */
    private String instanceName;
    /**
     * @return The IP Address requested
     * 
     */
    private String ip;
    /**
     * @return Name for the ip address
     * 
     */
    private @Nullable String name;
    /**
     * @return The region the ip address is in
     * 
     */
    private String region;

    private GetReservedIpResult() {}
    /**
     * @return ID for the ip address
     * 
     */
    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }
    /**
     * @return The ID of the instance the IP is attached to
     * 
     */
    public String instanceId() {
        return this.instanceId;
    }
    /**
     * @return The name of the instance the IP is attached to
     * 
     */
    public String instanceName() {
        return this.instanceName;
    }
    /**
     * @return The IP Address requested
     * 
     */
    public String ip() {
        return this.ip;
    }
    /**
     * @return Name for the ip address
     * 
     */
    public Optional<String> name() {
        return Optional.ofNullable(this.name);
    }
    /**
     * @return The region the ip address is in
     * 
     */
    public String region() {
        return this.region;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetReservedIpResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable String id;
        private String instanceId;
        private String instanceName;
        private String ip;
        private @Nullable String name;
        private String region;
        public Builder() {}
        public Builder(GetReservedIpResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.id = defaults.id;
    	      this.instanceId = defaults.instanceId;
    	      this.instanceName = defaults.instanceName;
    	      this.ip = defaults.ip;
    	      this.name = defaults.name;
    	      this.region = defaults.region;
        }

        @CustomType.Setter
        public Builder id(@Nullable String id) {

            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder instanceId(String instanceId) {
            if (instanceId == null) {
              throw new MissingRequiredPropertyException("GetReservedIpResult", "instanceId");
            }
            this.instanceId = instanceId;
            return this;
        }
        @CustomType.Setter
        public Builder instanceName(String instanceName) {
            if (instanceName == null) {
              throw new MissingRequiredPropertyException("GetReservedIpResult", "instanceName");
            }
            this.instanceName = instanceName;
            return this;
        }
        @CustomType.Setter
        public Builder ip(String ip) {
            if (ip == null) {
              throw new MissingRequiredPropertyException("GetReservedIpResult", "ip");
            }
            this.ip = ip;
            return this;
        }
        @CustomType.Setter
        public Builder name(@Nullable String name) {

            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder region(String region) {
            if (region == null) {
              throw new MissingRequiredPropertyException("GetReservedIpResult", "region");
            }
            this.region = region;
            return this;
        }
        public GetReservedIpResult build() {
            final var _resultValue = new GetReservedIpResult();
            _resultValue.id = id;
            _resultValue.instanceId = instanceId;
            _resultValue.instanceName = instanceName;
            _resultValue.ip = ip;
            _resultValue.name = name;
            _resultValue.region = region;
            return _resultValue;
        }
    }
}
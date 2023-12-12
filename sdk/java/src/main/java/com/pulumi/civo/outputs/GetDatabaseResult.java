// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetDatabaseResult {
    /**
     * @return The DNS endpoint of the database
     * 
     */
    private String dnsEndpoint;
    /**
     * @return The endpoint of the database
     * 
     */
    private String endpoint;
    /**
     * @return The engine of the database
     * 
     */
    private String engine;
    /**
     * @return The firewall id of the Database
     * 
     */
    private String firewallId;
    /**
     * @return The ID of the Database
     * 
     */
    private @Nullable String id;
    /**
     * @return The name of the Database
     * 
     */
    private @Nullable String name;
    /**
     * @return The network id of the Database
     * 
     */
    private String networkId;
    /**
     * @return Count of nodes
     * 
     */
    private Integer nodes;
    /**
     * @return The password of the database
     * 
     */
    private String password;
    /**
     * @return The port of the database
     * 
     */
    private Integer port;
    /**
     * @return The region of an existing Database
     * 
     */
    private String region;
    /**
     * @return Size of the database
     * 
     */
    private String size;
    /**
     * @return The status of the database
     * 
     */
    private String status;
    /**
     * @return The username of the database
     * 
     */
    private String username;
    /**
     * @return The version of the database
     * 
     */
    private String version;

    private GetDatabaseResult() {}
    /**
     * @return The DNS endpoint of the database
     * 
     */
    public String dnsEndpoint() {
        return this.dnsEndpoint;
    }
    /**
     * @return The endpoint of the database
     * 
     */
    public String endpoint() {
        return this.endpoint;
    }
    /**
     * @return The engine of the database
     * 
     */
    public String engine() {
        return this.engine;
    }
    /**
     * @return The firewall id of the Database
     * 
     */
    public String firewallId() {
        return this.firewallId;
    }
    /**
     * @return The ID of the Database
     * 
     */
    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }
    /**
     * @return The name of the Database
     * 
     */
    public Optional<String> name() {
        return Optional.ofNullable(this.name);
    }
    /**
     * @return The network id of the Database
     * 
     */
    public String networkId() {
        return this.networkId;
    }
    /**
     * @return Count of nodes
     * 
     */
    public Integer nodes() {
        return this.nodes;
    }
    /**
     * @return The password of the database
     * 
     */
    public String password() {
        return this.password;
    }
    /**
     * @return The port of the database
     * 
     */
    public Integer port() {
        return this.port;
    }
    /**
     * @return The region of an existing Database
     * 
     */
    public String region() {
        return this.region;
    }
    /**
     * @return Size of the database
     * 
     */
    public String size() {
        return this.size;
    }
    /**
     * @return The status of the database
     * 
     */
    public String status() {
        return this.status;
    }
    /**
     * @return The username of the database
     * 
     */
    public String username() {
        return this.username;
    }
    /**
     * @return The version of the database
     * 
     */
    public String version() {
        return this.version;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetDatabaseResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String dnsEndpoint;
        private String endpoint;
        private String engine;
        private String firewallId;
        private @Nullable String id;
        private @Nullable String name;
        private String networkId;
        private Integer nodes;
        private String password;
        private Integer port;
        private String region;
        private String size;
        private String status;
        private String username;
        private String version;
        public Builder() {}
        public Builder(GetDatabaseResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.dnsEndpoint = defaults.dnsEndpoint;
    	      this.endpoint = defaults.endpoint;
    	      this.engine = defaults.engine;
    	      this.firewallId = defaults.firewallId;
    	      this.id = defaults.id;
    	      this.name = defaults.name;
    	      this.networkId = defaults.networkId;
    	      this.nodes = defaults.nodes;
    	      this.password = defaults.password;
    	      this.port = defaults.port;
    	      this.region = defaults.region;
    	      this.size = defaults.size;
    	      this.status = defaults.status;
    	      this.username = defaults.username;
    	      this.version = defaults.version;
        }

        @CustomType.Setter
        public Builder dnsEndpoint(String dnsEndpoint) {
            this.dnsEndpoint = Objects.requireNonNull(dnsEndpoint);
            return this;
        }
        @CustomType.Setter
        public Builder endpoint(String endpoint) {
            this.endpoint = Objects.requireNonNull(endpoint);
            return this;
        }
        @CustomType.Setter
        public Builder engine(String engine) {
            this.engine = Objects.requireNonNull(engine);
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
        public Builder networkId(String networkId) {
            this.networkId = Objects.requireNonNull(networkId);
            return this;
        }
        @CustomType.Setter
        public Builder nodes(Integer nodes) {
            this.nodes = Objects.requireNonNull(nodes);
            return this;
        }
        @CustomType.Setter
        public Builder password(String password) {
            this.password = Objects.requireNonNull(password);
            return this;
        }
        @CustomType.Setter
        public Builder port(Integer port) {
            this.port = Objects.requireNonNull(port);
            return this;
        }
        @CustomType.Setter
        public Builder region(String region) {
            this.region = Objects.requireNonNull(region);
            return this;
        }
        @CustomType.Setter
        public Builder size(String size) {
            this.size = Objects.requireNonNull(size);
            return this;
        }
        @CustomType.Setter
        public Builder status(String status) {
            this.status = Objects.requireNonNull(status);
            return this;
        }
        @CustomType.Setter
        public Builder username(String username) {
            this.username = Objects.requireNonNull(username);
            return this;
        }
        @CustomType.Setter
        public Builder version(String version) {
            this.version = Objects.requireNonNull(version);
            return this;
        }
        public GetDatabaseResult build() {
            final var _resultValue = new GetDatabaseResult();
            _resultValue.dnsEndpoint = dnsEndpoint;
            _resultValue.endpoint = endpoint;
            _resultValue.engine = engine;
            _resultValue.firewallId = firewallId;
            _resultValue.id = id;
            _resultValue.name = name;
            _resultValue.networkId = networkId;
            _resultValue.nodes = nodes;
            _resultValue.password = password;
            _resultValue.port = port;
            _resultValue.region = region;
            _resultValue.size = size;
            _resultValue.status = status;
            _resultValue.username = username;
            _resultValue.version = version;
            return _resultValue;
        }
    }
}

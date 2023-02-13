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

    private GetDatabaseResult() {}
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

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetDatabaseResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String firewallId;
        private @Nullable String id;
        private @Nullable String name;
        private String networkId;
        private Integer nodes;
        private String password;
        private String region;
        private String size;
        private String status;
        private String username;
        public Builder() {}
        public Builder(GetDatabaseResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.firewallId = defaults.firewallId;
    	      this.id = defaults.id;
    	      this.name = defaults.name;
    	      this.networkId = defaults.networkId;
    	      this.nodes = defaults.nodes;
    	      this.password = defaults.password;
    	      this.region = defaults.region;
    	      this.size = defaults.size;
    	      this.status = defaults.status;
    	      this.username = defaults.username;
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
        public GetDatabaseResult build() {
            final var o = new GetDatabaseResult();
            o.firewallId = firewallId;
            o.id = id;
            o.name = name;
            o.networkId = networkId;
            o.nodes = nodes;
            o.password = password;
            o.region = region;
            o.size = size;
            o.status = status;
            o.username = username;
            return o;
        }
    }
}

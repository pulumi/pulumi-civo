// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class DatabaseState extends com.pulumi.resources.ResourceArgs {

    public static final DatabaseState Empty = new DatabaseState();

    /**
     * The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all)
     * 
     */
    @Import(name="firewallId")
    private @Nullable Output<String> firewallId;

    /**
     * @return The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all)
     * 
     */
    public Optional<Output<String>> firewallId() {
        return Optional.ofNullable(this.firewallId);
    }

    /**
     * Name of the database
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return Name of the database
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * The id of the associated network
     * 
     */
    @Import(name="networkId")
    private @Nullable Output<String> networkId;

    /**
     * @return The id of the associated network
     * 
     */
    public Optional<Output<String>> networkId() {
        return Optional.ofNullable(this.networkId);
    }

    /**
     * Count of nodes
     * 
     */
    @Import(name="nodes")
    private @Nullable Output<Integer> nodes;

    /**
     * @return Count of nodes
     * 
     */
    public Optional<Output<Integer>> nodes() {
        return Optional.ofNullable(this.nodes);
    }

    /**
     * The password of the database
     * 
     */
    @Import(name="password")
    private @Nullable Output<String> password;

    /**
     * @return The password of the database
     * 
     */
    public Optional<Output<String>> password() {
        return Optional.ofNullable(this.password);
    }

    /**
     * The region where the database will be created.
     * 
     */
    @Import(name="region")
    private @Nullable Output<String> region;

    /**
     * @return The region where the database will be created.
     * 
     */
    public Optional<Output<String>> region() {
        return Optional.ofNullable(this.region);
    }

    /**
     * Size of the database
     * 
     */
    @Import(name="size")
    private @Nullable Output<String> size;

    /**
     * @return Size of the database
     * 
     */
    public Optional<Output<String>> size() {
        return Optional.ofNullable(this.size);
    }

    /**
     * The status of the database
     * 
     */
    @Import(name="status")
    private @Nullable Output<String> status;

    /**
     * @return The status of the database
     * 
     */
    public Optional<Output<String>> status() {
        return Optional.ofNullable(this.status);
    }

    /**
     * The username of the database
     * 
     */
    @Import(name="username")
    private @Nullable Output<String> username;

    /**
     * @return The username of the database
     * 
     */
    public Optional<Output<String>> username() {
        return Optional.ofNullable(this.username);
    }

    private DatabaseState() {}

    private DatabaseState(DatabaseState $) {
        this.firewallId = $.firewallId;
        this.name = $.name;
        this.networkId = $.networkId;
        this.nodes = $.nodes;
        this.password = $.password;
        this.region = $.region;
        this.size = $.size;
        this.status = $.status;
        this.username = $.username;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(DatabaseState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private DatabaseState $;

        public Builder() {
            $ = new DatabaseState();
        }

        public Builder(DatabaseState defaults) {
            $ = new DatabaseState(Objects.requireNonNull(defaults));
        }

        /**
         * @param firewallId The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all)
         * 
         * @return builder
         * 
         */
        public Builder firewallId(@Nullable Output<String> firewallId) {
            $.firewallId = firewallId;
            return this;
        }

        /**
         * @param firewallId The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all)
         * 
         * @return builder
         * 
         */
        public Builder firewallId(String firewallId) {
            return firewallId(Output.of(firewallId));
        }

        /**
         * @param name Name of the database
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name Name of the database
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param networkId The id of the associated network
         * 
         * @return builder
         * 
         */
        public Builder networkId(@Nullable Output<String> networkId) {
            $.networkId = networkId;
            return this;
        }

        /**
         * @param networkId The id of the associated network
         * 
         * @return builder
         * 
         */
        public Builder networkId(String networkId) {
            return networkId(Output.of(networkId));
        }

        /**
         * @param nodes Count of nodes
         * 
         * @return builder
         * 
         */
        public Builder nodes(@Nullable Output<Integer> nodes) {
            $.nodes = nodes;
            return this;
        }

        /**
         * @param nodes Count of nodes
         * 
         * @return builder
         * 
         */
        public Builder nodes(Integer nodes) {
            return nodes(Output.of(nodes));
        }

        /**
         * @param password The password of the database
         * 
         * @return builder
         * 
         */
        public Builder password(@Nullable Output<String> password) {
            $.password = password;
            return this;
        }

        /**
         * @param password The password of the database
         * 
         * @return builder
         * 
         */
        public Builder password(String password) {
            return password(Output.of(password));
        }

        /**
         * @param region The region where the database will be created.
         * 
         * @return builder
         * 
         */
        public Builder region(@Nullable Output<String> region) {
            $.region = region;
            return this;
        }

        /**
         * @param region The region where the database will be created.
         * 
         * @return builder
         * 
         */
        public Builder region(String region) {
            return region(Output.of(region));
        }

        /**
         * @param size Size of the database
         * 
         * @return builder
         * 
         */
        public Builder size(@Nullable Output<String> size) {
            $.size = size;
            return this;
        }

        /**
         * @param size Size of the database
         * 
         * @return builder
         * 
         */
        public Builder size(String size) {
            return size(Output.of(size));
        }

        /**
         * @param status The status of the database
         * 
         * @return builder
         * 
         */
        public Builder status(@Nullable Output<String> status) {
            $.status = status;
            return this;
        }

        /**
         * @param status The status of the database
         * 
         * @return builder
         * 
         */
        public Builder status(String status) {
            return status(Output.of(status));
        }

        /**
         * @param username The username of the database
         * 
         * @return builder
         * 
         */
        public Builder username(@Nullable Output<String> username) {
            $.username = username;
            return this;
        }

        /**
         * @param username The username of the database
         * 
         * @return builder
         * 
         */
        public Builder username(String username) {
            return username(Output.of(username));
        }

        public DatabaseState build() {
            return $;
        }
    }

}

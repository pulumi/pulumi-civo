// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class DatabaseArgs extends com.pulumi.resources.ResourceArgs {

    public static final DatabaseArgs Empty = new DatabaseArgs();

    /**
     * The engine of the database
     * 
     */
    @Import(name="engine", required=true)
    private Output<String> engine;

    /**
     * @return The engine of the database
     * 
     */
    public Output<String> engine() {
        return this.engine;
    }

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
    @Import(name="nodes", required=true)
    private Output<Integer> nodes;

    /**
     * @return Count of nodes
     * 
     */
    public Output<Integer> nodes() {
        return this.nodes;
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
    @Import(name="size", required=true)
    private Output<String> size;

    /**
     * @return Size of the database
     * 
     */
    public Output<String> size() {
        return this.size;
    }

    /**
     * The version of the database
     * 
     */
    @Import(name="version", required=true)
    private Output<String> version;

    /**
     * @return The version of the database
     * 
     */
    public Output<String> version() {
        return this.version;
    }

    private DatabaseArgs() {}

    private DatabaseArgs(DatabaseArgs $) {
        this.engine = $.engine;
        this.firewallId = $.firewallId;
        this.name = $.name;
        this.networkId = $.networkId;
        this.nodes = $.nodes;
        this.region = $.region;
        this.size = $.size;
        this.version = $.version;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(DatabaseArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private DatabaseArgs $;

        public Builder() {
            $ = new DatabaseArgs();
        }

        public Builder(DatabaseArgs defaults) {
            $ = new DatabaseArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param engine The engine of the database
         * 
         * @return builder
         * 
         */
        public Builder engine(Output<String> engine) {
            $.engine = engine;
            return this;
        }

        /**
         * @param engine The engine of the database
         * 
         * @return builder
         * 
         */
        public Builder engine(String engine) {
            return engine(Output.of(engine));
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
        public Builder nodes(Output<Integer> nodes) {
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
        public Builder size(Output<String> size) {
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
         * @param version The version of the database
         * 
         * @return builder
         * 
         */
        public Builder version(Output<String> version) {
            $.version = version;
            return this;
        }

        /**
         * @param version The version of the database
         * 
         * @return builder
         * 
         */
        public Builder version(String version) {
            return version(Output.of(version));
        }

        public DatabaseArgs build() {
            if ($.engine == null) {
                throw new MissingRequiredPropertyException("DatabaseArgs", "engine");
            }
            if ($.nodes == null) {
                throw new MissingRequiredPropertyException("DatabaseArgs", "nodes");
            }
            if ($.size == null) {
                throw new MissingRequiredPropertyException("DatabaseArgs", "size");
            }
            if ($.version == null) {
                throw new MissingRequiredPropertyException("DatabaseArgs", "version");
            }
            return $;
        }
    }

}

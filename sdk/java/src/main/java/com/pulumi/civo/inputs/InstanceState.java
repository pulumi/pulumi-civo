// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class InstanceState extends com.pulumi.resources.ResourceArgs {

    public static final InstanceState Empty = new InstanceState();

    /**
     * (Number) Instance&#39;s CPU cores
     * 
     */
    @Import(name="cpuCores")
    private @Nullable Output<Integer> cpuCores;

    /**
     * @return (Number) Instance&#39;s CPU cores
     * 
     */
    public Optional<Output<Integer>> cpuCores() {
        return Optional.ofNullable(this.cpuCores);
    }

    /**
     * (String) Timestamp when the instance was created
     * 
     */
    @Import(name="createdAt")
    private @Nullable Output<String> createdAt;

    /**
     * @return (String) Timestamp when the instance was created
     * 
     */
    public Optional<Output<String>> createdAt() {
        return Optional.ofNullable(this.createdAt);
    }

    /**
     * (Number) Instance&#39;s disk (GB)
     * 
     */
    @Import(name="diskGb")
    private @Nullable Output<Integer> diskGb;

    /**
     * @return (Number) Instance&#39;s disk (GB)
     * 
     */
    public Optional<Output<Integer>> diskGb() {
        return Optional.ofNullable(this.diskGb);
    }

    /**
     * The ID for the disk image to use to build the instance
     * 
     */
    @Import(name="diskImage")
    private @Nullable Output<String> diskImage;

    /**
     * @return The ID for the disk image to use to build the instance
     * 
     */
    public Optional<Output<String>> diskImage() {
        return Optional.ofNullable(this.diskImage);
    }

    /**
     * The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open
     * to all)
     * 
     */
    @Import(name="firewallId")
    private @Nullable Output<String> firewallId;

    /**
     * @return The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open
     * to all)
     * 
     */
    public Optional<Output<String>> firewallId() {
        return Optional.ofNullable(this.firewallId);
    }

    /**
     * A fully qualified domain name that should be set as the instance&#39;s hostname
     * 
     */
    @Import(name="hostname")
    private @Nullable Output<String> hostname;

    /**
     * @return A fully qualified domain name that should be set as the instance&#39;s hostname
     * 
     */
    public Optional<Output<String>> hostname() {
        return Optional.ofNullable(this.hostname);
    }

    /**
     * (String, Sensitive) Initial password for login
     * 
     */
    @Import(name="initialPassword")
    private @Nullable Output<String> initialPassword;

    /**
     * @return (String, Sensitive) Initial password for login
     * 
     */
    public Optional<Output<String>> initialPassword() {
        return Optional.ofNullable(this.initialPassword);
    }

    /**
     * The name of the initial user created on the server (optional; this will default to the template&#39;s default_username and
     * fallback to civo)
     * 
     */
    @Import(name="initialUser")
    private @Nullable Output<String> initialUser;

    /**
     * @return The name of the initial user created on the server (optional; this will default to the template&#39;s default_username and
     * fallback to civo)
     * 
     */
    public Optional<Output<String>> initialUser() {
        return Optional.ofNullable(this.initialUser);
    }

    /**
     * This must be the ID of the network from the network listing (optional; default network used when not specified)
     * 
     */
    @Import(name="networkId")
    private @Nullable Output<String> networkId;

    /**
     * @return This must be the ID of the network from the network listing (optional; default network used when not specified)
     * 
     */
    public Optional<Output<String>> networkId() {
        return Optional.ofNullable(this.networkId);
    }

    /**
     * Add some notes to the instance
     * 
     */
    @Import(name="notes")
    private @Nullable Output<String> notes;

    /**
     * @return Add some notes to the instance
     * 
     */
    public Optional<Output<String>> notes() {
        return Optional.ofNullable(this.notes);
    }

    /**
     * (String) Instance&#39;s private IP address
     * 
     */
    @Import(name="privateIp")
    private @Nullable Output<String> privateIp;

    /**
     * @return (String) Instance&#39;s private IP address
     * 
     */
    public Optional<Output<String>> privateIp() {
        return Optional.ofNullable(this.privateIp);
    }

    /**
     * The private IPv4 address for the instance (optional)
     * 
     */
    @Import(name="privateIpv4")
    private @Nullable Output<String> privateIpv4;

    /**
     * @return The private IPv4 address for the instance (optional)
     * 
     */
    public Optional<Output<String>> privateIpv4() {
        return Optional.ofNullable(this.privateIpv4);
    }

    /**
     * (String) Instance&#39;s public IP address
     * 
     */
    @Import(name="publicIp")
    private @Nullable Output<String> publicIp;

    /**
     * @return (String) Instance&#39;s public IP address
     * 
     */
    public Optional<Output<String>> publicIp() {
        return Optional.ofNullable(this.publicIp);
    }

    /**
     * This should be either &#39;none&#39; or &#39;create&#39; (default: &#39;create&#39;)
     * 
     */
    @Import(name="publicIpRequired")
    private @Nullable Output<String> publicIpRequired;

    /**
     * @return This should be either &#39;none&#39; or &#39;create&#39; (default: &#39;create&#39;)
     * 
     */
    public Optional<Output<String>> publicIpRequired() {
        return Optional.ofNullable(this.publicIpRequired);
    }

    /**
     * (Number) Instance&#39;s RAM (MB)
     * 
     */
    @Import(name="ramMb")
    private @Nullable Output<Integer> ramMb;

    /**
     * @return (Number) Instance&#39;s RAM (MB)
     * 
     */
    public Optional<Output<Integer>> ramMb() {
        return Optional.ofNullable(this.ramMb);
    }

    /**
     * The region for the instance, if not declare we use the region in declared in the provider
     * 
     */
    @Import(name="region")
    private @Nullable Output<String> region;

    /**
     * @return The region for the instance, if not declare we use the region in declared in the provider
     * 
     */
    public Optional<Output<String>> region() {
        return Optional.ofNullable(this.region);
    }

    /**
     * Can be either the UUID, name, or the IP address of the reserved IP
     * 
     */
    @Import(name="reservedIpv4")
    private @Nullable Output<String> reservedIpv4;

    /**
     * @return Can be either the UUID, name, or the IP address of the reserved IP
     * 
     */
    public Optional<Output<String>> reservedIpv4() {
        return Optional.ofNullable(this.reservedIpv4);
    }

    /**
     * A fully qualified domain name that should be used as the instance&#39;s IP&#39;s reverse DNS (optional, uses the hostname if
     * unspecified)
     * 
     */
    @Import(name="reverseDns")
    private @Nullable Output<String> reverseDns;

    /**
     * @return A fully qualified domain name that should be used as the instance&#39;s IP&#39;s reverse DNS (optional, uses the hostname if
     * unspecified)
     * 
     */
    public Optional<Output<String>> reverseDns() {
        return Optional.ofNullable(this.reverseDns);
    }

    /**
     * The contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance,
     * read/write/executable only by root and then will be executed at the end of the cloud initialization
     * 
     */
    @Import(name="script")
    private @Nullable Output<String> script;

    /**
     * @return The contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance,
     * read/write/executable only by root and then will be executed at the end of the cloud initialization
     * 
     */
    public Optional<Output<String>> script() {
        return Optional.ofNullable(this.script);
    }

    /**
     * The name of the size, from the current list, e.g. g3.xsmall
     * 
     */
    @Import(name="size")
    private @Nullable Output<String> size;

    /**
     * @return The name of the size, from the current list, e.g. g3.xsmall
     * 
     */
    public Optional<Output<String>> size() {
        return Optional.ofNullable(this.size);
    }

    /**
     * (String) Instance&#39;s source ID
     * 
     */
    @Import(name="sourceId")
    private @Nullable Output<String> sourceId;

    /**
     * @return (String) Instance&#39;s source ID
     * 
     */
    public Optional<Output<String>> sourceId() {
        return Optional.ofNullable(this.sourceId);
    }

    /**
     * (String) Instance&#39;s source type
     * 
     */
    @Import(name="sourceType")
    private @Nullable Output<String> sourceType;

    /**
     * @return (String) Instance&#39;s source type
     * 
     */
    public Optional<Output<String>> sourceType() {
        return Optional.ofNullable(this.sourceType);
    }

    /**
     * The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn&#39;t provided a
     * random password will be set and returned in the initial_password field)
     * 
     */
    @Import(name="sshkeyId")
    private @Nullable Output<String> sshkeyId;

    /**
     * @return The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn&#39;t provided a
     * random password will be set and returned in the initial_password field)
     * 
     */
    public Optional<Output<String>> sshkeyId() {
        return Optional.ofNullable(this.sshkeyId);
    }

    /**
     * (String) Instance&#39;s status
     * 
     */
    @Import(name="status")
    private @Nullable Output<String> status;

    /**
     * @return (String) Instance&#39;s status
     * 
     */
    public Optional<Output<String>> status() {
        return Optional.ofNullable(this.status);
    }

    /**
     * An optional list of tags, represented as a key, value pair
     * 
     */
    @Import(name="tags")
    private @Nullable Output<List<String>> tags;

    /**
     * @return An optional list of tags, represented as a key, value pair
     * 
     */
    public Optional<Output<List<String>>> tags() {
        return Optional.ofNullable(this.tags);
    }

    /**
     * The type of volume to use, either &#39;ssd&#39; or &#39;bssd&#39; (optional; default &#39;ssd&#39;)
     * 
     */
    @Import(name="volumeType")
    private @Nullable Output<String> volumeType;

    /**
     * @return The type of volume to use, either &#39;ssd&#39; or &#39;bssd&#39; (optional; default &#39;ssd&#39;)
     * 
     */
    public Optional<Output<String>> volumeType() {
        return Optional.ofNullable(this.volumeType);
    }

    @Import(name="writePassword")
    private @Nullable Output<Boolean> writePassword;

    public Optional<Output<Boolean>> writePassword() {
        return Optional.ofNullable(this.writePassword);
    }

    private InstanceState() {}

    private InstanceState(InstanceState $) {
        this.cpuCores = $.cpuCores;
        this.createdAt = $.createdAt;
        this.diskGb = $.diskGb;
        this.diskImage = $.diskImage;
        this.firewallId = $.firewallId;
        this.hostname = $.hostname;
        this.initialPassword = $.initialPassword;
        this.initialUser = $.initialUser;
        this.networkId = $.networkId;
        this.notes = $.notes;
        this.privateIp = $.privateIp;
        this.privateIpv4 = $.privateIpv4;
        this.publicIp = $.publicIp;
        this.publicIpRequired = $.publicIpRequired;
        this.ramMb = $.ramMb;
        this.region = $.region;
        this.reservedIpv4 = $.reservedIpv4;
        this.reverseDns = $.reverseDns;
        this.script = $.script;
        this.size = $.size;
        this.sourceId = $.sourceId;
        this.sourceType = $.sourceType;
        this.sshkeyId = $.sshkeyId;
        this.status = $.status;
        this.tags = $.tags;
        this.volumeType = $.volumeType;
        this.writePassword = $.writePassword;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(InstanceState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private InstanceState $;

        public Builder() {
            $ = new InstanceState();
        }

        public Builder(InstanceState defaults) {
            $ = new InstanceState(Objects.requireNonNull(defaults));
        }

        /**
         * @param cpuCores (Number) Instance&#39;s CPU cores
         * 
         * @return builder
         * 
         */
        public Builder cpuCores(@Nullable Output<Integer> cpuCores) {
            $.cpuCores = cpuCores;
            return this;
        }

        /**
         * @param cpuCores (Number) Instance&#39;s CPU cores
         * 
         * @return builder
         * 
         */
        public Builder cpuCores(Integer cpuCores) {
            return cpuCores(Output.of(cpuCores));
        }

        /**
         * @param createdAt (String) Timestamp when the instance was created
         * 
         * @return builder
         * 
         */
        public Builder createdAt(@Nullable Output<String> createdAt) {
            $.createdAt = createdAt;
            return this;
        }

        /**
         * @param createdAt (String) Timestamp when the instance was created
         * 
         * @return builder
         * 
         */
        public Builder createdAt(String createdAt) {
            return createdAt(Output.of(createdAt));
        }

        /**
         * @param diskGb (Number) Instance&#39;s disk (GB)
         * 
         * @return builder
         * 
         */
        public Builder diskGb(@Nullable Output<Integer> diskGb) {
            $.diskGb = diskGb;
            return this;
        }

        /**
         * @param diskGb (Number) Instance&#39;s disk (GB)
         * 
         * @return builder
         * 
         */
        public Builder diskGb(Integer diskGb) {
            return diskGb(Output.of(diskGb));
        }

        /**
         * @param diskImage The ID for the disk image to use to build the instance
         * 
         * @return builder
         * 
         */
        public Builder diskImage(@Nullable Output<String> diskImage) {
            $.diskImage = diskImage;
            return this;
        }

        /**
         * @param diskImage The ID for the disk image to use to build the instance
         * 
         * @return builder
         * 
         */
        public Builder diskImage(String diskImage) {
            return diskImage(Output.of(diskImage));
        }

        /**
         * @param firewallId The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open
         * to all)
         * 
         * @return builder
         * 
         */
        public Builder firewallId(@Nullable Output<String> firewallId) {
            $.firewallId = firewallId;
            return this;
        }

        /**
         * @param firewallId The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open
         * to all)
         * 
         * @return builder
         * 
         */
        public Builder firewallId(String firewallId) {
            return firewallId(Output.of(firewallId));
        }

        /**
         * @param hostname A fully qualified domain name that should be set as the instance&#39;s hostname
         * 
         * @return builder
         * 
         */
        public Builder hostname(@Nullable Output<String> hostname) {
            $.hostname = hostname;
            return this;
        }

        /**
         * @param hostname A fully qualified domain name that should be set as the instance&#39;s hostname
         * 
         * @return builder
         * 
         */
        public Builder hostname(String hostname) {
            return hostname(Output.of(hostname));
        }

        /**
         * @param initialPassword (String, Sensitive) Initial password for login
         * 
         * @return builder
         * 
         */
        public Builder initialPassword(@Nullable Output<String> initialPassword) {
            $.initialPassword = initialPassword;
            return this;
        }

        /**
         * @param initialPassword (String, Sensitive) Initial password for login
         * 
         * @return builder
         * 
         */
        public Builder initialPassword(String initialPassword) {
            return initialPassword(Output.of(initialPassword));
        }

        /**
         * @param initialUser The name of the initial user created on the server (optional; this will default to the template&#39;s default_username and
         * fallback to civo)
         * 
         * @return builder
         * 
         */
        public Builder initialUser(@Nullable Output<String> initialUser) {
            $.initialUser = initialUser;
            return this;
        }

        /**
         * @param initialUser The name of the initial user created on the server (optional; this will default to the template&#39;s default_username and
         * fallback to civo)
         * 
         * @return builder
         * 
         */
        public Builder initialUser(String initialUser) {
            return initialUser(Output.of(initialUser));
        }

        /**
         * @param networkId This must be the ID of the network from the network listing (optional; default network used when not specified)
         * 
         * @return builder
         * 
         */
        public Builder networkId(@Nullable Output<String> networkId) {
            $.networkId = networkId;
            return this;
        }

        /**
         * @param networkId This must be the ID of the network from the network listing (optional; default network used when not specified)
         * 
         * @return builder
         * 
         */
        public Builder networkId(String networkId) {
            return networkId(Output.of(networkId));
        }

        /**
         * @param notes Add some notes to the instance
         * 
         * @return builder
         * 
         */
        public Builder notes(@Nullable Output<String> notes) {
            $.notes = notes;
            return this;
        }

        /**
         * @param notes Add some notes to the instance
         * 
         * @return builder
         * 
         */
        public Builder notes(String notes) {
            return notes(Output.of(notes));
        }

        /**
         * @param privateIp (String) Instance&#39;s private IP address
         * 
         * @return builder
         * 
         */
        public Builder privateIp(@Nullable Output<String> privateIp) {
            $.privateIp = privateIp;
            return this;
        }

        /**
         * @param privateIp (String) Instance&#39;s private IP address
         * 
         * @return builder
         * 
         */
        public Builder privateIp(String privateIp) {
            return privateIp(Output.of(privateIp));
        }

        /**
         * @param privateIpv4 The private IPv4 address for the instance (optional)
         * 
         * @return builder
         * 
         */
        public Builder privateIpv4(@Nullable Output<String> privateIpv4) {
            $.privateIpv4 = privateIpv4;
            return this;
        }

        /**
         * @param privateIpv4 The private IPv4 address for the instance (optional)
         * 
         * @return builder
         * 
         */
        public Builder privateIpv4(String privateIpv4) {
            return privateIpv4(Output.of(privateIpv4));
        }

        /**
         * @param publicIp (String) Instance&#39;s public IP address
         * 
         * @return builder
         * 
         */
        public Builder publicIp(@Nullable Output<String> publicIp) {
            $.publicIp = publicIp;
            return this;
        }

        /**
         * @param publicIp (String) Instance&#39;s public IP address
         * 
         * @return builder
         * 
         */
        public Builder publicIp(String publicIp) {
            return publicIp(Output.of(publicIp));
        }

        /**
         * @param publicIpRequired This should be either &#39;none&#39; or &#39;create&#39; (default: &#39;create&#39;)
         * 
         * @return builder
         * 
         */
        public Builder publicIpRequired(@Nullable Output<String> publicIpRequired) {
            $.publicIpRequired = publicIpRequired;
            return this;
        }

        /**
         * @param publicIpRequired This should be either &#39;none&#39; or &#39;create&#39; (default: &#39;create&#39;)
         * 
         * @return builder
         * 
         */
        public Builder publicIpRequired(String publicIpRequired) {
            return publicIpRequired(Output.of(publicIpRequired));
        }

        /**
         * @param ramMb (Number) Instance&#39;s RAM (MB)
         * 
         * @return builder
         * 
         */
        public Builder ramMb(@Nullable Output<Integer> ramMb) {
            $.ramMb = ramMb;
            return this;
        }

        /**
         * @param ramMb (Number) Instance&#39;s RAM (MB)
         * 
         * @return builder
         * 
         */
        public Builder ramMb(Integer ramMb) {
            return ramMb(Output.of(ramMb));
        }

        /**
         * @param region The region for the instance, if not declare we use the region in declared in the provider
         * 
         * @return builder
         * 
         */
        public Builder region(@Nullable Output<String> region) {
            $.region = region;
            return this;
        }

        /**
         * @param region The region for the instance, if not declare we use the region in declared in the provider
         * 
         * @return builder
         * 
         */
        public Builder region(String region) {
            return region(Output.of(region));
        }

        /**
         * @param reservedIpv4 Can be either the UUID, name, or the IP address of the reserved IP
         * 
         * @return builder
         * 
         */
        public Builder reservedIpv4(@Nullable Output<String> reservedIpv4) {
            $.reservedIpv4 = reservedIpv4;
            return this;
        }

        /**
         * @param reservedIpv4 Can be either the UUID, name, or the IP address of the reserved IP
         * 
         * @return builder
         * 
         */
        public Builder reservedIpv4(String reservedIpv4) {
            return reservedIpv4(Output.of(reservedIpv4));
        }

        /**
         * @param reverseDns A fully qualified domain name that should be used as the instance&#39;s IP&#39;s reverse DNS (optional, uses the hostname if
         * unspecified)
         * 
         * @return builder
         * 
         */
        public Builder reverseDns(@Nullable Output<String> reverseDns) {
            $.reverseDns = reverseDns;
            return this;
        }

        /**
         * @param reverseDns A fully qualified domain name that should be used as the instance&#39;s IP&#39;s reverse DNS (optional, uses the hostname if
         * unspecified)
         * 
         * @return builder
         * 
         */
        public Builder reverseDns(String reverseDns) {
            return reverseDns(Output.of(reverseDns));
        }

        /**
         * @param script The contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance,
         * read/write/executable only by root and then will be executed at the end of the cloud initialization
         * 
         * @return builder
         * 
         */
        public Builder script(@Nullable Output<String> script) {
            $.script = script;
            return this;
        }

        /**
         * @param script The contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance,
         * read/write/executable only by root and then will be executed at the end of the cloud initialization
         * 
         * @return builder
         * 
         */
        public Builder script(String script) {
            return script(Output.of(script));
        }

        /**
         * @param size The name of the size, from the current list, e.g. g3.xsmall
         * 
         * @return builder
         * 
         */
        public Builder size(@Nullable Output<String> size) {
            $.size = size;
            return this;
        }

        /**
         * @param size The name of the size, from the current list, e.g. g3.xsmall
         * 
         * @return builder
         * 
         */
        public Builder size(String size) {
            return size(Output.of(size));
        }

        /**
         * @param sourceId (String) Instance&#39;s source ID
         * 
         * @return builder
         * 
         */
        public Builder sourceId(@Nullable Output<String> sourceId) {
            $.sourceId = sourceId;
            return this;
        }

        /**
         * @param sourceId (String) Instance&#39;s source ID
         * 
         * @return builder
         * 
         */
        public Builder sourceId(String sourceId) {
            return sourceId(Output.of(sourceId));
        }

        /**
         * @param sourceType (String) Instance&#39;s source type
         * 
         * @return builder
         * 
         */
        public Builder sourceType(@Nullable Output<String> sourceType) {
            $.sourceType = sourceType;
            return this;
        }

        /**
         * @param sourceType (String) Instance&#39;s source type
         * 
         * @return builder
         * 
         */
        public Builder sourceType(String sourceType) {
            return sourceType(Output.of(sourceType));
        }

        /**
         * @param sshkeyId The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn&#39;t provided a
         * random password will be set and returned in the initial_password field)
         * 
         * @return builder
         * 
         */
        public Builder sshkeyId(@Nullable Output<String> sshkeyId) {
            $.sshkeyId = sshkeyId;
            return this;
        }

        /**
         * @param sshkeyId The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn&#39;t provided a
         * random password will be set and returned in the initial_password field)
         * 
         * @return builder
         * 
         */
        public Builder sshkeyId(String sshkeyId) {
            return sshkeyId(Output.of(sshkeyId));
        }

        /**
         * @param status (String) Instance&#39;s status
         * 
         * @return builder
         * 
         */
        public Builder status(@Nullable Output<String> status) {
            $.status = status;
            return this;
        }

        /**
         * @param status (String) Instance&#39;s status
         * 
         * @return builder
         * 
         */
        public Builder status(String status) {
            return status(Output.of(status));
        }

        /**
         * @param tags An optional list of tags, represented as a key, value pair
         * 
         * @return builder
         * 
         */
        public Builder tags(@Nullable Output<List<String>> tags) {
            $.tags = tags;
            return this;
        }

        /**
         * @param tags An optional list of tags, represented as a key, value pair
         * 
         * @return builder
         * 
         */
        public Builder tags(List<String> tags) {
            return tags(Output.of(tags));
        }

        /**
         * @param tags An optional list of tags, represented as a key, value pair
         * 
         * @return builder
         * 
         */
        public Builder tags(String... tags) {
            return tags(List.of(tags));
        }

        /**
         * @param volumeType The type of volume to use, either &#39;ssd&#39; or &#39;bssd&#39; (optional; default &#39;ssd&#39;)
         * 
         * @return builder
         * 
         */
        public Builder volumeType(@Nullable Output<String> volumeType) {
            $.volumeType = volumeType;
            return this;
        }

        /**
         * @param volumeType The type of volume to use, either &#39;ssd&#39; or &#39;bssd&#39; (optional; default &#39;ssd&#39;)
         * 
         * @return builder
         * 
         */
        public Builder volumeType(String volumeType) {
            return volumeType(Output.of(volumeType));
        }

        public Builder writePassword(@Nullable Output<Boolean> writePassword) {
            $.writePassword = writePassword;
            return this;
        }

        public Builder writePassword(Boolean writePassword) {
            return writePassword(Output.of(writePassword));
        }

        public InstanceState build() {
            return $;
        }
    }

}

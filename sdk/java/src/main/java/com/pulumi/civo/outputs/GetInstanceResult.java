// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetInstanceResult {
    /**
     * @return Total cpu of the inatance
     * 
     */
    private Integer cpuCores;
    /**
     * @return The date of creation of the instance
     * 
     */
    private String createdAt;
    /**
     * @return The size of the disk
     * 
     */
    private Integer diskGb;
    /**
     * @return The ID of the firewall used
     * 
     */
    private String firewallId;
    /**
     * @return The hostname of the Instance
     * 
     */
    private @Nullable String hostname;
    /**
     * @return The ID of this resource.
     * 
     */
    private @Nullable String id;
    /**
     * @return Instance initial password
     * 
     */
    private String initialPassword;
    /**
     * @return The name of the initial user created on the server
     * 
     */
    private String initialUser;
    /**
     * @return his will be the ID of the network
     * 
     */
    private String networkId;
    /**
     * @return The notes of the instance
     * 
     */
    private String notes;
    /**
     * @return The private IP
     * 
     */
    private String privateIp;
    /**
     * @return Is the ip that is used to route the public ip from the internet to the instance using NAT
     * 
     */
    private String pseudoIp;
    /**
     * @return The public IP
     * 
     */
    private String publicIp;
    /**
     * @return Total ram of the instance
     * 
     */
    private Integer ramMb;
    /**
     * @return The region of an existing Instance
     * 
     */
    private @Nullable String region;
    /**
     * @return A fully qualified domain name
     * 
     */
    private String reverseDns;
    /**
     * @return The contents of a script uploaded
     * 
     */
    private String script;
    /**
     * @return The name of the size
     * 
     */
    private String size;
    /**
     * @return The ID SSH key
     * 
     */
    private String sshkeyId;
    /**
     * @return The status of the instance
     * 
     */
    private String status;
    /**
     * @return An optional list of tags
     * 
     */
    private List<String> tags;
    /**
     * @return The ID for the disk image/template to used to build the instance
     * 
     */
    private String template;

    private GetInstanceResult() {}
    /**
     * @return Total cpu of the inatance
     * 
     */
    public Integer cpuCores() {
        return this.cpuCores;
    }
    /**
     * @return The date of creation of the instance
     * 
     */
    public String createdAt() {
        return this.createdAt;
    }
    /**
     * @return The size of the disk
     * 
     */
    public Integer diskGb() {
        return this.diskGb;
    }
    /**
     * @return The ID of the firewall used
     * 
     */
    public String firewallId() {
        return this.firewallId;
    }
    /**
     * @return The hostname of the Instance
     * 
     */
    public Optional<String> hostname() {
        return Optional.ofNullable(this.hostname);
    }
    /**
     * @return The ID of this resource.
     * 
     */
    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }
    /**
     * @return Instance initial password
     * 
     */
    public String initialPassword() {
        return this.initialPassword;
    }
    /**
     * @return The name of the initial user created on the server
     * 
     */
    public String initialUser() {
        return this.initialUser;
    }
    /**
     * @return his will be the ID of the network
     * 
     */
    public String networkId() {
        return this.networkId;
    }
    /**
     * @return The notes of the instance
     * 
     */
    public String notes() {
        return this.notes;
    }
    /**
     * @return The private IP
     * 
     */
    public String privateIp() {
        return this.privateIp;
    }
    /**
     * @return Is the ip that is used to route the public ip from the internet to the instance using NAT
     * 
     */
    public String pseudoIp() {
        return this.pseudoIp;
    }
    /**
     * @return The public IP
     * 
     */
    public String publicIp() {
        return this.publicIp;
    }
    /**
     * @return Total ram of the instance
     * 
     */
    public Integer ramMb() {
        return this.ramMb;
    }
    /**
     * @return The region of an existing Instance
     * 
     */
    public Optional<String> region() {
        return Optional.ofNullable(this.region);
    }
    /**
     * @return A fully qualified domain name
     * 
     */
    public String reverseDns() {
        return this.reverseDns;
    }
    /**
     * @return The contents of a script uploaded
     * 
     */
    public String script() {
        return this.script;
    }
    /**
     * @return The name of the size
     * 
     */
    public String size() {
        return this.size;
    }
    /**
     * @return The ID SSH key
     * 
     */
    public String sshkeyId() {
        return this.sshkeyId;
    }
    /**
     * @return The status of the instance
     * 
     */
    public String status() {
        return this.status;
    }
    /**
     * @return An optional list of tags
     * 
     */
    public List<String> tags() {
        return this.tags;
    }
    /**
     * @return The ID for the disk image/template to used to build the instance
     * 
     */
    public String template() {
        return this.template;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetInstanceResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private Integer cpuCores;
        private String createdAt;
        private Integer diskGb;
        private String firewallId;
        private @Nullable String hostname;
        private @Nullable String id;
        private String initialPassword;
        private String initialUser;
        private String networkId;
        private String notes;
        private String privateIp;
        private String pseudoIp;
        private String publicIp;
        private Integer ramMb;
        private @Nullable String region;
        private String reverseDns;
        private String script;
        private String size;
        private String sshkeyId;
        private String status;
        private List<String> tags;
        private String template;
        public Builder() {}
        public Builder(GetInstanceResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.cpuCores = defaults.cpuCores;
    	      this.createdAt = defaults.createdAt;
    	      this.diskGb = defaults.diskGb;
    	      this.firewallId = defaults.firewallId;
    	      this.hostname = defaults.hostname;
    	      this.id = defaults.id;
    	      this.initialPassword = defaults.initialPassword;
    	      this.initialUser = defaults.initialUser;
    	      this.networkId = defaults.networkId;
    	      this.notes = defaults.notes;
    	      this.privateIp = defaults.privateIp;
    	      this.pseudoIp = defaults.pseudoIp;
    	      this.publicIp = defaults.publicIp;
    	      this.ramMb = defaults.ramMb;
    	      this.region = defaults.region;
    	      this.reverseDns = defaults.reverseDns;
    	      this.script = defaults.script;
    	      this.size = defaults.size;
    	      this.sshkeyId = defaults.sshkeyId;
    	      this.status = defaults.status;
    	      this.tags = defaults.tags;
    	      this.template = defaults.template;
        }

        @CustomType.Setter
        public Builder cpuCores(Integer cpuCores) {
            this.cpuCores = Objects.requireNonNull(cpuCores);
            return this;
        }
        @CustomType.Setter
        public Builder createdAt(String createdAt) {
            this.createdAt = Objects.requireNonNull(createdAt);
            return this;
        }
        @CustomType.Setter
        public Builder diskGb(Integer diskGb) {
            this.diskGb = Objects.requireNonNull(diskGb);
            return this;
        }
        @CustomType.Setter
        public Builder firewallId(String firewallId) {
            this.firewallId = Objects.requireNonNull(firewallId);
            return this;
        }
        @CustomType.Setter
        public Builder hostname(@Nullable String hostname) {
            this.hostname = hostname;
            return this;
        }
        @CustomType.Setter
        public Builder id(@Nullable String id) {
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder initialPassword(String initialPassword) {
            this.initialPassword = Objects.requireNonNull(initialPassword);
            return this;
        }
        @CustomType.Setter
        public Builder initialUser(String initialUser) {
            this.initialUser = Objects.requireNonNull(initialUser);
            return this;
        }
        @CustomType.Setter
        public Builder networkId(String networkId) {
            this.networkId = Objects.requireNonNull(networkId);
            return this;
        }
        @CustomType.Setter
        public Builder notes(String notes) {
            this.notes = Objects.requireNonNull(notes);
            return this;
        }
        @CustomType.Setter
        public Builder privateIp(String privateIp) {
            this.privateIp = Objects.requireNonNull(privateIp);
            return this;
        }
        @CustomType.Setter
        public Builder pseudoIp(String pseudoIp) {
            this.pseudoIp = Objects.requireNonNull(pseudoIp);
            return this;
        }
        @CustomType.Setter
        public Builder publicIp(String publicIp) {
            this.publicIp = Objects.requireNonNull(publicIp);
            return this;
        }
        @CustomType.Setter
        public Builder ramMb(Integer ramMb) {
            this.ramMb = Objects.requireNonNull(ramMb);
            return this;
        }
        @CustomType.Setter
        public Builder region(@Nullable String region) {
            this.region = region;
            return this;
        }
        @CustomType.Setter
        public Builder reverseDns(String reverseDns) {
            this.reverseDns = Objects.requireNonNull(reverseDns);
            return this;
        }
        @CustomType.Setter
        public Builder script(String script) {
            this.script = Objects.requireNonNull(script);
            return this;
        }
        @CustomType.Setter
        public Builder size(String size) {
            this.size = Objects.requireNonNull(size);
            return this;
        }
        @CustomType.Setter
        public Builder sshkeyId(String sshkeyId) {
            this.sshkeyId = Objects.requireNonNull(sshkeyId);
            return this;
        }
        @CustomType.Setter
        public Builder status(String status) {
            this.status = Objects.requireNonNull(status);
            return this;
        }
        @CustomType.Setter
        public Builder tags(List<String> tags) {
            this.tags = Objects.requireNonNull(tags);
            return this;
        }
        public Builder tags(String... tags) {
            return tags(List.of(tags));
        }
        @CustomType.Setter
        public Builder template(String template) {
            this.template = Objects.requireNonNull(template);
            return this;
        }
        public GetInstanceResult build() {
            final var o = new GetInstanceResult();
            o.cpuCores = cpuCores;
            o.createdAt = createdAt;
            o.diskGb = diskGb;
            o.firewallId = firewallId;
            o.hostname = hostname;
            o.id = id;
            o.initialPassword = initialPassword;
            o.initialUser = initialUser;
            o.networkId = networkId;
            o.notes = notes;
            o.privateIp = privateIp;
            o.pseudoIp = pseudoIp;
            o.publicIp = publicIp;
            o.ramMb = ramMb;
            o.region = region;
            o.reverseDns = reverseDns;
            o.script = script;
            o.size = size;
            o.sshkeyId = sshkeyId;
            o.status = status;
            o.tags = tags;
            o.template = template;
            return o;
        }
    }
}
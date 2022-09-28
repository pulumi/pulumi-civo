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

    private GetInstanceResult() {}
    public Integer cpuCores() {
        return this.cpuCores;
    }
    public String createdAt() {
        return this.createdAt;
    }
    public Integer diskGb() {
        return this.diskGb;
    }
    public String firewallId() {
        return this.firewallId;
    }
    public Optional<String> hostname() {
        return Optional.ofNullable(this.hostname);
    }
    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }
    public String initialPassword() {
        return this.initialPassword;
    }
    public String initialUser() {
        return this.initialUser;
    }
    public String networkId() {
        return this.networkId;
    }
    public String notes() {
        return this.notes;
    }
    public String privateIp() {
        return this.privateIp;
    }
    public String pseudoIp() {
        return this.pseudoIp;
    }
    public String publicIp() {
        return this.publicIp;
    }
    public Integer ramMb() {
        return this.ramMb;
    }
    public Optional<String> region() {
        return Optional.ofNullable(this.region);
    }
    public String reverseDns() {
        return this.reverseDns;
    }
    public String script() {
        return this.script;
    }
    public String size() {
        return this.size;
    }
    public String sshkeyId() {
        return this.sshkeyId;
    }
    public String status() {
        return this.status;
    }
    public List<String> tags() {
        return this.tags;
    }
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

// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetKubernetesVersionVersion {
    private Boolean default_;
    private String label;
    private String type;
    private String version;

    private GetKubernetesVersionVersion() {}
    public Boolean default_() {
        return this.default_;
    }
    public String label() {
        return this.label;
    }
    public String type() {
        return this.type;
    }
    public String version() {
        return this.version;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetKubernetesVersionVersion defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private Boolean default_;
        private String label;
        private String type;
        private String version;
        public Builder() {}
        public Builder(GetKubernetesVersionVersion defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.default_ = defaults.default_;
    	      this.label = defaults.label;
    	      this.type = defaults.type;
    	      this.version = defaults.version;
        }

        @CustomType.Setter("default")
        public Builder default_(Boolean default_) {
            this.default_ = Objects.requireNonNull(default_);
            return this;
        }
        @CustomType.Setter
        public Builder label(String label) {
            this.label = Objects.requireNonNull(label);
            return this;
        }
        @CustomType.Setter
        public Builder type(String type) {
            this.type = Objects.requireNonNull(type);
            return this;
        }
        @CustomType.Setter
        public Builder version(String version) {
            this.version = Objects.requireNonNull(version);
            return this;
        }
        public GetKubernetesVersionVersion build() {
            final var o = new GetKubernetesVersionVersion();
            o.default_ = default_;
            o.label = label;
            o.type = type;
            o.version = version;
            return o;
        }
    }
}
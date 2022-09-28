// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetRegionRegion {
    private String code;
    private String country;
    private Boolean default_;
    private String name;

    private GetRegionRegion() {}
    public String code() {
        return this.code;
    }
    public String country() {
        return this.country;
    }
    public Boolean default_() {
        return this.default_;
    }
    public String name() {
        return this.name;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetRegionRegion defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String code;
        private String country;
        private Boolean default_;
        private String name;
        public Builder() {}
        public Builder(GetRegionRegion defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.code = defaults.code;
    	      this.country = defaults.country;
    	      this.default_ = defaults.default_;
    	      this.name = defaults.name;
        }

        @CustomType.Setter
        public Builder code(String code) {
            this.code = Objects.requireNonNull(code);
            return this;
        }
        @CustomType.Setter
        public Builder country(String country) {
            this.country = Objects.requireNonNull(country);
            return this;
        }
        @CustomType.Setter("default")
        public Builder default_(Boolean default_) {
            this.default_ = Objects.requireNonNull(default_);
            return this;
        }
        @CustomType.Setter
        public Builder name(String name) {
            this.name = Objects.requireNonNull(name);
            return this;
        }
        public GetRegionRegion build() {
            final var o = new GetRegionRegion();
            o.code = code;
            o.country = country;
            o.default_ = default_;
            o.name = name;
            return o;
        }
    }
}

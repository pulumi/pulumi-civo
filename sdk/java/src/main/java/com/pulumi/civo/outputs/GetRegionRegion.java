// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetRegionRegion {
    /**
     * @return The code of the region
     * 
     */
    private String code;
    /**
     * @return The country of the region
     * 
     */
    private String country;
    /**
     * @return If the region is the default region, this will return `true`
     * 
     */
    private Boolean default_;
    /**
     * @return A human name of the region
     * 
     */
    private String name;

    private GetRegionRegion() {}
    /**
     * @return The code of the region
     * 
     */
    public String code() {
        return this.code;
    }
    /**
     * @return The country of the region
     * 
     */
    public String country() {
        return this.country;
    }
    /**
     * @return If the region is the default region, this will return `true`
     * 
     */
    public Boolean default_() {
        return this.default_;
    }
    /**
     * @return A human name of the region
     * 
     */
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
            if (code == null) {
              throw new MissingRequiredPropertyException("GetRegionRegion", "code");
            }
            this.code = code;
            return this;
        }
        @CustomType.Setter
        public Builder country(String country) {
            if (country == null) {
              throw new MissingRequiredPropertyException("GetRegionRegion", "country");
            }
            this.country = country;
            return this;
        }
        @CustomType.Setter("default")
        public Builder default_(Boolean default_) {
            if (default_ == null) {
              throw new MissingRequiredPropertyException("GetRegionRegion", "default_");
            }
            this.default_ = default_;
            return this;
        }
        @CustomType.Setter
        public Builder name(String name) {
            if (name == null) {
              throw new MissingRequiredPropertyException("GetRegionRegion", "name");
            }
            this.name = name;
            return this;
        }
        public GetRegionRegion build() {
            final var _resultValue = new GetRegionRegion();
            _resultValue.code = code;
            _resultValue.country = country;
            _resultValue.default_ = default_;
            _resultValue.name = name;
            return _resultValue;
        }
    }
}

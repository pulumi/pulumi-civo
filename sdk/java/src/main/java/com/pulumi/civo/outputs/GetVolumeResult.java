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
public final class GetVolumeResult {
    /**
     * @return The date of the creation of the volume
     * 
     */
    private String createdAt;
    /**
     * @return The ID of this resource.
     * 
     */
    private @Nullable String id;
    /**
     * @return The mount point of the volume
     * 
     */
    private String mountPoint;
    /**
     * @return The name of the volume
     * 
     */
    private @Nullable String name;
    /**
     * @return The region where volume is running
     * 
     */
    private @Nullable String region;
    /**
     * @return The size of the volume (in GB)
     * 
     */
    private Integer sizeGb;

    private GetVolumeResult() {}
    /**
     * @return The date of the creation of the volume
     * 
     */
    public String createdAt() {
        return this.createdAt;
    }
    /**
     * @return The ID of this resource.
     * 
     */
    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }
    /**
     * @return The mount point of the volume
     * 
     */
    public String mountPoint() {
        return this.mountPoint;
    }
    /**
     * @return The name of the volume
     * 
     */
    public Optional<String> name() {
        return Optional.ofNullable(this.name);
    }
    /**
     * @return The region where volume is running
     * 
     */
    public Optional<String> region() {
        return Optional.ofNullable(this.region);
    }
    /**
     * @return The size of the volume (in GB)
     * 
     */
    public Integer sizeGb() {
        return this.sizeGb;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetVolumeResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String createdAt;
        private @Nullable String id;
        private String mountPoint;
        private @Nullable String name;
        private @Nullable String region;
        private Integer sizeGb;
        public Builder() {}
        public Builder(GetVolumeResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.createdAt = defaults.createdAt;
    	      this.id = defaults.id;
    	      this.mountPoint = defaults.mountPoint;
    	      this.name = defaults.name;
    	      this.region = defaults.region;
    	      this.sizeGb = defaults.sizeGb;
        }

        @CustomType.Setter
        public Builder createdAt(String createdAt) {
            this.createdAt = Objects.requireNonNull(createdAt);
            return this;
        }
        @CustomType.Setter
        public Builder id(@Nullable String id) {
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder mountPoint(String mountPoint) {
            this.mountPoint = Objects.requireNonNull(mountPoint);
            return this;
        }
        @CustomType.Setter
        public Builder name(@Nullable String name) {
            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder region(@Nullable String region) {
            this.region = region;
            return this;
        }
        @CustomType.Setter
        public Builder sizeGb(Integer sizeGb) {
            this.sizeGb = Objects.requireNonNull(sizeGb);
            return this;
        }
        public GetVolumeResult build() {
            final var o = new GetVolumeResult();
            o.createdAt = createdAt;
            o.id = id;
            o.mountPoint = mountPoint;
            o.name = name;
            o.region = region;
            o.sizeGb = sizeGb;
            return o;
        }
    }
}

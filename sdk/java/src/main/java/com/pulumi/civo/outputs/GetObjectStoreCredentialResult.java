// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetObjectStoreCredentialResult {
    /**
     * @return The access key id of the Object Store Credential
     * 
     */
    private String accessKeyId;
    /**
     * @return The ID of the Object Store Credential
     * 
     */
    private @Nullable String id;
    /**
     * @return The name of the Object Store Credential
     * 
     */
    private @Nullable String name;
    /**
     * @return The region of an existing Object Store
     * 
     */
    private @Nullable String region;
    /**
     * @return The secret access key of the Object Store Credential
     * 
     */
    private String secretAccessKey;
    /**
     * @return The status of the Object Store Credential
     * 
     */
    private String status;

    private GetObjectStoreCredentialResult() {}
    /**
     * @return The access key id of the Object Store Credential
     * 
     */
    public String accessKeyId() {
        return this.accessKeyId;
    }
    /**
     * @return The ID of the Object Store Credential
     * 
     */
    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }
    /**
     * @return The name of the Object Store Credential
     * 
     */
    public Optional<String> name() {
        return Optional.ofNullable(this.name);
    }
    /**
     * @return The region of an existing Object Store
     * 
     */
    public Optional<String> region() {
        return Optional.ofNullable(this.region);
    }
    /**
     * @return The secret access key of the Object Store Credential
     * 
     */
    public String secretAccessKey() {
        return this.secretAccessKey;
    }
    /**
     * @return The status of the Object Store Credential
     * 
     */
    public String status() {
        return this.status;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetObjectStoreCredentialResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String accessKeyId;
        private @Nullable String id;
        private @Nullable String name;
        private @Nullable String region;
        private String secretAccessKey;
        private String status;
        public Builder() {}
        public Builder(GetObjectStoreCredentialResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.accessKeyId = defaults.accessKeyId;
    	      this.id = defaults.id;
    	      this.name = defaults.name;
    	      this.region = defaults.region;
    	      this.secretAccessKey = defaults.secretAccessKey;
    	      this.status = defaults.status;
        }

        @CustomType.Setter
        public Builder accessKeyId(String accessKeyId) {
            this.accessKeyId = Objects.requireNonNull(accessKeyId);
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
        public Builder region(@Nullable String region) {
            this.region = region;
            return this;
        }
        @CustomType.Setter
        public Builder secretAccessKey(String secretAccessKey) {
            this.secretAccessKey = Objects.requireNonNull(secretAccessKey);
            return this;
        }
        @CustomType.Setter
        public Builder status(String status) {
            this.status = Objects.requireNonNull(status);
            return this;
        }
        public GetObjectStoreCredentialResult build() {
            final var _resultValue = new GetObjectStoreCredentialResult();
            _resultValue.accessKeyId = accessKeyId;
            _resultValue.id = id;
            _resultValue.name = name;
            _resultValue.region = region;
            _resultValue.secretAccessKey = secretAccessKey;
            _resultValue.status = status;
            return _resultValue;
        }
    }
}

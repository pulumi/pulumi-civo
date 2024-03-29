// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class ObjectStoreCredentialArgs extends com.pulumi.resources.ResourceArgs {

    public static final ObjectStoreCredentialArgs Empty = new ObjectStoreCredentialArgs();

    /**
     * The access key id of the Object Store Credential. It is generated by the provider.
     * 
     */
    @Import(name="accessKeyId")
    private @Nullable Output<String> accessKeyId;

    /**
     * @return The access key id of the Object Store Credential. It is generated by the provider.
     * 
     */
    public Optional<Output<String>> accessKeyId() {
        return Optional.ofNullable(this.accessKeyId);
    }

    /**
     * The name of the Object Store Credential. Must be unique.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return The name of the Object Store Credential. Must be unique.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * The region where the Object Store Credential will be created.
     * 
     */
    @Import(name="region")
    private @Nullable Output<String> region;

    /**
     * @return The region where the Object Store Credential will be created.
     * 
     */
    public Optional<Output<String>> region() {
        return Optional.ofNullable(this.region);
    }

    /**
     * The secret access key of the Object Store Credential. It is generated by the provider.
     * 
     */
    @Import(name="secretAccessKey")
    private @Nullable Output<String> secretAccessKey;

    /**
     * @return The secret access key of the Object Store Credential. It is generated by the provider.
     * 
     */
    public Optional<Output<String>> secretAccessKey() {
        return Optional.ofNullable(this.secretAccessKey);
    }

    private ObjectStoreCredentialArgs() {}

    private ObjectStoreCredentialArgs(ObjectStoreCredentialArgs $) {
        this.accessKeyId = $.accessKeyId;
        this.name = $.name;
        this.region = $.region;
        this.secretAccessKey = $.secretAccessKey;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ObjectStoreCredentialArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ObjectStoreCredentialArgs $;

        public Builder() {
            $ = new ObjectStoreCredentialArgs();
        }

        public Builder(ObjectStoreCredentialArgs defaults) {
            $ = new ObjectStoreCredentialArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param accessKeyId The access key id of the Object Store Credential. It is generated by the provider.
         * 
         * @return builder
         * 
         */
        public Builder accessKeyId(@Nullable Output<String> accessKeyId) {
            $.accessKeyId = accessKeyId;
            return this;
        }

        /**
         * @param accessKeyId The access key id of the Object Store Credential. It is generated by the provider.
         * 
         * @return builder
         * 
         */
        public Builder accessKeyId(String accessKeyId) {
            return accessKeyId(Output.of(accessKeyId));
        }

        /**
         * @param name The name of the Object Store Credential. Must be unique.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name The name of the Object Store Credential. Must be unique.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param region The region where the Object Store Credential will be created.
         * 
         * @return builder
         * 
         */
        public Builder region(@Nullable Output<String> region) {
            $.region = region;
            return this;
        }

        /**
         * @param region The region where the Object Store Credential will be created.
         * 
         * @return builder
         * 
         */
        public Builder region(String region) {
            return region(Output.of(region));
        }

        /**
         * @param secretAccessKey The secret access key of the Object Store Credential. It is generated by the provider.
         * 
         * @return builder
         * 
         */
        public Builder secretAccessKey(@Nullable Output<String> secretAccessKey) {
            $.secretAccessKey = secretAccessKey;
            return this;
        }

        /**
         * @param secretAccessKey The secret access key of the Object Store Credential. It is generated by the provider.
         * 
         * @return builder
         * 
         */
        public Builder secretAccessKey(String secretAccessKey) {
            return secretAccessKey(Output.of(secretAccessKey));
        }

        public ObjectStoreCredentialArgs build() {
            return $;
        }
    }

}

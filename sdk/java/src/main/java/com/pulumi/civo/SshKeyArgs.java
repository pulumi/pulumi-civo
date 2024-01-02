// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class SshKeyArgs extends com.pulumi.resources.ResourceArgs {

    public static final SshKeyArgs Empty = new SshKeyArgs();

    /**
     * a string that will be the reference for the SSH key.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return a string that will be the reference for the SSH key.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * a string containing the SSH public key.
     * 
     */
    @Import(name="publicKey", required=true)
    private Output<String> publicKey;

    /**
     * @return a string containing the SSH public key.
     * 
     */
    public Output<String> publicKey() {
        return this.publicKey;
    }

    private SshKeyArgs() {}

    private SshKeyArgs(SshKeyArgs $) {
        this.name = $.name;
        this.publicKey = $.publicKey;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(SshKeyArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private SshKeyArgs $;

        public Builder() {
            $ = new SshKeyArgs();
        }

        public Builder(SshKeyArgs defaults) {
            $ = new SshKeyArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param name a string that will be the reference for the SSH key.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name a string that will be the reference for the SSH key.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param publicKey a string containing the SSH public key.
         * 
         * @return builder
         * 
         */
        public Builder publicKey(Output<String> publicKey) {
            $.publicKey = publicKey;
            return this;
        }

        /**
         * @param publicKey a string containing the SSH public key.
         * 
         * @return builder
         * 
         */
        public Builder publicKey(String publicKey) {
            return publicKey(Output.of(publicKey));
        }

        public SshKeyArgs build() {
            if ($.publicKey == null) {
                throw new MissingRequiredPropertyException("SshKeyArgs", "publicKey");
            }
            return $;
        }
    }

}

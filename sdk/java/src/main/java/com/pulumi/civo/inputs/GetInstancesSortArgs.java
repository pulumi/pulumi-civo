// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetInstancesSortArgs extends com.pulumi.resources.ResourceArgs {

    public static final GetInstancesSortArgs Empty = new GetInstancesSortArgs();

    /**
     * The sort direction. This may be either `asc` or `desc`.
     * 
     */
    @Import(name="direction")
    private @Nullable Output<String> direction;

    /**
     * @return The sort direction. This may be either `asc` or `desc`.
     * 
     */
    public Optional<Output<String>> direction() {
        return Optional.ofNullable(this.direction);
    }

    /**
     * Sort instances by this key. This may be one of `cpu_cores`, `created_at`, `disk_gb`, `firewall_id`, `hostname`, `id`, `initial_password`, `initial_user`, `network_id`, `notes`, `private_ip`, `pseudo_ip`, `public_ip`, `ram_mb`, `region`, `reverse_dns`, `script`, `size`, `sshkey_id`, `status`, `template`.
     * 
     */
    @Import(name="key", required=true)
    private Output<String> key;

    /**
     * @return Sort instances by this key. This may be one of `cpu_cores`, `created_at`, `disk_gb`, `firewall_id`, `hostname`, `id`, `initial_password`, `initial_user`, `network_id`, `notes`, `private_ip`, `pseudo_ip`, `public_ip`, `ram_mb`, `region`, `reverse_dns`, `script`, `size`, `sshkey_id`, `status`, `template`.
     * 
     */
    public Output<String> key() {
        return this.key;
    }

    private GetInstancesSortArgs() {}

    private GetInstancesSortArgs(GetInstancesSortArgs $) {
        this.direction = $.direction;
        this.key = $.key;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetInstancesSortArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetInstancesSortArgs $;

        public Builder() {
            $ = new GetInstancesSortArgs();
        }

        public Builder(GetInstancesSortArgs defaults) {
            $ = new GetInstancesSortArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param direction The sort direction. This may be either `asc` or `desc`.
         * 
         * @return builder
         * 
         */
        public Builder direction(@Nullable Output<String> direction) {
            $.direction = direction;
            return this;
        }

        /**
         * @param direction The sort direction. This may be either `asc` or `desc`.
         * 
         * @return builder
         * 
         */
        public Builder direction(String direction) {
            return direction(Output.of(direction));
        }

        /**
         * @param key Sort instances by this key. This may be one of `cpu_cores`, `created_at`, `disk_gb`, `firewall_id`, `hostname`, `id`, `initial_password`, `initial_user`, `network_id`, `notes`, `private_ip`, `pseudo_ip`, `public_ip`, `ram_mb`, `region`, `reverse_dns`, `script`, `size`, `sshkey_id`, `status`, `template`.
         * 
         * @return builder
         * 
         */
        public Builder key(Output<String> key) {
            $.key = key;
            return this;
        }

        /**
         * @param key Sort instances by this key. This may be one of `cpu_cores`, `created_at`, `disk_gb`, `firewall_id`, `hostname`, `id`, `initial_password`, `initial_user`, `network_id`, `notes`, `private_ip`, `pseudo_ip`, `public_ip`, `ram_mb`, `region`, `reverse_dns`, `script`, `size`, `sshkey_id`, `status`, `template`.
         * 
         * @return builder
         * 
         */
        public Builder key(String key) {
            return key(Output.of(key));
        }

        public GetInstancesSortArgs build() {
            if ($.key == null) {
                throw new MissingRequiredPropertyException("GetInstancesSortArgs", "key");
            }
            return $;
        }
    }

}
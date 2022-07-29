// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.inputs;

import com.pulumi.core.annotations.Import;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetObjectStorePlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetObjectStorePlainArgs Empty = new GetObjectStorePlainArgs();

    @Import(name="id")
    private @Nullable String id;

    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }

    @Import(name="maxSizeGb")
    private @Nullable Integer maxSizeGb;

    public Optional<Integer> maxSizeGb() {
        return Optional.ofNullable(this.maxSizeGb);
    }

    @Import(name="name")
    private @Nullable String name;

    public Optional<String> name() {
        return Optional.ofNullable(this.name);
    }

    @Import(name="region")
    private @Nullable String region;

    public Optional<String> region() {
        return Optional.ofNullable(this.region);
    }

    private GetObjectStorePlainArgs() {}

    private GetObjectStorePlainArgs(GetObjectStorePlainArgs $) {
        this.id = $.id;
        this.maxSizeGb = $.maxSizeGb;
        this.name = $.name;
        this.region = $.region;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetObjectStorePlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetObjectStorePlainArgs $;

        public Builder() {
            $ = new GetObjectStorePlainArgs();
        }

        public Builder(GetObjectStorePlainArgs defaults) {
            $ = new GetObjectStorePlainArgs(Objects.requireNonNull(defaults));
        }

        public Builder id(@Nullable String id) {
            $.id = id;
            return this;
        }

        public Builder maxSizeGb(@Nullable Integer maxSizeGb) {
            $.maxSizeGb = maxSizeGb;
            return this;
        }

        public Builder name(@Nullable String name) {
            $.name = name;
            return this;
        }

        public Builder region(@Nullable String region) {
            $.region = region;
            return this;
        }

        public GetObjectStorePlainArgs build() {
            return $;
        }
    }

}

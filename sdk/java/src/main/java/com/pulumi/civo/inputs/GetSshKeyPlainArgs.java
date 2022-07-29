// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.inputs;

import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetSshKeyPlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetSshKeyPlainArgs Empty = new GetSshKeyPlainArgs();

    @Import(name="id")
    private @Nullable String id;

    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }

    @Import(name="name")
    private @Nullable String name;

    public Optional<String> name() {
        return Optional.ofNullable(this.name);
    }

    private GetSshKeyPlainArgs() {}

    private GetSshKeyPlainArgs(GetSshKeyPlainArgs $) {
        this.id = $.id;
        this.name = $.name;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetSshKeyPlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetSshKeyPlainArgs $;

        public Builder() {
            $ = new GetSshKeyPlainArgs();
        }

        public Builder(GetSshKeyPlainArgs defaults) {
            $ = new GetSshKeyPlainArgs(Objects.requireNonNull(defaults));
        }

        public Builder id(@Nullable String id) {
            $.id = id;
            return this;
        }

        public Builder name(@Nullable String name) {
            $.name = name;
            return this;
        }

        public GetSshKeyPlainArgs build() {
            return $;
        }
    }

}

// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class KubernetesClusterInstalledApplicationArgs extends com.pulumi.resources.ResourceArgs {

    public static final KubernetesClusterInstalledApplicationArgs Empty = new KubernetesClusterInstalledApplicationArgs();

    @Import(name="application")
    private @Nullable Output<String> application;

    public Optional<Output<String>> application() {
        return Optional.ofNullable(this.application);
    }

    @Import(name="category")
    private @Nullable Output<String> category;

    public Optional<Output<String>> category() {
        return Optional.ofNullable(this.category);
    }

    @Import(name="installed")
    private @Nullable Output<Boolean> installed;

    public Optional<Output<Boolean>> installed() {
        return Optional.ofNullable(this.installed);
    }

    @Import(name="version")
    private @Nullable Output<String> version;

    public Optional<Output<String>> version() {
        return Optional.ofNullable(this.version);
    }

    private KubernetesClusterInstalledApplicationArgs() {}

    private KubernetesClusterInstalledApplicationArgs(KubernetesClusterInstalledApplicationArgs $) {
        this.application = $.application;
        this.category = $.category;
        this.installed = $.installed;
        this.version = $.version;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(KubernetesClusterInstalledApplicationArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private KubernetesClusterInstalledApplicationArgs $;

        public Builder() {
            $ = new KubernetesClusterInstalledApplicationArgs();
        }

        public Builder(KubernetesClusterInstalledApplicationArgs defaults) {
            $ = new KubernetesClusterInstalledApplicationArgs(Objects.requireNonNull(defaults));
        }

        public Builder application(@Nullable Output<String> application) {
            $.application = application;
            return this;
        }

        public Builder application(String application) {
            return application(Output.of(application));
        }

        public Builder category(@Nullable Output<String> category) {
            $.category = category;
            return this;
        }

        public Builder category(String category) {
            return category(Output.of(category));
        }

        public Builder installed(@Nullable Output<Boolean> installed) {
            $.installed = installed;
            return this;
        }

        public Builder installed(Boolean installed) {
            return installed(Output.of(installed));
        }

        public Builder version(@Nullable Output<String> version) {
            $.version = version;
            return this;
        }

        public Builder version(String version) {
            return version(Output.of(version));
        }

        public KubernetesClusterInstalledApplicationArgs build() {
            return $;
        }
    }

}
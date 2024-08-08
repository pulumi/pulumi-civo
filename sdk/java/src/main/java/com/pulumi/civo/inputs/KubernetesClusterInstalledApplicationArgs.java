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

    /**
     * (String) name of the application
     * 
     */
    @Import(name="application")
    private @Nullable Output<String> application;

    /**
     * @return (String) name of the application
     * 
     */
    public Optional<Output<String>> application() {
        return Optional.ofNullable(this.application);
    }

    /**
     * (String) category of the application
     * 
     */
    @Import(name="category")
    private @Nullable Output<String> category;

    /**
     * @return (String) category of the application
     * 
     */
    public Optional<Output<String>> category() {
        return Optional.ofNullable(this.category);
    }

    /**
     * (Boolean) whether application is installed or not
     * 
     */
    @Import(name="installed")
    private @Nullable Output<Boolean> installed;

    /**
     * @return (Boolean) whether application is installed or not
     * 
     */
    public Optional<Output<Boolean>> installed() {
        return Optional.ofNullable(this.installed);
    }

    /**
     * (String) version of the application
     * 
     */
    @Import(name="version")
    private @Nullable Output<String> version;

    /**
     * @return (String) version of the application
     * 
     */
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

        /**
         * @param application (String) name of the application
         * 
         * @return builder
         * 
         */
        public Builder application(@Nullable Output<String> application) {
            $.application = application;
            return this;
        }

        /**
         * @param application (String) name of the application
         * 
         * @return builder
         * 
         */
        public Builder application(String application) {
            return application(Output.of(application));
        }

        /**
         * @param category (String) category of the application
         * 
         * @return builder
         * 
         */
        public Builder category(@Nullable Output<String> category) {
            $.category = category;
            return this;
        }

        /**
         * @param category (String) category of the application
         * 
         * @return builder
         * 
         */
        public Builder category(String category) {
            return category(Output.of(category));
        }

        /**
         * @param installed (Boolean) whether application is installed or not
         * 
         * @return builder
         * 
         */
        public Builder installed(@Nullable Output<Boolean> installed) {
            $.installed = installed;
            return this;
        }

        /**
         * @param installed (Boolean) whether application is installed or not
         * 
         * @return builder
         * 
         */
        public Builder installed(Boolean installed) {
            return installed(Output.of(installed));
        }

        /**
         * @param version (String) version of the application
         * 
         * @return builder
         * 
         */
        public Builder version(@Nullable Output<String> version) {
            $.version = version;
            return this;
        }

        /**
         * @param version (String) version of the application
         * 
         * @return builder
         * 
         */
        public Builder version(String version) {
            return version(Output.of(version));
        }

        public KubernetesClusterInstalledApplicationArgs build() {
            return $;
        }
    }

}

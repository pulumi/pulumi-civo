// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class KubernetesClusterInstalledApplication {
    /**
     * @return (String) name of the application
     * 
     */
    private @Nullable String application;
    /**
     * @return (String) category of the application
     * 
     */
    private @Nullable String category;
    /**
     * @return (Boolean) whether application is installed or not
     * 
     */
    private @Nullable Boolean installed;
    /**
     * @return (String) version of the application
     * 
     */
    private @Nullable String version;

    private KubernetesClusterInstalledApplication() {}
    /**
     * @return (String) name of the application
     * 
     */
    public Optional<String> application() {
        return Optional.ofNullable(this.application);
    }
    /**
     * @return (String) category of the application
     * 
     */
    public Optional<String> category() {
        return Optional.ofNullable(this.category);
    }
    /**
     * @return (Boolean) whether application is installed or not
     * 
     */
    public Optional<Boolean> installed() {
        return Optional.ofNullable(this.installed);
    }
    /**
     * @return (String) version of the application
     * 
     */
    public Optional<String> version() {
        return Optional.ofNullable(this.version);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(KubernetesClusterInstalledApplication defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable String application;
        private @Nullable String category;
        private @Nullable Boolean installed;
        private @Nullable String version;
        public Builder() {}
        public Builder(KubernetesClusterInstalledApplication defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.application = defaults.application;
    	      this.category = defaults.category;
    	      this.installed = defaults.installed;
    	      this.version = defaults.version;
        }

        @CustomType.Setter
        public Builder application(@Nullable String application) {

            this.application = application;
            return this;
        }
        @CustomType.Setter
        public Builder category(@Nullable String category) {

            this.category = category;
            return this;
        }
        @CustomType.Setter
        public Builder installed(@Nullable Boolean installed) {

            this.installed = installed;
            return this;
        }
        @CustomType.Setter
        public Builder version(@Nullable String version) {

            this.version = version;
            return this;
        }
        public KubernetesClusterInstalledApplication build() {
            final var _resultValue = new KubernetesClusterInstalledApplication();
            _resultValue.application = application;
            _resultValue.category = category;
            _resultValue.installed = installed;
            _resultValue.version = version;
            return _resultValue;
        }
    }
}

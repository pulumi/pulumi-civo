// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo;

import com.pulumi.core.internal.Codegen;
import java.lang.String;
import java.util.Optional;

public final class Config {

    private static final com.pulumi.Config config = com.pulumi.Config.of("civo");
/**
 * The Base URL to use for CIVO API.
 * 
 */
    public Optional<String> apiEndpoint() {
        return Codegen.stringProp("apiEndpoint").config(config).get();
    }
/**
 * Path to the Civo credentials file. Can be specified using CIVO_CREDENTIAL_FILE environment variable.
 * 
 */
    public Optional<String> credentialsFile() {
        return Codegen.stringProp("credentialsFile").config(config).get();
    }
/**
 * If region is not set, then no region will be used and them you need expensify in every resource even if you expensify
 * here you can overwrite in a resource.
 * 
 */
    public Optional<String> region() {
        return Codegen.stringProp("region").config(config).get();
    }
/**
 * This is the Civo API token. Alternatively, this can also be specified using `CIVO_TOKEN` environment variable.
 * 
 */
    public Optional<String> token() {
        return Codegen.stringProp("token").config(config).get();
    }
}

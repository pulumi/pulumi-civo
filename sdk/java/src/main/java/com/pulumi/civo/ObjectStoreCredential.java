// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo;

import com.pulumi.civo.ObjectStoreCredentialArgs;
import com.pulumi.civo.Utilities;
import com.pulumi.civo.inputs.ObjectStoreCredentialState;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import java.lang.String;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * Provides an Object Store Credential resource. This can be used to create, modify, and delete object stores credential.
 * 
 * ## Example Usage
 * ```java
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.civo.CivoFunctions;
 * import com.pulumi.civo.inputs.GetObjectStoreCredentialArgs;
 * import com.pulumi.civo.ObjectStoreCredential;
 * import com.pulumi.civo.ObjectStoreCredentialArgs;
 * import com.pulumi.civo.ObjectStore;
 * import com.pulumi.civo.ObjectStoreArgs;
 * import java.util.List;
 * import java.util.ArrayList;
 * import java.util.Map;
 * import java.io.File;
 * import java.nio.file.Files;
 * import java.nio.file.Paths;
 * 
 * public class App {
 *     public static void main(String[] args) {
 *         Pulumi.run(App::stack);
 *     }
 * 
 *     public static void stack(Context ctx) {
 *         final var backupObjectStoreCredential = CivoFunctions.getObjectStoreCredential(GetObjectStoreCredentialArgs.builder()
 *             .name(&#34;backup-server&#34;)
 *             .build());
 * 
 *         var backupIndex_objectStoreCredentialObjectStoreCredential = new ObjectStoreCredential(&#34;backupIndex/objectStoreCredentialObjectStoreCredential&#34;, ObjectStoreCredentialArgs.builder()        
 *             .accessKeyId(&#34;my-access-key&#34;)
 *             .secretAccessKey(&#34;my-secret-key&#34;)
 *             .build());
 * 
 *         var backupObjectStore = new ObjectStore(&#34;backupObjectStore&#34;, ObjectStoreArgs.builder()        
 *             .maxSizeGb(500)
 *             .region(&#34;LON1&#34;)
 *             .accessKeyId(backupIndex / objectStoreCredentialObjectStoreCredential.accessKeyId())
 *             .build());
 * 
 *     }
 * }
 * ```
 * 
 * ## Import
 * 
 * using ID
 * 
 * ```sh
 *  $ pulumi import civo:index/objectStoreCredential:ObjectStoreCredential custom_object b8ecd2ab-2267-4a5e-8692-cbf1d32583e3
 * ```
 * 
 */
@ResourceType(type="civo:index/objectStoreCredential:ObjectStoreCredential")
public class ObjectStoreCredential extends com.pulumi.resources.CustomResource {
    /**
     * The access key id of the Object Store Credential. It is generated by the provider.
     * 
     */
    @Export(name="accessKeyId", type=String.class, parameters={})
    private Output<String> accessKeyId;

    /**
     * @return The access key id of the Object Store Credential. It is generated by the provider.
     * 
     */
    public Output<String> accessKeyId() {
        return this.accessKeyId;
    }
    /**
     * The name of the Object Store Credential. Must be unique.
     * 
     */
    @Export(name="name", type=String.class, parameters={})
    private Output<String> name;

    /**
     * @return The name of the Object Store Credential. Must be unique.
     * 
     */
    public Output<String> name() {
        return this.name;
    }
    /**
     * The region where the Object Store Credential will be created.
     * 
     */
    @Export(name="region", type=String.class, parameters={})
    private Output</* @Nullable */ String> region;

    /**
     * @return The region where the Object Store Credential will be created.
     * 
     */
    public Output<Optional<String>> region() {
        return Codegen.optional(this.region);
    }
    /**
     * The secret access key of the Object Store Credential. It is generated by the provider.
     * 
     */
    @Export(name="secretAccessKey", type=String.class, parameters={})
    private Output<String> secretAccessKey;

    /**
     * @return The secret access key of the Object Store Credential. It is generated by the provider.
     * 
     */
    public Output<String> secretAccessKey() {
        return this.secretAccessKey;
    }
    /**
     * The status of the Object Store Credential.
     * 
     */
    @Export(name="status", type=String.class, parameters={})
    private Output<String> status;

    /**
     * @return The status of the Object Store Credential.
     * 
     */
    public Output<String> status() {
        return this.status;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public ObjectStoreCredential(String name) {
        this(name, ObjectStoreCredentialArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public ObjectStoreCredential(String name, @Nullable ObjectStoreCredentialArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public ObjectStoreCredential(String name, @Nullable ObjectStoreCredentialArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("civo:index/objectStoreCredential:ObjectStoreCredential", name, args == null ? ObjectStoreCredentialArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private ObjectStoreCredential(String name, Output<String> id, @Nullable ObjectStoreCredentialState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("civo:index/objectStoreCredential:ObjectStoreCredential", name, state, makeResourceOptions(options, id));
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .build();
        return com.pulumi.resources.CustomResourceOptions.merge(defaultOptions, options, id);
    }

    /**
     * Get an existing Host resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state
     * @param options Optional settings to control the behavior of the CustomResource.
     */
    public static ObjectStoreCredential get(String name, Output<String> id, @Nullable ObjectStoreCredentialState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new ObjectStoreCredential(name, id, state, options);
    }
}

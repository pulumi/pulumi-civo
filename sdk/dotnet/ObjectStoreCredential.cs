// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Civo
{
    /// <summary>
    /// Provides an Object Store Credential resource. This can be used to create, modify, and delete object stores credential.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using Pulumi;
    /// using Civo = Pulumi.Civo;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var backupObjectStoreCredential = Civo.GetObjectStoreCredential.Invoke(new()
    ///     {
    ///         Name = "backup-server",
    ///     });
    /// 
    ///     // Create a credential for the object store with a specific access key and secret key
    ///     var backupIndex_objectStoreCredentialObjectStoreCredential = new Civo.ObjectStoreCredential("backupIndex/objectStoreCredentialObjectStoreCredential", new()
    ///     {
    ///         AccessKeyId = "my-access-key",
    ///         SecretAccessKey = "my-secret-key",
    ///     });
    /// 
    ///     // Use the credential to create a bucket
    ///     var backupObjectStore = new Civo.ObjectStore("backupObjectStore", new()
    ///     {
    ///         MaxSizeGb = 500,
    ///         Region = "LON1",
    ///         AccessKeyId = backupIndex / objectStoreCredentialObjectStoreCredential.AccessKeyId,
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// using ID
    /// 
    /// ```sh
    ///  $ pulumi import civo:index/objectStoreCredential:ObjectStoreCredential custom_object b8ecd2ab-2267-4a5e-8692-cbf1d32583e3
    /// ```
    /// </summary>
    [CivoResourceType("civo:index/objectStoreCredential:ObjectStoreCredential")]
    public partial class ObjectStoreCredential : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The access key id of the Object Store Credential. It is generated by the provider.
        /// </summary>
        [Output("accessKeyId")]
        public Output<string> AccessKeyId { get; private set; } = null!;

        /// <summary>
        /// The name of the Object Store Credential. Must be unique.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The region where the Object Store Credential will be created.
        /// </summary>
        [Output("region")]
        public Output<string?> Region { get; private set; } = null!;

        /// <summary>
        /// The secret access key of the Object Store Credential. It is generated by the provider.
        /// </summary>
        [Output("secretAccessKey")]
        public Output<string> SecretAccessKey { get; private set; } = null!;

        /// <summary>
        /// The status of the Object Store Credential.
        /// </summary>
        [Output("status")]
        public Output<string> Status { get; private set; } = null!;


        /// <summary>
        /// Create a ObjectStoreCredential resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ObjectStoreCredential(string name, ObjectStoreCredentialArgs? args = null, CustomResourceOptions? options = null)
            : base("civo:index/objectStoreCredential:ObjectStoreCredential", name, args ?? new ObjectStoreCredentialArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ObjectStoreCredential(string name, Input<string> id, ObjectStoreCredentialState? state = null, CustomResourceOptions? options = null)
            : base("civo:index/objectStoreCredential:ObjectStoreCredential", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ObjectStoreCredential resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ObjectStoreCredential Get(string name, Input<string> id, ObjectStoreCredentialState? state = null, CustomResourceOptions? options = null)
        {
            return new ObjectStoreCredential(name, id, state, options);
        }
    }

    public sealed class ObjectStoreCredentialArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The access key id of the Object Store Credential. It is generated by the provider.
        /// </summary>
        [Input("accessKeyId")]
        public Input<string>? AccessKeyId { get; set; }

        /// <summary>
        /// The name of the Object Store Credential. Must be unique.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The region where the Object Store Credential will be created.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The secret access key of the Object Store Credential. It is generated by the provider.
        /// </summary>
        [Input("secretAccessKey")]
        public Input<string>? SecretAccessKey { get; set; }

        public ObjectStoreCredentialArgs()
        {
        }
        public static new ObjectStoreCredentialArgs Empty => new ObjectStoreCredentialArgs();
    }

    public sealed class ObjectStoreCredentialState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The access key id of the Object Store Credential. It is generated by the provider.
        /// </summary>
        [Input("accessKeyId")]
        public Input<string>? AccessKeyId { get; set; }

        /// <summary>
        /// The name of the Object Store Credential. Must be unique.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The region where the Object Store Credential will be created.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The secret access key of the Object Store Credential. It is generated by the provider.
        /// </summary>
        [Input("secretAccessKey")]
        public Input<string>? SecretAccessKey { get; set; }

        /// <summary>
        /// The status of the Object Store Credential.
        /// </summary>
        [Input("status")]
        public Input<string>? Status { get; set; }

        public ObjectStoreCredentialState()
        {
        }
        public static new ObjectStoreCredentialState Empty => new ObjectStoreCredentialState();
    }
}
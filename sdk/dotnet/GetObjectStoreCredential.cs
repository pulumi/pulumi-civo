// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Civo
{
    public static class GetObjectStoreCredential
    {
        /// <summary>
        /// Get information of an Object Store Credential for use in other resources. This data source provides all of the Object Store Credential's properties as configured on your Civo account.
        /// 
        /// Note: This data source returns a single Object Store Credential. When specifying a name, an error will be raised if more than one Object Store Credentials with the same name found.
        /// 
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Civo = Pulumi.Civo;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     // Read a credential for the object store
        ///     var backup = Civo.GetObjectStoreCredential.Invoke(new()
        ///     {
        ///         Name = "backup-server",
        ///     });
        /// 
        ///     // Use the credential to create a bucket
        ///     var backupObjectStore = new Civo.ObjectStore("backup", new()
        ///     {
        ///         Name = "backup-server",
        ///         MaxSizeGb = 500,
        ///         Region = "LON1",
        ///         AccessKeyId = backup.Apply(getObjectStoreCredentialResult =&gt; getObjectStoreCredentialResult.AccessKeyId),
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetObjectStoreCredentialResult> InvokeAsync(GetObjectStoreCredentialArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetObjectStoreCredentialResult>("civo:index/getObjectStoreCredential:getObjectStoreCredential", args ?? new GetObjectStoreCredentialArgs(), options.WithDefaults());

        /// <summary>
        /// Get information of an Object Store Credential for use in other resources. This data source provides all of the Object Store Credential's properties as configured on your Civo account.
        /// 
        /// Note: This data source returns a single Object Store Credential. When specifying a name, an error will be raised if more than one Object Store Credentials with the same name found.
        /// 
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Civo = Pulumi.Civo;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     // Read a credential for the object store
        ///     var backup = Civo.GetObjectStoreCredential.Invoke(new()
        ///     {
        ///         Name = "backup-server",
        ///     });
        /// 
        ///     // Use the credential to create a bucket
        ///     var backupObjectStore = new Civo.ObjectStore("backup", new()
        ///     {
        ///         Name = "backup-server",
        ///         MaxSizeGb = 500,
        ///         Region = "LON1",
        ///         AccessKeyId = backup.Apply(getObjectStoreCredentialResult =&gt; getObjectStoreCredentialResult.AccessKeyId),
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetObjectStoreCredentialResult> Invoke(GetObjectStoreCredentialInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetObjectStoreCredentialResult>("civo:index/getObjectStoreCredential:getObjectStoreCredential", args ?? new GetObjectStoreCredentialInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetObjectStoreCredentialArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the Object Store Credential
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// The name of the Object Store Credential
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// The region of an existing Object Store
        /// </summary>
        [Input("region")]
        public string? Region { get; set; }

        public GetObjectStoreCredentialArgs()
        {
        }
        public static new GetObjectStoreCredentialArgs Empty => new GetObjectStoreCredentialArgs();
    }

    public sealed class GetObjectStoreCredentialInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the Object Store Credential
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// The name of the Object Store Credential
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The region of an existing Object Store
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        public GetObjectStoreCredentialInvokeArgs()
        {
        }
        public static new GetObjectStoreCredentialInvokeArgs Empty => new GetObjectStoreCredentialInvokeArgs();
    }


    [OutputType]
    public sealed class GetObjectStoreCredentialResult
    {
        /// <summary>
        /// The access key id of the Object Store Credential
        /// </summary>
        public readonly string AccessKeyId;
        /// <summary>
        /// The ID of the Object Store Credential
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// The name of the Object Store Credential
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// The region of an existing Object Store
        /// </summary>
        public readonly string? Region;
        /// <summary>
        /// The secret access key of the Object Store Credential
        /// </summary>
        public readonly string SecretAccessKey;
        /// <summary>
        /// The status of the Object Store Credential
        /// </summary>
        public readonly string Status;

        [OutputConstructor]
        private GetObjectStoreCredentialResult(
            string accessKeyId,

            string? id,

            string? name,

            string? region,

            string secretAccessKey,

            string status)
        {
            AccessKeyId = accessKeyId;
            Id = id;
            Name = name;
            Region = region;
            SecretAccessKey = secretAccessKey;
            Status = status;
        }
    }
}

// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Civo
{
    public static class GetDatabase
    {
        /// <summary>
        /// Get information of an Database for use in other resources. This data source provides all of the Database's properties as configured on your Civo account.
        /// 
        /// Note: This data source returns a single Database. When specifying a name, an error will be raised if more than one Databases with the same name found.
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
        ///     var test = Civo.GetDatabase.Invoke(new()
        ///     {
        ///         Name = "test-database",
        ///         Region = "LON1",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetDatabaseResult> InvokeAsync(GetDatabaseArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDatabaseResult>("civo:index/getDatabase:getDatabase", args ?? new GetDatabaseArgs(), options.WithDefaults());

        /// <summary>
        /// Get information of an Database for use in other resources. This data source provides all of the Database's properties as configured on your Civo account.
        /// 
        /// Note: This data source returns a single Database. When specifying a name, an error will be raised if more than one Databases with the same name found.
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
        ///     var test = Civo.GetDatabase.Invoke(new()
        ///     {
        ///         Name = "test-database",
        ///         Region = "LON1",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetDatabaseResult> Invoke(GetDatabaseInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDatabaseResult>("civo:index/getDatabase:getDatabase", args ?? new GetDatabaseInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDatabaseArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the Database
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// The name of the Database
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// The region of an existing Database
        /// </summary>
        [Input("region")]
        public string? Region { get; set; }

        public GetDatabaseArgs()
        {
        }
        public static new GetDatabaseArgs Empty => new GetDatabaseArgs();
    }

    public sealed class GetDatabaseInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the Database
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// The name of the Database
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The region of an existing Database
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        public GetDatabaseInvokeArgs()
        {
        }
        public static new GetDatabaseInvokeArgs Empty => new GetDatabaseInvokeArgs();
    }


    [OutputType]
    public sealed class GetDatabaseResult
    {
        /// <summary>
        /// The DNS endpoint of the database
        /// </summary>
        public readonly string DnsEndpoint;
        /// <summary>
        /// The endpoint of the database
        /// </summary>
        public readonly string Endpoint;
        /// <summary>
        /// The engine of the database
        /// </summary>
        public readonly string Engine;
        /// <summary>
        /// The firewall id of the Database
        /// </summary>
        public readonly string FirewallId;
        /// <summary>
        /// The ID of the Database
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// The name of the Database
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// The network id of the Database
        /// </summary>
        public readonly string NetworkId;
        /// <summary>
        /// Count of nodes
        /// </summary>
        public readonly int Nodes;
        /// <summary>
        /// The password of the database
        /// </summary>
        public readonly string Password;
        /// <summary>
        /// The port of the database
        /// </summary>
        public readonly int Port;
        /// <summary>
        /// The region of an existing Database
        /// </summary>
        public readonly string Region;
        /// <summary>
        /// Size of the database
        /// </summary>
        public readonly string Size;
        /// <summary>
        /// The status of the database
        /// </summary>
        public readonly string Status;
        /// <summary>
        /// The username of the database
        /// </summary>
        public readonly string Username;
        /// <summary>
        /// The version of the database
        /// </summary>
        public readonly string Version;

        [OutputConstructor]
        private GetDatabaseResult(
            string dnsEndpoint,

            string endpoint,

            string engine,

            string firewallId,

            string? id,

            string? name,

            string networkId,

            int nodes,

            string password,

            int port,

            string region,

            string size,

            string status,

            string username,

            string version)
        {
            DnsEndpoint = dnsEndpoint;
            Endpoint = endpoint;
            Engine = engine;
            FirewallId = firewallId;
            Id = id;
            Name = name;
            NetworkId = networkId;
            Nodes = nodes;
            Password = password;
            Port = port;
            Region = region;
            Size = size;
            Status = status;
            Username = username;
            Version = version;
        }
    }
}

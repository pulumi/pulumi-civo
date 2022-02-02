// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Civo
{
    public static class GetNetwork
    {
        /// <summary>
        /// Retrieve information about a network for use in other resources.
        /// 
        /// This data source provides all of the network's properties as configured on your Civo account.
        /// 
        /// Networks may be looked up by id or label, and you can optionally pass region if you want to make a lookup for an expecific network inside that region.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Civo = Pulumi.Civo;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var test = Output.Create(Civo.GetNetwork.InvokeAsync(new Civo.GetNetworkArgs
        ///         {
        ///             Label = "test-network",
        ///             Region = "NYC1",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetNetworkResult> InvokeAsync(GetNetworkArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetNetworkResult>("civo:index/getNetwork:getNetwork", args ?? new GetNetworkArgs(), options.WithDefaults());

        /// <summary>
        /// Retrieve information about a network for use in other resources.
        /// 
        /// This data source provides all of the network's properties as configured on your Civo account.
        /// 
        /// Networks may be looked up by id or label, and you can optionally pass region if you want to make a lookup for an expecific network inside that region.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Civo = Pulumi.Civo;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var test = Output.Create(Civo.GetNetwork.InvokeAsync(new Civo.GetNetworkArgs
        ///         {
        ///             Label = "test-network",
        ///             Region = "NYC1",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetNetworkResult> Invoke(GetNetworkInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetNetworkResult>("civo:index/getNetwork:getNetwork", args ?? new GetNetworkInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetNetworkArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of this resource.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// The label of an existing network
        /// </summary>
        [Input("label")]
        public string? Label { get; set; }

        /// <summary>
        /// The region of an existing network
        /// </summary>
        [Input("region")]
        public string? Region { get; set; }

        public GetNetworkArgs()
        {
        }
    }

    public sealed class GetNetworkInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of this resource.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// The label of an existing network
        /// </summary>
        [Input("label")]
        public Input<string>? Label { get; set; }

        /// <summary>
        /// The region of an existing network
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        public GetNetworkInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetNetworkResult
    {
        /// <summary>
        /// If is the default network
        /// </summary>
        public readonly bool Default;
        /// <summary>
        /// The ID of this resource.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// The label of an existing network
        /// </summary>
        public readonly string? Label;
        /// <summary>
        /// The name of the network
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The region of an existing network
        /// </summary>
        public readonly string? Region;

        [OutputConstructor]
        private GetNetworkResult(
            bool @default,

            string? id,

            string? label,

            string name,

            string? region)
        {
            Default = @default;
            Id = id;
            Label = label;
            Name = name;
            Region = region;
        }
    }
}

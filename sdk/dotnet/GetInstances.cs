// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Civo
{
    public static class GetInstances
    {
        /// <summary>
        /// Get information on instances for use in other resources, with the ability to filter and sort the results. If no filters are specified, all instances will be returned.
        /// 
        /// Note: You can use the `civo.Instance` data source to obtain metadata about a single instance if you already know the id, unique hostname, or unique tag to retrieve.
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
        ///         var small_size = Output.Create(Civo.GetInstances.InvokeAsync(new Civo.GetInstancesArgs
        ///         {
        ///             Region = "NYC1",
        ///             Filters = 
        ///             {
        ///                 new Civo.Inputs.GetInstancesFilterArgs
        ///                 {
        ///                     Key = "size",
        ///                     Values = 
        ///                     {
        ///                         g3.Small,
        ///                     },
        ///                 },
        ///             },
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetInstancesResult> InvokeAsync(GetInstancesArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetInstancesResult>("civo:index/getInstances:getInstances", args ?? new GetInstancesArgs(), options.WithDefaults());

        /// <summary>
        /// Get information on instances for use in other resources, with the ability to filter and sort the results. If no filters are specified, all instances will be returned.
        /// 
        /// Note: You can use the `civo.Instance` data source to obtain metadata about a single instance if you already know the id, unique hostname, or unique tag to retrieve.
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
        ///         var small_size = Output.Create(Civo.GetInstances.InvokeAsync(new Civo.GetInstancesArgs
        ///         {
        ///             Region = "NYC1",
        ///             Filters = 
        ///             {
        ///                 new Civo.Inputs.GetInstancesFilterArgs
        ///                 {
        ///                     Key = "size",
        ///                     Values = 
        ///                     {
        ///                         g3.Small,
        ///                     },
        ///                 },
        ///             },
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetInstancesResult> Invoke(GetInstancesInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetInstancesResult>("civo:index/getInstances:getInstances", args ?? new GetInstancesInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetInstancesArgs : Pulumi.InvokeArgs
    {
        [Input("filters")]
        private List<Inputs.GetInstancesFilterArgs>? _filters;

        /// <summary>
        /// One or more key/value pairs on which to filter results
        /// </summary>
        public List<Inputs.GetInstancesFilterArgs> Filters
        {
            get => _filters ?? (_filters = new List<Inputs.GetInstancesFilterArgs>());
            set => _filters = value;
        }

        /// <summary>
        /// If used, all instances will be from the provided region
        /// </summary>
        [Input("region")]
        public string? Region { get; set; }

        [Input("sorts")]
        private List<Inputs.GetInstancesSortArgs>? _sorts;

        /// <summary>
        /// One or more key/direction pairs on which to sort results
        /// </summary>
        public List<Inputs.GetInstancesSortArgs> Sorts
        {
            get => _sorts ?? (_sorts = new List<Inputs.GetInstancesSortArgs>());
            set => _sorts = value;
        }

        public GetInstancesArgs()
        {
        }
    }

    public sealed class GetInstancesInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("filters")]
        private InputList<Inputs.GetInstancesFilterInputArgs>? _filters;

        /// <summary>
        /// One or more key/value pairs on which to filter results
        /// </summary>
        public InputList<Inputs.GetInstancesFilterInputArgs> Filters
        {
            get => _filters ?? (_filters = new InputList<Inputs.GetInstancesFilterInputArgs>());
            set => _filters = value;
        }

        /// <summary>
        /// If used, all instances will be from the provided region
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        [Input("sorts")]
        private InputList<Inputs.GetInstancesSortInputArgs>? _sorts;

        /// <summary>
        /// One or more key/direction pairs on which to sort results
        /// </summary>
        public InputList<Inputs.GetInstancesSortInputArgs> Sorts
        {
            get => _sorts ?? (_sorts = new InputList<Inputs.GetInstancesSortInputArgs>());
            set => _sorts = value;
        }

        public GetInstancesInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetInstancesResult
    {
        /// <summary>
        /// One or more key/value pairs on which to filter results
        /// </summary>
        public readonly ImmutableArray<Outputs.GetInstancesFilterResult> Filters;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly ImmutableArray<Outputs.GetInstancesInstanceResult> Instances;
        /// <summary>
        /// If used, all instances will be from the provided region
        /// </summary>
        public readonly string? Region;
        /// <summary>
        /// One or more key/direction pairs on which to sort results
        /// </summary>
        public readonly ImmutableArray<Outputs.GetInstancesSortResult> Sorts;

        [OutputConstructor]
        private GetInstancesResult(
            ImmutableArray<Outputs.GetInstancesFilterResult> filters,

            string id,

            ImmutableArray<Outputs.GetInstancesInstanceResult> instances,

            string? region,

            ImmutableArray<Outputs.GetInstancesSortResult> sorts)
        {
            Filters = filters;
            Id = id;
            Instances = instances;
            Region = region;
            Sorts = sorts;
        }
    }
}

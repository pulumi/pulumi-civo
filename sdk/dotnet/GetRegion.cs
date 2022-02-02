// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Civo
{
    public static class GetRegion
    {
        /// <summary>
        /// Retrieves information about the region that Civo supports, with the ability to filter the results.
        /// </summary>
        public static Task<GetRegionResult> InvokeAsync(GetRegionArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetRegionResult>("civo:index/getRegion:getRegion", args ?? new GetRegionArgs(), options.WithDefaults());

        /// <summary>
        /// Retrieves information about the region that Civo supports, with the ability to filter the results.
        /// </summary>
        public static Output<GetRegionResult> Invoke(GetRegionInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetRegionResult>("civo:index/getRegion:getRegion", args ?? new GetRegionInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetRegionArgs : Pulumi.InvokeArgs
    {
        [Input("filters")]
        private List<Inputs.GetRegionFilterArgs>? _filters;

        /// <summary>
        /// One or more key/value pairs on which to filter results
        /// </summary>
        public List<Inputs.GetRegionFilterArgs> Filters
        {
            get => _filters ?? (_filters = new List<Inputs.GetRegionFilterArgs>());
            set => _filters = value;
        }

        [Input("sorts")]
        private List<Inputs.GetRegionSortArgs>? _sorts;

        /// <summary>
        /// One or more key/direction pairs on which to sort results
        /// </summary>
        public List<Inputs.GetRegionSortArgs> Sorts
        {
            get => _sorts ?? (_sorts = new List<Inputs.GetRegionSortArgs>());
            set => _sorts = value;
        }

        public GetRegionArgs()
        {
        }
    }

    public sealed class GetRegionInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("filters")]
        private InputList<Inputs.GetRegionFilterInputArgs>? _filters;

        /// <summary>
        /// One or more key/value pairs on which to filter results
        /// </summary>
        public InputList<Inputs.GetRegionFilterInputArgs> Filters
        {
            get => _filters ?? (_filters = new InputList<Inputs.GetRegionFilterInputArgs>());
            set => _filters = value;
        }

        [Input("sorts")]
        private InputList<Inputs.GetRegionSortInputArgs>? _sorts;

        /// <summary>
        /// One or more key/direction pairs on which to sort results
        /// </summary>
        public InputList<Inputs.GetRegionSortInputArgs> Sorts
        {
            get => _sorts ?? (_sorts = new InputList<Inputs.GetRegionSortInputArgs>());
            set => _sorts = value;
        }

        public GetRegionInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetRegionResult
    {
        /// <summary>
        /// One or more key/value pairs on which to filter results
        /// </summary>
        public readonly ImmutableArray<Outputs.GetRegionFilterResult> Filters;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly ImmutableArray<Outputs.GetRegionRegionResult> Regions;
        /// <summary>
        /// One or more key/direction pairs on which to sort results
        /// </summary>
        public readonly ImmutableArray<Outputs.GetRegionSortResult> Sorts;

        [OutputConstructor]
        private GetRegionResult(
            ImmutableArray<Outputs.GetRegionFilterResult> filters,

            string id,

            ImmutableArray<Outputs.GetRegionRegionResult> regions,

            ImmutableArray<Outputs.GetRegionSortResult> sorts)
        {
            Filters = filters;
            Id = id;
            Regions = regions;
            Sorts = sorts;
        }
    }
}

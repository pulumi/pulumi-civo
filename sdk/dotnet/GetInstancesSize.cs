// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Civo
{
    public static class GetInstancesSize
    {
        public static Task<GetInstancesSizeResult> InvokeAsync(GetInstancesSizeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetInstancesSizeResult>("civo:index/getInstancesSize:getInstancesSize", args ?? new GetInstancesSizeArgs(), options.WithVersion());
    }


    public sealed class GetInstancesSizeArgs : Pulumi.InvokeArgs
    {
        [Input("filters")]
        private List<Inputs.GetInstancesSizeFilterArgs>? _filters;
        public List<Inputs.GetInstancesSizeFilterArgs> Filters
        {
            get => _filters ?? (_filters = new List<Inputs.GetInstancesSizeFilterArgs>());
            set => _filters = value;
        }

        [Input("sorts")]
        private List<Inputs.GetInstancesSizeSortArgs>? _sorts;
        public List<Inputs.GetInstancesSizeSortArgs> Sorts
        {
            get => _sorts ?? (_sorts = new List<Inputs.GetInstancesSizeSortArgs>());
            set => _sorts = value;
        }

        public GetInstancesSizeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetInstancesSizeResult
    {
        public readonly ImmutableArray<Outputs.GetInstancesSizeFilterResult> Filters;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly ImmutableArray<Outputs.GetInstancesSizeSizeResult> Sizes;
        public readonly ImmutableArray<Outputs.GetInstancesSizeSortResult> Sorts;

        [OutputConstructor]
        private GetInstancesSizeResult(
            ImmutableArray<Outputs.GetInstancesSizeFilterResult> filters,

            string id,

            ImmutableArray<Outputs.GetInstancesSizeSizeResult> sizes,

            ImmutableArray<Outputs.GetInstancesSizeSortResult> sorts)
        {
            Filters = filters;
            Id = id;
            Sizes = sizes;
            Sorts = sorts;
        }
    }
}

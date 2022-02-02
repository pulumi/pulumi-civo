// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Civo
{
    public static class GetDiskImage
    {
        /// <summary>
        /// Get information on an disk image for use in other resources (e.g. creating a instance) with the ability to filter the results.
        /// </summary>
        public static Task<GetDiskImageResult> InvokeAsync(GetDiskImageArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetDiskImageResult>("civo:index/getDiskImage:getDiskImage", args ?? new GetDiskImageArgs(), options.WithDefaults());

        /// <summary>
        /// Get information on an disk image for use in other resources (e.g. creating a instance) with the ability to filter the results.
        /// </summary>
        public static Output<GetDiskImageResult> Invoke(GetDiskImageInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetDiskImageResult>("civo:index/getDiskImage:getDiskImage", args ?? new GetDiskImageInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDiskImageArgs : Pulumi.InvokeArgs
    {
        [Input("filters")]
        private List<Inputs.GetDiskImageFilterArgs>? _filters;

        /// <summary>
        /// One or more key/value pairs on which to filter results
        /// </summary>
        public List<Inputs.GetDiskImageFilterArgs> Filters
        {
            get => _filters ?? (_filters = new List<Inputs.GetDiskImageFilterArgs>());
            set => _filters = value;
        }

        /// <summary>
        /// If is used, all disk image will be from this region. Required if no region is set in provider.
        /// </summary>
        [Input("region")]
        public string? Region { get; set; }

        [Input("sorts")]
        private List<Inputs.GetDiskImageSortArgs>? _sorts;

        /// <summary>
        /// One or more key/direction pairs on which to sort results
        /// </summary>
        public List<Inputs.GetDiskImageSortArgs> Sorts
        {
            get => _sorts ?? (_sorts = new List<Inputs.GetDiskImageSortArgs>());
            set => _sorts = value;
        }

        public GetDiskImageArgs()
        {
        }
    }

    public sealed class GetDiskImageInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("filters")]
        private InputList<Inputs.GetDiskImageFilterInputArgs>? _filters;

        /// <summary>
        /// One or more key/value pairs on which to filter results
        /// </summary>
        public InputList<Inputs.GetDiskImageFilterInputArgs> Filters
        {
            get => _filters ?? (_filters = new InputList<Inputs.GetDiskImageFilterInputArgs>());
            set => _filters = value;
        }

        /// <summary>
        /// If is used, all disk image will be from this region. Required if no region is set in provider.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        [Input("sorts")]
        private InputList<Inputs.GetDiskImageSortInputArgs>? _sorts;

        /// <summary>
        /// One or more key/direction pairs on which to sort results
        /// </summary>
        public InputList<Inputs.GetDiskImageSortInputArgs> Sorts
        {
            get => _sorts ?? (_sorts = new InputList<Inputs.GetDiskImageSortInputArgs>());
            set => _sorts = value;
        }

        public GetDiskImageInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetDiskImageResult
    {
        public readonly ImmutableArray<Outputs.GetDiskImageDiskimageResult> Diskimages;
        /// <summary>
        /// One or more key/value pairs on which to filter results
        /// </summary>
        public readonly ImmutableArray<Outputs.GetDiskImageFilterResult> Filters;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// If is used, all disk image will be from this region. Required if no region is set in provider.
        /// </summary>
        public readonly string? Region;
        /// <summary>
        /// One or more key/direction pairs on which to sort results
        /// </summary>
        public readonly ImmutableArray<Outputs.GetDiskImageSortResult> Sorts;

        [OutputConstructor]
        private GetDiskImageResult(
            ImmutableArray<Outputs.GetDiskImageDiskimageResult> diskimages,

            ImmutableArray<Outputs.GetDiskImageFilterResult> filters,

            string id,

            string? region,

            ImmutableArray<Outputs.GetDiskImageSortResult> sorts)
        {
            Diskimages = diskimages;
            Filters = filters;
            Id = id;
            Region = region;
            Sorts = sorts;
        }
    }
}

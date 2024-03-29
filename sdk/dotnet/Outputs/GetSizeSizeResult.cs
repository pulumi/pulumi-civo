// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Civo.Outputs
{

    [OutputType]
    public sealed class GetSizeSizeResult
    {
        /// <summary>
        /// Total of CPU
        /// </summary>
        public readonly int Cpu;
        /// <summary>
        /// A description of the instance size
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// The size of SSD
        /// </summary>
        public readonly int Disk;
        /// <summary>
        /// Total of GPU
        /// </summary>
        public readonly int Gpu;
        /// <summary>
        /// GPU type
        /// </summary>
        public readonly string GpuType;
        /// <summary>
        /// The name of the size
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Total of RAM
        /// </summary>
        public readonly int Ram;
        /// <summary>
        /// If can use the instance size
        /// </summary>
        public readonly bool Selectable;
        /// <summary>
        /// A human name of the size
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private GetSizeSizeResult(
            int cpu,

            string description,

            int disk,

            int gpu,

            string gpuType,

            string name,

            int ram,

            bool selectable,

            string type)
        {
            Cpu = cpu;
            Description = description;
            Disk = disk;
            Gpu = gpu;
            GpuType = gpuType;
            Name = name;
            Ram = ram;
            Selectable = selectable;
            Type = type;
        }
    }
}

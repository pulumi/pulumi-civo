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
        public readonly int Cpu;
        public readonly string Description;
        public readonly int Disk;
        public readonly int Gpu;
        public readonly string GpuType;
        public readonly string Name;
        public readonly int Ram;
        public readonly bool Selectable;
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

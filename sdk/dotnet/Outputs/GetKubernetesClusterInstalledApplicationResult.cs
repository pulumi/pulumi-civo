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
    public sealed class GetKubernetesClusterInstalledApplicationResult
    {
        /// <summary>
        /// The name of the application
        /// </summary>
        public readonly string Application;
        /// <summary>
        /// The category of the application
        /// </summary>
        public readonly string Category;
        /// <summary>
        /// If the application is installed, this will return `true`
        /// </summary>
        public readonly bool Installed;
        /// <summary>
        /// The version of the application
        /// </summary>
        public readonly string Version;

        [OutputConstructor]
        private GetKubernetesClusterInstalledApplicationResult(
            string application,

            string category,

            bool installed,

            string version)
        {
            Application = application;
            Category = category;
            Installed = installed;
            Version = version;
        }
    }
}

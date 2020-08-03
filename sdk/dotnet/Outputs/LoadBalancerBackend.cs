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
    public sealed class LoadBalancerBackend
    {
        public readonly string InstanceId;
        public readonly int Port;
        public readonly string Protocol;

        [OutputConstructor]
        private LoadBalancerBackend(
            string instanceId,

            int port,

            string protocol)
        {
            InstanceId = instanceId;
            Port = port;
            Protocol = protocol;
        }
    }
}

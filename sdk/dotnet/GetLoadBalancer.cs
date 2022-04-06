// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Civo
{
    public static class GetLoadBalancer
    {
        /// <summary>
        /// Get information on a load balancer for use in other resources. This data source provides all of the load balancers properties as configured on your Civo account.
        /// 
        /// An error will be raised if the provided load balancer name does not exist in your Civo account.
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
        ///         var my_lb = Output.Create(Civo.GetLoadBalancer.InvokeAsync(new Civo.GetLoadBalancerArgs
        ///         {
        ///             Name = "lb-name",
        ///             Region = "LON1",
        ///         }));
        ///         this.CivoLoadbalancerOutput = my_lb.Apply(my_lb =&gt; my_lb.PublicIp);
        ///     }
        /// 
        ///     [Output("civoLoadbalancerOutput")]
        ///     public Output&lt;string&gt; CivoLoadbalancerOutput { get; set; }
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetLoadBalancerResult> InvokeAsync(GetLoadBalancerArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetLoadBalancerResult>("civo:index/getLoadBalancer:getLoadBalancer", args ?? new GetLoadBalancerArgs(), options.WithDefaults());

        /// <summary>
        /// Get information on a load balancer for use in other resources. This data source provides all of the load balancers properties as configured on your Civo account.
        /// 
        /// An error will be raised if the provided load balancer name does not exist in your Civo account.
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
        ///         var my_lb = Output.Create(Civo.GetLoadBalancer.InvokeAsync(new Civo.GetLoadBalancerArgs
        ///         {
        ///             Name = "lb-name",
        ///             Region = "LON1",
        ///         }));
        ///         this.CivoLoadbalancerOutput = my_lb.Apply(my_lb =&gt; my_lb.PublicIp);
        ///     }
        /// 
        ///     [Output("civoLoadbalancerOutput")]
        ///     public Output&lt;string&gt; CivoLoadbalancerOutput { get; set; }
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetLoadBalancerResult> Invoke(GetLoadBalancerInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetLoadBalancerResult>("civo:index/getLoadBalancer:getLoadBalancer", args ?? new GetLoadBalancerInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetLoadBalancerArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The id of the load balancer to retrieve (You can find this id from service annotations 'kubernetes.civo.com/loadbalancer-id')
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// The name of the load balancer (You can find this name from service annotations 'kubernetes.civo.com/loadbalancer-name')
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// The region of the load balancer, if you delcare this field, the datasource will use this value instead of the one defined in the provider
        /// </summary>
        [Input("region")]
        public string? Region { get; set; }

        public GetLoadBalancerArgs()
        {
        }
    }

    public sealed class GetLoadBalancerInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The id of the load balancer to retrieve (You can find this id from service annotations 'kubernetes.civo.com/loadbalancer-id')
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// The name of the load balancer (You can find this name from service annotations 'kubernetes.civo.com/loadbalancer-name')
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The region of the load balancer, if you delcare this field, the datasource will use this value instead of the one defined in the provider
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        public GetLoadBalancerInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetLoadBalancerResult
    {
        /// <summary>
        /// The algorithm used by the load balancer
        /// </summary>
        public readonly string Algorithm;
        public readonly ImmutableArray<Outputs.GetLoadBalancerBackendResult> Backends;
        /// <summary>
        /// The cluster id of the load balancer
        /// </summary>
        public readonly string ClusterId;
        /// <summary>
        /// The enabled proxy protocol of the load balancer
        /// </summary>
        public readonly string EnableProxyProtocol;
        /// <summary>
        /// The external traffic policy of the load balancer
        /// </summary>
        public readonly string ExternalTrafficPolicy;
        /// <summary>
        /// The firewall id of the load balancer
        /// </summary>
        public readonly string FirewallId;
        /// <summary>
        /// The id of the load balancer to retrieve (You can find this id from service annotations 'kubernetes.civo.com/loadbalancer-id')
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// The name of the load balancer (You can find this name from service annotations 'kubernetes.civo.com/loadbalancer-name')
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// The private ip of the load balancer
        /// </summary>
        public readonly string PrivateIp;
        /// <summary>
        /// The public ip of the load balancer
        /// </summary>
        public readonly string PublicIp;
        /// <summary>
        /// The region of the load balancer, if you delcare this field, the datasource will use this value instead of the one defined in the provider
        /// </summary>
        public readonly string? Region;
        /// <summary>
        /// The session affinity of the load balancer
        /// </summary>
        public readonly string SessionAffinity;
        /// <summary>
        /// The session affinity config timeout of the load balancer
        /// </summary>
        public readonly int SessionAffinityConfigTimeout;
        /// <summary>
        /// The state of the load balancer
        /// </summary>
        public readonly string State;

        [OutputConstructor]
        private GetLoadBalancerResult(
            string algorithm,

            ImmutableArray<Outputs.GetLoadBalancerBackendResult> backends,

            string clusterId,

            string enableProxyProtocol,

            string externalTrafficPolicy,

            string firewallId,

            string? id,

            string? name,

            string privateIp,

            string publicIp,

            string? region,

            string sessionAffinity,

            int sessionAffinityConfigTimeout,

            string state)
        {
            Algorithm = algorithm;
            Backends = backends;
            ClusterId = clusterId;
            EnableProxyProtocol = enableProxyProtocol;
            ExternalTrafficPolicy = externalTrafficPolicy;
            FirewallId = firewallId;
            Id = id;
            Name = name;
            PrivateIp = privateIp;
            PublicIp = publicIp;
            Region = region;
            SessionAffinity = sessionAffinity;
            SessionAffinityConfigTimeout = sessionAffinityConfigTimeout;
            State = state;
        }
    }
}

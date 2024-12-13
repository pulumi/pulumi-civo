// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Civo
{
    public static class GetDnsDomainName
    {
        /// <summary>
        /// Get information on a domain. This data source provides the name and the id.
        /// 
        /// An error will be raised if the provided domain name is not in your Civo account.
        /// 
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Civo = Pulumi.Civo;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var domain = Civo.GetDnsDomainName.Invoke(new()
        ///     {
        ///         Name = "domain.com",
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["domainOutput"] = domain.Apply(getDnsDomainNameResult =&gt; getDnsDomainNameResult.Name),
        ///         ["domainIdOutput"] = domain.Apply(getDnsDomainNameResult =&gt; getDnsDomainNameResult.Id),
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Task<GetDnsDomainNameResult> InvokeAsync(GetDnsDomainNameArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDnsDomainNameResult>("civo:index/getDnsDomainName:getDnsDomainName", args ?? new GetDnsDomainNameArgs(), options.WithDefaults());

        /// <summary>
        /// Get information on a domain. This data source provides the name and the id.
        /// 
        /// An error will be raised if the provided domain name is not in your Civo account.
        /// 
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Civo = Pulumi.Civo;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var domain = Civo.GetDnsDomainName.Invoke(new()
        ///     {
        ///         Name = "domain.com",
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["domainOutput"] = domain.Apply(getDnsDomainNameResult =&gt; getDnsDomainNameResult.Name),
        ///         ["domainIdOutput"] = domain.Apply(getDnsDomainNameResult =&gt; getDnsDomainNameResult.Id),
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Output<GetDnsDomainNameResult> Invoke(GetDnsDomainNameInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDnsDomainNameResult>("civo:index/getDnsDomainName:getDnsDomainName", args ?? new GetDnsDomainNameInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// Get information on a domain. This data source provides the name and the id.
        /// 
        /// An error will be raised if the provided domain name is not in your Civo account.
        /// 
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Civo = Pulumi.Civo;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var domain = Civo.GetDnsDomainName.Invoke(new()
        ///     {
        ///         Name = "domain.com",
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["domainOutput"] = domain.Apply(getDnsDomainNameResult =&gt; getDnsDomainNameResult.Name),
        ///         ["domainIdOutput"] = domain.Apply(getDnsDomainNameResult =&gt; getDnsDomainNameResult.Id),
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Output<GetDnsDomainNameResult> Invoke(GetDnsDomainNameInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetDnsDomainNameResult>("civo:index/getDnsDomainName:getDnsDomainName", args ?? new GetDnsDomainNameInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDnsDomainNameArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of this resource.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// The name of the domain
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        public GetDnsDomainNameArgs()
        {
        }
        public static new GetDnsDomainNameArgs Empty => new GetDnsDomainNameArgs();
    }

    public sealed class GetDnsDomainNameInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of this resource.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// The name of the domain
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public GetDnsDomainNameInvokeArgs()
        {
        }
        public static new GetDnsDomainNameInvokeArgs Empty => new GetDnsDomainNameInvokeArgs();
    }


    [OutputType]
    public sealed class GetDnsDomainNameResult
    {
        /// <summary>
        /// The ID of this resource.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// The name of the domain
        /// </summary>
        public readonly string? Name;

        [OutputConstructor]
        private GetDnsDomainNameResult(
            string? id,

            string? name)
        {
            Id = id;
            Name = name;
        }
    }
}

// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Immutable;

namespace Pulumi.Civo
{
    public static class Config
    {
        [global::System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "IDE1006", Justification = 
        "Double underscore prefix used to avoid conflicts with variable names.")]
        private sealed class __Value<T>
        {
            private readonly Func<T> _getter;
            private T _value = default!;
            private bool _set;

            public __Value(Func<T> getter)
            {
                _getter = getter;
            }

            public T Get() => _set ? _value : _getter();

            public void Set(T value)
            {
                _value = value;
                _set = true;
            }
        }

        private static readonly global::Pulumi.Config __config = new global::Pulumi.Config("civo");

        private static readonly __Value<string?> _apiEndpoint = new __Value<string?>(() => __config.Get("apiEndpoint"));
        /// <summary>
        /// The Base URL to use for CIVO API.
        /// </summary>
        public static string? ApiEndpoint
        {
            get => _apiEndpoint.Get();
            set => _apiEndpoint.Set(value);
        }

        private static readonly __Value<string?> _credentialsFile = new __Value<string?>(() => __config.Get("credentialsFile"));
        /// <summary>
        /// Path to the Civo credentials file. Can be specified using CIVO_CREDENTIAL_FILE environment variable.
        /// </summary>
        public static string? CredentialsFile
        {
            get => _credentialsFile.Get();
            set => _credentialsFile.Set(value);
        }

        private static readonly __Value<string?> _region = new __Value<string?>(() => __config.Get("region"));
        /// <summary>
        /// If region is not set, then no region will be used and them you need expensify in every resource even if you expensify
        /// here you can overwrite in a resource.
        /// </summary>
        public static string? Region
        {
            get => _region.Get();
            set => _region.Set(value);
        }

        private static readonly __Value<string?> _token = new __Value<string?>(() => __config.Get("token"));
        /// <summary>
        /// This is the Civo API token. Alternatively, this can also be specified using `CIVO_TOKEN` environment variable.
        /// </summary>
        public static string? Token
        {
            get => _token.Get();
            set => _token.Set(value);
        }

    }
}

// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Civo
{
    /// <summary>
    /// Provides a resource which can be used to create a snapshot from an existing Civo Instance.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Civo = Pulumi.Civo;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var myinstance_backup = new Civo.Snapshot("myinstance-backup", new Civo.SnapshotArgs
    ///         {
    ///             InstanceId = civo_instance.Myinstance.Id,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class Snapshot : Pulumi.CustomResource
    {
        /// <summary>
        /// The date where the snapshot was completed.
        /// </summary>
        [Output("completedAt")]
        public Output<string> CompletedAt { get; private set; } = null!;

        /// <summary>
        /// If a valid cron string is passed, the snapshot will be saved as an automated snapshot 
        /// continuing to automatically update based on the schedule of the cron sequence provided
        /// The default is nil meaning the snapshot will be saved as a one-off snapshot.
        /// </summary>
        [Output("cronTiming")]
        public Output<string?> CronTiming { get; private set; } = null!;

        /// <summary>
        /// The hostname of the instance.
        /// </summary>
        [Output("hostname")]
        public Output<string> Hostname { get; private set; } = null!;

        /// <summary>
        /// The ID of the Instance from which the snapshot will be taken.
        /// </summary>
        [Output("instanceId")]
        public Output<string> InstanceId { get; private set; } = null!;

        /// <summary>
        /// A name for the instance snapshot.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// if cron was define this date will be the next execution date.
        /// </summary>
        [Output("nextExecution")]
        public Output<string> NextExecution { get; private set; } = null!;

        /// <summary>
        /// The region where the snapshot was take.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// The date where the snapshot was requested.
        /// </summary>
        [Output("requestedAt")]
        public Output<string> RequestedAt { get; private set; } = null!;

        /// <summary>
        /// If `true` the instance will be shut down during the snapshot to ensure all files 
        /// are in a consistent state (e.g. database tables aren't in the middle of being optimised
        /// and hence risking corruption). The default is `false` so you experience no interruption
        /// of service, but a small risk of corruption.
        /// </summary>
        [Output("safe")]
        public Output<bool?> Safe { get; private set; } = null!;

        /// <summary>
        /// The size of the snapshot in GB.
        /// </summary>
        [Output("sizeGb")]
        public Output<int> SizeGb { get; private set; } = null!;

        /// <summary>
        /// The status of the snapshot.
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;

        /// <summary>
        /// The template id.
        /// </summary>
        [Output("templateId")]
        public Output<string> TemplateId { get; private set; } = null!;


        /// <summary>
        /// Create a Snapshot resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Snapshot(string name, SnapshotArgs args, CustomResourceOptions? options = null)
            : base("civo:index/snapshot:Snapshot", name, args ?? new SnapshotArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Snapshot(string name, Input<string> id, SnapshotState? state = null, CustomResourceOptions? options = null)
            : base("civo:index/snapshot:Snapshot", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Snapshot resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Snapshot Get(string name, Input<string> id, SnapshotState? state = null, CustomResourceOptions? options = null)
        {
            return new Snapshot(name, id, state, options);
        }
    }

    public sealed class SnapshotArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// If a valid cron string is passed, the snapshot will be saved as an automated snapshot 
        /// continuing to automatically update based on the schedule of the cron sequence provided
        /// The default is nil meaning the snapshot will be saved as a one-off snapshot.
        /// </summary>
        [Input("cronTiming")]
        public Input<string>? CronTiming { get; set; }

        /// <summary>
        /// The ID of the Instance from which the snapshot will be taken.
        /// </summary>
        [Input("instanceId", required: true)]
        public Input<string> InstanceId { get; set; } = null!;

        /// <summary>
        /// A name for the instance snapshot.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// If `true` the instance will be shut down during the snapshot to ensure all files 
        /// are in a consistent state (e.g. database tables aren't in the middle of being optimised
        /// and hence risking corruption). The default is `false` so you experience no interruption
        /// of service, but a small risk of corruption.
        /// </summary>
        [Input("safe")]
        public Input<bool>? Safe { get; set; }

        public SnapshotArgs()
        {
        }
    }

    public sealed class SnapshotState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The date where the snapshot was completed.
        /// </summary>
        [Input("completedAt")]
        public Input<string>? CompletedAt { get; set; }

        /// <summary>
        /// If a valid cron string is passed, the snapshot will be saved as an automated snapshot 
        /// continuing to automatically update based on the schedule of the cron sequence provided
        /// The default is nil meaning the snapshot will be saved as a one-off snapshot.
        /// </summary>
        [Input("cronTiming")]
        public Input<string>? CronTiming { get; set; }

        /// <summary>
        /// The hostname of the instance.
        /// </summary>
        [Input("hostname")]
        public Input<string>? Hostname { get; set; }

        /// <summary>
        /// The ID of the Instance from which the snapshot will be taken.
        /// </summary>
        [Input("instanceId")]
        public Input<string>? InstanceId { get; set; }

        /// <summary>
        /// A name for the instance snapshot.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// if cron was define this date will be the next execution date.
        /// </summary>
        [Input("nextExecution")]
        public Input<string>? NextExecution { get; set; }

        /// <summary>
        /// The region where the snapshot was take.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The date where the snapshot was requested.
        /// </summary>
        [Input("requestedAt")]
        public Input<string>? RequestedAt { get; set; }

        /// <summary>
        /// If `true` the instance will be shut down during the snapshot to ensure all files 
        /// are in a consistent state (e.g. database tables aren't in the middle of being optimised
        /// and hence risking corruption). The default is `false` so you experience no interruption
        /// of service, but a small risk of corruption.
        /// </summary>
        [Input("safe")]
        public Input<bool>? Safe { get; set; }

        /// <summary>
        /// The size of the snapshot in GB.
        /// </summary>
        [Input("sizeGb")]
        public Input<int>? SizeGb { get; set; }

        /// <summary>
        /// The status of the snapshot.
        /// </summary>
        [Input("state")]
        public Input<string>? State { get; set; }

        /// <summary>
        /// The template id.
        /// </summary>
        [Input("templateId")]
        public Input<string>? TemplateId { get; set; }

        public SnapshotState()
        {
        }
    }
}

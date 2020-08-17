import * as pulumi from "@pulumi/pulumi";
import * as k8s from "@pulumi/kubernetes";

export interface AmbassadorIngressDeploymentArgs {
}

export class AmbassadorIngressDeployment extends pulumi.ComponentResource {
    public ingressControllerService: pulumi.Output<k8s.core.v1.Service>;
    public ingressControllerNamespace: pulumi.Output<string>;
    public ingressIps: pulumi.Output<string[]>;

    constructor(name: string, args: AmbassadorIngressDeploymentArgs, opts?: pulumi.ComponentResourceOptions) {
        super("pulumicivo:k8s:AmbassadorIngressDeployment", name, {}, opts);

        const ambassadorCrdCG = new k8s.yaml.ConfigGroup(`${name}-crd-manifests`,
            {
                files: "ingress-ambassador/yaml/crd.yaml"
            },
            {
                parent: this
            }
        );

        const ambassadorNamespace = new k8s.core.v1.Namespace(`${name}-namespace`,
            {
                metadata: {
                    name: "ambassador"
                }
            },
            {
                parent: this,
                dependsOn: [ ambassadorCrdCG ]
            }
        );

        const ambassadorCG = new k8s.yaml.ConfigGroup(`${name}-manifests`,
            {
                files: [
                    "ingress-ambassador/yaml/ambassador-rbac.yaml",
                    "ingress-ambassador/yaml/ambassador-service.yaml",
                    "ingress-ambassador/yaml/ambassador-config.yaml"
                ]
            },
            {
                parent: this,
                dependsOn: [ ambassadorCrdCG, ambassadorNamespace ]
            }
        );

        this.ingressControllerService = ambassadorCG.getResource("v1/Service", "ambassador/ambassador");
        this.ingressControllerNamespace = pulumi.output("ambassador");
        this.ingressIps = this.ingressControllerService.apply(
            service => service.status.apply(
                status => status.loadBalancer.ingress.map(function (ingress) {
                    return ingress.ip;
                })
            )
        );

        super.registerOutputs({
            ingressControllerService: this.ingressControllerService,
            ingressControllerNamespace: this.ingressControllerNamespace,
            ingressIps: this.ingressIps
        });
    }
}
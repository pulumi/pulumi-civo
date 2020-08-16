import * as k8s from "@pulumi/kubernetes";
import * as civo from "@pulumi/civo"
import * as fs from "fs";
import * as pulumi from "@pulumi/pulumi";
import {AmbassadorIngressDeployment} from "./ingress-ambassador/ingress-ambassador";
import {MinioDeployment} from "./minio/minio";
import {getBooleanOrDefault} from "./utils/configutils";

// Our configuration
const config = new pulumi.Config();
const useAmbassadorIngress = getBooleanOrDefault(config, "useAmbassadorIngress", false);

// Cluster and provider
const cluster = new civo.KubernetesCluster("acc-test", {
    applications: useAmbassadorIngress ? "-traefik" : undefined,
    kubernetesVersion: "1.18.6+k3s1",
    targetNodesSize: "g2.medium",
    numTargetNodes: 4,
    tags: "demo-kubernetes-typescript"
});

const k8sProvider = new k8s.Provider("acc-provider-test", {
    kubeconfig: cluster.kubeconfig
})

export let ingressIps: pulumi.Output<string[]>;

if (useAmbassadorIngress) {
    // Ambassador API Gateway (OSS)
    const ingressController = new AmbassadorIngressDeployment("ingress",
        {},
        {
            providers: {
                kubernetes: k8sProvider
            },
            dependsOn: [ k8sProvider ]
        }
    );

    ingressIps = ingressController.ingressIps;

    // Minio deployment
    const minioDeployment = new MinioDeployment("minio",
        {
            useAmbassadorIngress: useAmbassadorIngress
        },
        {
            providers: {
                kubernetes: k8sProvider
            },
            dependsOn: [ ingressController ]
        }
    );
}
else {
    // Minio deployment
    const minioDeployment = new MinioDeployment("minio",
        {
            useAmbassadorIngress: useAmbassadorIngress
        },
        {
            providers: {
                kubernetes: k8sProvider
            }
        }
    );
}

// Exported variables (shown on screen)
export const clusterName = cluster.name;
export const kubeConfigFileName = pulumi.all([cluster.kubeconfig, clusterName]).apply(([config, name]) => {
   const kubeConfigName = "kubeconfig." + pulumi.getStack();
   fs.writeFileSync(kubeConfigName, config, "utf-8");

   return kubeConfigName;
});

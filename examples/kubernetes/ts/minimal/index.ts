import * as k8s from "@pulumi/kubernetes";
import * as civo from "@pulumi/civo"

const cluster = new civo.KubernetesCluster("acc-test", {
    tags: "demo-kubernetes-typescript",
    kubernetesVersion: "1.18.6+k3s1",
});

const k8sProvider = new k8s.Provider("acc-provider-test", {
    kubeconfig: cluster.kubeconfig
})

const appLabels = { app: "nginx" };
const deployment = new k8s.apps.v1.Deployment("nginx", {
    spec: {
        selector: { matchLabels: appLabels },
        replicas: 1,
        template: {
            metadata: { labels: appLabels },
            spec: { containers: [{ name: "nginx", image: "nginx" }] }
        }
    }
}, {
    provider: k8sProvider
});

export const clusterName = cluster.name;

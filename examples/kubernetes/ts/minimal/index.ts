import * as k8s from "@pulumi/kubernetes";
import * as civo from "@pulumi/civo"
import * as pulumi from "@pulumi/pulumi";

const fw = new civo.Firewall("k8s-sample-fw")

const cluster = new civo.KubernetesCluster("acc-test", {
    tags: "demo-kubernetes-typescript",
    region: "lon1",
    firewallId: fw.id,
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

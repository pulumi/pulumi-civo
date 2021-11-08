import * as civo from "@pulumi/civo";

const fw = new civo.Firewall("k8s-sample-fw", {
    region: "lon1",
})

const cluster = new civo.KubernetesCluster("acc-test", {
    tags: "demo-kubernetes-typescript",
    region: "lon1",
    firewallId: fw.id,
});

export const clusterName = cluster.name;

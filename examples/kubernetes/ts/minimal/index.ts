import * as civo from "@pulumi/civo";

const fw = new civo.Firewall("k8s-sample-fw", {
    region: "lon1",
});

const cluster = new civo.KubernetesCluster("acc-test", {
    tags: "demo-kubernetes-typescript",
    region: "lon1",
    firewallId: fw.id,
}, {
    // Tags (K8s labels) are applied with runtime information, which leads to
    // spurrious pending changes in our integration tests, so we ignore changes
    // to tags:
    ignoreChanges: ["tags"]
});

export const clusterName = cluster.name;

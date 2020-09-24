import * as k8s from "@pulumi/kubernetes";
import * as civo from "@pulumi/civo"
import * as fs from "fs";
import * as pulumi from "@pulumi/pulumi";

const version = civo.getKubernetesVersion({
    filters: [{
        key: "type",
        values: ["stable"],
    }],
}).then(x => x.versions[0].version)

// Cluster and provider
const cluster = new civo.KubernetesCluster("acc-test", {
    applications: "-traefik",
    kubernetesVersion: version,
    targetNodesSize: "g2.medium",
    numTargetNodes: 4,
    tags: "demo-kubernetes-typescript"
});

const k8sProvider = new k8s.Provider("acc-provider-test", {
    kubeconfig: cluster.kubeconfig
})

// Ambassador API Gateway (OSS)
const ambassadorCrdCG = new k8s.yaml.ConfigGroup("ambassador-crd-manifests",
    {
        files: "ambassador-yaml/crd.yaml"
    },
    {
        provider: k8sProvider
    }
);

const ambassadorNamespace = new k8s.core.v1.Namespace("ambassador-namespace",
    {
        metadata: {
            name: "ambassador"
        }
    },
    {
        provider: k8sProvider,
        dependsOn: [ ambassadorCrdCG ]
    }
);

const ambassadorCG = new k8s.yaml.ConfigGroup("ambassador-manifests",
    {
        files: [
            "ambassador-yaml/ambassador-rbac.yaml",
            "ambassador-yaml/ambassador-service.yaml",
            "ambassador-yaml/ambassador-config.yaml"
        ]
    },
    {
        provider: k8sProvider,
        dependsOn: [ ambassadorCrdCG, ambassadorNamespace ]
    }
);

const ambassadorService = ambassadorCG.getResource("v1/Service", "ambassador/ambassador");

export const ingressIp = ambassadorService.apply(
    service => service.status.apply(
        status => status.loadBalancer.ingress.map(function (ingress) {
            return ingress.ip;
        })
    )
);

// Echo app
const namespace = new k8s.core.v1.Namespace("echo",
    {
        metadata: {
            name: "echo"
        }
    },
    {
        provider: k8sProvider
    }
);

const appLabels = { app: "echo" };
const deployment = new k8s.apps.v1.Deployment("echo", {
    metadata: {
        name: "echo",
        namespace: "echo",
        labels: appLabels
    },
    spec: {
        selector: { matchLabels: appLabels },
        replicas: 1,
        template: {
            metadata: { labels: appLabels },
            spec: {
                containers: [
                    {
                        name: "echo",
                        image: "cilium/echoserver:1.10.2",
                        ports: [
                            {
                                name: "http",
                                containerPort: 8080
                            }
                        ]
                    }
                ]
            }
        }
    }
}, {
    provider: k8sProvider,
    dependsOn: [ namespace ]
});

const service = new k8s.core.v1.Service("echo", {
    metadata: {
        name: "echo",
        namespace: "echo",
        labels: appLabels
    },
    spec: {
        selector: appLabels,
        ports: [
            {
                name: "http",
                targetPort: "http",
                port: 8080
            }
        ],
        type: "ClusterIP"
    }
}, {
    provider: k8sProvider,
    dependsOn: [ namespace ]
})

const echoMapping = new k8s.apiextensions.CustomResource("echo-mapping",
    {
        kind: "Mapping",
        apiVersion: "getambassador.io/v2",
        metadata: {
            name: "echo",
            namespace: "echo"
        },
        spec: {
            prefix: "/echo",
            service: "echo:8080"
        }
    },
    {
        provider: k8sProvider,
        dependsOn: [ namespace, ambassadorService ]
    }
);

// Exported variables (shown on screen)
export const clusterName = cluster.name;
export const kubeConfigFileName = pulumi.all([cluster.kubeconfig, clusterName]).apply(([config, name]) => {
   const kubeConfigName = "kubeconfig." + name;
   fs.writeFileSync(kubeConfigName, config, "utf-8");

   return kubeConfigName;
});
export const echoUrl = ingressIp.apply(ip => {
   return "http://" + ip + "/echo"
});

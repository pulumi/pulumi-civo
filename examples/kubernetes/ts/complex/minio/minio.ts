import * as pulumi from "@pulumi/pulumi";
import * as k8s from "@pulumi/kubernetes";
import * as minioConfigLoader from "./minio_config";
import {hasText} from "../utils/textutils";

export interface MinioDeploymentArgs {
    useAmbassadorIngress: boolean
}

export class MinioDeployment extends pulumi.ComponentResource {
    constructor(name: string, args: MinioDeploymentArgs, opts?: pulumi.ComponentResourceOptions) {
        super("pulumicivo:k8s:MinioDeployment", name, {}, opts);
        const minioConfig = minioConfigLoader.getMinioConfig();

        pulumi.all([minioConfig.accessKey, minioConfig.secretKey]).apply(([accessKey, secretKey]) => {
            if ((accessKey === undefined) || (!hasText(accessKey))) {
                throw new Error("Configuration value: minio:accessKey must be set and can't be an empty string.");
            }

            if ((secretKey === undefined) || (!hasText(secretKey))) {
                throw new Error("Configuration value: minio:secretKey must be set and can't be an empty string.");
            }
        });

        const minioNamespace = new k8s.core.v1.Namespace("minio-ns",
            {
                metadata: {
                    name: "minio"
                }
            },
            {
                parent: this
            }
        );

        let configValues = {
            accessKey: minioConfig.accessKey,
            secretKey: minioConfig.secretKey,
            ingress: {
                enabled: minioConfig.exposeWithIngress && (!args.useAmbassadorIngress)
            },
            persistence: {
                enabled: minioConfig.persistenceEnabled,
                size: minioConfig.persistenceSize,
                storageClass: (minioConfig.persistenceStorageClass === undefined) ? null : minioConfig.persistenceStorageClass,
                existingClaim: (minioConfig.persistenceExistingClaim === undefined) ? null : minioConfig.persistenceExistingClaim
            }
        }

        const minioChart = new k8s.helm.v2.Chart("minio",
            {
                repo: "minio",
                chart: "minio",
                version: "6.0.2",
                namespace: "minio",
                values: configValues,
                transformations: [
                    (obj: any) => {
                        if (!minioConfig.persistenceStorageClassInstalled) {
                            if ((obj.kind == "PersistentVolumeClaim") || (obj.kind == "Service") || (obj.kind == "Deployment")){
                                obj.metadata.annotations = {
                                    "pulumi.com/skipAwait": "true"
                                };
                            }
                        }
                    },
                    (obj: any, opts: pulumi.CustomResourceOptions) => {
                        if (obj.kind == "Deployment" && obj.metadata.name === "minio") {
                            opts.ignoreChanges = ["spec.template.metadata.annotations.rollme"]
                        }
                    }
                ]
            },
            {
                parent: this,
                dependsOn: [ minioNamespace ]
            }
        );

        if (minioConfig.exposeWithIngress && args.useAmbassadorIngress) {
            interface MappingSpec {
                prefix: string,
                service: string,
                host?: string,
                host_regex?: boolean
            }

            let mappingSpec: MappingSpec;
            mappingSpec = {
                prefix: "/",
                service: "minio:9000"
            };

            if (minioConfig.exposeDomainPrefix !== undefined) {
                mappingSpec.host = "^" + minioConfig.exposeDomainPrefix + "\\..*$";
                mappingSpec.host_regex = true;
            }

            const minioMapping = new k8s.apiextensions.CustomResource("minio-mapping",
                {
                    kind: "Mapping",
                    apiVersion: "getambassador.io/v2",
                    metadata: {
                        name: "minio",
                        namespace: "minio"
                    },
                    spec: mappingSpec
                },
                {
                    parent: this,
                    dependsOn: [ minioNamespace, minioChart ]
                }
            );
        }
    }
}

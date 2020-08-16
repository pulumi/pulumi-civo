import * as pulumi from "@pulumi/pulumi";
import {getBooleanOrDefault, getStringOrDefault} from "../utils/configutils"

export class MinioConfig {
    readonly accessKey?: pulumi.Output<string>;
    readonly secretKey?: pulumi.Output<string>;
    readonly persistenceEnabled: boolean;
    readonly persistenceSize: string;
    readonly persistenceStorageClass?: string;
    readonly persistenceStorageClassInstalled: boolean;
    readonly persistenceExistingClaim?: string;
    readonly exposeWithIngress: boolean;
    readonly exposeDomainPrefix?: string;

    constructor() {
        const theConfig = new pulumi.Config("minio");

        this.accessKey = theConfig.getSecret("accessKey");
        this.secretKey = theConfig.getSecret("secretKey");
        this.persistenceEnabled = getBooleanOrDefault(theConfig, "persistenceEnabled", true);
        this.persistenceSize = getStringOrDefault(theConfig, "persistenceSize", "10Gi");
        this.persistenceStorageClass = theConfig.get("persistenceStorageClass");
        this.persistenceStorageClassInstalled = getBooleanOrDefault(theConfig, "persistenceStorageClassInstalled", true);
        this.persistenceExistingClaim = theConfig.get("persistenceExistingClaim");
        this.exposeWithIngress = getBooleanOrDefault(theConfig, "exposeWithIngress", false);
        this.exposeDomainPrefix = theConfig.get("exposeDomainPrefix");
    }
}

export function getMinioConfig(): MinioConfig {
    return new MinioConfig();
}
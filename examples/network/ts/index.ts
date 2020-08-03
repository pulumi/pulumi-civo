import * as pulumi from "@pulumi/pulumi";
import * as civo from "@pulumi/civo";

const network = new civo.Network("acc-test", {
    label: "demo-network-typescript"
});

export const networkCidr = network.cidr;

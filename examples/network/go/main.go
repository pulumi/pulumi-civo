package main

import (
	"github.com/pulumi/pulumi-civo/sdk/v2/go/civo"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		network, err := civo.NewNetwork(ctx, "network-go", &civo.NetworkArgs{
			Label: pulumi.String("demo-network-go"),
		})
		if err != nil {
			return err
		}

		ctx.Export("name", network.Name)
		return nil
	})
}

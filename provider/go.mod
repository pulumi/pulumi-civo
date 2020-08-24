module github.com/pulumi/pulumi-civo/provider

go 1.14

replace github.com/Azure/go-autorest => github.com/Azure/go-autorest v12.4.3+incompatible

require (
	github.com/civo/terraform-provider-civo v0.9.15
	github.com/hashicorp/terraform-plugin-sdk v1.14.0
	github.com/mitchellh/go-homedir v1.1.0 // indirect
	github.com/pulumi/pulumi-terraform-bridge/v2 v2.7.3
	github.com/pulumi/pulumi/sdk/v2 v2.9.1-0.20200825190708-910aa96016cd
)

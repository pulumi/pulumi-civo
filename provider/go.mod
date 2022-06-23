module github.com/pulumi/pulumi-civo/provider/v2

go 1.16

replace (
	github.com/hashicorp/go-getter v1.5.0 => github.com/hashicorp/go-getter v1.4.0
	github.com/hashicorp/terraform-plugin-sdk/v2 => github.com/pulumi/terraform-plugin-sdk/v2 v2.0.0-20220505215311-795430389fa7
)

require (
	github.com/civo/terraform-provider-civo v1.0.18
	github.com/hashicorp/terraform-plugin-sdk v1.14.0 // indirect
	github.com/pulumi/pulumi-terraform-bridge/v3 v3.25.1
	github.com/pulumi/pulumi/sdk/v3 v3.35.0
)

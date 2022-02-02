module github.com/pulumi/pulumi-civo/provider/v2

go 1.16

replace (
	github.com/civo/terraform-provider-civo => github.com/pulumi/terraform-provider-civo v1.0.3-0.20211220140709-ec6772fae234
	github.com/hashicorp/go-getter v1.5.0 => github.com/hashicorp/go-getter v1.4.0
	github.com/hashicorp/terraform-plugin-sdk/v2 => github.com/pulumi/terraform-plugin-sdk/v2 v2.0.0-20211019194827-62530c6537a4
)

require (
	github.com/civo/terraform-provider-civo v1.0.2
	github.com/hashicorp/terraform-plugin-sdk v1.14.0 // indirect
	github.com/pulumi/pulumi-terraform-bridge/v3 v3.18.0
	github.com/pulumi/pulumi/sdk/v3 v3.23.2
)

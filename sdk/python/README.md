[![Actions Status](https://github.com/pulumi/pulumi-civo/workflows/master/badge.svg)](https://github.com/pulumi/pulumi-civo/actions)
[![Slack](http://www.pulumi.com/images/docs/badges/slack.svg)](https://slack.pulumi.com)
[![NPM version](https://badge.fury.io/js/%40pulumi%2Fcivo.svg)](https://www.npmjs.com/package/@pulumi/civo)
[![Python version](https://badge.fury.io/py/pulumi-civo.svg)](https://pypi.org/project/pulumi-civo)
[![NuGet version](https://badge.fury.io/nu/pulumi.civo.svg)](https://badge.fury.io/nu/pulumi.civo)
[![PkgGoDev](https://pkg.go.dev/badge/github.com/pulumi/pulumi-civo/sdk/v2/go)](https://pkg.go.dev/github.com/pulumi/pulumi-civo/sdk/v2/go)
[![License](https://img.shields.io/npm/l/%40pulumi%2Fpulumi.svg)](https://github.com/pulumi/pulumi-civo/blob/master/LICENSE)

# Civo Resource Provider

>[!NOTE] As of v2.4.8, this provider is DEPRECATED and will no longer be maintained by Pulumi.
> We recommend using the [Local Provider](https://www.pulumi.com/blog/any-terraform-provider/) version of this package, 
> which can be generated from the  Civo Terraform provider as follows:
> `pulumi package add terraform-provider registry.opentofu.org/civo/civo <version>`
> and follow the instructions.

## Migration

The currently recommended migration path is to use `pulumi import` to migrate existing Civo Cloud resources onto a
new stack which uses the local provider package.

---

## Reference

For further information, please visit [the Civo provider docs](https://www.pulumi.com/docs/intro/cloud-providers/civo)
or for detailed reference documentation, please visit [the API docs](https://www.pulumi.com/docs/reference/pkg/civo).

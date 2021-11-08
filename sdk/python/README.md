[![Actions Status](https://github.com/pulumi/pulumi-civo/workflows/master/badge.svg)](https://github.com/pulumi/pulumi-civo/actions)
[![Slack](http://www.pulumi.com/images/docs/badges/slack.svg)](https://slack.pulumi.com)
[![NPM version](https://badge.fury.io/js/%40pulumi%2Fcivo.svg)](https://www.npmjs.com/package/@pulumi/civo)
[![Python version](https://badge.fury.io/py/pulumi-civo.svg)](https://pypi.org/project/pulumi-civo)
[![NuGet version](https://badge.fury.io/nu/pulumi.civo.svg)](https://badge.fury.io/nu/pulumi.civo)
[![PkgGoDev](https://pkg.go.dev/badge/github.com/pulumi/pulumi-civo/sdk/v2/go)](https://pkg.go.dev/github.com/pulumi/pulumi-civo/sdk/v2/go)
[![License](https://img.shields.io/npm/l/%40pulumi%2Fpulumi.svg)](https://github.com/pulumi/pulumi-civo/blob/master/LICENSE)

# Civo Resource Provider

The Civo Resource Provider lets you manage Civo resources.

## Installing

This package is available in many languages in the standard packaging formats.

### Node.js (Java/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

    $ npm install @pulumi/civo

or `yarn`:

    $ yarn add @pulumi/civo

### Python

To use from Python, install using `pip`:

    $ pip install pulumi_civo

### Go

To use from Go, use `go get` to grab the latest version of the library

    $ go get github.com/pulumi/pulumi-civo/sdk/v2

### .NET

To use from .NET, install using `dotnet add package`:

    $ dotnet add package Pulumi.Civo

## Configuration

The following configuration points are available:

- `civo:token` - (Required) This is the Civo API token. It can also be sourced from the `CIVO_TOKEN`
  environment variable.
- `civo:region` - (Optional) Region in which to create Civo resources.  It can also be sourced from the `CIVO_REGION`
  environment variable.

## Reference

For further information, please visit [the Civo provider docs](https://www.pulumi.com/docs/intro/cloud-providers/civo)
or for detailed reference documentation, please visit [the API docs](https://www.pulumi.com/docs/reference/pkg/civo).

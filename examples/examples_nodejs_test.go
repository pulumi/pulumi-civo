// Copyright 2016-2020, Pulumi Corporation.  All rights reserved.
//go:build nodejs || all
// +build nodejs all

package examples

import (
	"path"
	"testing"

	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
)

func TestAccNetworkTs(t *testing.T) {
	// TODO[pulumi/home#3623]: Re-enable this test once the account issues are resolved.
	t.Skipf("Skipping due to issues with account")
	test := getJSBaseOptions(t).
		With(integration.ProgramTestOptions{
			Dir: path.Join(getCwd(t), "network", "ts"),
		})

	integration.ProgramTest(t, &test)
}

func TestKubernetesMinimalTs(t *testing.T) {
	t.Skip("Civo API returns intermittent 500 error on deleting firewalls; see https://github.com/civo/terraform-provider-civo/issues/138")
	test := getJSBaseOptions(t).
		With(integration.ProgramTestOptions{
			RunUpdateTest: false,
			Dir:           path.Join(getCwd(t), "kubernetes", "ts", "minimal"),
		})

	integration.ProgramTest(t, &test)
}

func getJSBaseOptions(t *testing.T) integration.ProgramTestOptions {
	base := getBaseOptions(t)
	baseJS := base.With(integration.ProgramTestOptions{
		Dependencies: []string{
			"@pulumi/civo",
		},
	})

	return baseJS
}

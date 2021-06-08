// Copyright 2016-2020, Pulumi Corporation.  All rights reserved.
// +build nodejs all

package examples

import (
	"path"
	"testing"

	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
)

func TestAccNetworkTs(t *testing.T) {
	test := getJSBaseOptions(t).
		With(integration.ProgramTestOptions{
			Dir: path.Join(getCwd(t), "network", "ts"),
		})

	integration.ProgramTest(t, &test)
}

func TestKubernetesMinimalTs(t *testing.T) {
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

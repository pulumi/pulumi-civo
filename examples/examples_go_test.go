// Copyright 2016-2020, Pulumi Corporation.  All rights reserved.
//go:build go || all
// +build go all

package examples

import (
	"path/filepath"
	"testing"

	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
)

func TestAccNetworkGo(t *testing.T) {
	// TODO[pulumi/home#3623]: Re-enable this test once the account issues are resolved.
	t.Skipf("Skipping due to issues with account")
	test := getGoBaseOptions(t).
		With(integration.ProgramTestOptions{
			Dir: filepath.Join(getCwd(t), "network", "go"),
		})

	integration.ProgramTest(t, &test)
}

func getGoBaseOptions(t *testing.T) integration.ProgramTestOptions {
	base := getBaseOptions(t)
	baseGo := base.With(integration.ProgramTestOptions{
		Dependencies: []string{
			"github.com/pulumi/pulumi-civo/sdk/v2",
		},
	})

	return baseGo
}

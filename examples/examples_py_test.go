// Copyright 2016-2020, Pulumi Corporation.  All rights reserved.
//go:build python || all
// +build python all

package examples

import (
	"path"
	"path/filepath"
	"testing"

	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
)

func TestAccNetworkPython(t *testing.T) {
	// TODO[pulumi/home#3623]: Re-enable this test once the account issues are resolved.
	t.Skipf("Skipping due to issues with account")
	test := getPythonBaseOptions(t).
		With(integration.ProgramTestOptions{
			Dir: path.Join(getCwd(t), "network", "python"),
		})

	integration.ProgramTest(t, &test)
}

func getPythonBaseOptions(t *testing.T) integration.ProgramTestOptions {
	base := getBaseOptions(t)
	basePy := base.With(integration.ProgramTestOptions{
		Dependencies: []string{
			filepath.Join("..", "sdk", "python", "bin"),
		},
	})

	return basePy
}

package examples

import (
	"os"
	"testing"

	"github.com/pulumi/pulumi/pkg/v2/testing/integration"
)

func getBaseOptions(t *testing.T) integration.ProgramTestOptions {
	checkCivoToken(t)
	return integration.ProgramTestOptions{
		ExpectRefreshChanges: true,
	}
}

func checkCivoToken(t *testing.T) {
	token := os.Getenv("CIVO_TOKEN")
	if token == "" {
		t.Skipf("Skipping test due to missing CIVO_TOKEN environment variable")
	}
}

func getCwd(t *testing.T) string {
	cwd, err := os.Getwd()
	if err != nil {
		t.FailNow()
	}

	return cwd
}

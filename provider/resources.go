// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package civo

import (
	"fmt"
	"path/filepath"
	"unicode"

	"github.com/civo/terraform-provider-civo/civo"
	"github.com/pulumi/pulumi-civo/provider/v2/pkg/version"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	shimv2 "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim/sdk-v2"
	"github.com/pulumi/pulumi/sdk/v3/go/common/tokens"
)

// all of the token components used below.
const (
	// packages:
	mainPkg = "civo"
	// modules:
	mainMod = "index" // the y module
)

// makeMember manufactures a type token for the package and the given module and type.
func makeMember(mod string, mem string) tokens.ModuleMember {
	return tokens.ModuleMember(mainPkg + ":" + mod + ":" + mem)
}

// makeType manufactures a type token for the package and the given module and type.
func makeType(mod string, typ string) tokens.Type {
	return tokens.Type(makeMember(mod, typ))
}

// makeDataSource manufactures a standard resource token given a module and resource name.  It
// automatically uses the main package and names the file by simply lower casing the data source's
// first character.
func makeDataSource(mod string, res string) tokens.ModuleMember {
	fn := string(unicode.ToLower(rune(res[0]))) + res[1:]
	return makeMember(mod+"/"+fn, res)
}

// makeResource manufactures a standard resource token given a module and resource name.  It
// automatically uses the main package and names the file by simply lower casing the resource's
// first character.
func makeResource(mod string, res string) tokens.Type {
	fn := string(unicode.ToLower(rune(res[0]))) + res[1:]
	return makeType(mod+"/"+fn, res)
}

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	// Instantiate the Terraform provider
	p := shimv2.NewProvider(civo.Provider())

	// Create a Pulumi provider mapping
	prov := tfbridge.ProviderInfo{
		P:           p,
		Name:        "civo",
		Description: "A Pulumi package for creating and managing Civo cloud resources.",
		Keywords:    []string{"pulumi", "civo"},
		License:     "Apache-2.0",
		Homepage:    "https://pulumi.io",
		Repository:  "https://github.com/pulumi/pulumi-civo",
		GitHubOrg:   "civo",
		Config:      map[string]*tfbridge.SchemaInfo{},
		Resources: map[string]*tfbridge.ResourceInfo{
			"civo_instance":                        {Tok: makeResource(mainMod, "Instance")},
			"civo_network":                         {Tok: makeResource(mainMod, "Network")},
			"civo_volume":                          {Tok: makeResource(mainMod, "Volume")},
			"civo_volume_attachment":               {Tok: makeResource(mainMod, "VolumeAttachment")},
			"civo_dns_domain_name":                 {Tok: makeResource(mainMod, "DnsDomainName")},
			"civo_dns_domain_record":               {Tok: makeResource(mainMod, "DnsDomainRecord")},
			"civo_firewall":                        {Tok: makeResource(mainMod, "Firewall")},
			"civo_firewall_rule":                   {Tok: makeResource(mainMod, "FirewallRule")},
			"civo_ssh_key":                         {Tok: makeResource(mainMod, "SshKey")},
			"civo_kubernetes_cluster":              {Tok: makeResource(mainMod, "KubernetesCluster")},
			"civo_kubernetes_node_pool":            {Tok: makeResource(mainMod, "KubernetesNodePool")},
			"civo_instance_reserved_ip_assignment": {Tok: makeResource(mainMod, "InstanceReservedIpAssignment")},
			"civo_reserved_ip":                     {Tok: makeResource(mainMod, "ReservedIp")},
			"civo_object_store":                    {Tok: makeResource(mainMod, "ObjectStore")},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			"civo_kubernetes_cluster": {Tok: makeDataSource(mainMod, "getKubernetesCluster")},
			"civo_kubernetes_version": {Tok: makeDataSource(mainMod, "getKubernetesVersion")},
			"civo_instances_size":     {Tok: makeDataSource(mainMod, "getInstancesSize")},
			"civo_instances":          {Tok: makeDataSource(mainMod, "getInstances")},
			"civo_instance":           {Tok: makeDataSource(mainMod, "getInstance")},
			"civo_dns_domain_name":    {Tok: makeDataSource(mainMod, "getDnsDomainName")},
			"civo_dns_domain_record":  {Tok: makeDataSource(mainMod, "getDnsDomainRecord")},
			"civo_network":            {Tok: makeDataSource(mainMod, "getNetwork")},
			"civo_volume":             {Tok: makeDataSource(mainMod, "getVolume")},
			"civo_ssh_key":            {Tok: makeDataSource(mainMod, "getSshKey")},
			"civo_region":             {Tok: makeDataSource(mainMod, "getRegion")},
			"civo_disk_image":         {Tok: makeDataSource(mainMod, "getDiskImage")},
			"civo_firewall":           {Tok: makeDataSource(mainMod, "getFirewall")},
			"civo_size":               {Tok: makeDataSource(mainMod, "getSize")},
			"civo_loadbalancer":       {Tok: makeDataSource(mainMod, "getLoadBalancer")},
			"civo_reserved_ip":        {Tok: makeDataSource(mainMod, "getReservedIp")},
			"civo_object_store":       {Tok: makeDataSource(mainMod, "getObjectStore")},
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			// List any npm dependencies and their versions
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^3.0.0",
			},
			DevDependencies: map[string]string{
				"@types/node": "^10.0.0", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
		},
		Python: &tfbridge.PythonInfo{
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: filepath.Join(
				fmt.Sprintf("github.com/pulumi/pulumi-%[1]s/sdk/", mainPkg),
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				mainPkg,
			),
			GenerateResourceContainerTypes: true,
		},
		CSharp: &tfbridge.CSharpInfo{
			PackageReferences: map[string]string{
				"Pulumi": "3.*",
			},
			Namespaces: map[string]string{
				"civo": "Civo",
			},
		},
	}

	prov.SetAutonaming(255, "-")

	return prov
}

// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package civo

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "civo:index/database:Database":
		r = &Database{}
	case "civo:index/dnsDomainName:DnsDomainName":
		r = &DnsDomainName{}
	case "civo:index/dnsDomainRecord:DnsDomainRecord":
		r = &DnsDomainRecord{}
	case "civo:index/firewall:Firewall":
		r = &Firewall{}
	case "civo:index/firewallRule:FirewallRule":
		r = &FirewallRule{}
	case "civo:index/instance:Instance":
		r = &Instance{}
	case "civo:index/instanceReservedIpAssignment:InstanceReservedIpAssignment":
		r = &InstanceReservedIpAssignment{}
	case "civo:index/kubernetesCluster:KubernetesCluster":
		r = &KubernetesCluster{}
	case "civo:index/kubernetesNodePool:KubernetesNodePool":
		r = &KubernetesNodePool{}
	case "civo:index/network:Network":
		r = &Network{}
	case "civo:index/objectStore:ObjectStore":
		r = &ObjectStore{}
	case "civo:index/objectStoreCredential:ObjectStoreCredential":
		r = &ObjectStoreCredential{}
	case "civo:index/reservedIp:ReservedIp":
		r = &ReservedIp{}
	case "civo:index/sshKey:SshKey":
		r = &SshKey{}
	case "civo:index/volume:Volume":
		r = &Volume{}
	case "civo:index/volumeAttachment:VolumeAttachment":
		r = &VolumeAttachment{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

type pkg struct {
	version semver.Version
}

func (p *pkg) Version() semver.Version {
	return p.version
}

func (p *pkg) ConstructProvider(ctx *pulumi.Context, name, typ, urn string) (pulumi.ProviderResource, error) {
	if typ != "pulumi:providers:civo" {
		return nil, fmt.Errorf("unknown provider type: %s", typ)
	}

	r := &Provider{}
	err := ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return r, err
}

func init() {
	version, _ := PkgVersion()
	pulumi.RegisterResourceModule(
		"civo",
		"index/database",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"civo",
		"index/dnsDomainName",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"civo",
		"index/dnsDomainRecord",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"civo",
		"index/firewall",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"civo",
		"index/firewallRule",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"civo",
		"index/instance",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"civo",
		"index/instanceReservedIpAssignment",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"civo",
		"index/kubernetesCluster",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"civo",
		"index/kubernetesNodePool",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"civo",
		"index/network",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"civo",
		"index/objectStore",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"civo",
		"index/objectStoreCredential",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"civo",
		"index/reservedIp",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"civo",
		"index/sshKey",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"civo",
		"index/volume",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"civo",
		"index/volumeAttachment",
		&module{version},
	)
	pulumi.RegisterResourcePackage(
		"civo",
		&pkg{version},
	)
}

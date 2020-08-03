"""A Python Pulumi program"""

import pulumi
import pulumi_civo as civo

network = civo.Network("acc-test-py",
                       label="Demo Network Python")

pulumi.export("network_cidr", network.cidr)

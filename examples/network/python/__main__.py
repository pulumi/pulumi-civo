"""A Python Pulumi program"""

import pulumi
import pulumi_civo as civo

network = civo.Network("acc-test-py",
                       label="demo-network-python")

pulumi.export("network_name", network.name)

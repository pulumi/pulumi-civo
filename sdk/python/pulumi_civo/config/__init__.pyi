# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

apiEndpoint: Optional[str]
"""
The Base URL to use for CIVO API.
"""

region: Optional[str]
"""
If region is not set, then no region will be used and them you need expensify in every resource even if you expensify
here you can overwrite in a resource.
"""

token: Optional[str]
"""
This is the Civo API token. Alternatively, this can also be specified using `CIVO_TOKEN` environment variable.
"""


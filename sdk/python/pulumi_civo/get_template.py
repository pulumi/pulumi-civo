# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetTemplateResult',
    'AwaitableGetTemplateResult',
    'get_template',
]

@pulumi.output_type
class GetTemplateResult:
    """
    A collection of values returned by getTemplate.
    """
    def __init__(__self__, filters=None, id=None, region=None, sorts=None, templates=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if sorts and not isinstance(sorts, list):
            raise TypeError("Expected argument 'sorts' to be a list")
        pulumi.set(__self__, "sorts", sorts)
        if templates and not isinstance(templates, list):
            raise TypeError("Expected argument 'templates' to be a list")
        pulumi.set(__self__, "templates", templates)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetTemplateFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def sorts(self) -> Optional[Sequence['outputs.GetTemplateSortResult']]:
        return pulumi.get(self, "sorts")

    @property
    @pulumi.getter
    def templates(self) -> Sequence['outputs.GetTemplateTemplateResult']:
        return pulumi.get(self, "templates")


class AwaitableGetTemplateResult(GetTemplateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTemplateResult(
            filters=self.filters,
            id=self.id,
            region=self.region,
            sorts=self.sorts,
            templates=self.templates)


def get_template(filters: Optional[Sequence[pulumi.InputType['GetTemplateFilterArgs']]] = None,
                 region: Optional[str] = None,
                 sorts: Optional[Sequence[pulumi.InputType['GetTemplateSortArgs']]] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTemplateResult:
    """
    Use this data source to access information about an existing resource.

    :param Sequence[pulumi.InputType['GetTemplateFilterArgs']] filters: Filter the results. The `filter` block is documented below.
    :param str region: If is used, them all instances will be from that region.
    :param Sequence[pulumi.InputType['GetTemplateSortArgs']] sorts: Sort the results. The `sort` block is documented below.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['region'] = region
    __args__['sorts'] = sorts
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('civo:index/getTemplate:getTemplate', __args__, opts=opts, typ=GetTemplateResult).value

    return AwaitableGetTemplateResult(
        filters=__ret__.filters,
        id=__ret__.id,
        region=__ret__.region,
        sorts=__ret__.sorts,
        templates=__ret__.templates)

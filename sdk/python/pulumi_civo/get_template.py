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
    'get_template_output',
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
        """
        One or more key/value pairs on which to filter results
        """
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
        """
        One or more key/direction pairs on which to sort results
        """
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
    `get_template` data source is deprecated. Moving forward, please use `get_disk_image` data source.

    Get information on an template for use in other resources (e.g. creating a instance) with the ability to filter the results.


    :param Sequence[pulumi.InputType['GetTemplateFilterArgs']] filters: One or more key/value pairs on which to filter results
    :param Sequence[pulumi.InputType['GetTemplateSortArgs']] sorts: One or more key/direction pairs on which to sort results
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


@_utilities.lift_output_func(get_template)
def get_template_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetTemplateFilterArgs']]]]] = None,
                        region: Optional[pulumi.Input[Optional[str]]] = None,
                        sorts: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetTemplateSortArgs']]]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTemplateResult]:
    """
    `get_template` data source is deprecated. Moving forward, please use `get_disk_image` data source.

    Get information on an template for use in other resources (e.g. creating a instance) with the ability to filter the results.


    :param Sequence[pulumi.InputType['GetTemplateFilterArgs']] filters: One or more key/value pairs on which to filter results
    :param Sequence[pulumi.InputType['GetTemplateSortArgs']] sorts: One or more key/direction pairs on which to sort results
    """
    ...

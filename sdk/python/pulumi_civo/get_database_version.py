# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetDatabaseVersionResult',
    'AwaitableGetDatabaseVersionResult',
    'get_database_version',
    'get_database_version_output',
]

@pulumi.output_type
class GetDatabaseVersionResult:
    """
    A collection of values returned by getDatabaseVersion.
    """
    def __init__(__self__, filters=None, id=None, sorts=None, versions=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if sorts and not isinstance(sorts, list):
            raise TypeError("Expected argument 'sorts' to be a list")
        pulumi.set(__self__, "sorts", sorts)
        if versions and not isinstance(versions, list):
            raise TypeError("Expected argument 'versions' to be a list")
        pulumi.set(__self__, "versions", versions)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetDatabaseVersionFilterResult']]:
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
    def sorts(self) -> Optional[Sequence['outputs.GetDatabaseVersionSortResult']]:
        """
        One or more key/direction pairs on which to sort results
        """
        return pulumi.get(self, "sorts")

    @property
    @pulumi.getter
    def versions(self) -> Sequence['outputs.GetDatabaseVersionVersionResult']:
        return pulumi.get(self, "versions")


class AwaitableGetDatabaseVersionResult(GetDatabaseVersionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatabaseVersionResult(
            filters=self.filters,
            id=self.id,
            sorts=self.sorts,
            versions=self.versions)


def get_database_version(filters: Optional[Sequence[Union['GetDatabaseVersionFilterArgs', 'GetDatabaseVersionFilterArgsDict']]] = None,
                         sorts: Optional[Sequence[Union['GetDatabaseVersionSortArgs', 'GetDatabaseVersionSortArgsDict']]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatabaseVersionResult:
    """
    Retrieves information about the database versions that Civo supports, with the ability to filter the results.


    :param Sequence[Union['GetDatabaseVersionFilterArgs', 'GetDatabaseVersionFilterArgsDict']] filters: One or more key/value pairs on which to filter results
    :param Sequence[Union['GetDatabaseVersionSortArgs', 'GetDatabaseVersionSortArgsDict']] sorts: One or more key/direction pairs on which to sort results
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['sorts'] = sorts
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('civo:index/getDatabaseVersion:getDatabaseVersion', __args__, opts=opts, typ=GetDatabaseVersionResult).value

    return AwaitableGetDatabaseVersionResult(
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        sorts=pulumi.get(__ret__, 'sorts'),
        versions=pulumi.get(__ret__, 'versions'))
def get_database_version_output(filters: Optional[pulumi.Input[Optional[Sequence[Union['GetDatabaseVersionFilterArgs', 'GetDatabaseVersionFilterArgsDict']]]]] = None,
                                sorts: Optional[pulumi.Input[Optional[Sequence[Union['GetDatabaseVersionSortArgs', 'GetDatabaseVersionSortArgsDict']]]]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatabaseVersionResult]:
    """
    Retrieves information about the database versions that Civo supports, with the ability to filter the results.


    :param Sequence[Union['GetDatabaseVersionFilterArgs', 'GetDatabaseVersionFilterArgsDict']] filters: One or more key/value pairs on which to filter results
    :param Sequence[Union['GetDatabaseVersionSortArgs', 'GetDatabaseVersionSortArgsDict']] sorts: One or more key/direction pairs on which to sort results
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['sorts'] = sorts
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('civo:index/getDatabaseVersion:getDatabaseVersion', __args__, opts=opts, typ=GetDatabaseVersionResult)
    return __ret__.apply(lambda __response__: GetDatabaseVersionResult(
        filters=pulumi.get(__response__, 'filters'),
        id=pulumi.get(__response__, 'id'),
        sorts=pulumi.get(__response__, 'sorts'),
        versions=pulumi.get(__response__, 'versions')))

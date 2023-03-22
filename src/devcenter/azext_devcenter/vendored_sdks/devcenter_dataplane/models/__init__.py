# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ActionRequest
    from ._models_py3 import Artifact
    from ._models_py3 import ArtifactListResult
    from ._models_py3 import CatalogItem
    from ._models_py3 import CatalogItemAction
    from ._models_py3 import CatalogItemListResult
    from ._models_py3 import CatalogItemParameter
    from ._models_py3 import CatalogItemVersion
    from ._models_py3 import CatalogItemVersionListResult
    from ._models_py3 import CloudErrorBody
    from ._models_py3 import DevBox
    from ._models_py3 import DevBoxListResult
    from ._models_py3 import DevBoxProvisioningNotification
    from ._models_py3 import EmailNotification
    from ._models_py3 import Environment
    from ._models_py3 import EnvironmentListResult
    from ._models_py3 import EnvironmentType
    from ._models_py3 import EnvironmentTypeListResult
    from ._models_py3 import EnvironmentUpdateProperties
    from ._models_py3 import HardwareProfile
    from ._models_py3 import ImageReference
    from ._models_py3 import NotificationChannel
    from ._models_py3 import NotificationSettings
    from ._models_py3 import NotificationSettingsAllowedCulturesListResult
    from ._models_py3 import NotificationType
    from ._models_py3 import OsDisk
    from ._models_py3 import Pool
    from ._models_py3 import PoolListResult
    from ._models_py3 import Project
    from ._models_py3 import ProjectListResult
    from ._models_py3 import ProvisioningError
    from ._models_py3 import RemoteConnection
    from ._models_py3 import Schedule
    from ._models_py3 import ScheduleListResult
    from ._models_py3 import ScheduledTask
    from ._models_py3 import StorageProfile
    from ._models_py3 import LongRunningOperationErrorDetails
    from ._models_py3 import LongRunningOperationStatus
    from ._models_py3 import UpcomingAction
    from ._models_py3 import UpcomingActionsListResult
    from ._models_py3 import WebhookNotification
except (SyntaxError, ImportError):
    from ._models import ActionRequest  # type: ignore
    from ._models import Artifact  # type: ignore
    from ._models import ArtifactListResult  # type: ignore
    from ._models import CatalogItem  # type: ignore
    from ._models import CatalogItemAction  # type: ignore
    from ._models import CatalogItemListResult  # type: ignore
    from ._models import CatalogItemParameter  # type: ignore
    from ._models import CatalogItemVersion  # type: ignore
    from ._models import CatalogItemVersionListResult  # type: ignore
    from ._models import CloudErrorBody  # type: ignore
    from ._models import DevBox  # type: ignore
    from ._models import DevBoxListResult  # type: ignore
    from ._models import DevBoxProvisioningNotification  # type: ignore
    from ._models import EmailNotification  # type: ignore
    from ._models import Environment  # type: ignore
    from ._models import EnvironmentListResult  # type: ignore
    from ._models import EnvironmentType  # type: ignore
    from ._models import EnvironmentTypeListResult  # type: ignore
    from ._models import EnvironmentUpdateProperties  # type: ignore
    from ._models import HardwareProfile  # type: ignore
    from ._models import ImageReference  # type: ignore
    from ._models import NotificationChannel  # type: ignore
    from ._models import NotificationSettings  # type: ignore
    from ._models import NotificationSettingsAllowedCulturesListResult  # type: ignore
    from ._models import NotificationType  # type: ignore
    from ._models import OsDisk  # type: ignore
    from ._models import Pool  # type: ignore
    from ._models import PoolListResult  # type: ignore
    from ._models import Project  # type: ignore
    from ._models import ProjectListResult  # type: ignore
    from ._models import ProvisioningError  # type: ignore
    from ._models import RemoteConnection  # type: ignore
    from ._models import Schedule  # type: ignore
    from ._models import ScheduleListResult  # type: ignore
    from ._models import ScheduledTask  # type: ignore
    from ._models import StorageProfile  # type: ignore
    from ._models import UpcomingAction  # type: ignore
    from ._models import UpcomingActionsListResult  # type: ignore
    from ._models import WebhookNotification  # type: ignore

from ._dev_center_dataplane_client_enums import (
    ActionType,
    EnableStatus,
    HibernateSupport,
    LocalAdminStatus,
    OsType,
    ParameterType,
    PowerState,
    ScheduledFrequency,
    ScheduledTaskType,
    ScheduledType,
    UpcomingActionReason,
    UpcomingActionType,
)

__all__ = [
    'ActionRequest',
    'Artifact',
    'ArtifactListResult',
    'CatalogItem',
    'CatalogItemAction',
    'CatalogItemListResult',
    'CatalogItemParameter',
    'CatalogItemVersion',
    'CatalogItemVersionListResult',
    'CloudErrorBody',
    'DevBox',
    'DevBoxListResult',
    'DevBoxProvisioningNotification',
    'EmailNotification',
    'Environment',
    'EnvironmentListResult',
    'EnvironmentType',
    'EnvironmentTypeListResult',
    'EnvironmentUpdateProperties',
    'HardwareProfile',
    'ImageReference',
    'NotificationChannel',
    'NotificationSettings',
    'NotificationSettingsAllowedCulturesListResult',
    'NotificationType',
    'OsDisk',
    'Pool',
    'PoolListResult',
    'Project',
    'ProjectListResult',
    'ProvisioningError',
    'RemoteConnection',
    'Schedule',
    'ScheduleListResult',
    'ScheduledTask',
    'StorageProfile',
    'UpcomingAction',
    'UpcomingActionsListResult',
    'WebhookNotification',
    'ActionType',
    'EnableStatus',
    'HibernateSupport',
    'LocalAdminStatus',
    'OsType',
    'ParameterType',
    'PowerState',
    'ScheduledFrequency',
    'ScheduledTaskType',
    'ScheduledType',
    'UpcomingActionReason',
    'UpcomingActionType',
    'LongRunningOperationErrorDetails',
    'LongRunningOperationStatus'
]
---
title: "SMS_CIDeploymentUnknownStatus Class"
type: reference
domain: sccm
slug: develop-sms-cideploymentunknownstatus-server-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/apps/sms_cideploymentunknownstatus-server-wmi-class
family: develop
documentKind: "reference"
abstract: "Learn how to represent the status of a configuration item deployment for unknown status using SMS_CIDeploymentUnknownStatus class."
---

# SMS_CIDeploymentUnknownStatus Class

# SMS_CIDeploymentUnknownStatus Server WMI Class
The `SMS_CIDeploymentUnknownStatus` Windows Management Instrumentation (WMI) class is an SMS Provider server class, in Configuration Manager, that represents the status of a configuration item deployment for unknown status.

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class SMS_CIDeploymentUnknownStatus : SMS_BaseClass
{
    UInt32 AssignmentID;
    String AssignmentUniqueID;
    UInt32 Category;
    UInt32 CI_ID;
    String CollectionID;
    String CollectionName;
    UInt32 DeploymentIntent;
    UInt32 PolicyModelID;
    String SoftwareName;
    DateTime StartTime;
    UInt32 Total;
};
```

## Methods
 The `SMS_CIDeploymentUnknownStatus` class does not define any methods.

## Properties
 `AssignmentID`
 Data type: `UInt32`

 Access type: Read-only

 Qualifiers: [key, not_null, read]

 See [SMS_AppDeploymentAssetDetails Server WMI Class](../../../develop/reference/apps/sms_appdeploymentassetdetails-server-wmi-class.md).

 `AssignmentUniqueID`
 Data type: `String`

 Access type: Read-only

 Qualifiers: [not_null, read]

 See [SMS_AppDeploymentAssetDetails Server WMI Class](../../../develop/reference/apps/sms_appdeploymentassetdetails-server-wmi-class.md).

 `Category`
 Data type: `UInt32`

 Access type: Read-only

 Qualifiers: [key, not_null, read]

 Status category.

 `CI_ID`
 Data type: `UInt32`

 Access type: Read-only

 Qualifiers: [not_null, read]

 See [SMS_ConfigurationItemLatestBaseClass Server WMI Class](../../../develop/reference/compliance/sms_configurationitemlatestbaseclass-server-wmi-class.md).

 `CollectionID`
 Data type: `String`

 Access type: Read-only

 Qualifiers: [not_null, read]

 See [SMS_AppDeploymentAssetDetails Server WMI Class](../../../develop/reference/apps/sms_appdeploymentassetdetails-server-wmi-class.md).

 `CollectionName`
 Data type: `String`

 Access type: Read-only

 Qualifiers: [not_null, read]

 See [SMS_AppDeploymentAssetDetails Server WMI Class](../../../develop/reference/apps/sms_appdeploymentassetdetails-server-wmi-class.md).

 `DeploymentIntent`
 Data type: `UInt32`

 Access type: Read-only

 Qualifiers: [read]

 See [SMS_AppDeploymentAssetDetails Server WMI Class](../../../develop/reference/apps/sms_appdeploymentassetdetails-server-wmi-class.md).

 `PolicyModelID`
 Data type: `UInt32`

 Access type: Read-only

 Qualifiers: [not_null, read]

 Model ID of the policy.

 `SoftwareName`
 Data type: `String`

 Access type: Read-only

 Qualifiers: [read]

 Name of the software.

 `StartTime`
 Data type: `DateTime`

 Access type: Read-only

 Qualifiers: [read]

 See [SMS_AppDeploymentAssetDetails Server WMI Class](../../../develop/reference/apps/sms_appdeploymentassetdetails-server-wmi-class.md).

 `Total`
 Data type: `UInt32`

 Access type: Read-only

 Qualifiers: [read]

 Total number of resources in this state.

## Remarks

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).

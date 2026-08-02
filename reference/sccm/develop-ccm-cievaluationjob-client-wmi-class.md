---
title: "CCM_CIEvaluationJob Class"
type: reference
domain: sccm
slug: develop-ccm-cievaluationjob-client-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/sdk/ccm_cievaluationjob-client-wmi-class
family: develop
documentKind: "reference"
abstract: "The CCM_CIEvaluationJob Windows Management Instrumentation (WMI) class is an SMS Provider server class, in Configuration Manager, that represents a configuration item evaluation job."
---

# CCM_CIEvaluationJob Class

# CCM_CIEvaluationJob Client WMI Class
The `CCM_CIEvaluationJob` Windows Management Instrumentation (WMI) class is an SMS Provider server class, in Configuration Manager, that represents a configuration item evaluation job.

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class CCM_CIEvaluationJob :
{
    String CIAgentJobId;
    UInt32 ErrorCode;
    String Id;
    Boolean IsMachineTarget;
    Boolean IsRebootRequired;
    String JobState;
    DateTime LastModifiedTime;
    String OwnerSID;
    String Type;
    String UserSID;
};
```

## Methods
 The `CCM_CIEvaluationJob` class doesn't define any methods.

## Properties
 `CIAgentJobId`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: none

 CI agent job identifier.

 `ErrorCode`
 Data type: `UInt32`

 Access type: Read/Write

 Qualifiers: none

 Error code.

 `Id`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: [key]

 Identifier.

 `IsMachineTarget`
 Data type: `Boolean`

 Access type: Read/Write

 Qualifiers: none

 `true` if this is a device targeted application.

 `IsRebootRequired`
 Data type: `Boolean`

 Access type: Read/Write

 Qualifiers: none

 `true` if a reboot is required.

 `JobState`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: [values]

 Job state. Possible values are:

|Value|
|-|
|Idle|
|Evaluating|
|Success|
|Error|
|CanceledOrDeleted|

 `LastModifiedTime`
 Data type: `DateTime`

 Access type: Read/Write

 Qualifiers: none

 Last modified time.

 `OwnerSID`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: none

 Owner identifier (SID).

 `Type`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: [valuemap]

 Job type. Possible values are:

|Value|
|-|
|DesiredConfiguration|
|ApplicationManagement|
|SoftwareUpdates|

 `UserSID`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: none

 User identifier (SID).

## Remarks

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

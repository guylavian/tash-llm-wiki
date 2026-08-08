---
title: "SMS_TaskSequenceAppReferencesInfo Class"
type: reference
domain: sccm
slug: develop-sms-tasksequenceappreferencesinfo-server-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/osd/sms_tasksequenceappreferencesinfo-server-wmi-class
family: develop
documentKind: "reference"
abstract: "Learn how to represent a Configuration Manager application in the task sequence using SMS_TaskSequenceAppReferencesInfo class."
---

# SMS_TaskSequenceAppReferencesInfo Class

# SMS_TaskSequenceAppReferencesInfo Server WMI Class
The `SMS_TaskSequenceAppReferencesInfo` Windows Management Instrumentation (WMI) class is an SMS Provider server class, in Configuration Manager, that represents a Configuration Manager application in the task sequence.

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class SMS_TaskSequenceAppReferencesInfo : SMS_BaseClass
{
    String PackageID;
    SInt32 RefAppCI_ID;
    String RefAppModelName;
    String RefAppPackageID;
};
```

## Methods
 The `SMS_TaskSequenceAppReferencesInfo` class does not define any methods.

## Properties
 `PackageID`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: [key]

 Package ID of the task sequence.

 `RefAppCI_ID`
 Data type: `SInt32`

 Access type: Read/Write

 Qualifiers: none

 CI_ID of the referenced by task sequence application.

 `RefAppModelName`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: none

 The model name of the referenced by task sequence application.

 `RefAppPackageID`
 Data type: `String`

 Access type: Read/Write

 Qualifiers: none

 Package ID of the referenced by task sequence application.

## Remarks

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).

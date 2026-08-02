---
title: "SMS_TaskSequencePackageReference_All Class"
type: reference
domain: sccm
slug: develop-sms-tasksequencepackagereference-all-server-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/osd/sms_tasksequencepackagereference_all-server-wmi-class
family: develop
documentKind: "reference"
abstract: "Learn about the simplified syntax, methods, properties, and requirements of the SMS_TaskSequencePackageReference_All server class."
---

# SMS_TaskSequencePackageReference_All Class

# SMS_TaskSequencePackageReference_All Server WMI Class
The `SMS_TaskSequencePackageReference_All` Windows Management Instrumentation (WMI) class is an SMS Provider server class, in Configuration Manager, that allows the retrieval of all task sequence package or application references (including those that do not contain any content files).

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class SMS_TaskSequencePackageReference_All : SMS_BaseClass
{
    String ObjectID;
    String PackageID;
    String RefPackageID;
};
```

## Methods
 The `SMS_TaskSequencePackageReference_All` class does not define any methods.

## Properties
 `ObjectID`
 Data type: `String`

 Access type: Read

 Qualifiers: [key]

 If the Task Sequence reference is to a legacy package, this property is the package identifier of the legacy package. If the Task Sequence reference is to an application, this property is the package identifier of the application.

 `PackageID`
 Data type: `String`

 Access type: Read

 Qualifiers: [key]

 Package identifier of the task sequence for which the user requests package or application references.

 `RefPackageID`
 Data type: `String`

 Access type: Read

 Qualifiers: none

 If the Task Sequence reference is to a legacy package, this property is the package identifier of the legacy package. If the Task Sequence reference is to an application, this property is the package identifier of the application.

## Remarks

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).

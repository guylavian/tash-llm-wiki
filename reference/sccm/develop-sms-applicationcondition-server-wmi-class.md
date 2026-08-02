---
title: "SMS_ApplicationCondition Class"
type: reference
domain: sccm
slug: develop-sms-applicationcondition-server-wmi-class
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/apps/sms_applicationcondition-server-wmi-class
family: develop
documentKind: "reference"
abstract: "An SMS Provider server class that represents relationships between global conditions and applications."
---

# SMS_ApplicationCondition Class

# SMS_ApplicationCondition Server WMI Class
The `SMS_ApplicationCondition` Windows Management Instrumentation (WMI) class is an SMS Provider server class, in Configuration Manager, that represents relationships between global conditions and applications.

 The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

```
Class SMS_ApplicationCondition : SMS_BaseClass
{
    String ApplicationGUID;
    String ConditionDisplayName;
    UInt32 ConditionID;
    String ConditionModelName;
};
```

## Methods
 The `SMS_ApplicationCondition` class does not define any methods.

## Properties
 `ApplicationGUID`
 Data type: `String`

 Access type: Read-only

 Qualifiers: [not_null, read]

 Unique identifier of the application.

 `ConditionDisplayName`
 Data type: `String`

 Access type: Read-only

 Qualifiers: [read]

 Condition display name.

 `ConditionID`
 Data type: `UInt32`

 Access type: Read-only

 Qualifiers: [not_null, read]

 Identifier of the application condition.

 `ConditionModelName`
 Data type: `String`

 Access type: Read-only

 Qualifiers: [not_null, read]

 Model name of the condition.

## Requirements

### Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

### Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).

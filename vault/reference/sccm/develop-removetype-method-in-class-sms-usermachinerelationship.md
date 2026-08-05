---
title: "RemoveType Method"
type: reference
domain: sccm
slug: develop-removetype-method-in-class-sms-usermachinerelationship
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/manage/removetype-method-in-class-sms_usermachinerelationship
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, the RemoveType WMI class method removes a type of the relationship between a user and a device."
---

# RemoveType Method

# RemoveType Method in Class SMS_UserMachineRelationship
The `RemoveType` Windows Management Instrumentation (WMI) class method, in Configuration Manager, removes a type of the relationship between a user and a device.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
sint32 RemoveType(
     uint32 TypeId
);
```

#### Parameters
 `TypeId`
 Data type: `UInt32`

 Qualifiers: `[in]`

The type ID.

## Return Values
 An  `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For more information about handling returned errors, see [About Configuration Manager Errors](../../../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_Application Server WMI Class](../../../../../develop/reference/apps/sms_application-server-wmi-class.md)

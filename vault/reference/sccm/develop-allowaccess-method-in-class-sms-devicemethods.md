---
title: "AllowAccess Method"
type: reference
domain: sccm
slug: develop-allowaccess-method-in-class-sms-devicemethods
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/mdm/allowaccess-method-in-class-sms_devicemethods
family: develop
documentKind: "reference"
abstract: "Learn about the simplified syntax, parameters, return values, and requirement of the AllowAccess method."
---

# AllowAccess Method

# AllowAccess Method in Class SMS_DeviceMethods
The `AllowAccess` Windows Management Instrumentation (WMI) class method, in Configuration Manager, lets the Exchange ActiveSync device connect to Exchange.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
SInt32 AllowAccess(
   UInt32 ResourceId
   String EASIdentities[]
);
```

#### Parameters
 `ResourceId`
 Data type: `UInt32`

 Qualifiers: [in]

 ID of the resource.

 `EASIdentities`
 Data type: `String` Array

 Qualifiers: [in]

 Array of Exchange ActiveSync identities.

## Return Values
 An `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For information about handling returned errors, see [About Configuration Manager Errors](../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

## See Also
 [SMS_DeviceMethods Server WMI Class](../../../develop/reference/mdm/sms_devicemethods-server-wmi-class.md)

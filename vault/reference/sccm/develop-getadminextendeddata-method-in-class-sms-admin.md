---
title: "GetAdminExtendedData Method"
type: reference
domain: sccm
slug: develop-getadminextendeddata-method-in-class-sms-admin
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/configure/getadminextendeddata-method-in-class-sms_admin
family: develop
documentKind: "reference"
abstract: "Learn how to get the extended data that the current user and its groups have using GetAdminExtendedData."
---

# GetAdminExtendedData Method

# GetAdminExtendedData Method in Class SMS_Admin
The `GetAdminExtendedData` Windows Management Instrumentation (WMI) class method, in Configuration Manager, gets the extended data that the current user and its groups have for a given type.

> [!WARNING]
>  This method is reserved for internal use.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
sint32 GetAdminExtendedData(
    [in] uint32 Type,
    [out] string ExtendedData[]);
};
```

#### Parameters
 `Type`
 Data type: `UInt32`

 Qualifiers: [in]

 The type associated with the user.

 `ExtendedData`
 Data type: `String` Array

 Qualifiers: [out]

 The extended data that the current user and its groups have for a given type.

## Return Values
 An `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_Admin Server WMI Class](../../../../../develop/reference/core/servers/configure/sms_admin-server-wmi-class.md)

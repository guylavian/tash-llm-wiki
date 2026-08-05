---
title: "ImportGlobalUserAccountEx Method"
type: reference
domain: sccm
slug: develop-importglobaluseraccountex-method-in-class-sms-site
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/configure/importglobaluseraccountex-method-in-class-sms_site
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, the ImportGlobalUserAccountEx WMI class method encrypts data that is shared in the hierarchy."
---

# ImportGlobalUserAccountEx Method

# ImportGlobalUserAccountEx Method in Class SMS_Site
The `ImportGlobalUserAccountEx` Windows Management Instrumentation (WMI) class method, in Configuration Manager, encrypts data that is shared in the hierarchy.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
SInt32 ImportGlobalUserAccountEx(
     String UserName,
     String Password
);
```

#### Parameters
 `UserName`
 Data type: `String`

 Qualifiers: [in]

 Name of the global user account to import.

 `Password`
 Data type: `String`

 Qualifiers: [in]

 Password.

## Return Values
 An `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For information about handling returned errors, see [About Configuration Manager Errors](../../../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_Site Server WMI Class](../../../../../develop/reference/core/servers/configure/sms_site-server-wmi-class.md)

---
title: "SetIsExpired method in class SMS_ApplicationLatest"
type: reference
domain: sccm
slug: develop-setisexpired-method-in-class-sms-applicationlatest
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/apps/setisexpired-method-in-class-sms_applicationlatest
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, the SetIsExpired WMI class method sets the expired status of this application."
---

# SetIsExpired method in class SMS_ApplicationLatest

# SetIsExpired Method in Class SMS_ApplicationLatest
The `SetIsExpired` Windows Management Instrumentation (WMI) class method, in Configuration Manager, sets the expired status of this application.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
sint32 SetIsExpired (
     boolean Expired
);
```

#### Parameters
 `Expired`
 Data type: `Boolean`

 Qualifiers: [in]

 `true` to set the state to expired. The default value is `true`.

## Return Values
 An `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For more information about handling returned errors, see [About Configuration Manager Errors](../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_ApplicationLatest Server WMI Class](../../../develop/reference/apps/sms_applicationlatest-server-wmi-class.md)

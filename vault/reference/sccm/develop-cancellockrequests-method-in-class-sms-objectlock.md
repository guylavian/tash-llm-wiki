---
title: "CancelLockRequests Method"
type: reference
domain: sccm
slug: develop-cancellockrequests-method-in-class-sms-objectlock
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/misc/cancellockrequests-method-in-class-sms_objectlock
family: develop
documentKind: "reference"
abstract: "The CancelLockRequests WMI class method, in Configuration Manager, cancels multiple lock requests."
---

# CancelLockRequests Method

# CancelLockRequests Method in Class SMS_ObjectLock
The `CancelLockRequests` Windows Management Instrumentation (WMI) class method, in Configuration Manager, cancels multiple lock requests.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
SInt32 CancelLockRequests(
    string RequestIDs[]
);
```

#### Parameters
 `RequestIDs`
 Data type: `String`  Array

 Qualifiers: [in]

 Array of unique identifiers of the request.

## Return Values
 An `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For information about handling returned errors, see [About Configuration Manager Errors](../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_ObjectLock Server WMI Class](../../../develop/reference/misc/sms_objectlock-server-wmi-class.md)

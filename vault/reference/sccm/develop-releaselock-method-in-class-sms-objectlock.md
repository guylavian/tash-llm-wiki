---
title: "ReleaseLock Method"
type: reference
domain: sccm
slug: develop-releaselock-method-in-class-sms-objectlock
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/misc/releaselock-method-in-class-sms_objectlock
family: develop
documentKind: "reference"
abstract: "The ReleaseLock Windows Management Instrumentation (WMI) class method releases a lock to a global object."
---

# ReleaseLock Method

# ReleaseLock Method in Class SMS_ObjectLock
The `ReleaseLock` Windows Management Instrumentation (WMI) class method, in Configuration Manager, releases a lock to a global object.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
SInt32 ReleaseLock(
    string ObjectRelPath
);
```

#### Parameters
 `ObjectRelPath`
 Data type: `String`

 Qualifiers: [in]

 The path of the object from which to release the lock.

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

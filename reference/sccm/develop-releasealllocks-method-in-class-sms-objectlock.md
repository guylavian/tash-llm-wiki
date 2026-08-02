---
title: "ReleaseAllLocks Method"
type: reference
domain: sccm
slug: develop-releasealllocks-method-in-class-sms-objectlock
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/misc/releasealllocks-method-in-class-sms_objectlock
family: develop
documentKind: "reference"
abstract: "Learn how to use the ReleaseAllLocks method in Configuration Manager to release all locks for a session."
---

# ReleaseAllLocks Method

# ReleaseAllLocks Method in Class SMS_ObjectLock
The `ReleaseAllLocks` Windows Management Instrumentation (WMI) class method, in Configuration Manager, releases all locks for a session.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
SInt32 ReleaseAllLocks();
```

#### Parameters
 None.

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

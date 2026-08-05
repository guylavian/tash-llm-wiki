---
title: "Unlock Method in Class SMS_Package"
type: reference
domain: sccm
slug: develop-unlock-method-in-class-sms-package
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/configure/unlock-method-in-class-sms_package
family: develop
documentKind: "reference"
abstract: "A Windows Management Instrumentation class method that sets the source site to the current site, unlocking the package."
---

# Unlock Method in Class SMS_Package

# Unlock Method in Class SMS_Package
The `Unlock` Windows Management Instrumentation (WMI) class method, in Configuration Manager, sets the source site to the current site, unlocking the package.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
SInt32 Unlock();
```

#### Parameters
 None.

## Return Values
 An `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For information about handling returned errors, see [About Configuration Manager Errors](../../../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_Package Server WMI Class](../../../../../develop/reference/core/servers/configure/sms_package-server-wmi-class.md)

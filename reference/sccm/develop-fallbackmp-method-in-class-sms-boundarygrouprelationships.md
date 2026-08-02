---
title: "FallbackMP Method"
type: reference
domain: sccm
slug: develop-fallbackmp-method-in-class-sms-boundarygrouprelationships
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/configure/fallbackmp-method-in-class-sms-boundarygrouprelationships
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, the FallbackMP Windows Management Instrumentation class method sets the fallback time in minutes for a management point with the default value of 120."
---

# FallbackMP Method

# FallbackMP Method in Class SMS_BoundaryGroupRelationships
 The `FallbackMP` Windows Management Instrumentation (WMI) class method, in Configuration Manager, sets the fallback time, in minutes, for a management point (MP). The default value is 120.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
SInt32 FallbackMP();
```

### Parameters
 None.

## Return Values
 An `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For information about handling returned errors, see [About Configuration Manager Errors](../../../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

### Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

### Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_BoundaryGroupRelationships Server WMI Class](../../../../../develop/reference/core/servers/configure/sms-boundarygrouprelationships-server-wmi-class.md)

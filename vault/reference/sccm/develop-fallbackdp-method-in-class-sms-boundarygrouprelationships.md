---
title: "FallbackDP Method"
type: reference
domain: sccm
slug: develop-fallbackdp-method-in-class-sms-boundarygrouprelationships
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/configure/fallbackdp-method-in-class-sms-boundarygrouprelationships
family: develop
documentKind: "reference"
abstract: "Learn how to set the fallback time, in minutes, for a distribution point (DP) in Configuration Manager."
---

# FallbackDP Method

# FallbackDP Method in Class SMS_BoundaryGroupRelationships
 The `FallbackDP` Windows Management Instrumentation (WMI) class method, in Configuration Manager, sets the fallback time, in minutes, for a distribution point (DP). The default value is 120.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
SInt32 FallbackDP();
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

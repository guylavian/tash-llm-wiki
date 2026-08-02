---
title: "RefreshDPGroup Method"
type: reference
domain: sccm
slug: develop-refreshdpgroup-method-in-class-sms-distributionpointgroup
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/servers/configure/refreshdpgroup-method-in-class-sms_distributionpointgroup
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, WMI class method refreshes all of the member distribution points with the latest version of the targeted packages."
---

# RefreshDPGroup Method

# RefreshDPGroup Method in Class SMS_DistributionPointGroup
The `RefreshDPGroup` Windows Management Instrumentation (WMI) class method, in Configuration Manager, refreshes all of the member distribution points with the latest version of the targeted packages.

 The following syntax is simplified from Managed Object Format (MOF) code and defines the method.

## Syntax

```
sint32 RefreshDPGroup();
```

#### Parameters
 None.

## Return Values
 An  `SInt32` data type that is 0 to indicate success or non-zero to indicate failure.

 For more information about handling returned errors, see [About Configuration Manager Errors](../../../../../develop/core/understand/about-configuration-manager-errors.md).

## Requirements

## Runtime Requirements
 For more information, see [Configuration Manager Server Runtime Requirements](../../../../../develop/core/reqs/server-runtime-requirements.md).

## Development Requirements
 For more information, see [Configuration Manager Server Development Requirements](../../../../../develop/core/reqs/server-development-requirements.md).

## See Also
 [SMS_Application Server WMI Class](../../../../../develop/reference/apps/sms_application-server-wmi-class.md)
